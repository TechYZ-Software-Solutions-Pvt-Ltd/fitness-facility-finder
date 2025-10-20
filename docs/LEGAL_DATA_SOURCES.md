# Legal Data Sources & APIs

This document outlines all legal and ethical ways to obtain business data that can be combined with Google Places API and web scraping.

## 🌐 **Primary Data Sources**

### **1. Google Places API** ✅
- **Status:** Currently implemented
- **Legal:** Official Google API with proper licensing
- **Data:** Basic business info, ratings, contact details
- **Cost:** Pay-per-use with free tier
- **Rate Limits:** 1000 requests/day (free), higher with paid plans

### **2. Foursquare Places API** ✅
- **Status:** Available for implementation
- **Legal:** Official API with proper licensing
- **Data:** 100M+ POIs, user reviews, photos, detailed categories
- **Cost:** Free tier available, reasonable pricing
- **Rate Limits:** 1000 requests/day (free)
- **Setup:** Get API key from [Foursquare Developer](https://developer.foursquare.com/)

### **3. Yelp Fusion API** ✅
- **Status:** Available for implementation
- **Legal:** Official business directory API
- **Data:** Reviews, ratings, photos, business details, hours
- **Cost:** Free tier (500 requests/day)
- **Rate Limits:** 500 requests/day (free)
- **Setup:** Get API key from [Yelp Developers](https://www.yelp.com/developers/)

### **4. OpenStreetMap (OSM) Overpass API** ✅
- **Status:** Available for implementation
- **Legal:** Open-source, completely free
- **Data:** Global business and POI data, community-maintained
- **Cost:** Completely free
- **Rate Limits:** Reasonable limits, no strict quotas
- **Setup:** No API key required

## 🔗 **Social Media APIs**

### **5. Facebook Graph API** ✅
- **Status:** Available for implementation
- **Legal:** Official Facebook API for business pages
- **Data:** Business info, posts, reviews, hours, contact details
- **Cost:** Free with rate limits
- **Rate Limits:** Varies by endpoint
- **Setup:** Create Facebook App, get App ID and Secret

### **6. Instagram Basic Display API** ✅
- **Status:** Available for implementation
- **Legal:** Official Instagram business API
- **Data:** Business posts, followers, engagement metrics
- **Cost:** Free with rate limits
- **Rate Limits:** Varies by endpoint
- **Setup:** Create Instagram App, get App ID and Secret

### **7. LinkedIn Company API** ✅
- **Status:** Available for implementation
- **Legal:** Official LinkedIn business directory
- **Data:** Company info, employee count, industry, contact details
- **Cost:** Free tier available
- **Rate Limits:** Varies by endpoint
- **Setup:** Create LinkedIn App, get Client ID and Secret

## 🏛️ **Government & Public Data**

### **8. Open Data Portals** ✅
- **Status:** Available for implementation
- **Legal:** Public government data (varies by jurisdiction)
- **Data:** Business registrations, licenses, permits, compliance status
- **Cost:** Usually free
- **Rate Limits:** Varies by source
- **Examples:**
  - USA: [data.gov](https://data.gov/)
  - UK: [data.gov.uk](https://data.gov.uk/)
  - EU: [European Data Portal](https://www.europeandataportal.eu/)

### **9. Chamber of Commerce APIs** ✅
- **Status:** Available for implementation
- **Legal:** Official business directories
- **Data:** Member businesses, contact info, business categories
- **Cost:** Varies by location and organization
- **Rate Limits:** Varies by source
- **Examples:**
  - Local chamber websites
  - Regional business directories
  - Industry-specific associations

## 📊 **Business Intelligence APIs**

### **10. Clearbit Enrichment API** ✅
- **Status:** Available for implementation
- **Legal:** Official business data API
- **Data:** Company information, employee count, funding, social profiles
- **Cost:** Free tier available, paid plans
- **Rate Limits:** 50 requests/month (free)
- **Setup:** Get API key from [Clearbit](https://clearbit.com/)

### **11. FullContact Person API** ✅
- **Status:** Available for implementation
- **Legal:** Official contact enrichment API
- **Data:** Social profiles, contact information, professional details
- **Cost:** Free tier available, paid plans
- **Rate Limits:** 100 requests/month (free)
- **Setup:** Get API key from [FullContact](https://www.fullcontact.com/)

### **12. Hunter.io Email Finder** ✅
- **Status:** Available for implementation
- **Legal:** Official email discovery API
- **Data:** Business email addresses, email verification
- **Cost:** Free tier available, paid plans
- **Rate Limits:** 25 requests/month (free)
- **Setup:** Get API key from [Hunter.io](https://hunter.io/)

## 🌍 **Geographic & Location APIs**

### **13. Mapbox Geocoding API** ✅
- **Status:** Available for implementation
- **Legal:** Official mapping and geocoding service
- **Data:** Address geocoding, reverse geocoding, place search
- **Cost:** Free tier available, paid plans
- **Rate Limits:** 100,000 requests/month (free)
- **Setup:** Get API key from [Mapbox](https://www.mapbox.com/)

### **14. HERE Geocoding API** ✅
- **Status:** Available for implementation
- **Legal:** Official mapping and location services
- **Data:** Geocoding, reverse geocoding, place search, routing
- **Cost:** Free tier available, paid plans
- **Rate Limits:** 1000 requests/month (free)
- **Setup:** Get API key from [HERE Developer](https://developer.here.com/)

## 🔍 **Web Scraping (Legal & Ethical)**

### **15. Public Website Scraping** ✅
- **Status:** Currently implemented
- **Legal:** When done ethically and legally
- **Data:** Contact info, social media links, business descriptions
- **Cost:** Free (server resources only)
- **Rate Limits:** Self-imposed to be respectful
- **Best Practices:**
  - Respect robots.txt
  - Use reasonable delays between requests
  - Don't overload servers
  - Follow terms of service

### **16. RSS Feeds & Sitemaps** ✅
- **Status:** Available for implementation
- **Legal:** Publicly available data
- **Data:** Business updates, news, announcements
- **Cost:** Free
- **Rate Limits:** Self-imposed
- **Examples:**
  - Business blog RSS feeds
  - News site business sections
  - Industry publication feeds

## 📈 **Implementation Strategy**

### **Phase 1: Core APIs** (Current)
- ✅ Google Places API
- ✅ Web Scraping
- ✅ OpenStreetMap

### **Phase 2: Business Directories** (Next)
- 🔄 Foursquare Places API
- 🔄 Yelp Fusion API
- 🔄 Government Open Data

### **Phase 3: Social Media** (Future)
- 🔄 Facebook Graph API
- 🔄 Instagram Basic Display API
- 🔄 LinkedIn Company API

### **Phase 4: Advanced Enrichment** (Future)
- 🔄 Clearbit Enrichment API
- 🔄 Hunter.io Email Finder
- 🔄 FullContact Person API

## ⚖️ **Legal Considerations**

### **✅ Always Legal:**
- Official APIs with proper licensing
- Public government data
- OpenStreetMap data
- Publicly available website content (with proper attribution)

### **⚠️ Requires Care:**
- Web scraping (respect robots.txt and terms of service)
- Social media APIs (follow platform guidelines)
- Rate limiting (don't overload services)

### **❌ Avoid:**
- Scraping private or protected data
- Violating terms of service
- Overwhelming servers with requests
- Using data without proper attribution

## 💰 **Cost Optimization**

### **Free Tier Strategy:**
1. **Primary:** Google Places API (free tier)
2. **Secondary:** OpenStreetMap (completely free)
3. **Tertiary:** Foursquare, Yelp (free tiers)
4. **Fallback:** Web scraping (free but limited)

### **Paid Tier Strategy:**
1. **Scale up:** Google Places API paid tier
2. **Add depth:** Foursquare, Yelp paid tiers
3. **Social data:** Facebook, Instagram APIs
4. **Advanced:** Clearbit, Hunter.io for email discovery

## 🚀 **Benefits of Multi-Source Approach**

### **Data Quality:**
- **Verification:** Cross-reference data from multiple sources
- **Completeness:** Fill gaps where one source lacks data
- **Accuracy:** Higher confidence with multiple confirmations

### **Reliability:**
- **Redundancy:** If one source fails, others continue working
- **Coverage:** Different sources excel in different regions/industries
- **Freshness:** Some sources update more frequently than others

### **Competitive Advantage:**
- **Richer profiles:** More comprehensive business information
- **Better user experience:** Complete data in one place
- **Higher value:** More useful than single-source solutions

## 📋 **Setup Instructions**

### **1. API Key Configuration:**
```bash
# Copy the example file
cp config/api_keys.env.example config/api_keys.env

# Edit with your actual API keys
nano config/api_keys.env
```

### **2. Environment Variables:**
```bash
# Add to your .env file
FOURSQUARE_API_KEY=your_key_here
YELP_API_KEY=your_key_here
FACEBOOK_APP_ID=your_app_id_here
# ... etc
```

### **3. Enable Sources:**
```python
# In enrichment_service.py
self.sources = {
    'foursquare': DataSource(..., enabled=True),
    'yelp': DataSource(..., enabled=True),
    'osm': DataSource(..., enabled=True),
    # ... etc
}
```

This comprehensive approach ensures you get the best possible business data while staying completely legal and ethical!
