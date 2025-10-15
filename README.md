# 🏋️‍♂️ Fitness Facility Finder

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Streamlit Cloud](https://img.shields.io/badge/Streamlit%20Cloud-Ready-FF4B4B.svg)](https://share.streamlit.io/)

A powerful open-source Streamlit application that helps you find fitness facilities (gyms, yoga studios, fitness centers) in your area using Google Places API and web scraping technology.

## ✨ Features

- **🔍 Smart Search**: Find fitness facilities by location and type
- **✏️ Custom Business Types**: Enter your own fitness facility type or choose from 80+ predefined options
- **📊 Detailed Information**: Get contact details, ratings, and more
- **🌍 Global Coverage**: Search in multiple countries and cities
- **🏛️ India Support**: Complete state and district coverage for India
- **📱 Mobile Responsive**: Works perfectly on desktop and mobile devices
- **🔒 Secure**: Built-in security features and rate limiting
- **✅ Form Validation**: Smart validation with auto-focus on required fields
- **📥 Export Data**: Download results as CSV files
- **☁️ Free Deployment**: Deploy to Streamlit Cloud for free
- **🚀 One-Click Deploy**: Easy deployment with Streamlit Community Cloud

## 🚀 Quick Start

### Option 1: Streamlit Cloud (Recommended - FREE!)

[![Deploy to Streamlit Cloud](https://img.shields.io/badge/Deploy%20to-Streamlit%20Cloud-FF4B4B?style=for-the-badge&logo=streamlit)](https://share.streamlit.io/)

1. **Fork this repository** on GitHub
2. **Go to [share.streamlit.io](https://share.streamlit.io)**
3. **Sign in with GitHub**
4. **Click "New app"**
5. **Select your forked repository**
6. **Set main file path**: `app.py`
7. **Deploy!** 🎉

### Option 2: Local Development

```bash
# Clone and setup
git clone https://github.com/yourusername/fitness-facility-finder.git
cd fitness-facility-finder

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp config/env.example .env
# Edit .env with your Google Places API key

# Run the application
python run.py
# OR
streamlit run app.py
```

### Option 3: Using Make (Linux/Mac)

```bash
# Setup and run
make dev

# Or individual commands
make install    # Install dependencies
make setup-env  # Setup environment file
make run        # Run application
```

**Access the app**: http://localhost:8501

## 🔑 Getting Your API Key

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable **Places API**
4. Create an **API Key**
5. Set up **billing** (required for Places API)
6. Add the key to your `.env` file

## 📖 Usage

1. **Enter your Google Places API key** (required)
2. **Select your country and city** (required)
3. **Choose the type of fitness facility**:
   - Select from 80+ predefined options (Gym, Yoga Studio, CrossFit, etc.)
   - Or choose "Custom..." to enter your own business type
4. **Set maximum results** (1-60)
5. **Click "Search Facilities"**
6. **View and download results**

### 🎯 Custom Business Types
- Select "Custom..." from the Business Type dropdown
- Enter any fitness facility type (e.g., "CrossFit Box", "MMA Gym", "Dance Studio")
- The app will search for facilities matching your custom term

## 🚀 Deployment Options

### 🆓 **Free Deployment (Recommended)**

#### **Railway** (Easiest)
1. Push to GitHub
2. Connect to [railway.app](https://railway.app)
3. Add `GOOGLE_PLACES_API_KEY` environment variable
4. Deploy automatically!

**Quick Start**: See [deploy-railway.md](deploy-railway.md) for step-by-step guide

#### **Other Free Options**
- **Render**: 750 hours/month free
- **Heroku**: 550-1000 hours/month free  
- **Google Cloud Run**: 2M requests/month free
- **Vercel**: Unlimited personal projects free

📖 **Complete Guide**: [FREE_DEPLOYMENT.md](FREE_DEPLOYMENT.md)

### 🐳 Docker Deployment
```bash
cd deploy && docker-compose up -d
```

### ☁️ Paid Cloud Platforms
- **AWS Elastic Beanstalk**: `eb deploy`
- **Azure Container Instances**: Deploy via Azure CLI
- **DigitalOcean App Platform**: One-click deployment

See [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) for detailed instructions.

## 🛠️ Development

### Prerequisites
- Python 3.8+
- Google Places API key
- Git

### Setup
```bash
# Fork and clone
git clone https://github.com/YOUR_USERNAME/fitness-facility-finder.git
cd fitness-facility-finder

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp config/env.example .env
# Edit .env with your API key

# Run development server
python run.py
# OR
streamlit run app.py
```

### Testing
```bash
# Test Docker build
docker build -f deploy/Dockerfile -t fitness-finder .

# Test docker-compose
cd deploy && docker-compose up
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](docs/CONTRIBUTING.md).

### Ways to Contribute
- 🐛 **Bug fixes**
- ✨ **New features**
- 📚 **Documentation**
- 🎨 **UI/UX improvements**
- 🧪 **Tests**

### Quick Contribution
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 🔒 Security Features

- **🔐 API Key Protection**: Secure handling of API keys
- **⏱️ Rate Limiting**: Prevents API abuse (10 requests/session)
- **🛡️ Input Sanitization**: Protects against injection attacks
- **📊 Secure Logging**: Monitors all requests
- **⏰ Session Management**: Automatic session timeout
- **🔍 Health Checks**: Built-in monitoring

## 📊 Project Structure

```
fitness-facility-finder/
├── app.py               # Main Streamlit application
├── assets/              # Static assets
│   └── gym360_logo.png  # Application logo
├── config/              # Configuration files
│   ├── env.example      # Environment variables template
│   └── .streamlit/      # Streamlit configuration
├── docs/                # Documentation
│   ├── CONTRIBUTING.md  # Contribution guidelines
│   ├── CODE_OF_CONDUCT.md # Code of conduct
│   └── SECURITY.md      # Security policy
├── testing/             # Testing documentation
│   ├── LOCAL_TESTING.md # Local testing guide
│   └── MOBILE_TESTING.md # Mobile testing guide
├── run.py               # Main entry point script
├── requirements.txt     # Python dependencies
├── LICENSE              # MIT License
├── README.md            # This file
├── .gitignore           # Git ignore rules
├── PROJECT_STRUCTURE.md # Detailed structure guide
└── STREAMLIT_CLOUD_DEPLOY.md # Streamlit Cloud deployment guide
```

📖 **For detailed structure information, see [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)**

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python 3.8+
- **APIs**: Google Places API
- **Web Scraping**: BeautifulSoup, Requests
- **Data Processing**: Pandas
- **Containerization**: Docker
- **Deployment**: Multi-platform support

## 📈 Roadmap

- [ ] **v2.0**: User authentication system
- [ ] **v2.1**: Advanced filtering options
- [ ] **v2.2**: Facility reviews and ratings
- [ ] **v2.3**: Mobile app version
- [ ] **v2.4**: Real-time notifications
- [ ] **v2.5**: API for third-party integrations

## 🆘 Support

- **🐛 Bug Reports**: [GitHub Issues](https://github.com/yourusername/fitness-facility-finder/issues)
- **💬 Discussions**: [GitHub Discussions](https://github.com/yourusername/fitness-facility-finder/discussions)
- **📧 Email**: info@techyz.net
- **📖 Documentation**: [Wiki](https://github.com/yourusername/fitness-facility-finder/wiki)

## 🙏 Acknowledgments

- **Google Places API** for location data
- **Streamlit** for the web framework
- **BeautifulSoup** for web scraping
- **Pandas** for data manipulation
- **Docker** for containerization
- **All contributors** who help improve this project

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/fitness-facility-finder&type=Date)](https://star-history.com/#yourusername/fitness-facility-finder&Date)

---

<div align="center">

**🚀 Powered by [Techyz Software Solutions Private Limited](https://techyz.com)**

[![GitHub stars](https://img.shields.io/github/stars/yourusername/fitness-facility-finder?style=social)](https://github.com/yourusername/fitness-facility-finder)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/fitness-facility-finder?style=social)](https://github.com/yourusername/fitness-facility-finder)
[![GitHub watchers](https://img.shields.io/github/watchers/yourusername/fitness-facility-finder?style=social)](https://github.com/yourusername/fitness-facility-finder)

</div>