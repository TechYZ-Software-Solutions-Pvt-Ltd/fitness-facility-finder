"""
Enhanced web scraping utilities for extracting comprehensive business information from websites.
"""

import requests
from bs4 import BeautifulSoup
import re
from typing import Tuple, Dict, List, Optional
import logging
from urllib.parse import urljoin, urlparse
import json

from models.facility import ContactInfo

logger = logging.getLogger(__name__)


def scrape_website_for_contacts(website: str) -> ContactInfo:
    """
    Extract contact information from a website with legal compliance checks.
    
    Args:
        website: The website URL to scrape
        
    Returns:
        ContactInfo object with extracted contact details
    """
    if not website:
        return ContactInfo()
    
    try:
        # Import compliance checker
        from .legal_compliance import compliance_checker
        
        # Check legal compliance before scraping
        compliance_check = compliance_checker.check_website_compliance(website)
        
        if not compliance_check.is_compliant:
            logger.warning(f"Website {website} failed compliance check: {compliance_check.violations}")
            return ContactInfo()
        
        # Log warnings if any
        if compliance_check.warnings:
            logger.info(f"Compliance warnings for {website}: {compliance_check.warnings}")
        
        # Enforce rate limiting
        domain = urlparse(website).netloc
        if not compliance_checker.enforce_rate_limit(domain):
            logger.warning(f"Rate limit exceeded for {domain}")
            return ContactInfo()
        
        # Set headers to mimic a real browser with legal compliance notice
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; LegalComplianceBot/1.0; +https://example.com/legal-compliance)',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'X-Compliance-Notice': 'This request is made in compliance with robots.txt and terms of service'
        }
        
        response = requests.get(website, timeout=10, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract comprehensive business information
        business_info = _extract_comprehensive_business_info(soup, website)
        
        # Validate data usage compliance
        data_validation = compliance_checker.validate_data_usage(business_info, 'web_scraping')
        if not data_validation.is_compliant:
            logger.warning(f"Data usage validation failed for {website}: {data_validation.violations}")
        
        return ContactInfo(
            email=business_info.get('email', ''),
            whatsapp=business_info.get('whatsapp', ''),
            instagram=business_info.get('instagram', ''),
            established_year=business_info.get('established_year', '')
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


def _extract_comprehensive_business_info(soup: BeautifulSoup, base_url: str) -> Dict[str, str]:
    """
    Extract comprehensive business information from website.
    
    Args:
        soup: BeautifulSoup object of the webpage
        base_url: Base URL for resolving relative links
        
    Returns:
        Dictionary with extracted business information
    """
    info = {}
    
    # Extract contact information
    info['email'] = _extract_email(soup)
    info['whatsapp'] = _extract_whatsapp(soup)
    info['instagram'] = _extract_instagram(soup)
    info['established_year'] = _extract_established_year(soup)
    
    # Extract additional social media links
    info['facebook'] = _extract_facebook(soup)
    info['twitter'] = _extract_twitter(soup)
    info['linkedin'] = _extract_linkedin(soup)
    info['youtube'] = _extract_youtube(soup)
    
    # Extract business details
    info['phone'] = _extract_phone_numbers(soup)
    info['address'] = _extract_address(soup)
    info['hours'] = _extract_business_hours(soup)
    info['description'] = _extract_business_description(soup)
    
    # Extract structured data (JSON-LD)
    structured_data = _extract_structured_data(soup)
    if structured_data:
        info.update(structured_data)
    
    return info


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


def _extract_facebook(soup: BeautifulSoup) -> str:
    """Extract Facebook page from website."""
    fb_link = soup.select_one('a[href*="facebook.com"]')
    if fb_link:
        return fb_link['href']
    return ""


def _extract_twitter(soup: BeautifulSoup) -> str:
    """Extract Twitter handle from website."""
    twitter_link = soup.select_one('a[href*="twitter.com"], a[href*="x.com"]')
    if twitter_link:
        return twitter_link['href']
    return ""


def _extract_linkedin(soup: BeautifulSoup) -> str:
    """Extract LinkedIn page from website."""
    linkedin_link = soup.select_one('a[href*="linkedin.com"]')
    if linkedin_link:
        return linkedin_link['href']
    return ""


def _extract_youtube(soup: BeautifulSoup) -> str:
    """Extract YouTube channel from website."""
    youtube_link = soup.select_one('a[href*="youtube.com"]')
    if youtube_link:
        return youtube_link['href']
    return ""


def _extract_phone_numbers(soup: BeautifulSoup) -> str:
    """Extract phone numbers from website."""
    text = soup.get_text()
    # Phone number patterns
    phone_patterns = [
        r'\+?[\d\s\-\(\)]{10,}',  # General phone pattern
        r'\(\d{3}\)\s?\d{3}-\d{4}',  # US format
        r'\d{3}-\d{3}-\d{4}',  # US format
        r'\+1\s?\d{3}\s?\d{3}\s?\d{4}',  # International US
    ]
    
    phones = []
    for pattern in phone_patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            # Clean and validate phone number
            clean_phone = re.sub(r'[^\d+]', '', match)
            if len(clean_phone) >= 10:
                phones.append(match.strip())
    
    return ', '.join(phones[:3])  # Return up to 3 phone numbers


def _extract_address(soup: BeautifulSoup) -> str:
    """Extract business address from website."""
    # Look for address in structured data
    address_selectors = [
        '[itemprop="address"]',
        '.address',
        '.location',
        '[class*="address"]',
        '[class*="location"]'
    ]
    
    for selector in address_selectors:
        address_elem = soup.select_one(selector)
        if address_elem:
            return address_elem.get_text().strip()
    
    return ""


def _extract_business_hours(soup: BeautifulSoup) -> str:
    """Extract business hours from website."""
    hours_selectors = [
        '[itemprop="openingHours"]',
        '.hours',
        '.business-hours',
        '[class*="hours"]',
        '[class*="time"]'
    ]
    
    for selector in hours_selectors:
        hours_elem = soup.select_one(selector)
        if hours_elem:
            return hours_elem.get_text().strip()
    
    return ""


def _extract_business_description(soup: BeautifulSoup) -> str:
    """Extract business description from website."""
    # Look for meta description first
    meta_desc = soup.select_one('meta[name="description"]')
    if meta_desc and meta_desc.get('content'):
        return meta_desc['content'].strip()
    
    # Look for structured data description
    desc_selectors = [
        '[itemprop="description"]',
        '.description',
        '.about',
        '[class*="description"]',
        '[class*="about"]'
    ]
    
    for selector in desc_selectors:
        desc_elem = soup.select_one(selector)
        if desc_elem:
            text = desc_elem.get_text().strip()
            if len(text) > 50:  # Only return substantial descriptions
                return text[:500]  # Limit to 500 characters
    
    return ""


def _extract_structured_data(soup: BeautifulSoup) -> Dict[str, str]:
    """Extract structured data (JSON-LD) from website."""
    structured_data = {}
    
    # Look for JSON-LD structured data
    json_scripts = soup.find_all('script', type='application/ld+json')
    
    for script in json_scripts:
        try:
            data = json.loads(script.string)
            if isinstance(data, dict):
                # Extract business information from structured data
                if data.get('@type') in ['LocalBusiness', 'Organization', 'Business']:
                    if 'name' in data:
                        structured_data['business_name'] = data['name']
                    if 'description' in data:
                        structured_data['business_description'] = data['description']
                    if 'telephone' in data:
                        structured_data['phone'] = data['telephone']
                    if 'email' in data:
                        structured_data['email'] = data['email']
                    if 'address' in data:
                        addr = data['address']
                        if isinstance(addr, dict):
                            structured_data['address'] = addr.get('streetAddress', '')
                        elif isinstance(addr, str):
                            structured_data['address'] = addr
                    if 'openingHours' in data:
                        structured_data['hours'] = ', '.join(data['openingHours'])
                    if 'foundingDate' in data:
                        structured_data['founded'] = data['foundingDate']
                    if 'sameAs' in data:
                        structured_data['social_links'] = ', '.join(data['sameAs'])
        except (json.JSONDecodeError, TypeError, KeyError):
            continue
    
    return structured_data


def _is_valid_email(email: str) -> bool:
    """Validate email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
