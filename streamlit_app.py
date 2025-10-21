"""
JustList
Streamlit version of our React application
"""

import streamlit as st
import requests
import json
import time
from datetime import datetime
import pandas as pd
from typing import List, Dict, Any, Optional

# Page configuration
st.set_page_config(
    page_title="JustList",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS to match our React app styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1976d2;
        text-align: center;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .search-container {
        background-color: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }
    .result-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border-left: 4px solid #1976d2;
    }
    .facility-name {
        font-size: 1.3rem;
        font-weight: bold;
        color: #1976d2;
        margin-bottom: 0.5rem;
    }
    .facility-address {
        color: #666;
        margin-bottom: 0.5rem;
    }
    .facility-rating {
        color: #ff9800;
        font-weight: bold;
    }
    .login-container {
        max-width: 400px;
        margin: 0 auto;
        padding: 2rem;
        background-color: white;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .success-message {
        background-color: #e8f5e8;
        color: #2e7d32;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    .error-message {
        background-color: #ffebee;
        color: #c62828;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'user' not in st.session_state:
    st.session_state.user = None
if 'search_history' not in st.session_state:
    st.session_state.search_history = []
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

# API Configuration
API_BASE_URL = "http://localhost:8000"  # This would be your backend URL

def login_user(username: str, password: str) -> bool:
    """Login user and return success status"""
    try:
        response = requests.post(
            f"{API_BASE_URL}/auth/login",
            json={"username": username, "password": password}
        )
        if response.status_code == 200:
            data = response.json()
            st.session_state.authenticated = True
            st.session_state.user = data.get('user')
            st.session_state.access_token = data.get('access_token')
            return True
        return False
    except:
        return False

def register_user(username: str, email: str, password: str, full_name: str) -> bool:
    """Register user and return success status"""
    try:
        response = requests.post(
            f"{API_BASE_URL}/auth/register",
            json={
                "username": username,
                "email": email,
                "password": password,
                "full_name": full_name
            }
        )
        return response.status_code == 201
    except:
        return False

def search_facilities(api_key: str, country: str, city: str, facility_type: str, max_results: int) -> List[Dict]:
    """Search for facilities using the API"""
    try:
        response = requests.post(
            f"{API_BASE_URL}/facilities/search",
            json={
                "api_key": api_key,
                "country": country,
                "city": city,
                "place_type": facility_type,
                "max_results": max_results
            }
        )
        if response.status_code == 200:
            data = response.json()
            return data.get('facilities', [])
        return []
    except:
        return []

def logout_user():
    """Logout user"""
    st.session_state.authenticated = False
    st.session_state.user = None
    st.session_state.access_token = None
    st.session_state.current_page = 'home'

# Header
st.markdown('<div class="main-header">🏢 JustList</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Find facilities worldwide using Google Places API</div>', unsafe_allow_html=True)

# Navigation
if st.session_state.authenticated:
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        if st.button("🏠 Home", key="nav_home"):
            st.session_state.current_page = 'home'
    with col2:
        if st.button("📋 Search History", key="nav_history"):
            st.session_state.current_page = 'history'
    with col3:
        if st.button("⚙️ Settings", key="nav_settings"):
            st.session_state.current_page = 'settings'
    with col4:
        if st.button("🚪 Logout", key="nav_logout"):
            logout_user()
            st.rerun()
    
    st.markdown(f"**Welcome, {st.session_state.user.get('username', 'User')}**")
else:
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🔐 Login", key="nav_login"):
            st.session_state.current_page = 'login'
    with col2:
        if st.button("📝 Register", key="nav_register"):
            st.session_state.current_page = 'register'

# Main content based on current page
if not st.session_state.authenticated:
    if st.session_state.current_page == 'login':
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.markdown("### 🔐 Login")
        
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Login")
            
            if submit:
                if login_user(username, password):
                    st.markdown('<div class="success-message">✅ Login successful!</div>', unsafe_allow_html=True)
                    st.session_state.current_page = 'home'
                    time.sleep(1)
                    st.rerun()
                else:
                    st.markdown('<div class="error-message">❌ Invalid username or password</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    elif st.session_state.current_page == 'register':
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.markdown("### 📝 Register")
        
        with st.form("register_form"):
            username = st.text_input("Username")
            email = st.text_input("Email")
            full_name = st.text_input("Full Name")
            password = st.text_input("Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            submit = st.form_submit_button("Register")
            
            if submit:
                if password != confirm_password:
                    st.markdown('<div class="error-message">❌ Passwords do not match</div>', unsafe_allow_html=True)
                elif register_user(username, email, password, full_name):
                    st.markdown('<div class="success-message">✅ Registration successful! Please login.</div>', unsafe_allow_html=True)
                    st.session_state.current_page = 'login'
                    time.sleep(1)
                    st.rerun()
                else:
                    st.markdown('<div class="error-message">❌ Registration failed. Please try again.</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    else:
        # Public home page
        st.markdown("""
        ### Welcome to JustList
        
        **Find facilities worldwide using Google Places API**
        
        Please login or register to access the full features:
        - 🔍 Advanced facility search
        - 📋 Search history
        - ⚙️ Customizable settings
        - 💾 Save your preferences
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔐 Login Now", key="home_login"):
                st.session_state.current_page = 'login'
                st.rerun()
        with col2:
            if st.button("📝 Register Now", key="home_register"):
                st.session_state.current_page = 'register'
                st.rerun()

else:
    # Authenticated user content
    if st.session_state.current_page == 'home':
        st.markdown('<div class="search-container">', unsafe_allow_html=True)
        st.markdown("### 🔍 Search Facilities")
        
        with st.form("search_form"):
            col1, col2 = st.columns(2)
            with col1:
                api_key = st.text_input("Google Places API Key", type="password", help="Enter your Google Places API key")
                country = st.text_input("Country", value="India")
                city = st.text_input("City", value="Mumbai")
            with col2:
                facility_type = st.selectbox(
                    "Facility Type",
                    ["gym", "hospital", "restaurant", "school", "bank", "pharmacy", "gas_station", "shopping_mall"]
                )
                max_results = st.slider("Max Results", 1, 60, 20)
            
            search_button = st.form_submit_button("🔍 Search Facilities", type="primary")
            
            if search_button:
                if not api_key:
                    st.error("Please enter your Google Places API key")
                else:
                    with st.spinner("Searching facilities..."):
                        facilities = search_facilities(api_key, country, city, facility_type, max_results)
                        
                        if facilities:
                            st.success(f"Found {len(facilities)} facilities!")
                            
                            # Add to search history
                            search_entry = {
                                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                "country": country,
                                "city": city,
                                "facility_type": facility_type,
                                "results_count": len(facilities)
                            }
                            st.session_state.search_history.insert(0, search_entry)
                            
                            # Display results
                            for i, facility in enumerate(facilities, 1):
                                with st.container():
                                    st.markdown(f"""
                                    <div class="result-card">
                                        <div class="facility-name">{i}. {facility.get('name', 'N/A')}</div>
                                        <div class="facility-address">📍 {facility.get('formatted_address', 'Address not available')}</div>
                                        <div class="facility-rating">⭐ Rating: {facility.get('rating', 'N/A')} ({facility.get('user_ratings_total', 0)} reviews)</div>
                                        <div>📞 {facility.get('formatted_phone_number', 'Phone not available')}</div>
                                        <div>🌐 {facility.get('website', 'Website not available')}</div>
                                    </div>
                                    """, unsafe_allow_html=True)
                        else:
                            st.error("No facilities found. Please check your API key and search parameters.")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    elif st.session_state.current_page == 'history':
        st.markdown("### 📋 Search History")
        
        if st.session_state.search_history:
            for entry in st.session_state.search_history:
                st.markdown(f"""
                **{entry['timestamp']}** - {entry['facility_type'].title()} in {entry['city']}, {entry['country']} 
                ({entry['results_count']} results)
                """)
        else:
            st.info("No search history available. Start searching to see your history here!")
    
    elif st.session_state.current_page == 'settings':
        st.markdown("### ⚙️ Settings")
        
        st.markdown("#### Search Preferences")
        default_country = st.text_input("Default Country", value="India")
        default_city = st.text_input("Default City", value="Mumbai")
        default_max_results = st.slider("Default Max Results", 1, 60, 20)
        
        if st.button("💾 Save Settings"):
            st.success("Settings saved successfully!")
        
        st.markdown("#### Data Sources")
        st.checkbox("Google Places API", value=True, disabled=True)
        st.checkbox("Web Scraping", value=True)
        st.checkbox("Foursquare API", value=False)
        st.checkbox("Yelp API", value=False)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    Built with ❤️ using Streamlit | Powered by Google Places API<br>
    For support, visit our <a href="https://github.com/TechYZ-Software-Solutions-Pvt-Ltd/justlist" target="_blank">GitHub repository</a>
</div>
""", unsafe_allow_html=True)