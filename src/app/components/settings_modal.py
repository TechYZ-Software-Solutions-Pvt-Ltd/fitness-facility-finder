"""
Professional Settings Component.
Uses Streamlit's native components for better integration.
"""

import streamlit as st
from typing import List
from ..config.settings import settings


def render_settings_icon():
    """Render the settings icon in the header."""
    # Add a small settings indicator in the top-right
    st.markdown("""
    <div style="position: fixed; top: 10px; right: 10px; z-index: 999;">
        <div style="background: #f0f2f6; padding: 8px 12px; border-radius: 20px; border: 1px solid #e0e0e0; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <span style="font-size: 14px; color: #666;">⚙️ Settings available in sidebar</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_settings_sidebar():
    """Render settings as a sidebar for desktop and expandable for mobile."""
    with st.sidebar:
        # Header
        st.markdown("### ⚙️ Search Settings")
        st.markdown("---")
        
        # Initialize session state
        if 'selected_fields' not in st.session_state:
            st.session_state.selected_fields = set(settings.fields.default_fields)
        
        selected_fields = set(st.session_state.selected_fields)
        
        # Show selected count
        st.info(f"📊 **{len(selected_fields)} fields selected**")
        
        # Field selection by category
        for category, fields in settings.fields.AVAILABLE_FIELDS.items():
            with st.expander(f"📋 {category}", expanded=(category == "Essential Information")):
                for field_key, field_name in fields.items():
                    is_selected = field_key in selected_fields
                    
                    if st.checkbox(
                        field_name,
                        value=is_selected,
                        key=f"settings_{field_key}",
                        help=settings.fields.field_descriptions.get(field_key, "")
                    ):
                        selected_fields.add(field_key)
                    else:
                        selected_fields.discard(field_key)
        
        # Update session state
        st.session_state.selected_fields = selected_fields
        
        # Action buttons
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🔄 Reset", help="Reset to default fields"):
                st.session_state.selected_fields = set(settings.fields.default_fields)
                st.rerun()
        
        with col2:
            if st.button("✅ Apply", help="Apply current selection"):
                st.success("Settings applied!")
                st.rerun()
        
        # Show selected fields summary
        if selected_fields:
            with st.expander("📝 Selected Fields", expanded=False):
                for category, fields in settings.fields.AVAILABLE_FIELDS.items():
                    category_fields = [f for f in selected_fields if f in fields]
                    if category_fields:
                        st.write(f"**{category}:**")
                        for field in category_fields:
                            st.write(f"• {fields[field]}")
        
        # API Setup Guide Section
        st.markdown("---")
        st.markdown("### 🔑 API Setup Guide")
        
        # Download button for API setup guide
        with open("docs/GOOGLE_PLACES_API_SETUP_GUIDE.txt", "r", encoding="utf-8") as file:
            guide_content = file.read()
        
        st.download_button(
            label="📥 Download Google API Key Setup Guide",
            data=guide_content,
            file_name="Google_Places_API_Setup_Guide.txt",
            mime="text/plain",
            help="Complete step-by-step guide for getting Google Places API key",
            use_container_width=True
        )
        
        # Quick help text
        st.info("💡 **Need help?** Download the complete setup guide above for detailed instructions on obtaining your Google API key.")


def get_selected_fields() -> List[str]:
    """Get currently selected fields from session state."""
    return list(st.session_state.get('selected_fields', settings.fields.default_fields))


def update_selected_fields(selected_fields: List[str]):
    """Update selected fields in session state."""
    st.session_state.selected_fields = set(selected_fields)


def get_fields_string() -> str:
    """Get selected fields as comma-separated string for API request."""
    selected = get_selected_fields()
    return ','.join(selected) if selected else ','.join(settings.fields.default_fields)
