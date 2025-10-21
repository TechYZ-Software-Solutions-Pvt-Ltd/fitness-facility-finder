# 🏢 JustList - Universal Facility Finder

A powerful, full-stack web application for finding any type of facilities worldwide using Google Places API with comprehensive data enrichment, search history management, and legal compliance.

**🌐 Live Demo**: [Your Netlify URL]  
**📊 Backend API**: [Your Render URL]  
**📁 Repository**: https://github.com/TechYZ-Software-Solutions-Pvt-Ltd/justlist

## ✨ Features

### 🔍 **Advanced Search Capabilities**
- **Google Places API Integration** - Find facilities worldwide
- **29 Facility Categories** - Fitness, Healthcare, Education, Retail, Hospitality, Finance, and more
- **Hundreds of Facility Types** - Comprehensive taxonomy covering all business types
- **Multi-source Data Enrichment** - Combines Google Places, Foursquare, Yelp, and web scraping
- **Smart Location Selection** - Country, State, City dropdowns with filtering
- **Customizable Results** - Choose which fields to display from 10+ options

### 📊 **Data Management**
- **Search History** - Store and manage up to 30 recent searches
- **Persistent Storage** - All search results saved to database
- **Offline Access** - View stored results without re-querying APIs
- **Data Export** - Export search results in multiple formats

### 🔐 **User Authentication**
- **Secure Login/Registration** - JWT-based authentication
- **User Profiles** - Personalized search history
- **API Key Management** - Secure storage of Google Places API keys

### ⚖️ **Legal Compliance**
- **GDPR Compliant** - Privacy-first data handling
- **CCPA Compliant** - California Consumer Privacy Act compliance
- **Robots.txt Respect** - Web scraping follows website policies
- **Rate Limiting** - Respectful API usage
- **Data Attribution** - Proper source attribution

## 🚀 Deployment

### **Option 1: Use Live Deployment** (Recommended)
The app is already deployed and ready to use:
- **Frontend (Netlify)**: Free, fast, globally distributed
- **Backend (Render)**: Free tier, auto-scales
- **Total Cost**: $0/month

See `CONNECT_FRONTEND_BACKEND.md` for connection details.

### **Option 2: Local Development**

For local development and testing, see `LOCAL_SETUP.md` for complete instructions.

#### Prerequisites
- Node.js 18+ and npm
- Python 3.8+
- Google Places API key (optional for registration/login testing)

#### Quick Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/TechYZ-Software-Solutions-Pvt-Ltd/justlist.git
   cd justlist
   ```

2. **Backend Setup**
   ```bash
   # Install Python dependencies
   pip install -r requirements.txt
   
   # Start the backend server
   python start_backend.py
   ```

3. **Frontend Setup**
   ```bash
   # Navigate to frontend directory
   cd frontend
   
   # Install dependencies
   npm install
   
   # Start the development server
   npm start
   ```

4. **Access the Application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## 🔧 Configuration

### Google Places API Setup
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Enable Places API
3. Create credentials (API Key)
4. Copy your API key
5. Enter it in the search form

### Environment Variables
Create `config/api_keys.env`:
```env
GOOGLE_PLACES_API_KEY=your_google_places_api_key
FOURSQUARE_API_KEY=your_foursquare_api_key
YELP_API_KEY=your_yelp_api_key
```

## 📁 Project Structure

```
Facilty Search Demo/
├── frontend/                 # React frontend
│   ├── src/
│   │   ├── components/       # Reusable UI components
│   │   ├── pages/           # Page components
│   │   ├── services/        # API services
│   │   ├── contexts/        # React contexts
│   │   └── utils/           # Utility functions
├── src/app/                 # FastAPI backend
│   ├── api/                 # API endpoints
│   ├── auth/                # Authentication
│   ├── database/            # Database models
│   ├── services/            # Business logic
│   └── utils/               # Utilities
├── docs/                    # Documentation
├── config/                  # Configuration files
└── requirements.txt         # Python dependencies
```

## 🛠️ Technology Stack

### Frontend
- **React 18** - UI framework
- **TypeScript** - Type safety
- **Material-UI** - Component library
- **React Router** - Navigation
- **Axios** - HTTP client

### Backend
- **FastAPI** - Web framework
- **SQLAlchemy** - ORM
- **SQLite** - Database
- **Pydantic** - Data validation
- **JWT** - Authentication

### Data Sources
- **Google Places API** - Primary data source
- **Foursquare Places API** - Additional venue data
- **Yelp Fusion API** - Business reviews and ratings
- **OpenStreetMap** - Open-source mapping data
- **Web Scraping** - Additional business information

## 📊 API Endpoints

### Authentication
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `GET /auth/me` - Get current user
- `POST /auth/refresh` - Refresh token

### Facilities
- `POST /facilities/search` - Search facilities
- `GET /facilities/history` - Get search history
- `GET /facilities/history/{id}/facilities` - Get stored results
- `DELETE /facilities/history/{id}` - Delete search history

## 🔒 Security Features

- **JWT Authentication** - Secure token-based auth
- **Password Hashing** - bcrypt password encryption
- **CORS Protection** - Cross-origin request security
- **Input Validation** - Pydantic data validation
- **SQL Injection Prevention** - SQLAlchemy ORM protection
- **Rate Limiting** - API abuse prevention

## 📈 Performance

- **Database Indexing** - Optimized queries
- **Caching** - Search result caching
- **Pagination** - Efficient data loading
- **Lazy Loading** - On-demand component loading
- **Compression** - Gzip response compression

## 🧪 Testing

```bash
# Backend tests
python -m pytest tests/

# Frontend tests
cd frontend
npm test
```

## 🚀 Deployment

### Streamlit Cloud
1. Connect your GitHub repository
2. Set environment variables
3. Deploy automatically

### Docker
```bash
# Build and run with Docker
docker-compose up --build
```

### Manual Deployment
1. Set up production database
2. Configure environment variables
3. Build frontend: `npm run build`
4. Start backend: `python start_backend.py`

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Check the documentation in `/docs`
- Review the API documentation at `/docs` endpoint

## 🙏 Acknowledgments

- Google Places API for location data
- Material-UI for UI components
- FastAPI for backend framework
- React community for frontend tools

---

**Built with ❤️ for efficient facility discovery**