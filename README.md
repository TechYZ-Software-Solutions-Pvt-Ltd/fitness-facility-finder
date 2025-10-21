# 🏢 JustList - Universal Facility Finder

A powerful, full-stack web application for finding any type of facilities worldwide using Google Places API with comprehensive data enrichment, search history management, and legal compliance.

**🌐 Live Demo**: https://techyz-software-solutions-pvt-ltd.github.io/justlist/  
**📁 Repository**: https://github.com/TechYZ-Software-Solutions-Pvt-Ltd/justlist  
**📚 Documentation**: See `DEPLOYMENT_COMPLETE.md` for full deployment guide

## ✅ **Latest Updates (v3.0 - October 2025)**

### **🔧 Recent Fixes:**
- ✅ **Navigation 404 Fixed**: React Router navigation working perfectly on GitHub Pages
- ✅ **Custom 404.html**: Automatic redirects for all unknown routes
- ✅ **FormLink Component**: Smart routing for internal/external links
- ✅ **Critical Bug Fixed**: Google Places API URL corrected - search working!
- ✅ **Better Error Messages**: Detailed error reporting from backend

### **✨ New Features:**
- ✅ **180+ Facility Types**: Comprehensive taxonomy across 29 categories
- ✅ **Search History**: Store up to 30 searches with delete functionality
- ✅ **Data Sources Tab**: Manage API keys for 6 different data providers
- ✅ **Listing Customization**: Choose which facility info to display
- ✅ **Help Documentation**: Complete setup guides for all APIs
- ✅ **Professional UI**: Responsive design with Material-UI

### **🚀 Deployment:**
- ✅ **GitHub Pages**: Free frontend hosting
- ✅ **Render Backend**: Free API hosting
- ✅ **Total Cost**: $0/month
- ✅ **Automated Deployment**: One-click deployment scripts

## ✨ Features

### 🔍 **Advanced Search Capabilities**
- **Google Places API Integration** - Find facilities worldwide
- **180+ Facility Types** - Comprehensive taxonomy covering:
  - Fitness & Sports (gyms, studios, sports facilities)
  - Healthcare (hospitals, clinics, pharmacies)
  - Education (schools, universities, libraries)
  - Retail (stores, malls, markets)
  - Hospitality (hotels, restaurants, cafes)
  - Finance (banks, ATMs, insurance)
  - Professional Services (legal, consulting, real estate)
  - Entertainment (theaters, museums, parks)
  - And 21 more categories!
- **Smart Location Selection** - Country → State → City filtering
- **Real-time Results** - Instant search with loading indicators
- **Customizable Display** - Choose which facility details to show

### 📊 **Search History Management**
- **Up to 30 Recent Searches** - Automatic history tracking
- **View Previous Results** - Click any history item to see results
- **Delete Entries** - Remove unwanted search records
- **Pagination** - Easy navigation through history
- **User-Specific** - Each user's history is private

### 🔐 **User Authentication**
- **Secure Registration** - Email validation and password strength checks
- **Encrypted Passwords** - bcrypt-sha256 hashing
- **Session Management** - Persistent login state
- **Logout Redirect** - Automatic redirect to login page
- **User Profiles** - Personalized experience

### 🎛️ **Settings & Customization**

#### **Data Sources Tab** (Logged-in users only)
Manage API keys for:
- Google Places API
- Foursquare Places API
- Yelp Fusion API
- OpenStreetMap Overpass API
- Facebook Graph API
- Instagram Basic Display API

#### **Listing Tab**
Customize displayed facility information:
- Name, Address, Phone Number
- Website, Rating, Reviews
- Opening Hours, Price Level
- Photos, Types, and more

#### **Help Tab**
Complete setup guides for all 6 data sources with step-by-step instructions.

### ⚖️ **Legal Compliance**
- **Publicly Available Data Only** - No unauthorized scraping
- **Respects robots.txt** - Web scraping follows website policies
- **Rate Limiting** - Respectful API usage
- **Data Attribution** - Proper source credits
- **MIT License** - Clear legal framework

## 🚀 Quick Start

### **Option 1: Use Live App** (Recommended)

Simply visit: https://techyz-software-solutions-pvt-ltd.github.io/justlist/

1. Register a new account
2. Login with your credentials
3. Go to Settings → Data Sources
4. Add your Google Places API key
5. Start searching for facilities!

### **Option 2: Local Development**

#### Prerequisites
- Node.js 18+ and npm
- Python 3.11+
- Google Places API key (optional for testing)

