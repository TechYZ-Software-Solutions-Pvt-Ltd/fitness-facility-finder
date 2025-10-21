@echo off
echo ========================================
echo   JustList - Deploy to GitHub Pages
echo   with Backend Connection
echo ========================================
echo.

REM Check if backend URL is provided
if "%1"=="" (
    echo ERROR: Backend URL not provided!
    echo.
    echo Usage: deploy-with-backend.bat YOUR_RENDER_URL
    echo Example: deploy-with-backend.bat https://justlist-backend.onrender.com
    echo.
    echo To get your Render URL:
    echo 1. Go to https://dashboard.render.com/
    echo 2. Find your "justlist-backend" service
    echo 3. Copy the URL
    echo.
    pause
    exit /b 1
)

set BACKEND_URL=%1

echo Backend URL: %BACKEND_URL%
echo.
echo Building frontend with backend connection...
echo.

REM Navigate to frontend
cd frontend

REM Set environment variable and build
set REACT_APP_API_URL=%BACKEND_URL%
echo REACT_APP_API_URL is set to: %REACT_APP_API_URL%
echo.

REM Build the app
echo Building React app...
call npm run build

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Build failed!
    pause
    exit /b 1
)

REM Go back to root
cd ..

REM Copy to docs folder
echo.
echo Copying to docs folder...
xcopy /E /Y frontend\build\* docs\

REM Add and commit
echo.
echo Committing changes...
git add docs/
git add frontend/
git commit -m "Deploy with backend: %BACKEND_URL%"

REM Push to GitHub
echo.
echo Pushing to GitHub...
git push origin main

echo.
echo ========================================
echo   Deployment Complete!
echo ========================================
echo.
echo Backend: %BACKEND_URL%
echo Frontend: https://techyz-software-solutions-pvt-ltd.github.io/justlist/
echo.
echo Wait 2-5 minutes for GitHub Pages to update.
echo.
pause

