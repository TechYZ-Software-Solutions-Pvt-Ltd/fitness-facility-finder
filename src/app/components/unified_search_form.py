"""
Unified search form component with hierarchical location selection.
Country -> State/Province -> City/Town structure for all countries.
"""

import streamlit as st
from typing import Tuple, Optional

from ..models.data import UNIFIED_LOCATIONS, BUSINESS_CATEGORIES
from ..config.settings import settings


def render_unified_search_form() -> Tuple[str, str, str, str, int]:
    """
    Render the unified hierarchical search form and return user inputs.
    
    Returns:
        Tuple of (api_key, country, state, city, place_type, max_results)
    """
    # Check if search is in progress
    is_loading = st.session_state.get('search_in_progress', False)
    
    # API Key input with enhanced help
    api_key = st.text_input(
        'Google Places API Key *', 
        type='password', 
        help="Enter your Google Places API key. Don't have one? Check the settings sidebar for a complete setup guide! 📥", 
        placeholder="AIza...",
        disabled=is_loading
    )
    
    # Additional help text for API key
    if not api_key:
        st.info("💡 **Need an API key?** Open the settings sidebar and download the complete setup guide!")
    
    # Location selection with hierarchical structure
    st.markdown("#### 🌍 Location Selection")
    
    # Country selection
    country_options = list(UNIFIED_LOCATIONS.keys())
    if not country_options:
        st.error("No countries available. Please check the data configuration.")
        return "", "", "", "", 20
    
    country = st.selectbox(
        'Country *', 
        country_options, 
        index=0, 
        disabled=is_loading,
        help="Select your country"
    )
    
    # State/Province selection
    if country in UNIFIED_LOCATIONS:
        state_options = list(UNIFIED_LOCATIONS[country].keys())
        if not state_options:
            st.error(f"No states available for {country}. Please check the data configuration.")
            return "", "", "", "", 20
            
        state = st.selectbox(
            'State/Province *', 
            state_options, 
            index=0, 
            disabled=is_loading,
            help="Select your state or province"
        )
        
        # City/Town selection
        if state in UNIFIED_LOCATIONS[country]:
            city_options = UNIFIED_LOCATIONS[country][state] + ['Custom...']
            if not city_options or len(city_options) <= 1:  # Only 'Custom...' available
                st.error(f"No cities available for {state}, {country}. Please check the data configuration.")
                return "", "", "", "", 20
                
            city_selection = st.selectbox(
                'City/Town/Area *', 
                city_options, 
                index=0, 
                disabled=is_loading,
                help="Select your city, town, or area"
            )
            
            if city_selection == 'Custom...':
                city = st.text_input(
                    'Enter Custom City/Town/Area *', 
                    placeholder='Enter the name of your city/town/area',
                    disabled=is_loading
                )
            else:
                city = city_selection
        else:
            st.error(f"State '{state}' not found for {country}. Please select a different state.")
            return "", "", "", "", 20
    else:
        st.error(f"Country '{country}' not found in location data. Please select a different country.")
        return "", "", "", "", 20
    
    # Business type selection
    place_type = _render_business_type_selection(is_loading)
    
    # Max results
    max_results = st.number_input(
        'Max Results', 
        min_value=1, 
        max_value=settings.api.max_results_limit, 
        value=settings.api.default_max_results, 
        step=1,
        disabled=is_loading
    )
    
    return api_key, country, state, city, place_type, max_results


def render_search_button() -> bool:
    """Render the search button with styling."""
    # Check if search is in progress
    is_loading = st.session_state.get('search_in_progress', False)
    
    # Button styling
    st.markdown("""
    <style>
        .stButton > button {
            background: #2E86AB;
            color: white;
            border: none;
            border-radius: 12px;
            padding: 0.8rem 1.5rem;
            font-weight: 600;
            font-size: 1.1rem;
            box-shadow: 0 4px 12px rgba(46, 134, 171, 0.3);
            transition: all 0.3s ease;
            width: 100%;
            min-width: 200px;
        }
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(46, 134, 171, 0.4);
            background: #1f5f7a;
        }
        .stButton > button:active {
            transform: translateY(0);
        }
        .stButton > button:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
            background: #cccccc !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Mobile responsive search button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col3:
        return st.button(
            '⚡ Search Facilities' if not is_loading else '🔍 Searching...', 
            width='stretch', 
            disabled=is_loading,
            key="search_facilities_button"
        )


def _render_business_type_selection(is_loading: bool = False) -> str:
    """Render hierarchical business type selection with custom option."""
    st.markdown("#### 🏢 Business Type Selection")
    
    # First level: General Category
    category_options = list(BUSINESS_CATEGORIES.keys()) + ['Custom...']
    selected_category = st.selectbox(
        'General Category *', 
        category_options, 
        index=0,
        help="Select the general category of business you're looking for",
        disabled=is_loading
    )
    
    if selected_category == 'Custom...':
        # Direct custom input
        custom_type = st.text_input(
            'Enter Custom Business Type *', 
            placeholder='e.g., Yoga Studio, CrossFit Box, Restaurant',
            disabled=is_loading
        )
        return custom_type if custom_type else "Fitness Centre"
    
    # Second level: Subcategory
    subcategories = list(BUSINESS_CATEGORIES[selected_category].keys())
    if len(subcategories) > 1:
        selected_subcategory = st.selectbox(
            'Subcategory *', 
            subcategories, 
            index=0,
            help="Select a more specific subcategory",
            disabled=is_loading
        )
    else:
        selected_subcategory = subcategories[0]
    
    # Third level: Specific Business Type
    business_types = BUSINESS_CATEGORIES[selected_category][selected_subcategory] + ['Custom...']
    selected_business_type = st.selectbox(
        'Specific Business Type *', 
        business_types, 
        index=0,
        help="Select the specific type of business",
        disabled=is_loading
    )
    
    if selected_business_type == 'Custom...':
        custom_type = st.text_input(
            'Enter Custom Business Type *', 
            placeholder=f'Custom {selected_subcategory.lower()} type',
            disabled=is_loading
        )
        return custom_type if custom_type else business_types[0]
    else:
        return selected_business_type


def get_location_display_name(country: str, state: str, city: str) -> str:
    """
    Get a formatted location display name for search queries.
    
    Args:
        country: Selected country
        state: Selected state/province
        city: Selected city/town
        
    Returns:
        Formatted location string for Google Places API
    """
    if not country:
        return ""
    
    # For countries without states (like Singapore, Bahrain)
    if not state or state == country:
        return f"{city}, {country}"
    
    # For countries with states/provinces
    return f"{city}, {state}, {country}"