#### Quick Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/TechYZ-Software-Solutions-Pvt-Ltd/justlist.git
   cd justlist
   ```

2. **Initialize Database**
   ```bash
   python init_database.py
   ```

3. **Backend Setup**
   ```bash
   # Install Python dependencies
   pip install -r requirements.txt
   
   # Start the backend server
   python start_backend.py
   ```

4. **Frontend Setup** (in a new terminal)
   ```bash
   cd frontend
   
   # Install dependencies
   npm install
   
   # Start the development server
   npm start
   ```

5. **Access the Application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

See `LOCAL_SETUP.md` for detailed instructions.

## 🔧 Configuration

### Google Places API Setup
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable "Places API"
4. Create credentials → API Key
5. **Important**: Enable billing (required for Places API)
6. Copy your API key
7. In the app: Settings → Data Sources → Paste your key

For detailed guides for all 6 APIs, see Settings → Help in the app.

## 📁 Project Structure

```
justlist/
├── frontend/                    # React frontend
│   ├── public/
│   │   ├── index.html          # Main HTML file
│   │   └── 404.html            # GitHub Pages redirect
│   ├── src/
│   │   ├── components/         # Reusable UI components
│   │   │   ├── forms/          # Generic form components
│   │   │   ├── Header.tsx      # App header with settings
│   │   │   ├── SearchForm.tsx  # Main search form
│   │   │   └── ResultsDisplay.tsx
│   │   ├── pages/              # Page components
│   │   │   ├── HomePage.tsx
│   │   │   ├── LoginPage.tsx
│   │   │   └── RegisterPage.tsx
│   │   ├── contexts/           # React contexts
│   │   │   └── AuthContext.tsx
│   │   ├── services/           # API services
│   │   ├── utils/              # Utility functions
│   │   └── data/               # Static data (taxonomy, fields)
│   └── package.json
├── src/app/                    # FastAPI backend
│   ├── api/                    # API endpoints
│   │   ├── auth.py            # Authentication
│   │   └── facilities_simple.py
│   ├── database/               # Database layer
│   │   ├── connection.py
│   │   └── models.py          # SQLAlchemy models
│   ├── services/               # Business logic
│   │   └── places_service.py  # Google Places integration
│   └── utils/                  # Utilities
├── docs/                       # Build output for GitHub Pages
├── init_database.py            # Database initialization
├── start_backend.py            # Backend startup script
├── requirements.txt            # Python dependencies
├── deploy-simple.bat           # Windows deployment
├── deploy-to-github-pages.sh  # Linux/macOS deployment
├── DEPLOYMENT_COMPLETE.md      # Complete deployment guide
├── TROUBLESHOOTING.md          # Troubleshooting guide
└── README.md                   # This file
```

## 🛠️ Technology Stack

### Frontend
- **React 18** - Modern UI framework
- **TypeScript** - Type safety and better DX
- **Material-UI (MUI) v5** - Professional component library
- **React Router DOM v6** - Client-side routing
- **React Query** - Data fetching and caching
- **Axios** - HTTP client
- **Country-State-City** - Location data

### Backend
- **FastAPI** - High-performance web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **SQLite** - Lightweight database
- **Pydantic** - Data validation
- **bcrypt-sha256** - Password hashing
- **python-jose** - JWT tokens

### Deployment
- **GitHub Pages** - Frontend hosting (free)
- **Render** - Backend hosting (free tier)
- **GitHub Actions** - CI/CD ready

### Data Sources (Optional)
- **Google Places API** - Primary data source
- **Foursquare Places API** - Additional venue data
- **Yelp Fusion API** - Business reviews and ratings
- **OpenStreetMap** - Open-source mapping data
- **Facebook Graph API** - Social media integration
- **Instagram Basic Display API** - Photo integration

## 📊 API Endpoints

### Authentication
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `POST /auth/logout` - User logout
- `GET /auth/me` - Get current user

### Facilities
- `POST /facilities/search` - Search facilities (requires Google API key)
- `GET /facilities/history` - Get user's search history
- `GET /facilities/history/{id}/facilities` - Get stored results for a search
- `DELETE /facilities/history/{id}` - Delete a search history entry

Full API documentation available at: http://localhost:8000/docs (when running locally)

## 🔒 Security Features

- **JWT Authentication** - Secure token-based authentication
- **Password Encryption** - bcrypt-sha256 hashing (up to 72 chars)
- **User Isolation** - Each user's data is private
- **CORS Protection** - Configured for production origins
- **Input Validation** - Comprehensive validation on frontend and backend
- **SQL Injection Prevention** - SQLAlchemy ORM protection
- **Session Management** - Secure session handling

## 🎯 Deployment

### **GitHub Pages Deployment** (Automated)

#### Windows:
```bash
cd "Facilty Search Production"
.\deploy-simple.bat
```

#### Linux/macOS:
```bash
cd "Facilty Search Production"
./deploy-to-github-pages.sh
```

### **Manual Deployment**

See `DEPLOYMENT_COMPLETE.md` for complete deployment instructions including:
- GitHub Pages setup
- Render backend deployment
- Connecting frontend to backend
- Environment variables configuration

## 🧪 Testing

```bash
# Backend tests
python -m pytest tests/

# Frontend tests
cd frontend
npm test

# Type checking
npm run type-check

# Linting
npm run lint
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Key Points:**
- ✅ Free to use, modify, and distribute
- ✅ Commercial use allowed
- ✅ Only uses publicly available data
- ✅ Respects all data source terms of service

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

For support and questions:
- **Issues**: Create an issue on [GitHub](https://github.com/TechYZ-Software-Solutions-Pvt-Ltd/justlist/issues)
- **Documentation**: Check `DEPLOYMENT_COMPLETE.md` and `TROUBLESHOOTING.md`
- **API Docs**: Visit `/docs` endpoint when running locally

## 🎉 Acknowledgments

- **Google Places API** - Primary facility data source
- **Material-UI** - Beautiful React components
- **FastAPI** - Modern Python web framework
- **React Community** - Excellent ecosystem and tools
- **Open Source Community** - For all the amazing libraries

## 📈 Roadmap

### Planned Features:
- [ ] Map view for search results
- [ ] Advanced filtering and sorting
- [ ] Facility comparison tool
- [ ] Export results to CSV/PDF
- [ ] Mobile app (React Native)
- [ ] Multi-language support
- [ ] Dark mode theme
- [ ] Favorites/Bookmarks
- [ ] Social sharing

## 🌟 Star History

If you find this project useful, please consider giving it a star on GitHub! ⭐

---

**Built with ❤️ by TechYZ Software Solutions Pvt Ltd**

**Live App**: https://techyz-software-solutions-pvt-ltd.github.io/justlist/

**Version**: 3.0.0 | **Last Updated**: October 21, 2025 | **Status**: ✅ Production Ready