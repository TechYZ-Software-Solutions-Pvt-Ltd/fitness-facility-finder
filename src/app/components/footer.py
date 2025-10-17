"""
Footer component for the application.
"""

import streamlit as st


def render_footer():
    """Render the application footer with security info and branding."""
    # Security footer
    st.markdown("---")
    st.markdown("### 🔒 Security & Privacy")
    st.info('🔐 **Secure Operation**: Your API key is protected, data is processed securely, and never stored. Rate limited to 50 requests per 30 minutes.')
    
    # Techyz Software Solutions Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 20px; background-color: #f8f9fa; border-radius: 10px; margin-top: 20px;">
        <p style="color: #2E86AB; font-size: 14px; margin: 0; font-weight: bold;">
            Powered by Techyz Software Solutions Private Limited
        </p>
        <p style="color: #888; font-size: 12px; margin: 5px 0 0 0;">
            Secure • Reliable • Professional
        </p>
    </div>
    """, unsafe_allow_html=True)
