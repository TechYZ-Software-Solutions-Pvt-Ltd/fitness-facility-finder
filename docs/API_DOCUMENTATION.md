# API Documentation

*Auto-generated on 2025-10-16 19:56:30*

## Overview
This document provides comprehensive API documentation for the Fitness Facility Finder application.

## Core Models

### Facility Model
```python
@dataclass
class Facility:
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
```

**Methods:**
- `to_dict() -> Dict[str, Any]`: Convert facility to dictionary for DataFrame creation
- `from_google_place(place_data: Dict[str, Any], location: str) -> Facility`: Create from Google Places API response

### SearchQuery Model
```python
@dataclass
class SearchQuery:
    place_type: str
    city: str
    country: str
    max_results: int = 20
```

**Methods:**
- `to_google_query() -> str`: Convert to Google Places API query format
- `validate() -> Tuple[bool, str]`: Validate search query parameters

### SearchResult Model
```python
@dataclass
class SearchResult:
    facilities: List[Facility]
    total_found: int
    search_query: SearchQuery
    timestamp: datetime
    success: bool = True
    error_message: str = ""
```

**Methods:**
- `to_dataframe_dict() -> List[Dict[str, Any]]`: Convert facilities to list of dictionaries for DataFrame

## Services

### PlacesService
Main service for interacting with Google Places API.

**Constructor:**
```python
def __init__(self, api_key: str)
```

**Methods:**
- `search_places(query: SearchQuery) -> SearchResult`: Search for places using Google Places API
- `verify_place(place_name: str, country: str) -> Tuple[bool, str]`: Verify if a place exists

## Utilities

### Security Utilities
- `sanitize_input(text: str) -> str`: Sanitize user input to prevent injection attacks
- `validate_api_key(api_key: str) -> Tuple[bool, str]`: Validate Google Places API key format
- `check_rate_limit() -> bool`: Check if user has exceeded rate limits
- `increment_request_count()`: Increment the request counter
- `secure_log_request(operation: str, success: bool = True, error_msg: str = "")`: Log requests securely

### Web Scraper Utilities
- `scrape_website_for_contacts(website: str) -> ContactInfo`: Extract contact information from website

## Configuration

### Settings
Centralized configuration management.

**SecurityConfig:**
- `max_requests_per_session: int = 50`
- `session_timeout_minutes: int = 30`
- `request_timeout_seconds: int = 15`

**APIConfig:**
- `google_places_base_url: str = "https://maps.googleapis.com/maps/api/place"`
- `max_results_limit: int = 60`
- `default_max_results: int = 20`

**UIConfig:**
- `app_title: str = "JustList"`
- `app_description: str = "Find fitness facilities near you"`
- `default_country: str = "Bahrain"`

## Components

### UI Components
- `render_header()`: Render the application header with styling
- `render_search_form() -> Tuple[str, str, str, str, int]`: Render the search form and return user inputs
- `render_search_button() -> bool`: Render the search button with styling
- `render_search_results(result: SearchResult)`: Render search results in a formatted display
- `render_footer()`: Render the application footer with security info and branding

## Data Constants

### Countries and Cities
- `COUNTRIES`: Dictionary of countries and their cities
- `INDIA_STATES_DISTRICTS`: Dictionary of Indian states and districts
- `FITNESS_TYPES`: List of fitness facility types

## Error Handling

The application includes comprehensive error handling:
- Input validation and sanitization
- API key validation
- Rate limiting
- Network error handling
- Graceful degradation

## Security Features

- API key protection
- Input sanitization
- Rate limiting (50 requests per 30 minutes)
- Secure logging
- Session management
- XSS protection

---
*This documentation is automatically generated and updated with code changes.*
