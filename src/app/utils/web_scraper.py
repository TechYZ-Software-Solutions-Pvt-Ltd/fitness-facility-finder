"""
Web scraping utilities for extracting contact information from websites.
"""

import requests
from bs4 import BeautifulSoup
import re
from typing import Tuple
import logging

from ..models.facility import ContactInfo

logger = logging.getLogger(__name__)


def scrape_website_for_contacts(website: str) -> ContactInfo:
    """
    Extract contact information from a website.
    
    Args:
        website: The website URL to scrape
        
    Returns:
        ContactInfo object with extracted contact details
    """
    if not website:
        return ContactInfo()
    
    try:
        # Set headers to mimic a real browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(website, timeout=5, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract email
        email = _extract_email(soup)
        
        # Extract WhatsApp
        whatsapp = _extract_whatsapp(soup)
        
        # Extract Instagram
        instagram = _extract_instagram(soup)
        
        # Extract established year
        established_year = _extract_established_year(soup)
        
        return ContactInfo(
            email=email,
            whatsapp=whatsapp,
            instagram=instagram,
            established_year=established_year
        )
        
    except requests.RequestException as e:
        logger.warning(f"Failed to scrape website {website}: {e}")
        return ContactInfo()
    except (ValueError, TypeError, AttributeError) as e:
        logger.warning(f"Data processing error scraping website {website}: {e}")
        return ContactInfo()
    except Exception as e:
        logger.error(f"Unexpected error scraping website {website}: {e}")
        return ContactInfo()


def _extract_email(soup: BeautifulSoup) -> str:
    """Extract email address from website."""
    # Look for mailto links
    mailto_link = soup.select_one('a[href^=mailto]')
    if mailto_link:
        email = mailto_link['href'].replace('mailto:', '').strip()
        if _is_valid_email(email):
            return email
    
    # Look for email patterns in text
    text = soup.get_text()
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    
    for email in emails:
        if _is_valid_email(email):
            return email
    
    return ""


def _extract_whatsapp(soup: BeautifulSoup) -> str:
    """Extract WhatsApp number from website."""
    # Look for WhatsApp links
    wa_link = soup.select_one('a[href*="wa.me"]')
    if wa_link:
        whatsapp = wa_link['href'].split('wa.me/')[-1].split('?')[0].replace('/', '')
        if whatsapp:
            return whatsapp
    
    # Look for WhatsApp links with different patterns
    wa_link = soup.select_one('a[href*="whatsapp.com"]')
    if wa_link:
        whatsapp = wa_link['href'].split('whatsapp.com/')[-1].split('?')[0].replace('/', '')
        if whatsapp:
            return whatsapp
    
    return ""


def _extract_instagram(soup: BeautifulSoup) -> str:
    """Extract Instagram handle from website."""
    # Look for Instagram links
    insta_link = soup.select_one('a[href*="instagram.com"]')
    if insta_link:
        instagram = insta_link['href'].split('instagram.com/')[-1].split('?')[0].replace('/', '')
        if instagram and not instagram.startswith('http'):
            return instagram
    
    return ""


def _extract_established_year(soup: BeautifulSoup) -> str:
    """Extract established year from website."""
    text = soup.get_text().lower()
    
    # Keywords that might indicate establishment year
    keywords = ['since', 'established', 'founded', 'started', 'opened']
    
    for keyword in keywords:
        # Look for patterns like "since 2020", "established in 2015", etc.
        pattern = rf"{keyword}[\s:]*([12][0-9]{{3}})"
        match = re.search(pattern, text)
        if match:
            year = match.group(1)
            # Validate year (reasonable range)
            if 1900 <= int(year) <= 2025:
                return year
    
    return ""


def _is_valid_email(email: str) -> bool:
    """Validate email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
