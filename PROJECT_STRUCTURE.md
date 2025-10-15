# 📁 Project Structure Guide

This document explains the organized folder structure of the Fitness Facility Finder project.

## 🏗️ Directory Structure

```
fitness-facility-finder/
├── 📁 src/                    # Source Code
│   ├── app.py                # Main Streamlit application
│   └── main.py               # Google App Engine entry point
├── 📁 assets/                # Static Assets
│   └── gym360_logo.png       # Application logo
├── 📁 config/                # Configuration Files
│   ├── env.example           # Environment variables template
│   └── .streamlit/           # Streamlit configuration
│       └── config.toml       # Streamlit settings
├── 📁 deploy/                # Deployment Files
│   ├── Dockerfile            # Docker container configuration
│   ├── docker-compose.yml    # Docker Compose setup
│   ├── deploy.sh             # Linux/Mac deployment script
│   ├── deploy.bat            # Windows deployment script
│   ├── Procfile              # Heroku deployment configuration
│   └── app.yaml              # Google App Engine configuration
├── 📁 docs/                  # Documentation
│   ├── CONTRIBUTING.md       # Contribution guidelines
│   ├── DEPLOYMENT.md         # Deployment guide
│   ├── QUICK_DEPLOY.md       # Quick deployment guide
│   ├── GITHUB_SETUP.md       # GitHub repository setup
│   ├── CODE_OF_CONDUCT.md    # Community code of conduct
│   └── SECURITY.md           # Security policy
├── run.py                    # Main entry point script
├── setup.py                  # Python package setup
├── Makefile                  # Development commands
├── requirements.txt          # Python dependencies
├── LICENSE                   # MIT License
├── README.md                 # Main project documentation
├── .gitignore                # Git ignore rules
└── PROJECT_STRUCTURE.md      # This file
```

## 📂 Directory Purposes

### 🎯 `src/` - Source Code
- **Purpose**: Contains all application source code
- **Files**:
  - `app.py`: Main Streamlit application with all functionality
  - `main.py`: Entry point for Google App Engine deployment

### 🎨 `assets/` - Static Assets
- **Purpose**: Contains images, icons, and other static files
- **Files**:
  - `gym360_logo.png`: Application logo used in the UI

### ⚙️ `config/` - Configuration
- **Purpose**: Contains configuration files and templates
- **Files**:
  - `env.example`: Template for environment variables
  - `.streamlit/config.toml`: Streamlit application settings

### 🚀 `deploy/` - Deployment
- **Purpose**: Contains all deployment-related files
- **Files**:
  - `Dockerfile`: Docker container configuration
  - `docker-compose.yml`: Multi-container Docker setup
  - `deploy.sh` & `deploy.bat`: Deployment scripts for different OS
  - `Procfile`: Heroku deployment configuration
  - `app.yaml`: Google App Engine configuration

### 📚 `docs/` - Documentation
- **Purpose**: Contains all project documentation
- **Files**:
  - `CONTRIBUTING.md`: Guidelines for contributors
  - `DEPLOYMENT.md`: Comprehensive deployment guide
  - `QUICK_DEPLOY.md`: Quick start deployment guide
  - `GITHUB_SETUP.md`: GitHub repository setup guide
  - `CODE_OF_CONDUCT.md`: Community standards
  - `SECURITY.md`: Security policy and vulnerability reporting

### 🏠 Root Directory
- **Purpose**: Contains main project files and entry points
- **Files**:
  - `run.py`: Main entry point for running the application
  - `setup.py`: Python package configuration
  - `Makefile`: Development and deployment commands
  - `requirements.txt`: Python package dependencies
  - `LICENSE`: MIT License
  - `README.md`: Main project documentation
  - `.gitignore`: Git ignore rules

## 🚀 Quick Commands

### Development
```bash
# Run the application
python run.py

# Install dependencies
pip install -r requirements.txt

# Setup environment
cp config/env.example .env
```

### Deployment
```bash
# Docker deployment
make docker-build
make docker-run

# Docker Compose deployment
make deploy

# Cloud deployment
# See docs/DEPLOYMENT.md for detailed instructions
```

### Development Tools
```bash
# Show all available commands
make help

# Run tests
make test

# Clean temporary files
make clean

# Format code
make format
```

## 🔧 File Path Updates

After restructuring, all file paths have been updated:

### Application Files
- **Logo**: `assets/gym360_logo.png`
- **Main App**: `src/app.py`
- **Config**: `config/.streamlit/config.toml`

### Deployment Files
- **Docker**: `deploy/Dockerfile`
- **Docker Compose**: `deploy/docker-compose.yml`
- **Scripts**: `deploy/deploy.sh`, `deploy/deploy.bat`

### Documentation
- **Contributing**: `docs/CONTRIBUTING.md`
- **Deployment**: `docs/DEPLOYMENT.md`
- **Security**: `docs/SECURITY.md`

## 📋 Benefits of This Structure

### ✅ **Organization**
- Clear separation of concerns
- Easy to find specific files
- Logical grouping of related files

### ✅ **Maintainability**
- Easy to update and modify
- Clear file responsibilities
- Scalable structure

### ✅ **Deployment**
- Separate deployment configurations
- Easy to deploy to different platforms
- Clear deployment scripts

### ✅ **Documentation**
- Centralized documentation
- Easy to find specific guides
- Professional structure

### ✅ **Development**
- Clear development workflow
- Easy to add new features
- Standard Python project structure

## 🔄 Migration Notes

If you're migrating from the old structure:

1. **Update imports**: All file paths have been updated
2. **Update scripts**: Use new entry points (`run.py`)
3. **Update documentation**: References point to new locations
4. **Update deployment**: Use new deployment scripts

## 📞 Support

For questions about the project structure:
- Check the documentation in `docs/`
- Review the `README.md` for quick start
- See `CONTRIBUTING.md` for development guidelines

---

**This structure follows Python and open source best practices for maintainable, scalable projects.**
