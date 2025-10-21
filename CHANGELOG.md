# 📋 Changelog

All notable changes to JustList project are documented in this file.

## [2.0.0] - 2025-10-21

### 🎉 **Major Release - Production Ready**

#### 🐛 **Critical Bug Fixes**
- **Fixed Google Places API URL** - Added missing trailing slash that was causing 404 errors on all searches
- **Fixed database initialization** - Added `init_database.py` script for easy setup
- **Fixed `.gitignore`** - Data files now properly tracked in repository
- **Fixed error handling** - Frontend now displays detailed backend error messages

#### ✨ **New Features**
- **29 Facility Categories** - Universal facility finder with comprehensive taxonomy
- **API Key Browser Storage** - User API keys saved in localStorage (not database)
- **Registration Success Message** - Professional green alert with auto-redirect to login
- **Comprehensive Help Tab** - Setup guides for all 6 data sources:
  - Google Places API
  - Foursquare Places API
  - Yelp Fusion API
  - OpenStreetMap
  - Facebook Graph API
  - Instagram Basic Display API
- **Better Error Messages** - Detailed error reporting from Google API
- **Improved Logging** - Registration and search endpoints have detailed logging

#### 📚 **Documentation**
- Added `DEPLOYMENT_STATUS.md` - Current deployment status and next steps
- Added `LOCAL_SETUP.md` - Complete local development guide
- Added `CONNECT_FRONTEND_BACKEND.md` - Netlify + Render connection guide
- Added `DEPLOYMENT_GUIDE.md` - Comprehensive deployment instructions
- Added `TROUBLESHOOTING.md` - Consolidated troubleshooting guide
- Added `CLEANUP_SUMMARY.md` - Repository cleanup history
- Added `init_database.py` - Database initialization script
- Updated `README.md` - Latest features and updates
- Updated all deployment documentation

#### 🧹 **Cleanup**
- Removed redundant documentation files (4 files)
- Removed Vercel configuration (using Netlify)
- Removed duplicate data files
- Consolidated troubleshooting guides
- Cleaned Python cache and log files
- Total: ~1,100 lines of redundant code removed

#### 🚀 **Deployment**
- **Frontend**: Netlify configuration (`netlify.toml`)
- **Backend**: Render configuration (`render.yaml`)
- **Cost**: $0/month (both free tiers)
- **Status**: Production-ready

#### 🔧 **Technical Improvements**
- Better error handling in search endpoint
- Improved registration validation
- Enhanced logging throughout backend
- Professional success/error messages
- Responsive UI improvements

---

## [1.0.0] - Initial Release

### ✨ **Features**
- Basic facility search functionality
- User registration and authentication
- Search history for logged-in users
- Google Places API integration
- Material-UI responsive design
- FastAPI backend
- SQLite database
- JWT authentication

---

## Versioning

This project follows [Semantic Versioning](https://semver.org/):
- **MAJOR**: Incompatible API changes
- **MINOR**: New functionality (backwards-compatible)
- **PATCH**: Bug fixes (backwards-compatible)

---

## Links

- **Repository**: https://github.com/TechYZ-Software-Solutions-Pvt-Ltd/justlist
- **Issues**: https://github.com/TechYZ-Software-Solutions-Pvt-Ltd/justlist/issues
- **Documentation**: See README.md and docs/ folder

