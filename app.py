"""
Streamlit Cloud Entry Point for Fitness Facility Finder.
This file serves as the main entry point for Streamlit Cloud deployment.
"""

import streamlit as st
import time
import logging
import sys
import os

# Add the src/app directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src', 'app'))

# Import all the components and modules
from components.header import render_header
from components.unified_search_form import render_unified_search_form, render_search_button, get_location_display_name
from components.results_display import render_search_results, render_error_messages
from components.footer import render_footer
from services.places_service import PlacesService
from models.facility import SearchQuery
from utils.security import (
    validate_api_key, 
    check_rate_limit, 
    validate_search_inputs,
    initialize_session_security
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize session security
initialize_session_security()


def main():
    """Main application function with error recovery."""
    try:
        # Render header
        render_header()
        
        # Render unified search form
        try:
            api_key, country, state, city, place_type, max_results = render_unified_search_form()
            
            # Render search button
            search_clicked = render_search_button()
            
            # Handle search
            if search_clicked:
                # Set loading state immediately when search is clicked
                st.session_state.search_in_progress = True
                # Force re-render to update button state
                st.rerun()
                _handle_search(api_key, country, state, city, place_type, max_results)
        except Exception as e:
            logger.error(f"Error in search: {e}")
            st.error("❌ An error occurred in the search form. Please try refreshing the page.")
        
        # Render footer
        render_footer()
        
    except Exception as e:
        logger.error(f"Critical error in main application: {e}")
        st.error("🚨 A critical error occurred. The application will attempt to recover.")
        st.info("Please refresh the page to restart the application.")
        
        # Show error details in expander for debugging
        with st.expander("Error Details (for debugging)"):
            st.code(f"Error: {str(e)}")
            st.code(f"Type: {type(e).__name__}")


def _handle_search(api_key: str, country: str, state: str, city: str, place_type: str, max_results: int):
    """Handle the unified search functionality with error recovery."""
    try:
        # Validate inputs
        is_valid, error_msg = validate_search_inputs(place_type, city, country, max_results)
        
        if not is_valid:
            st.error(f"❌ {error_msg}")
            return
        
        # Validate API key
        api_key_valid, api_key_error = validate_api_key(api_key)
        
        # Render error messages if any
        render_error_messages(api_key, city, place_type, api_key_valid, api_key_error)
        
        # Proceed with search if all validations pass
        if api_key and city and place_type and api_key_valid:
            if not check_rate_limit():
                st.error(f"❌ Rate limit exceeded. Maximum 50 requests per 30 minutes.")
                return
            
            # Create search query with unified location
            location_display = get_location_display_name(country, state, city)
            search_query = SearchQuery(
                place_type=place_type,
                city=location_display,
                country=country,
                max_results=max_results
            )
            
            # Perform search
            _perform_search(search_query, api_key)
            
    except Exception as e:
        logger.error(f"Error in unified search handler: {e}")
        st.error("❌ An error occurred during the search. Please try again.")
        st.info("💡 Try checking your API key and search parameters.")


def _perform_search(search_query: SearchQuery, api_key: str):
    """Perform the actual search using PlacesService with error recovery."""
    try:
        # Initialize places service
        places_service = PlacesService(api_key)
        
        # Create a prominent loading indicator
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Perform search with progress updates
        with st.spinner(''):
            status_text.text("🔍 Searching facilities...")
            progress_bar.progress(20)
            
            # Simulate progress for better UX
            time.sleep(0.5)
            progress_bar.progress(40)
            status_text.text("🌐 Connecting to Google Places API...")
            
            time.sleep(0.5)
            progress_bar.progress(60)
            status_text.text("📍 Finding facilities in your area...")
            
            # Perform actual search
            result = places_service.search_places(search_query)
            
            progress_bar.progress(80)
            status_text.text("📊 Processing results...")
            
            time.sleep(0.3)
            progress_bar.progress(100)
            status_text.text("✅ Search completed!")
            
            # Clear loading indicators
            time.sleep(0.5)
            progress_bar.empty()
            status_text.empty()
            
            # Clear loading state
            st.session_state.search_in_progress = False
            
            # Display results
            render_search_results(result)
        
    except Exception as e:
        logger.error(f"Error performing search: {e}")
        # Clear loading state on error
        st.session_state.search_in_progress = False
        st.error("❌ An error occurred while searching. Please try again.")
        st.info("💡 This might be due to network issues or API problems.")


if __name__ == "__main__":
    main()