"""
Security utilities for input validation, sanitization, and rate limiting.
"""

import re
import time
import streamlit as st
from typing import Tuple
from datetime import datetime
import logging
import threading

# Configuration constants (replacing deleted config.settings)
MAX_REQUESTS_PER_SESSION = 50
SESSION_TIMEOUT_MINUTES = 30
REQUEST_TIMEOUT_SECONDS = 15

logger = logging.getLogger(__name__)

# Thread lock for session state operations
_session_lock = threading.Lock()


def sanitize_input(text: str) -> str:
    """Sanitize user input to prevent injection attacks."""
    if not text:
        return ""
    
    # Convert to string and strip whitespace
    text = str(text).strip()
    
    # Remove potentially dangerous characters
    sanitized = re.sub(r'[<>"\';\\&]', '', text)
    
    # Remove any remaining control characters
    sanitized = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', sanitized)
    
    # Limit length to prevent buffer overflow
    return sanitized[:100]


def validate_location_input(location: str) -> Tuple[bool, str]:
    """Validate location input for safety and format."""
    if not location or not location.strip():
        return False, "Location cannot be empty"
    
    location = location.strip()
    
    # Check for minimum length
    if len(location) < 2:
        return False, "Location must be at least 2 characters long"
    
    # Check for maximum length
    if len(location) > 100:
        return False, "Location must be less than 100 characters"
    
    # Check for valid characters (letters, numbers, spaces, common punctuation)
    if not re.match(r'^[a-zA-Z0-9\s\.,\-\'()]+$', location):
        return False, "Location contains invalid characters"
    
    # Check for suspicious patterns
    suspicious_patterns = [
        r'<script', r'javascript:', r'data:', r'vbscript:',
        r'on\w+\s*=', r'<iframe', r'<object', r'<embed'
    ]
    
    for pattern in suspicious_patterns:
        if re.search(pattern, location, re.IGNORECASE):
            return False, "Location contains potentially harmful content"
    
    return True, "Valid location"


def validate_business_type_input(business_type: str) -> Tuple[bool, str]:
    """Validate business type input for safety and format."""
    if not business_type or not business_type.strip():
        return False, "Business type cannot be empty"
    
    business_type = business_type.strip()
    
    # Check for minimum length
    if len(business_type) < 2:
        return False, "Business type must be at least 2 characters long"
    
    # Check for maximum length
    if len(business_type) > 50:
        return False, "Business type must be less than 50 characters"
    
    # Check for valid characters
    if not re.match(r'^[a-zA-Z0-9\s\.,\-\'&]+$', business_type):
        return False, "Business type contains invalid characters"
    
    return True, "Valid business type"


def validate_api_key(api_key: str) -> Tuple[bool, str]:
    """Validate Google Places API key format."""
    # Simple API key validation
    if not api_key:
        return False, "API key is required"
    
    if len(api_key) < 20 or len(api_key) > 200:
        return False, "API key must be between 20 and 200 characters"
    
    # Google API key format validation
    if not re.match(r'^AIza[0-9A-Za-z_-]{35}$', api_key):
        return False, "Invalid Google API key format"
    
    return True, "Valid API key"


def check_rate_limit() -> bool:
    """Check if user has exceeded rate limits (thread-safe)."""
    with _session_lock:
        current_time = time.time()
        session_start = st.session_state.get('session_start', current_time)
        session_duration = current_time - session_start
        
        # Check if session has expired
        if session_duration > SESSION_TIMEOUT_MINUTES * 60:
            # Reset session but add cooldown period to prevent rapid resets
            cooldown_period = 60  # 1 minute cooldown
            last_reset = st.session_state.get('last_reset', 0)
            
            if current_time - last_reset > cooldown_period:
                st.session_state.request_count = 0
                st.session_state.session_start = current_time
                st.session_state.last_reset = current_time
                return True
            else:
                # Still in cooldown period
                return False
        
        # Check current request count
        current_count = st.session_state.get('request_count', 0)
        return current_count < MAX_REQUESTS_PER_SESSION


def increment_request_count():
    """Increment the request counter (thread-safe)."""
    with _session_lock:
        if 'request_count' not in st.session_state:
            st.session_state.request_count = 0
        st.session_state.request_count += 1


def secure_log_request(operation: str, success: bool = True, error_msg: str = ""):
    """Log requests securely without exposing sensitive data."""
    timestamp = datetime.now().isoformat()
    log_data = {
        'timestamp': timestamp,
        'operation': operation,
        'success': success,
        'error': error_msg if not success else None
    }
    logger.info(f"Request logged: {log_data}")


def initialize_session_security():
    """Initialize security-related session state variables (thread-safe)."""
    with _session_lock:
        current_time = time.time()
        
        if 'request_count' not in st.session_state:
            st.session_state.request_count = 0
        if 'session_start' not in st.session_state:
            st.session_state.session_start = current_time
        if 'last_reset' not in st.session_state:
            st.session_state.last_reset = 0


def validate_search_inputs(place_type: str, city: str, country: str, max_results: int) -> Tuple[bool, str]:
    """Validate all search input parameters."""
    # Validate business type
    is_valid, error_msg = validate_business_type_input(place_type)
    if not is_valid:
        return False, f"Business type: {error_msg}"
    
    # Validate city
    is_valid, error_msg = validate_location_input(city)
    if not is_valid:
        return False, f"City: {error_msg}"
    
    # Validate country
    is_valid, error_msg = validate_location_input(country)
    if not is_valid:
        return False, f"Country: {error_msg}"
    
    # Validate max results
    if not isinstance(max_results, int) or max_results < 1 or max_results > 60:
        return False, f"Max results must be between 1 and 60"
    
    return True, "Valid inputs"
