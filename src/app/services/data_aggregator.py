"""
Comprehensive data aggregation service that combines multiple legal data sources.
"""

import requests
import time
import logging
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor, as_completed

from ..models.facility import Facility
from ..utils.web_scraper import scrape_website_for_contacts

logger = logging.getLogger(__name__)


@dataclass
class DataSource:
    """Represents a data source configuration."""
    name: str
    api_key: str
    base_url: str
    rate_limit: int  # requests per minute
    enabled: bool = True


class DataAggregator:
    """
    Aggregates data from multiple legal sources to create comprehensive business profiles.
    """
    
    def __init__(self):
        self.sources = {
            'foursquare': DataSource(
                name='Foursquare',
                api_key='',  # Set via environment variable
                base_url='https://api.foursquare.com/v3/places',
                rate_limit=1000
            ),
            'yelp': DataSource(
                name='Yelp',
                api_key='',  # Set via environment variable
                base_url='https://api.yelp.com/v3/businesses',
                rate_limit=500
            ),
            'osm': DataSource(
                name='OpenStreetMap',
                api_key='',  # Not needed for OSM
                base_url='https://overpass-api.de/api/interpreter',
                rate_limit=1000
            )
        }
    
    def enrich_facility(self, facility: Facility) -> Facility:
        """
        Enrich a facility with data from multiple sources.
        
        Args:
            facility: Basic facility from Google Places
            
        Returns:
            Enriched facility with additional data
        """
        if not facility.name or not facility.place_id:
            return facility
        
        # Use parallel processing to fetch data from multiple sources
        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = {
                executor.submit(self._get_foursquare_data, facility): 'foursquare',
                executor.submit(self._get_yelp_data, facility): 'yelp',
                executor.submit(self._get_osm_data, facility): 'osm'
            }
            
            for future in as_completed(futures):
                source = futures[future]
                try:
                    data = future.result(timeout=10)
                    if data:
                        facility = self._merge_data(facility, data, source)
                except Exception as e:
                    logger.warning(f"Failed to get data from {source}: {e}")
        
        # Always try web scraping as fallback
        if facility.website:
            try:
                scraped_data = scrape_website_for_contacts(facility.website)
                facility = self._merge_scraped_data(facility, scraped_data)
            except Exception as e:
                logger.warning(f"Failed to scrape website: {e}")
        
        return facility
    
    def _get_foursquare_data(self, facility: Facility) -> Optional[Dict[str, Any]]:
        """Get data from Foursquare Places API."""
        if not self.sources['foursquare'].enabled or not self.sources['foursquare'].api_key:
            return None
        
        try:
            headers = {
                'Authorization': f"Bearer {self.sources['foursquare'].api_key}",
                'Accept': 'application/json'
            }
            
            # Search for the business
            params = {
                'query': facility.name,
                'near': facility.location,
                'limit': 1
            }
            
            response = requests.get(
                f"{self.sources['foursquare'].base_url}/search",
                headers=headers,
                params=params,
                timeout=5
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('results'):
                    return data['results'][0]
        
        except Exception as e:
            logger.warning(f"Foursquare API error: {e}")
        
        return None
    
    def _get_yelp_data(self, facility: Facility) -> Optional[Dict[str, Any]]:
        """Get data from Yelp Fusion API."""
        if not self.sources['yelp'].enabled or not self.sources['yelp'].api_key:
            return None
        
        try:
            headers = {
                'Authorization': f"Bearer {self.sources['yelp'].api_key}",
                'Accept': 'application/json'
            }
            
            # Search for the business
            params = {
                'term': facility.name,
                'location': facility.location,
                'limit': 1
            }
            
            response = requests.get(
                f"{self.sources['yelp'].base_url}/search",
                headers=headers,
                params=params,
                timeout=5
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('businesses'):
                    return data['businesses'][0]
        
        except Exception as e:
            logger.warning(f"Yelp API error: {e}")
        
        return None
    
    def _get_osm_data(self, facility: Facility) -> Optional[Dict[str, Any]]:
        """Get data from OpenStreetMap Overpass API."""
        if not self.sources['osm'].enabled:
            return None
        
        try:
            # Overpass QL query to find business
            query = f"""
            [out:json][timeout:5];
            (
              node["name"~"{facility.name}",i]["shop"~".*"];
              way["name"~"{facility.name}",i]["shop"~".*"];
              relation["name"~"{facility.name}",i]["shop"~".*"];
            );
            out center;
            """
            
            response = requests.post(
                self.sources['osm'].base_url,
                data=query,
                timeout=5
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('elements'):
                    return data['elements'][0]
        
        except Exception as e:
            logger.warning(f"OSM API error: {e}")
        
        return None
    
    def _merge_data(self, facility: Facility, data: Dict[str, Any], source: str) -> Facility:
        """Merge data from external source into facility."""
        try:
            if source == 'foursquare':
                # Foursquare data mapping
                if 'location' in data:
                    loc = data['location']
                    if 'address' in loc and not facility.formatted_address:
                        facility.formatted_address = loc['address']
                    if 'city' in loc and not facility.location:
                        facility.location = loc['city']
                
                if 'rating' in data and data['rating'] > facility.google_rating:
                    facility.google_rating = data['rating']
                
                if 'price' in data and not facility.price_level:
                    facility.price_level = data['price']
                
                if 'categories' in data:
                    categories = [cat.get('name', '') for cat in data['categories']]
                    if categories and not facility.types:
                        facility.types = categories
            
            elif source == 'yelp':
                # Yelp data mapping
                if 'location' in data:
                    loc = data['location']
                    if 'address1' in loc and not facility.formatted_address:
                        address_parts = [loc.get('address1', ''), loc.get('address2', '')]
                        facility.formatted_address = ', '.join(filter(None, address_parts))
                
                if 'rating' in data and data['rating'] > facility.google_rating:
                    facility.google_rating = data['rating']
                
                if 'price' in data and not facility.price_level:
                    facility.price_level = len(data['price'])
                
                if 'categories' in data:
                    categories = [cat.get('title', '') for cat in data['categories']]
                    if categories and not facility.types:
                        facility.types = categories
                
                if 'url' in data and not facility.url:
                    facility.url = data['url']
            
            elif source == 'osm':
                # OpenStreetMap data mapping
                if 'tags' in data:
                    tags = data['tags']
                    if 'addr:full' in tags and not facility.formatted_address:
                        facility.formatted_address = tags['addr:full']
                    if 'opening_hours' in tags and not facility.hours:
                        facility.hours = tags['opening_hours']
                    if 'website' in tags and not facility.website:
                        facility.website = tags['website']
                    if 'phone' in tags and not facility.formatted_phone_number:
                        facility.formatted_phone_number = tags['phone']
        
        except Exception as e:
            logger.warning(f"Error merging {source} data: {e}")
        
        return facility
    
    def _merge_scraped_data(self, facility: Facility, scraped_data) -> Facility:
        """Merge web scraped data into facility."""
        try:
            if scraped_data.email and not facility.email:
                facility.email = scraped_data.email
            if scraped_data.whatsapp and not facility.whatsapp_number:
                facility.whatsapp_number = scraped_data.whatsapp
            if scraped_data.instagram and not facility.instagram_id:
                facility.instagram_id = scraped_data.instagram
            if scraped_data.established_year and not facility.established_year:
                facility.established_year = scraped_data.established_year
        except Exception as e:
            logger.warning(f"Error merging scraped data: {e}")
        
        return facility


# Global instance
data_aggregator = DataAggregator()
