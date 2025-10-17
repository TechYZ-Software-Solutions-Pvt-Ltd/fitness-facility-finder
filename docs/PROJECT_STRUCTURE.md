# Project Structure

*Auto-generated on 2025-10-16 19:56:30*

## Overview
This document shows the current project structure of the Facility Finder application.

## Directory Structure

```
Facility Search Production/
├── requirements.txt                # Python dependencies
├── README.md                       # Main documentation
├── LICENSE                         # MIT License
├── config/
│   └── env.example                 # Environment variables template
├── docs/                           # Documentation
│   ├── API_DOCUMENTATION.md        # Auto-generated API docs
│   ├── PROJECT_STRUCTURE.md        # This file
│   └── GOOGLE_PLACES_API_SETUP_GUIDE.txt # API setup guide
├── src/                            # Source code
│   └── app/                        # Main application
│       ├── main.py                 # Streamlit app entry point
│       ├── components/             # UI components
│       │   ├── __init__.py
│       │   ├── header.py           # Header component
│       │   ├── unified_search_form.py # Unified search form component
│       │   ├── results_display.py  # Results display component
│       │   ├── settings_modal.py   # Settings modal component
│       │   └── footer.py           # Footer component
│       ├── services/               # Business logic
│       │   ├── __init__.py
│       │   └── places_service.py   # Google Places API service
│       ├── models/                 # Data models
│       │   ├── __init__.py
│       │   ├── facility.py         # Facility data models
│       │   └── data.py             # Static data constants
│       ├── utils/                  # Utilities
│       │   ├── __init__.py
│       │   ├── security.py         # Security utilities
│       │   └── web_scraper.py      # Web scraping utilities
│       └── config/                 # Configuration
│           ├── __init__.py
│           └── settings.py         # Application settings
```

## File Descriptions

### Core Application Files
- **`src/app/main.py`**: Main Streamlit application entry point with UI logic
- **`requirements.txt`**: Python package dependencies

### Components (`src/app/components/`)
- **`header.py`**: Application header with styling and mobile responsiveness
- **`unified_search_form.py`**: Unified search form with hierarchical location and business type selection
- **`results_display.py`**: Results table and download functionality
- **`settings_modal.py`**: Settings modal with field selection and API setup guide
- **`footer.py`**: Footer with security info and branding

### Services (`src/app/services/`)
- **`places_service.py`**: Google Places API integration and search logic

### Models (`src/app/models/`)
- **`facility.py`**: Data models for facilities, search queries, and results
- **`data.py`**: Static data constants (countries, cities, facility types)

### Utilities (`src/app/utils/`)
- **`security.py`**: Security utilities (validation, sanitization, rate limiting)
- **`web_scraper.py`**: Web scraping for contact information extraction
- **`doc_generator.py`**: Automated documentation generation

### Configuration (`src/app/config/`)
- **`settings.py`**: Centralized configuration management

### Documentation (`docs/`)
- **`API_DOCUMENTATION.md`**: Auto-generated API documentation
- **`PROJECT_STRUCTURE.md`**: This file - project structure documentation
- **`COMPONENT_DOCUMENTATION.md`**: Detailed component documentation
- **`CHANGELOG.md`**: Change log with version history

### Tests (`tests/`)
- **`test_basic.py`**: Basic functionality tests for all modules

## Architecture Principles

1. **Separation of Concerns**: Each module has a single responsibility
2. **Modularity**: Components can be easily modified or replaced
3. **Testability**: Each module can be tested independently
4. **Maintainability**: Clear structure makes code easy to maintain
5. **Scalability**: Easy to add new features without affecting existing code

## Development Guidelines

1. **New Features**: Add new components in appropriate directories
2. **Documentation**: Update documentation when making changes
3. **Testing**: Add tests for new functionality
4. **Configuration**: Use centralized settings for configuration
5. **Security**: Follow security best practices in all modules

---
*This structure documentation is automatically generated and updated with code changes.*
