"""
Streamlit App for Facility Finder
This is a simplified version for Streamlit Cloud deployment
"""

import streamlit as st
import requests
import json
from datetime import datetime
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Facility Finder",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .search-container {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .result-card {
        background-color: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# API Configuration
try:
    API_BASE_URL = st.secrets.get("API_BASE_URL", "http://localhost:8000")
except:
    API_BASE_URL = "http://localhost:8000"

def search_facilities(api_key, place_type, city, country, max_results=20):
    """Search for facilities using the API"""
    try:
        response = requests.post(
            f"{API_BASE_URL}/facilities/search",
            json={
                "api_key": api_key,
                "place_type": place_type,
                "city": city,
                "country": country,
                "max_results": max_results
            },
            timeout=30
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        st.error(f"Connection Error: {str(e)}")
        return None

def main():
    # Header
    st.markdown('<h1 class="main-header">🏢 Facility Finder</h1>', unsafe_allow_html=True)
    st.markdown("Find facilities worldwide using Google Places API")
    
    # Sidebar for search parameters
    with st.sidebar:
        st.header("🔍 Search Parameters")
        
        # API Key
        api_key = st.text_input(
            "Google Places API Key",
            type="password",
            help="Get your free API key from Google Cloud Console"
        )
        
        # Location
        country = st.text_input("Country", value="India", placeholder="e.g., India")
        city = st.text_input("City", value="Mumbai", placeholder="e.g., Mumbai")
        
        # Facility type
        facility_types = [
            "hospital", "school", "restaurant", "hotel", "bank", "pharmacy",
            "gym", "library", "museum", "shopping_mall", "gas_station",
            "atm", "post_office", "police", "fire_station"
        ]
        place_type = st.selectbox("Facility Type", facility_types)
        
        # Max results
        max_results = st.slider("Max Results", 1, 50, 20)
        
        # Search button
        search_button = st.button("🔍 Search Facilities", type="primary")
    
    # Main content area
    if search_button:
        if not api_key:
            st.error("Please enter your Google Places API key")
            return
        
        if not city or not country:
            st.error("Please enter both city and country")
            return
        
        # Show loading
        with st.spinner("Searching for facilities..."):
            results = search_facilities(api_key, place_type, city, country, max_results)
        
        if results and results.get("success"):
            facilities = results.get("facilities", [])
            
            if facilities:
                st.success(f"Found {len(facilities)} facilities!")
                
                # Display results
                for i, facility in enumerate(facilities, 1):
                    with st.container():
                        st.markdown(f"""
                        <div class="result-card">
                            <h3>{i}. {facility.get('name', 'Unknown')}</h3>
                            <p><strong>Address:</strong> {facility.get('formatted_address', 'Not available')}</p>
                            <p><strong>Rating:</strong> {facility.get('google_rating', 'N/A')}/5</p>
                            <p><strong>Phone:</strong> {facility.get('formatted_phone_number', 'Not available')}</p>
                            <p><strong>Website:</strong> {facility.get('website', 'Not available')}</p>
                        </div>
                        """, unsafe_allow_html=True)
                
                # Download option
                if facilities:
                    df = pd.DataFrame(facilities)
                    csv = df.to_csv(index=False)
                    st.download_button(
                        label="📥 Download Results as CSV",
                        data=csv,
                        file_name=f"facilities_{city}_{place_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                        mime="text/csv"
                    )
            else:
                st.warning("No facilities found for the given criteria")
        else:
            st.error("Search failed. Please check your API key and try again.")
    
    # Instructions
    with st.expander("📖 How to Use"):
        st.markdown("""
        ### Getting Started
        1. **Get a Google Places API Key:**
           - Go to [Google Cloud Console](https://console.cloud.google.com/)
           - Enable the Places API
           - Create credentials (API Key)
           - Copy your API key
        
        2. **Search for Facilities:**
           - Enter your API key in the sidebar
           - Select your location (country and city)
           - Choose the type of facility you're looking for
           - Click "Search Facilities"
        
        3. **View Results:**
           - Browse through the found facilities
           - See ratings, addresses, and contact information
           - Download results as CSV for further analysis
        
        ### Supported Facility Types
        - Healthcare: hospitals, pharmacies
        - Education: schools, libraries, museums
        - Food: restaurants, cafes
        - Accommodation: hotels, hostels
        - Services: banks, ATMs, post offices
        - Recreation: gyms, shopping malls
        - And many more!
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>Built with ❤️ using Streamlit | Powered by Google Places API</p>
        <p>For support, visit our <a href='#'>GitHub repository</a></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
