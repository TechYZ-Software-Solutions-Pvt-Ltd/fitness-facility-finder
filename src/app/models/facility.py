"""
Data models for fitness facilities and related entities.
"""

from dataclasses import dataclass
from typing import Optional, List, Dict, Any, Union
from datetime import datetime


@dataclass
class Facility:
    """Represents a fitness facility with all its details."""
    name: str
    contact_number: str = ""
    whatsapp_number: str = ""
    email: str = ""
    established_year: str = ""
    location: str = ""
    address: str = ""
    google_rating: float = 0.0
    instagram_id: str = ""
    website: str = ""
    place_id: str = ""
    
    # Google Places API fields (only fields that Google actually provides)
    formatted_address: str = ""
    international_phone_number: str = ""
    formatted_phone_number: str = ""
    url: str = ""
    user_ratings_total: int = 0
    price_level: int = 0
    business_status: str = ""
    types: List[str] = None
    vicinity: str = ""
    plus_code: str = ""
    geometry: Dict[str, Any] = None
    
    # Additional scraped fields from websites
    facebook: str = ""
    twitter: str = ""
    linkedin: str = ""
    youtube: str = ""
    phone: str = ""
    hours: str = ""
    description: str = ""
    founded: str = ""
    
    def __post_init__(self):
        """Initialize default values for mutable fields."""
        if self.types is None:
            self.types = []
        if self.geometry is None:
            self.geometry = {}
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert facility to dictionary for DataFrame creation."""
        result = {
            'Facility Name': self.name,
            'Contact Number': self.contact_number,
            'WhatsApp Number': self.whatsapp_number,
            'email ID': self.email,
            'Established Year': self.established_year,
            'Location': self.location,
            'Address': self.address,
            'Google Rating': self.google_rating,
            'Instagram id': self.instagram_id,
            'Website': self.website,
            'Place ID': self.place_id
        }
        
        # Add additional fields if they have values
        if self.formatted_address:
            result['Formatted Address'] = self.formatted_address
        if self.international_phone_number:
            result['International Phone'] = self.international_phone_number
        if self.formatted_phone_number:
            result['Formatted Phone'] = self.formatted_phone_number
        if self.url:
            result['Google Maps URL'] = self.url
        if self.user_ratings_total > 0:
            result['Total Reviews'] = self.user_ratings_total
        if self.price_level > 0:
            result['Price Level'] = self.price_level
        if self.business_status:
            result['Business Status'] = self.business_status
        if self.types:
            result['Business Types'] = ', '.join(self.types)
        if self.vicinity:
            result['Vicinity'] = self.vicinity
        if self.plus_code:
            result['Plus Code'] = self.plus_code
        if self.geometry and 'location' in self.geometry:
            lat = self.geometry['location'].get('lat', '')
            lng = self.geometry['location'].get('lng', '')
            if lat and lng:
                result['Coordinates'] = f"{lat}, {lng}"
        
        # Add scraped fields if they have values
        if self.facebook:
            result['Facebook'] = self.facebook
        if self.twitter:
            result['Twitter/X'] = self.twitter
        if self.linkedin:
            result['LinkedIn'] = self.linkedin
        if self.youtube:
            result['YouTube'] = self.youtube
        if self.phone:
            result['Additional Phone'] = self.phone
        if self.hours:
            result['Business Hours'] = self.hours
        if self.description:
            result['Description'] = self.description
        if self.founded:
            result['Founded'] = self.founded
        
        return result
    
    @classmethod
    def from_google_place(cls, place_data: Dict[str, Any], location: str) -> 'Facility':
        """Create Facility instance from Google Places API response."""
        return cls(
            name=place_data.get('name', ''),
            contact_number=place_data.get('international_phone_number', ''),
            address=place_data.get('formatted_address', ''),
            google_rating=place_data.get('rating', 0.0) or 0.0,
            website=place_data.get('website', ''),
            place_id=place_data.get('place_id', ''),
            location=location,
            # Additional fields
            formatted_address=place_data.get('formatted_address', ''),
            international_phone_number=place_data.get('international_phone_number', ''),
            formatted_phone_number=place_data.get('formatted_phone_number', ''),
            url=place_data.get('url', ''),
            user_ratings_total=place_data.get('user_ratings_total', 0),
            price_level=place_data.get('price_level', 0),
            business_status=place_data.get('business_status', ''),
            types=place_data.get('types', []),
            vicinity=place_data.get('vicinity', ''),
            plus_code=place_data.get('plus_code', {}).get('global_code', '') if place_data.get('plus_code') else '',
            geometry=place_data.get('geometry', {})
        )


@dataclass
class SearchQuery:
    """Represents a search query for facilities."""
    place_type: str
    city: str
    country: str
    max_results: int = 20
    
    def to_google_query(self) -> str:
        """Convert to Google Places API query format."""
        return f"{self.place_type} in {self.city}, {self.country}"
    
    def validate(self) -> tuple[bool, str]:
        """Validate search query parameters."""
        if not self.place_type or not self.place_type.strip():
            return False, "Business type is required"
        
        if not self.city or not self.city.strip():
            return False, "City is required"
        
        if not self.country or not self.country.strip():
            return False, "Country is required"
        
        if self.max_results < 1 or self.max_results > 60:
            return False, "Max results must be between 1 and 60"
        
        return True, "Valid query"


@dataclass
class ContactInfo:
    """Represents contact information extracted from website."""
    email: str = ""
    whatsapp: str = ""
    instagram: str = ""
    established_year: str = ""
    
    def is_empty(self) -> bool:
        """Check if contact info is empty."""
        return not any([self.email, self.whatsapp, self.instagram, self.established_year])


@dataclass
class SearchResult:
    """Represents the result of a facility search."""
    facilities: List[Facility]
    total_found: int
    search_query: SearchQuery
    timestamp: Union[datetime, float]
    success: bool = True
    error_message: str = ""
    
    def __post_init__(self):
        """Convert timestamp to datetime if it's a float."""
        if isinstance(self.timestamp, float):
            self.timestamp = datetime.fromtimestamp(self.timestamp)
    
    def to_dataframe_dict(self) -> List[Dict[str, Any]]:
        """Convert facilities to list of dictionaries for DataFrame."""
        return [facility.to_dict() for facility in self.facilities]
