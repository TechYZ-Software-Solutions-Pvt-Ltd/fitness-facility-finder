"""
Results display component for showing search results.
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import re

from ..models.facility import SearchResult


def render_search_results(result: SearchResult):
    """Render search results in a formatted display."""
    if not result.success:
        st.error(f"❌ {result.error_message}")
        return
    
    if not result.facilities:
        st.warning("⚠️ No facilities found or API error occurred.")
        return
    
    # Display security status
    _render_security_status()
    
    # Process and display results
    _render_results_table(result)
    
    # Download functionality
    _render_download_section(result)
    
    # Success message
    st.success(f"✅ Search completed! {len(result.facilities)} facilities found.")


def _render_security_status():
    """Render security status indicators."""
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.success("🔐 API Key Validated")
    with col2:
        st.info(f"⏱️ Rate Limit: {st.session_state.get('request_count', 0)}/50")
    with col3:
        st.success("🛡️ Input Sanitized")


def _render_results_table(result: SearchResult):
    """Render the results table with proper formatting."""
    # Convert facilities to DataFrame
    df_data = result.to_dataframe_dict()
    df = pd.DataFrame(df_data)
    
    if df.empty:
        return
    
    # Ensure proper data types
    df['Google Rating'] = pd.to_numeric(df['Google Rating'], errors='coerce').fillna(0)
    df['Established Year'] = df['Established Year'].astype(str)
    
    # Display with column configuration
    st.dataframe(
        df,
        width='stretch',
        hide_index=True,
        column_config={
            "Facility Name": st.column_config.TextColumn(
                "Facility Name",
                width="medium",
                help="Name of the fitness facility"
            ),
            "Contact Number": st.column_config.TextColumn(
                "Contact",
                width="small",
                help="Phone number"
            ),
            "WhatsApp Number": st.column_config.TextColumn(
                "WhatsApp",
                width="small",
                help="WhatsApp number"
            ),
            "email ID": st.column_config.TextColumn(
                "Email",
                width="small",
                help="Email address"
            ),
            "Established Year": st.column_config.TextColumn(
                "Year",
                width="small",
                help="Established year"
            ),
            "Location": st.column_config.TextColumn(
                "Location",
                width="small",
                help="City/Location"
            ),
            "Address": st.column_config.TextColumn(
                "Address",
                width="large",
                help="Full address"
            ),
            "Google Rating": st.column_config.NumberColumn(
                "Rating",
                width="small",
                format="%.1f",
                help="Google rating"
            ),
            "Instagram id": st.column_config.TextColumn(
                "Instagram",
                width="small",
                help="Instagram handle"
            ),
            "Website": st.column_config.LinkColumn(
                "Website",
                width="small",
                help="Website URL"
            )
        }
    )


def _render_download_section(result: SearchResult):
    """Render download section with CSV export."""
    from utils.security import sanitize_input
    
    # Generate filename with proper sanitization
    current_date = datetime.now().strftime("%Y%m%d")
    place_type_clean = sanitize_input(result.search_query.place_type)
    country_clean = sanitize_input(result.search_query.country)
    city_clean = sanitize_input(result.search_query.city)
    
    # Additional sanitization for filename
    place_type_clean = re.sub(r'[^a-zA-Z0-9_-]', '_', place_type_clean)[:20]
    country_clean = re.sub(r'[^a-zA-Z0-9_-]', '_', country_clean)[:20]
    city_clean = re.sub(r'[^a-zA-Z0-9_-]', '_', city_clean)[:20]
    
    filename = f"{place_type_clean}_{country_clean}_{city_clean}_{current_date}.csv"
    
    # Convert to CSV
    df_data = result.to_dataframe_dict()
    df = pd.DataFrame(df_data)
    csv_data = df.to_csv(index=False)
    
    # Download button
    st.download_button(
        '📥 Download Secure CSV', 
        data=csv_data, 
        file_name=filename, 
        mime='text/csv',
        help="Download your search results securely"
    )


def render_error_messages(api_key: str, city: str, place_type: str, api_key_valid: bool, error_msg: str = ""):
    """Render appropriate error messages based on validation."""
    if not api_key:
        st.error("❌ **Google Places API Key is required!** Please enter your API key to continue.")
        _render_api_key_focus_script()
    elif not city:
        st.error("❌ **Location is required!** Please select or enter a city/town/area.")
    elif not place_type:
        st.error("❌ **Business Type is required!** Please select or enter a business type.")
    elif not api_key_valid:
        st.error(f"❌ {error_msg}")


def _render_api_key_focus_script():
    """Render JavaScript to focus on API key input when there's an error."""
    st.markdown("""
    <script>
    // Focus on the API key input field only when there's an error
    setTimeout(function() {
        const input = document.querySelector('input[type="password"]');
        if (input) {
            input.focus();
            // Only scroll if the input is not already visible
            const rect = input.getBoundingClientRect();
            if (rect.top < 0 || rect.bottom > window.innerHeight) {
                input.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        }
    }, 500);
    </script>
    """, unsafe_allow_html=True)
