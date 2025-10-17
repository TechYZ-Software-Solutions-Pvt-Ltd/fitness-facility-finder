"""
Header component for the application.
"""

import streamlit as st
from ..config.settings import settings
from .settings_modal import render_settings_icon, render_settings_sidebar


def render_header():
    """Render the application header with styling."""
    # CSS for mobile responsiveness and styling
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Shadows+Into+Light&display=swap');
        
        /* Mobile Responsive Styles */
        @media (max-width: 768px) {
            /* Enhanced header font size for tablets (25% increase) */
            div[style*="font-family: 'Shadows Into Light'"] h1 {
                font-size: 4.2rem !important;
            }
            
            /* Make form elements stack vertically on mobile */
            .stSelectbox > div > div {
                width: 100% !important;
            }
            
            .stNumberInput > div > div {
                width: 100% !important;
            }
            
            .stTextInput > div > div {
                width: 100% !important;
            }
            
            /* Optimize button for mobile */
            .stButton > button {
                width: 100% !important;
                min-width: unset !important;
                font-size: 1rem !important;
                padding: 0.7rem 1rem !important;
            }
            
            /* Make columns stack on mobile */
            .mobile-stack {
                display: flex !important;
                flex-direction: column !important;
            }
            
            /* Optimize dataframe for mobile */
            .stDataFrame {
                font-size: 0.8rem !important;
            }
            
            /* Make security features stack on mobile */
            .security-features {
                display: flex !important;
                flex-direction: column !important;
                gap: 10px !important;
            }
            
            .security-feature {
                width: 100% !important;
                margin-bottom: 10px !important;
            }
        }
        
        @media (max-width: 480px) {
            /* Further optimize for very small screens */
            .stMarkdown h1 {
                font-size: 1.2rem !important;
            }
            
            /* Enhanced header font size for mobile (40% increase) */
            div[style*="font-family: 'Shadows Into Light'"] h1 {
                font-size: 4.6rem !important;
            }
        }
        
        @media (max-width: 360px) {
            /* Extra small phones - make header even more prominent */
            div[style*="font-family: 'Shadows Into Light'"] h1 {
                font-size: 5.0rem !important;
                line-height: 1.1 !important;
            }
            
            /* Optimize for touch screens */
            .stButton > button {
                min-height: 44px !important;
                touch-action: manipulation !important;
            }
            
            /* Better spacing for mobile */
            .stSelectbox, .stTextInput, .stNumberInput {
                margin-bottom: 1rem !important;
            }
            
            /* Improve table scrolling on mobile */
            .stDataFrame {
                overflow-x: auto !important;
                -webkit-overflow-scrolling: touch !important;
            }
            
            /* Make download button more touch-friendly */
            .stDownloadButton > button {
                min-height: 44px !important;
                font-size: 1rem !important;
            }
        }
        
        /* Additional mobile optimizations */
        @media (max-width: 768px) {
            /* Make all interactive elements touch-friendly */
            .stButton > button, .stDownloadButton > button {
                min-height: 44px;
                touch-action: manipulation;
            }
            
            /* Improve form spacing */
            .stForm {
                padding: 1rem !important;
            }
            
            /* Better text readability */
            .stMarkdown {
                font-size: 0.9rem !important;
                line-height: 1.4 !important;
            }
            
            /* Optimize sidebar if used */
            .stSidebar {
                width: 100% !important;
            }
        }
        
        /* Enhanced loading indicator styling */
        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, #4CAF50, #45a049, #4CAF50);
            background-size: 200% 100%;
            animation: loading-shimmer 2s ease-in-out infinite;
        }
        
        @keyframes loading-shimmer {
            0% { background-position: -200% 0; }
            100% { background-position: 200% 0; }
        }
        
        /* Status text styling */
        .stText {
            font-weight: 600;
            color: #2c3e50;
        }
    </style>
    """, unsafe_allow_html=True)

    # Simple scroll to top fix
    st.markdown("""
    <style>
        /* Simple scroll to top fix */
        html, body {
            scroll-behavior: auto !important;
        }
        
        /* Force page to start at top */
        .main .block-container {
            padding-top: 0.2rem !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # Main heading with enhanced font styling
    st.markdown(f"""
    <div style="text-align: center; margin-top: 0px; margin-bottom: 30px; position: relative;">
        <h1 style="color: #000000; font-family: 'Shadows Into Light', cursive; font-weight: bold; margin: 0; font-size: 3.3rem;"> 
            {settings.ui.app_title}
        </h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Render settings icon and sidebar
    render_settings_icon()
    render_settings_sidebar()
