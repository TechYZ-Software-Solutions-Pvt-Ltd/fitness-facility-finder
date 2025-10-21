"""
Google Places API service for searching and retrieving facility information.
"""

import requests
import time
import logging
from typing import List, Dict, Any, Optional, Tuple

# Configuration constants (replacing deleted config.settings)
GOOGLE_PLACES_BASE_URL = "https://maps.googleapis.com/maps/api/place"
USER_AGENT = "Fitness-Facility-Finder/2.0"
MAX_RESULTS_LIMIT = 60
DEFAULT_MAX_RESULTS = 20
from src.app.models.facility import Facility, SearchQuery, SearchResult, ContactInfo
from src.app.utils.security import check_rate_limit, increment_request_count, secure_log_request
from src.app.utils.web_scraper import scrape_website_for_contacts

logger = logging.getLogger(__name__)


class PlacesService:
    """Service for interacting with Google Places API."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = GOOGLE_PLACES_BASE_URL
    
    def search_places(self, query: SearchQuery) -> SearchResult:
        """
        Search for places using Google Places API.
        
        Args:
            query: SearchQuery object with search parameters
            
        Returns:
            SearchResult object with found facilities
        """
        if not check_rate_limit():
            return SearchResult(
                facilities=[],
                total_found=0,
                search_query=query,
                timestamp=time.time(),
                success=False,
                error_message=f"Rate limit exceeded. Maximum 50 requests per 30 minutes."
            )
        
        try:
            # Get initial results
            places = self._get_places_from_api(query.to_google_query(), query.max_results)
            
            if not places:
                # Try to provide more specific error message
                error_msg = "No facilities found for the given search criteria. "
                error_msg += f"Query: '{query.to_google_query()}'. "
                error_msg += "This could be due to: 1) No facilities in the area, 2) API quota exceeded, 3) Invalid location, or 4) API key issues."
                
                # Debug UI removed to keep backend lean and headless
                
                return SearchResult(
                    facilities=[],
                    total_found=0,
                    search_query=query,
                    timestamp=time.time(),
                    success=False,
                    error_message=error_msg
                )
            
            # Build fast results from text search only
            facilities = self._process_places_basic(places, query.city, query.max_results)

            # Enrich with details for selected results within time budget
            facilities = self._enrich_facilities_with_details(facilities)
            
            secure_log_request("search_places", success=True)
            
            return SearchResult(
                facilities=facilities,
                total_found=len(facilities),
                search_query=query,
                timestamp=time.time(),
                success=True
            )
            
        except requests.RequestException as e:
            logger.error(f"Network error during search: {e}")
            secure_log_request("search_places", success=False, error_msg=f"Network error: {str(e)}")
            
            return SearchResult(
                facilities=[],
                total_found=0,
                search_query=query,
                timestamp=time.time(),
                success=False,
                error_message="Network error occurred. Please check your internet connection and try again."
            )
        except (ValueError, TypeError, KeyError) as e:
            logger.error(f"Data processing error during search: {e}")
            secure_log_request("search_places", success=False, error_msg=f"Data error: {str(e)}")
            
            return SearchResult(
                facilities=[],
                total_found=0,
                search_query=query,
                timestamp=time.time(),
                success=False,
                error_message="Data processing error occurred. Please try again with different search parameters."
            )
        except Exception as e:
            logger.error(f"Unexpected error during search: {e}")
            secure_log_request("search_places", success=False, error_msg=f"Unexpected error: {str(e)}")
            
            return SearchResult(
                facilities=[],
                total_found=0,
                search_query=query,
                timestamp=time.time(),
                success=False,
                error_message="An unexpected error occurred. Please try again later."
            )
    
    def verify_place(self, place_name: str, country: str) -> Tuple[bool, str]:
        """
        Verify if a place exists using Google Places API.
        
        Args:
            place_name: Name of the place to verify
            country: Country where the place should be located
            
        Returns:
            Tuple of (is_valid, message)
        """
        if not check_rate_limit():
            return False, f"Rate limit exceeded. Maximum 50 requests per 30 minutes."
        
        try:
            query = f"{place_name}, {country}"
            places = self._get_places_from_api(query, 1)
            
            if places:
                for place in places:
                    if country.lower() in place.get('formatted_address', '').lower():
                        return True, f"Verified: {place.get('formatted_address', '')}"
                return False, "Place not found in specified country"
            else:
                return False, "Place not found"
                
        except requests.RequestException as e:
            logger.error(f"Network error verifying place: {e}")
            return False, "Network error occurred while verifying place"
        except (ValueError, TypeError) as e:
            logger.error(f"Data error verifying place: {e}")
            return False, "Invalid place data provided"
        except Exception as e:
            logger.error(f"Unexpected error verifying place: {e}")
            return False, "An unexpected error occurred while verifying place"
    
    def _get_places_from_api(self, query: str, max_results: int) -> List[Dict[str, Any]]:
        """Get places from Google Places API with pagination support."""
        url = f"{self.base_url}textsearch/json"
        params = {'query': query, 'key': self.api_key}
        headers = {
            'User-Agent': USER_AGENT,
            'Accept': 'application/json'
        }
        
        all_places = []
        
        try:
            response = requests.get(
                url, 
                params=params, 
                headers=headers, 
                timeout=min(8, 15)
            )
            response.raise_for_status()
            
            data = response.json()
            increment_request_count()
            
            if data.get('status') != 'OK':
                error_status = data.get('status')
                error_message = data.get('error_message', 'No error message provided')
                logger.warning(f"Google Places API error: {error_status} - {error_message}")
                
                # Log the query that failed for debugging
                logger.warning(f"Failed query: {query}")
                
                return []
            
            places = data.get('results', [])
            all_places.extend(places)
            
            # Skip pagination to keep responses fast; first page only
            
            return all_places[:max_results]
            
        except requests.RequestException as e:
            logger.error(f"Request error: {e}")
            return []
        except (ValueError, TypeError, KeyError) as e:
            logger.error(f"Data processing error: {e}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return []
    
    def _process_places(self, places: List[Dict[str, Any]], location: str) -> List[Facility]:
        """Process raw place data and enrich with detailed information under a time budget."""
        facilities: List[Facility] = []
        start_time = time.time()
        time_budget_seconds = 20
        
        max_details = 6
        for idx, place in enumerate(places):
            if idx >= max_details:
                break
            # stop if nearing time budget
            if time.time() - start_time > time_budget_seconds:
                break
            try:
                # Get detailed information
                details = self._get_place_details(place['place_id'])
                
                if not details:
                    continue
                
                # Create facility from details
                facility = Facility.from_google_place(details, location)
                
                # Enable comprehensive data enrichment
                try:
                    from services.enrichment_service import enrichment_service
                    enrichment_result = enrichment_service.enrich_facility(facility)
                    facility = enrichment_result.facility
                    logger.info(f"Enriched facility {facility.name} using sources: {enrichment_result.sources_used}")
                except Exception as e:
                    logger.warning(f"Failed to enrich facility {facility.name}: {e}")
                    # Fallback to basic web scraping
                    if facility.website:
                        try:
                            from utils.web_scraper import scrape_website_for_contacts
                            scraped_data = scrape_website_for_contacts(facility.website)
                            
                            if scraped_data.email:
                                facility.email = scraped_data.email
                            if scraped_data.whatsapp:
                                facility.whatsapp_number = scraped_data.whatsapp
                            if scraped_data.instagram:
                                facility.instagram_id = scraped_data.instagram
                            if scraped_data.established_year:
                                facility.established_year = scraped_data.established_year
                        except Exception as scrape_error:
                            logger.warning(f"Failed to scrape website {facility.website}: {scrape_error}")
                
                # Only add facilities with valid names
                if facility.name.strip():
                    facilities.append(facility)
                    
            except (ValueError, TypeError, KeyError) as e:
                logger.warning(f"Data error processing place {place.get('place_id', 'unknown')}: {e}")
                continue
            except Exception as e:
                logger.warning(f"Unexpected error processing place {place.get('place_id', 'unknown')}: {e}")
                continue
        
        return facilities

    def _process_places_basic(self, places: List[Dict[str, Any]], location: str, limit: int) -> List[Facility]:
        """Build basic facility info from text search results only (no details requests)."""
        facilities: List[Facility] = []
        for place in places[: max(0, limit)]:
            try:
                name = place.get('name', '')
                if not name:
                    continue
                facility = Facility(
                    name=name,
                    address=place.get('formatted_address') or place.get('vicinity', ''),
                    google_rating=place.get('rating', 0.0) or 0.0,
                    website='',
                    place_id=place.get('place_id', ''),
                    location=location,
                    user_ratings_total=place.get('user_ratings_total', 0),
                    business_status=place.get('business_status', ''),
                    types=place.get('types', []) or [],
                    geometry=place.get('geometry', {}) or {}
                )
                facilities.append(facility)
            except Exception:
                continue
        return facilities

    def _enrich_facilities_with_details(self, facilities: List[Facility]) -> List[Facility]:
        """Fetch details for facilities within a strict time budget to populate selected fields (phone, website, etc)."""
        start_time = time.time()
        time_budget_seconds = 20
        per_request_timeout_seconds = 6
        enriched: List[Facility] = []

        for idx, f in enumerate(facilities):
            if time.time() - start_time > time_budget_seconds:
                # Out of budget; return what we have (mix of enriched/unenriched)
                enriched.extend(facilities[idx:])
                break
            if not f.place_id:
                enriched.append(f)
                continue

            # Reuse _get_place_details (already has timeout caps)
            details = self._get_place_details(f.place_id)
            if not details:
                enriched.append(f)
                continue

            # Merge details into existing record
            try:
                f.formatted_address = details.get('formatted_address', f.formatted_address)
                f.international_phone_number = details.get('international_phone_number', f.international_phone_number)
                f.formatted_phone_number = details.get('formatted_phone_number', f.formatted_phone_number)
                f.website = details.get('website', f.website)
                f.google_rating = details.get('rating', f.google_rating) or f.google_rating
                f.user_ratings_total = details.get('user_ratings_total', f.user_ratings_total)
                f.business_status = details.get('business_status', f.business_status)
                f.types = details.get('types', f.types) or f.types
                f.geometry = details.get('geometry', f.geometry) or f.geometry
                
                # Enable website scraping for additional data
                if f.website:
                    try:
                        from utils.web_scraper import scrape_website_for_contacts
                        scraped_data = scrape_website_for_contacts(f.website)
                        
                        # Merge scraped data into facility
                        if scraped_data.email:
                            f.email = scraped_data.email
                        if scraped_data.whatsapp:
                            f.whatsapp_number = scraped_data.whatsapp
                        if scraped_data.instagram:
                            f.instagram_id = scraped_data.instagram
                        if scraped_data.established_year:
                            f.established_year = scraped_data.established_year
                            
                    except Exception as e:
                        logger.warning(f"Failed to scrape website {f.website}: {e}")
                        # Continue without scraped data
                        
            except Exception:
                pass

            enriched.append(f)

        return enriched
    
    def _get_place_details(self, place_id: str) -> Optional[Dict[str, Any]]:
        """Get detailed information for a specific place."""
        if not check_rate_limit():
            return None
        
        url = f"{self.base_url}details/json"
        # Request only essential fields to reduce latency
        fields = (
            "place_id,name,formatted_address,international_phone_number,"
            "formatted_phone_number,website,rating,user_ratings_total,"
            "business_status,types,geometry,url"
        )
        params = {
            'place_id': place_id,
            'fields': fields,
            'key': self.api_key
        }
        headers = {
            'User-Agent': USER_AGENT,
            'Accept': 'application/json'
        }
        
        try:
            response = requests.get(
                url, 
                params=params, 
                headers=headers, 
                timeout=min(6, 15)
            )
            response.raise_for_status()
            
            data = response.json()
            increment_request_count()
            
            if data.get('status') == 'OK':
                return data.get('result', {})
            else:
                logger.warning(f"Place details API error: {data.get('status')}")
                return None
                
        except requests.RequestException as e:
            logger.error(f"Request error getting place details: {e}")
            return None
        except (ValueError, TypeError, KeyError) as e:
            logger.error(f"Data error getting place details: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error getting place details: {e}")
            return None
