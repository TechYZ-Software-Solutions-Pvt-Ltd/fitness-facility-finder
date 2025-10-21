@echo off
REM Simple GitHub Pages Deployment Script
echo 🚀 Deploying to GitHub Pages...

REM Build the app
cd frontend
echo 📦 Building React app...
call npm run build

REM Go back to root
cd ..

REM Copy to docs folder
echo 📁 Copying to docs folder...
xcopy /E /Y frontend\build\* docs\

REM Add and commit
echo 📝 Committing changes...
git add docs/
git commit -m "Deploy to GitHub Pages - %date% %time%"

REM Push to GitHub
echo 🚀 Pushing to GitHub...
git push origin main

echo ✅ Deployment complete!
echo 🌐 Your site should be live at: https://techyz-software-solutions-pvt-ltd.github.io/justlist/
echo ⏰ It may take 5-10 minutes for changes to appear
echo.
echo 📋 IMPORTANT: Make sure GitHub Pages is enabled in repository settings:
echo 1. Go to: https://github.com/TechYZ-Software-Solutions-Pvt-Ltd/justlist/settings/pages
echo 2. Source: Deploy from a branch
echo 3. Branch: main
echo 4. Folder: /docs
echo 5. Save
pause
