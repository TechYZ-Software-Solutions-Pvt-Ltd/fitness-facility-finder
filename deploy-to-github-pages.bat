@echo off
REM GitHub Pages Deployment Script for Windows
REM This script builds the React app and deploys it to GitHub Pages

echo 🚀 Starting GitHub Pages deployment...

REM Check if we're in the right directory
if not exist "frontend" (
    echo ❌ Error: frontend directory not found
    echo Please run this script from the project root directory
    pause
    exit /b 1
)

REM Navigate to frontend directory
cd frontend

REM Install dependencies
echo 📦 Installing dependencies...
call npm install

REM Build the React app
echo 🔨 Building React app...
call npm run build

REM Check if build was successful
if not exist "build" (
    echo ❌ Error: Build failed - build directory not found
    pause
    exit /b 1
)

echo ✅ Build successful!

REM Go back to project root
cd ..

REM Create gh-pages branch if it doesn't exist
echo 🌿 Setting up gh-pages branch...
git checkout -b gh-pages 2>nul || git checkout gh-pages

REM Copy build files to root
echo 📁 Copying build files...
xcopy /E /Y frontend\build\* .

REM Add all files
git add .

REM Commit changes
git commit -m "Deploy to GitHub Pages - %date% %time%"

REM Push to gh-pages branch
echo 🚀 Pushing to GitHub Pages...
git push origin gh-pages

REM Switch back to main branch
git checkout main

echo ✅ Deployment complete!
echo 🌐 Your site should be live at: https://techyz-software-solutions-pvt-ltd.github.io/justlist
echo ⏰ It may take 5-10 minutes for changes to appear
pause
