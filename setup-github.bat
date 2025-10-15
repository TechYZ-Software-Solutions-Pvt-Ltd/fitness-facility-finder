@echo off
echo 🚀 Setting up GitHub repository for Fitness Facility Finder
echo ========================================================

echo.
echo 📋 Prerequisites:
echo - GitHub account
echo - Git installed
echo - Google Places API key ready
echo.

set /p repo_name="Enter your GitHub username: "
set /p app_name="Enter repository name (default: fitness-facility-finder): "

if "%app_name%"=="" set app_name=fitness-facility-finder

echo.
echo 🔧 Setting up Git repository...

REM Initialize git if not already done
if not exist .git (
    echo Initializing Git repository...
    git init
) else (
    echo Git repository already initialized.
)

REM Add all files
echo Adding files to Git...
git add .

REM Create initial commit
echo Creating initial commit...
git commit -m "Initial commit: Fitness Facility Finder v1.0"

REM Add remote origin
echo Setting up remote origin...
git remote add origin https://github.com/%repo_name%/%app_name%.git

echo.
echo ✅ Git setup complete!
echo.
echo 📝 Next steps:
echo 1. Go to https://github.com/new
echo 2. Create repository named: %app_name%
echo 3. Don't initialize with README (we already have one)
echo 4. Click "Create repository"
echo 5. Run: git push -u origin main
echo.
echo 🚀 Then deploy to Railway:
echo 1. Go to https://railway.app
echo 2. Sign up with GitHub
echo 3. Deploy from GitHub repo
echo 4. Add GOOGLE_PLACES_API_KEY environment variable
echo.

pause
