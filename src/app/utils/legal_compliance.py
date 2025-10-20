"""
Legal compliance utilities to ensure the application operates within legal boundaries.
"""

import requests
import time
import logging
from typing import Dict, List, Optional, Tuple
from urllib.parse import urljoin, urlparse
from dataclasses import dataclass
import re

logger = logging.getLogger(__name__)


@dataclass
class ComplianceCheck:
    """Result of a legal compliance check."""
    is_compliant: bool
    violations: List[str]
    warnings: List[str]
    recommendations: List[str]


class LegalComplianceChecker:
    """
    Ensures all data collection activities comply with legal requirements.
    """
    
    def __init__(self):
        self.rate_limits = {}
        self.last_request_time = {}
        self.robots_cache = {}
        
        # Legal compliance rules
        self.max_requests_per_minute = 10
        self.min_delay_between_requests = 6  # seconds
        self.respect_robots_txt = True
        self.require_attribution = True
    
    def check_website_compliance(self, url: str) -> ComplianceCheck:
        """
        Check if a website can be scraped legally and ethically.
        
        Args:
            url: Website URL to check
            
        Returns:
            ComplianceCheck with compliance status and recommendations
        """
        violations = []
        warnings = []
        recommendations = []
        
        try:
            parsed_url = urlparse(url)
            domain = parsed_url.netloc
            
            # Check robots.txt
            if self.respect_robots_txt:
                robots_compliant, robots_warnings = self._check_robots_txt(domain)
                if not robots_compliant:
                    violations.append(f"robots.txt disallows scraping for {domain}")
                warnings.extend(robots_warnings)
            
            # Check if URL is publicly accessible
            if not self._is_publicly_accessible(url):
                violations.append(f"URL {url} is not publicly accessible")
            
            # Check for authentication requirements
            if self._requires_authentication(url):
                violations.append(f"URL {url} requires authentication")
            
            # Check rate limiting
            if not self._check_rate_limit(domain):
                warnings.append(f"Rate limit exceeded for {domain}")
                recommendations.append("Wait before making more requests")
            
            # Check for sensitive data patterns
            sensitive_patterns = self._check_sensitive_data_patterns(url)
            if sensitive_patterns:
                warnings.extend(sensitive_patterns)
            
            # Check terms of service compliance
            tos_compliant, tos_warnings = self._check_terms_of_service(domain)
            if not tos_compliant:
                violations.append(f"Terms of service violation for {domain}")
            warnings.extend(tos_warnings)
            
            is_compliant = len(violations) == 0
            
            if not is_compliant:
                recommendations.append("Do not scrape this website")
            elif warnings:
                recommendations.append("Proceed with caution and respect rate limits")
            else:
                recommendations.append("Website appears safe to scrape")
            
            return ComplianceCheck(
                is_compliant=is_compliant,
                violations=violations,
                warnings=warnings,
                recommendations=recommendations
            )
            
        except Exception as e:
            logger.error(f"Error checking compliance for {url}: {e}")
            return ComplianceCheck(
                is_compliant=False,
                violations=[f"Error checking compliance: {str(e)}"],
                warnings=[],
                recommendations=["Do not scrape this website due to errors"]
            )
    
    def _check_robots_txt(self, domain: str) -> Tuple[bool, List[str]]:
        """Check robots.txt compliance."""
        warnings = []
        
        try:
            if domain in self.robots_cache:
                return self.robots_cache[domain]
            
            robots_url = f"https://{domain}/robots.txt"
            response = requests.get(robots_url, timeout=5)
            
            if response.status_code == 200:
                robots_content = response.text.lower()
                
                # Check for disallow rules
                if "disallow: /" in robots_content:
                    self.robots_cache[domain] = (False, ["robots.txt disallows all scraping"])
                    return False, ["robots.txt disallows all scraping"]
                
                # Check for specific disallow rules
                disallow_patterns = re.findall(r'disallow:\s*(.+)', robots_content)
                if disallow_patterns:
                    warnings.append(f"robots.txt has disallow rules: {disallow_patterns}")
                
                # Check for crawl delay
                crawl_delay_match = re.search(r'crawl-delay:\s*(\d+)', robots_content)
                if crawl_delay_match:
                    delay = int(crawl_delay_match.group(1))
                    warnings.append(f"robots.txt specifies crawl delay of {delay} seconds")
                
                self.robots_cache[domain] = (True, warnings)
                return True, warnings
            
            else:
                warnings.append(f"Could not fetch robots.txt for {domain}")
                self.robots_cache[domain] = (True, warnings)
                return True, warnings
                
        except Exception as e:
            warnings.append(f"Error checking robots.txt for {domain}: {e}")
            self.robots_cache[domain] = (True, warnings)
            return True, warnings
    
    def _is_publicly_accessible(self, url: str) -> bool:
        """Check if URL is publicly accessible without authentication."""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (compatible; LegalComplianceBot/1.0)'
            }
            
            response = requests.head(url, headers=headers, timeout=5, allow_redirects=True)
            
            # Check for authentication requirements
            if response.status_code == 401:
                return False
            if response.status_code == 403:
                return False
            if 'www-authenticate' in response.headers:
                return False
            
            return response.status_code == 200
            
        except Exception:
            return False
    
    def _requires_authentication(self, url: str) -> bool:
        """Check if URL requires authentication."""
        try:
            response = requests.head(url, timeout=5)
            return response.status_code in [401, 403]
        except Exception:
            return False
    
    def _check_rate_limit(self, domain: str) -> bool:
        """Check if we're within rate limits for a domain."""
        current_time = time.time()
        
        if domain not in self.rate_limits:
            self.rate_limits[domain] = []
        
        # Remove old requests (older than 1 minute)
        self.rate_limits[domain] = [
            req_time for req_time in self.rate_limits[domain]
            if current_time - req_time < 60
        ]
        
        # Check if we're under the limit
        if len(self.rate_limits[domain]) >= self.max_requests_per_minute:
            return False
        
        # Add current request
        self.rate_limits[domain].append(current_time)
        return True
    
    def _check_sensitive_data_patterns(self, url: str) -> List[str]:
        """Check for patterns that might indicate sensitive data."""
        warnings = []
        
        sensitive_patterns = [
            r'/admin',
            r'/private',
            r'/internal',
            r'/secure',
            r'/login',
            r'/dashboard',
            r'/api/private',
            r'/user/',
            r'/profile/',
            r'/account/'
        ]
        
        for pattern in sensitive_patterns:
            if re.search(pattern, url, re.IGNORECASE):
                warnings.append(f"URL contains potentially sensitive pattern: {pattern}")
        
        return warnings
    
    def _check_terms_of_service(self, domain: str) -> Tuple[bool, List[str]]:
        """Check terms of service compliance (basic checks)."""
        warnings = []
        
        # Common TOS patterns that might restrict scraping
        tos_indicators = [
            'no scraping',
            'no automated access',
            'no data mining',
            'prohibited use',
            'unauthorized access'
        ]
        
        try:
            # Try to fetch terms of service page
            tos_urls = [
                f"https://{domain}/terms",
                f"https://{domain}/terms-of-service",
                f"https://{domain}/tos",
                f"https://{domain}/legal"
            ]
            
            for tos_url in tos_urls:
                try:
                    response = requests.get(tos_url, timeout=5)
                    if response.status_code == 200:
                        content = response.text.lower()
                        
                        for indicator in tos_indicators:
                            if indicator in content:
                                warnings.append(f"Terms of service may restrict scraping: {indicator}")
                        
                        break
                except Exception:
                    continue
            
        except Exception as e:
            warnings.append(f"Could not check terms of service for {domain}: {e}")
        
        return True, warnings  # Assume compliant unless proven otherwise
    
    def enforce_rate_limit(self, domain: str) -> bool:
        """Enforce rate limiting for a domain."""
        if not self._check_rate_limit(domain):
            logger.warning(f"Rate limit exceeded for {domain}")
            return False
        
        # Enforce minimum delay between requests
        if domain in self.last_request_time:
            time_since_last = time.time() - self.last_request_time[domain]
            if time_since_last < self.min_delay_between_requests:
                sleep_time = self.min_delay_between_requests - time_since_last
                logger.info(f"Rate limiting: sleeping for {sleep_time:.2f} seconds")
                time.sleep(sleep_time)
        
        self.last_request_time[domain] = time.time()
        return True
    
    def get_attribution_requirements(self, data_source: str) -> List[str]:
        """Get attribution requirements for a data source."""
        attribution_map = {
            'google_places': [
                'Data provided by Google Places API',
                '© Google LLC. All rights reserved.',
                'Google and the Google logo are registered trademarks of Google LLC.'
            ],
            'foursquare': [
                'Data provided by Foursquare Places API',
                '© Foursquare Labs, Inc. All rights reserved.',
                'Foursquare and the Foursquare logo are registered trademarks of Foursquare Labs, Inc.'
            ],
            'yelp': [
                'Data provided by Yelp Fusion API',
                '© Yelp Inc. All rights reserved.',
                'Yelp and the Yelp logo are registered trademarks of Yelp Inc.'
            ],
            'osm': [
                'Data provided by OpenStreetMap contributors',
                '© OpenStreetMap contributors. Licensed under ODbL.',
                'OpenStreetMap data is available under the Open Database License.'
            ],
            'web_scraping': [
                'Data scraped from publicly available websites',
                'Respects robots.txt and terms of service',
                'Attribution provided where required'
            ]
        }
        
        return attribution_map.get(data_source, [
            'Data source attribution required',
            'Please check original source for attribution requirements'
        ])
    
    def validate_data_usage(self, data: Dict[str, any], source: str) -> ComplianceCheck:
        """Validate that data usage is compliant."""
        violations = []
        warnings = []
        recommendations = []
        
        # Check for personal information
        personal_info_fields = ['email', 'phone', 'address', 'name']
        for field in personal_info_fields:
            if field in data and data[field]:
                warnings.append(f"Data contains personal information: {field}")
                recommendations.append("Ensure data is publicly available and properly attributed")
        
        # Check for copyrighted content
        if 'description' in data and data['description']:
            if len(data['description']) > 100:
                warnings.append("Long description may contain copyrighted content")
                recommendations.append("Verify content is publicly available and properly attributed")
        
        # Check attribution requirements
        if self.require_attribution:
            attribution_reqs = self.get_attribution_requirements(source)
            recommendations.extend(attribution_reqs)
        
        is_compliant = len(violations) == 0
        
        return ComplianceCheck(
            is_compliant=is_compliant,
            violations=violations,
            warnings=warnings,
            recommendations=recommendations
        )


# Global compliance checker instance
compliance_checker = LegalComplianceChecker()
