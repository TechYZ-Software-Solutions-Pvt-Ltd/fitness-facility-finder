# 📁 Project Structure Guide

This document explains the organized folder structure of the Fitness Facility Finder project after cleanup and optimization.

## 🏗️ **Current Directory Structure**

```
📦 fitness-facility-finder/
├── 📁 src/                       # Source Code
│   └── app.py                   # Main Streamlit application
├── 📁 assets/                   # Static Assets
│   └── gym360_logo.png         # Application logo
├── 📁 config/                   # Configuration Files
│   ├── env.example             # Environment variables template
│   └── .streamlit/             # Streamlit configuration
│       └── config.toml         # Streamlit settings
├── 📁 docs/                     # Documentation
│   ├── CONTRIBUTING.md         # Contribution guidelines
│   ├── CODE_OF_CONDUCT.md      # Community code of conduct
│   └── SECURITY.md             # Security policy
├── 📁 testing/                  # Testing Documentation
│   ├── LOCAL_TESTING.md        # Local testing guide
│   └── MOBILE_TESTING.md       # Mobile responsiveness testing
├── 📄 .gitignore               # Git ignore rules
├── 📄 LICENSE                  # MIT License
├── 📄 README.md                # Main project documentation
├── 📄 requirements.txt         # Python dependencies
├── 📄 run.py                   # Application entry point
├── 📄 PROJECT_STRUCTURE.md     # This file
└── 📄 STREAMLIT_CLOUD_DEPLOY.md # Streamlit Cloud deployment guide
```

## 📋 **File Descriptions**

### **Source Code (`src/`)**
- **`app.py`**: Main Streamlit application with all functionality
  - Mobile responsive design
  - Google Places API integration
  - Web scraping capabilities
  - Security features and rate limiting
  - CSV export functionality

### **Assets (`assets/`)**
- **`gym360_logo.png`**: Application logo (secure, non-downloadable)

### **Configuration (`config/`)**
- **`env.example`**: Template for environment variables
- **`.streamlit/config.toml`**: Streamlit configuration settings

### **Documentation (`docs/`)**
- **`CONTRIBUTING.md`**: Guidelines for contributing to the project
- **`CODE_OF_CONDUCT.md`**: Community code of conduct
- **`SECURITY.md`**: Security policy and vulnerability reporting

### **Testing (`testing/`)**
- **`LOCAL_TESTING.md`**: Comprehensive local testing guide
- **`MOBILE_TESTING.md`**: Mobile responsiveness testing guide

### **Root Files**
- **`README.md`**: Main project documentation with deployment instructions
- **`requirements.txt`**: Python package dependencies
- **`run.py`**: Simple entry point for running the application
- **`STREAMLIT_CLOUD_DEPLOY.md`**: Step-by-step Streamlit Cloud deployment guide
- **`LICENSE`**: MIT License for open source distribution
- **`.gitignore`**: Git ignore rules for common files

## 🚀 **Deployment Strategy**

### **Primary: Streamlit Cloud (FREE)**
- **File**: `STREAMLIT_CLOUD_DEPLOY.md`
- **Target**: [share.streamlit.io](https://share.streamlit.io)
- **Benefits**: Free, automatic deployments, HTTPS included

### **Local Development**
- **File**: `run.py` or `python -m streamlit run src/app.py`
- **Target**: Local development and testing

## 🧪 **Testing Structure**

### **Local Testing**
- **Guide**: `testing/LOCAL_TESTING.md`
- **Covers**: UI/UX, functionality, API integration, security

### **Mobile Testing**
- **Guide**: `testing/MOBILE_TESTING.md`
- **Covers**: Responsive design, touch interfaces, mobile optimization

## 🔧 **Development Workflow**

### **Running Locally**
```bash
# Method 1: Using run.py
python run.py

# Method 2: Direct Streamlit
python -m streamlit run src/app.py
```

### **Testing**
1. **Local Testing**: Follow `testing/LOCAL_TESTING.md`
2. **Mobile Testing**: Follow `testing/MOBILE_TESTING.md`

### **Deployment**
1. **Streamlit Cloud**: Follow `STREAMLIT_CLOUD_DEPLOY.md`
2. **Code Changes**: Push to GitHub for automatic deployment

## 📱 **Mobile Responsiveness**

The application is fully mobile responsive with:
- **Flexible layouts** that adapt to screen sizes
- **Touch-friendly** buttons and inputs
- **Optimized data tables** for mobile viewing
- **Responsive typography** and spacing

## 🔒 **Security Features**

- **Rate limiting**: 50 requests per 30 minutes (increased from 10)
- **API key validation**: Secure Google Places API key handling
- **Input sanitization**: Protection against malicious inputs
- **Logo protection**: Prevents right-click, drag, and download
- **Session management**: Automatic session timeout

## 🌍 **Internationalization**

- **Multi-country support**: 20+ countries with cities
- **Custom location input**: For locations not in predefined lists
- **Localized search**: Country-specific fitness facility types

## 📊 **Data Export**

- **CSV download**: Export search results with all details
- **Formatted filenames**: Include search parameters and date
- **Complete data**: Contact info, ratings, addresses, websites

## 🎯 **Key Features**

- **Smart Search**: Google Places API integration
- **Web Scraping**: Additional contact information extraction
- **Mobile First**: Responsive design for all devices
- **Security Focused**: Multiple layers of protection
- **User Friendly**: Intuitive interface and clear feedback
- **Open Source**: MIT licensed for community use

## 📈 **Performance Optimizations**

- **Efficient API calls**: Optimized Google Places API usage
- **Caching**: Session-based caching for better performance
- **Error handling**: Graceful error management and user feedback
- **Loading states**: Clear progress indicators for long operations

---

**This structure is optimized for easy maintenance, clear organization, and simple deployment to Streamlit Cloud.**