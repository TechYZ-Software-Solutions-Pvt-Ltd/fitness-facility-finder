"""
Google Places API service for searching and retrieving facility information.
"""

import requests
import time
import logging
import streamlit as st
from typing import List, Dict, Any, Optional, Tuple

from config.settings import settings
from models.facility import Facility, SearchQuery, SearchResult, ContactInfo
from utils.security import check_rate_limit, increment_request_count, secure_log_request
from utils.web_scraper import scrape_website_for_contacts
from components.settings_modal import get_fields_string

logger = logging.getLogger(__name__)


class PlacesService:
    """Service for interacting with Google Places API."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = settings.get_google_places_url("")
    
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
                error_message=f"Rate limit exceeded. Maximum {settings.security.max_requests_per_session} requests per {settings.security.session_timeout_minutes} minutes."
            )
        
        try:
            # Get initial results
            places = self._get_places_from_api(query.to_google_query(), query.max_results)
            
            if not places:
                # Try to provide more specific error message
                error_msg = "No facilities found for the given search criteria. "
                error_msg += f"Query: '{query.to_google_query()}'. "
                error_msg += "This could be due to: 1) No facilities in the area, 2) API quota exceeded, 3) Invalid location, or 4) API key issues."
                
                # Add debug information
                with st.expander("🔧 Debug Information", expanded=False):
                    st.write(f"**Search Query:** `{query.to_google_query()}`")
                    st.write(f"**API URL:** `{self.base_url}textsearch/json`")
                    st.write(f"**API Key:** `{self.api_key[:10]}...` (first 10 characters)")
                    st.write("**Troubleshooting Tips:**")
                    st.write("1. Try a more common location like 'New York, USA' or 'London, UK'")
                    st.write("2. Check if your API key has Places API enabled")
                    st.write("3. Verify you have sufficient API quota")
                    st.write("4. Try different business types like 'Fitness Centre' or 'Health Club'")
                
                return SearchResult(
                    facilities=[],
                    total_found=0,
                    search_query=query,
                    timestamp=time.time(),
                    success=False,
                    error_message=error_msg
                )
            
            # Process places and get detailed information
            facilities = self._process_places(places, query.city)
            
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
            return False, f"Rate limit exceeded. Maximum {settings.security.max_requests_per_session} requests per {settings.security.session_timeout_minutes} minutes."
        
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
            'User-Agent': settings.api.user_agent,
            'Accept': 'application/json'
        }
        
        all_places = []
        
        try:
            response = requests.get(
                url, 
                params=params, 
                headers=headers, 
                timeout=settings.security.request_timeout_seconds
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
            
            # Handle pagination
            while 'next_page_token' in data and len(all_places) < max_results:
                if not check_rate_limit():
                    break
                
                time.sleep(2)  # Required delay for next_page_token
                params['pagetoken'] = data['next_page_token']
                
                response = requests.get(
                    url, 
                    params=params, 
                    headers=headers, 
                    timeout=settings.security.request_timeout_seconds
                )
                response.raise_for_status()
                
                data = response.json()
                increment_request_count()
                
                if data.get('status') != 'OK':
                    break
                
                places = data.get('results', [])
                all_places.extend(places)
            
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
        """Process raw place data and enrich with detailed information."""
        facilities = []
        
        for place in places:
            try:
                # Get detailed information
                details = self._get_place_details(place['place_id'])
                
                if not details:
                    continue
                
                # Create facility from details
                facility = Facility.from_google_place(details, location)
                
                # Scrape website for additional contact info
                if facility.website:
                    contact_info = scrape_website_for_contacts(facility.website)
                    facility.email = contact_info.email
                    facility.whatsapp_number = contact_info.whatsapp
                    facility.instagram_id = contact_info.instagram
                    facility.established_year = contact_info.established_year
                
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
    
    def _get_place_details(self, place_id: str) -> Optional[Dict[str, Any]]:
        """Get detailed information for a specific place."""
        if not check_rate_limit():
            return None
        
        url = f"{self.base_url}details/json"
        params = {
            'place_id': place_id,
            'fields': get_fields_string(),
            'key': self.api_key
        }
        headers = {
            'User-Agent': settings.api.user_agent,
            'Accept': 'application/json'
        }
        
        try:
            response = requests.get(
                url, 
                params=params, 
                headers=headers, 
                timeout=settings.security.request_timeout_seconds
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
