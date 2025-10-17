"""
Configuration management for Facility Finder.
All settings are centralized here for easy management.
"""

import os
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass


@dataclass
class SecurityConfig:
    """Security-related configuration."""
    max_requests_per_session: int = 50
    session_timeout_minutes: int = 30
    request_timeout_seconds: int = 15
    api_key_min_length: int = 20
    api_key_max_length: int = 200


@dataclass
class APIConfig:
    """API-related configuration."""
    google_places_base_url: str = "https://maps.googleapis.com/maps/api/place"
    user_agent: str = "Fitness-Facility-Finder/2.0"
    max_results_limit: int = 60
    default_max_results: int = 20


@dataclass
class UIConfig:
    """UI-related configuration."""
    app_title: str = "JustList"
    app_description: str = "Find facilities near you"
    default_country: str = "Bahrain"
    default_city: str = "Manama"


@dataclass
class FieldConfig:
    """Configuration for Google Places API fields to fetch."""
    
    # Available Google Places API fields (only fields that Google actually provides)
    AVAILABLE_FIELDS = {
        "Essential Information": {
            "name": "Business Name",
            "formatted_address": "Address",
            "international_phone_number": "Phone Number",
            "website": "Website"
        },
        "Location Details": {
            "geometry": "Coordinates (Lat/Lng)",
            "vicinity": "Area/Vicinity",
            "place_id": "Place ID",
            "url": "Google Maps URL"
        },
        "Business Information": {
            "rating": "Rating",
            "user_ratings_total": "Total Reviews",
            "types": "Business Types",
            "price_level": "Price Level"
        },
        "Additional Details": {
            "formatted_phone_number": "Formatted Phone",
            "opening_hours": "Opening Hours",
            "business_status": "Business Status",
            "plus_code": "Plus Code"
        }
    }
    
    # Default fields to fetch (most essential information)
    default_fields = [
        "name", "international_phone_number", "formatted_address", 
        "website", "rating", "geometry"
    ]
    
    # Field descriptions for help text (only for fields Google actually provides)
    field_descriptions = {
        "name": "The business name as it appears on Google Maps",
        "formatted_address": "Complete address in a readable format",
        "international_phone_number": "Phone number in international format (+country code)",
        "website": "Official business website URL",
        "geometry": "Latitude and longitude coordinates for mapping",
        "vicinity": "General area or neighborhood name",
        "place_id": "Unique Google identifier for the place",
        "url": "Direct link to Google Maps listing",
        "rating": "Average rating from 1-5 stars",
        "user_ratings_total": "Total number of customer reviews",
        "types": "Business categories (e.g., gym, restaurant, etc.)",
        "price_level": "Price range indicator (0-4, where 4 is most expensive)",
        "formatted_phone_number": "Phone number in local format",
        "opening_hours": "Business hours and days open",
        "business_status": "Whether business is operational (OPERATIONAL, CLOSED_TEMPORARILY, etc.)",
        "plus_code": "Open Location Code for precise location"
    }


class Settings:
    """Main settings class that combines all configuration."""
    
    def __init__(self):
        self.security = SecurityConfig()
        self.api = APIConfig()
        self.ui = UIConfig()
        self.fields = FieldConfig()
        
        # Load environment variables
        self._load_env_vars()
    
    def _load_env_vars(self):
        """Load configuration from environment variables."""
        # Security settings
        self.security.max_requests_per_session = int(
            os.getenv('MAX_REQUESTS_PER_SESSION', self.security.max_requests_per_session)
        )
        self.security.session_timeout_minutes = int(
            os.getenv('SESSION_TIMEOUT_MINUTES', self.security.session_timeout_minutes)
        )
        
        # API settings
        self.api.max_results_limit = int(
            os.getenv('MAX_RESULTS_LIMIT', self.api.max_results_limit)
        )
        
        # UI settings
        self.ui.app_title = os.getenv('APP_TITLE', self.ui.app_title)
        self.ui.default_country = os.getenv('DEFAULT_COUNTRY', self.ui.default_country)
    
    def get_google_places_url(self, endpoint: str) -> str:
        """Get full Google Places API URL for given endpoint."""
        return f"{self.api.google_places_base_url}/{endpoint}"
    
    def validate_api_key(self, api_key: str) -> Tuple[bool, str]:
        """Validate API key format."""
        if not api_key:
            return False, "API key is required"
        
        if len(api_key) < self.security.api_key_min_length or len(api_key) > self.security.api_key_max_length:
            return False, f"API key must be between {self.security.api_key_min_length} and {self.security.api_key_max_length} characters"
        
        # Google API key format validation
        import re
        if not re.match(r'^AIza[0-9A-Za-z_-]{35}$', api_key):
            return False, "Invalid Google API key format"
        
        return True, "Valid API key"


# Global settings instance
settings = Settings()