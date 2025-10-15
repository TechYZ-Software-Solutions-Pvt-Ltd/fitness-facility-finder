@echo off
echo 🚀 Fitness Facility Finder - Cloud Deployment
echo ==============================================

REM Check if Docker is installed
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker is not installed. Please install Docker Desktop first.
    pause
    exit /b 1
)

REM Check if .env file exists
if not exist .env (
    echo ⚠️  .env file not found. Creating from template...
    copy ..\config\env.example .env
    echo 📝 Please edit .env file with your Google Places API key
    echo    Then run this script again.
    pause
    exit /b 1
)

REM Build Docker image
echo 🔨 Building Docker image...
docker build -t fitness-finder .

if %errorlevel% equ 0 (
    echo ✅ Docker image built successfully!
) else (
    echo ❌ Docker build failed!
    pause
    exit /b 1
)

REM Run with docker-compose
echo 🚀 Starting application with docker-compose...
docker-compose up -d

if %errorlevel% equ 0 (
    echo ✅ Application deployed successfully!
    echo 🌐 Access your app at: http://localhost:8501
    echo 📊 View logs with: docker-compose logs -f
    echo 🛑 Stop with: docker-compose down
) else (
    echo ❌ Deployment failed!
    pause
    exit /b 1
)

pause
