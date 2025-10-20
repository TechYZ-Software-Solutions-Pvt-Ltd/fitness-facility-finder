"""
Comprehensive data enrichment service using multiple legal data sources.
"""

import os
import requests
import time
import logging
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor, as_completed
import json

from ..models.facility import Facility
from ..utils.web_scraper import scrape_website_for_contacts

logger = logging.getLogger(__name__)


@dataclass
class EnrichmentResult:
    """Result of data enrichment process."""
    facility: Facility
    sources_used: List[str]
    confidence_score: float
    data_quality: str


class DataEnrichmentService:
    """
    Comprehensive data enrichment using multiple legal sources.
    """
    
    def __init__(self):
        self.api_keys = self._load_api_keys()
        self.rate_limits = {}
        self.last_request_time = {}
    
    def _load_api_keys(self) -> Dict[str, str]:
        """Load API keys from environment variables."""
        return {
            'foursquare': os.getenv('FOURSQUARE_API_KEY', ''),
            'yelp': os.getenv('YELP_API_KEY', ''),
            'facebook': os.getenv('FACEBOOK_APP_ID', ''),
            'instagram': os.getenv('INSTAGRAM_APP_ID', ''),
            'linkedin': os.getenv('LINKEDIN_CLIENT_ID', '')
        }
    
    def enrich_facility(self, facility: Facility) -> EnrichmentResult:
        """
        Enrich a facility with data from multiple legal sources.
        
        Args:
            facility: Basic facility from Google Places
            
        Returns:
            EnrichmentResult with enriched facility and metadata
        """
        if not facility.name:
            return EnrichmentResult(facility, [], 0.0, "insufficient_data")
        
        sources_used = []
        confidence_score = 0.0
        enrichment_data = {}
        
        # Parallel data fetching from multiple sources
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = {
                executor.submit(self._enrich_from_foursquare, facility): 'foursquare',
                executor.submit(self._enrich_from_yelp, facility): 'yelp',
                executor.submit(self._enrich_from_osm, facility): 'osm',
                executor.submit(self._enrich_from_web_scraping, facility): 'web_scraping'
            }
            
            for future in as_completed(futures):
                source = futures[future]
                try:
                    data = future.result(timeout=15)
                    if data:
                        enrichment_data[source] = data
                        sources_used.append(source)
                        confidence_score += 0.2  # Each source adds 20% confidence
                except Exception as e:
                    logger.warning(f"Failed to enrich from {source}: {e}")
        
        # Merge all enrichment data
        enriched_facility = self._merge_enrichment_data(facility, enrichment_data)
        
        # Calculate data quality
        data_quality = self._assess_data_quality(enriched_facility, sources_used)
        
        return EnrichmentResult(
            facility=enriched_facility,
            sources_used=sources_used,
            confidence_score=min(confidence_score, 1.0),
            data_quality=data_quality
        )
    
    def _enrich_from_foursquare(self, facility: Facility) -> Optional[Dict[str, Any]]:
        """Enrich facility with Foursquare data."""
        if not self.api_keys['foursquare']:
            return None
        
        try:
            headers = {
                'Authorization': f"Bearer {self.api_keys['foursquare']}",
                'Accept': 'application/json'
            }
            
            params = {
                'query': facility.name,
                'near': facility.location or facility.address,
                'limit': 1,
                'fields': 'name,location,rating,price,categories,contact,website,hours'
            }
            
            response = requests.get(
                'https://api.foursquare.com/v3/places/search',
                headers=headers,
                params=params,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('results'):
                    return {
                        'source': 'foursquare',
                        'data': data['results'][0],
                        'confidence': 0.8
                    }
        
        except Exception as e:
            logger.warning(f"Foursquare enrichment failed: {e}")
        
        return None
    
    def _enrich_from_yelp(self, facility: Facility) -> Optional[Dict[str, Any]]:
        """Enrich facility with Yelp data."""
        if not self.api_keys['yelp']:
            return None
        
        try:
            headers = {
                'Authorization': f"Bearer {self.api_keys['yelp']}",
                'Accept': 'application/json'
            }
            
            params = {
                'term': facility.name,
                'location': facility.location or facility.address,
                'limit': 1
            }
            
            response = requests.get(
                'https://api.yelp.com/v3/businesses/search',
                headers=headers,
                params=params,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('businesses'):
                    return {
                        'source': 'yelp',
                        'data': data['businesses'][0],
                        'confidence': 0.9
                    }
        
        except Exception as e:
            logger.warning(f"Yelp enrichment failed: {e}")
        
        return None
    
    def _enrich_from_osm(self, facility: Facility) -> Optional[Dict[str, Any]]:
        """Enrich facility with OpenStreetMap data."""
        try:
            # Overpass QL query
            query = f"""
            [out:json][timeout:10];
            (
              node["name"~"{facility.name}",i]["shop"~".*"];
              way["name"~"{facility.name}",i]["shop"~".*"];
              relation["name"~"{facility.name}",i]["shop"~".*"];
            );
            out center;
            """
            
            response = requests.post(
                'https://overpass-api.de/api/interpreter',
                data=query,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('elements'):
                    return {
                        'source': 'osm',
                        'data': data['elements'][0],
                        'confidence': 0.7
                    }
        
        except Exception as e:
            logger.warning(f"OSM enrichment failed: {e}")
        
        return None
    
    def _enrich_from_web_scraping(self, facility: Facility) -> Optional[Dict[str, Any]]:
        """Enrich facility with web scraping data."""
        if not facility.website:
            return None
        
        try:
            scraped_data = scrape_website_for_contacts(facility.website)
            if scraped_data and not scraped_data.is_empty():
                return {
                    'source': 'web_scraping',
                    'data': scraped_data,
                    'confidence': 0.6
                }
        
        except Exception as e:
            logger.warning(f"Web scraping enrichment failed: {e}")
        
        return None
    
    def _merge_enrichment_data(self, facility: Facility, enrichment_data: Dict[str, Any]) -> Facility:
        """Merge all enrichment data into facility."""
        for source, data in enrichment_data.items():
            try:
                if source == 'foursquare':
                    facility = self._merge_foursquare_data(facility, data['data'])
                elif source == 'yelp':
                    facility = self._merge_yelp_data(facility, data['data'])
                elif source == 'osm':
                    facility = self._merge_osm_data(facility, data['data'])
                elif source == 'web_scraping':
                    facility = self._merge_scraped_data(facility, data['data'])
            except Exception as e:
                logger.warning(f"Error merging {source} data: {e}")
        
        return facility
    
    def _merge_foursquare_data(self, facility: Facility, data: Dict[str, Any]) -> Facility:
        """Merge Foursquare data into facility."""
        try:
            # Location data
            if 'location' in data:
                loc = data['location']
                if 'address' in loc and not facility.formatted_address:
                    facility.formatted_address = loc['address']
                if 'city' in loc and not facility.location:
                    facility.location = loc['city']
            
            # Rating (use highest rating)
            if 'rating' in data and data['rating'] > facility.google_rating:
                facility.google_rating = data['rating']
            
            # Price level
            if 'price' in data and not facility.price_level:
                facility.price_level = data['price']
            
            # Categories
            if 'categories' in data and not facility.types:
                categories = [cat.get('name', '') for cat in data['categories']]
                facility.types = categories
            
            # Contact info
            if 'contact' in data:
                contact = data['contact']
                if 'phone' in contact and not facility.formatted_phone_number:
                    facility.formatted_phone_number = contact['phone']
                if 'website' in contact and not facility.website:
                    facility.website = contact['website']
            
            # Hours
            if 'hours' in data and not facility.hours:
                hours = data['hours']
                if 'display' in hours:
                    facility.hours = hours['display']
        
        except Exception as e:
            logger.warning(f"Error merging Foursquare data: {e}")
        
        return facility
    
    def _merge_yelp_data(self, facility: Facility, data: Dict[str, Any]) -> Facility:
        """Merge Yelp data into facility."""
        try:
            # Location data
            if 'location' in data:
                loc = data['location']
                if 'address1' in loc and not facility.formatted_address:
                    address_parts = [loc.get('address1', ''), loc.get('address2', '')]
                    facility.formatted_address = ', '.join(filter(None, address_parts))
                if 'city' in loc and not facility.location:
                    facility.location = loc['city']
            
            # Rating (use highest rating)
            if 'rating' in data and data['rating'] > facility.google_rating:
                facility.google_rating = data['rating']
            
            # Price level
            if 'price' in data and not facility.price_level:
                facility.price_level = len(data['price'])
            
            # Categories
            if 'categories' in data and not facility.types:
                categories = [cat.get('title', '') for cat in data['categories']]
                facility.types = categories
            
            # Contact info
            if 'phone' in data and not facility.formatted_phone_number:
                facility.formatted_phone_number = data['phone']
            if 'url' in data and not facility.url:
                facility.url = data['url']
            
            # Hours
            if 'hours' in data and not facility.hours:
                hours = data['hours']
                if isinstance(hours, list) and hours:
                    facility.hours = hours[0].get('open', [])
        
        except Exception as e:
            logger.warning(f"Error merging Yelp data: {e}")
        
        return facility
    
    def _merge_osm_data(self, facility: Facility, data: Dict[str, Any]) -> Facility:
        """Merge OpenStreetMap data into facility."""
        try:
            if 'tags' in data:
                tags = data['tags']
                
                # Address
                if 'addr:full' in tags and not facility.formatted_address:
                    facility.formatted_address = tags['addr:full']
                elif 'addr:street' in tags and not facility.formatted_address:
                    street = tags['addr:street']
                    city = tags.get('addr:city', '')
                    facility.formatted_address = f"{street}, {city}".strip(', ')
                
                # Hours
                if 'opening_hours' in tags and not facility.hours:
                    facility.hours = tags['opening_hours']
                
                # Website
                if 'website' in tags and not facility.website:
                    facility.website = tags['website']
                
                # Phone
                if 'phone' in tags and not facility.formatted_phone_number:
                    facility.formatted_phone_number = tags['phone']
                
                # Categories
                if 'shop' in tags and not facility.types:
                    facility.types = [tags['shop']]
        
        except Exception as e:
            logger.warning(f"Error merging OSM data: {e}")
        
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
    
    def _assess_data_quality(self, facility: Facility, sources_used: List[str]) -> str:
        """Assess the quality of enriched data."""
        quality_score = 0
        
        # Basic info
        if facility.name:
            quality_score += 1
        if facility.formatted_address or facility.address:
            quality_score += 1
        if facility.formatted_phone_number or facility.international_phone_number:
            quality_score += 1
        if facility.website:
            quality_score += 1
        if facility.google_rating > 0:
            quality_score += 1
        
        # Additional info
        if facility.email:
            quality_score += 1
        if facility.hours:
            quality_score += 1
        if facility.types:
            quality_score += 1
        if facility.business_status:
            quality_score += 1
        
        # Social media
        social_media_count = sum([
            bool(facility.facebook),
            bool(facility.twitter),
            bool(facility.linkedin),
            bool(facility.youtube),
            bool(facility.instagram_id)
        ])
        quality_score += min(social_media_count, 2)
        
        # Source diversity bonus
        quality_score += min(len(sources_used), 3)
        
        if quality_score >= 8:
            return "excellent"
        elif quality_score >= 6:
            return "good"
        elif quality_score >= 4:
            return "fair"
        else:
            return "poor"


# Global instance
enrichment_service = DataEnrichmentService()
