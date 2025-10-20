@echo off
REM Production Deployment Script for Facility Finder (Windows)
echo 🚀 Starting Production Deployment...

REM Set production environment
set NODE_ENV=production
set FASTAPI_ENV=production

REM Install dependencies
echo 📦 Installing dependencies...
cd frontend
call npm ci --production
cd ..

REM Build frontend
echo 🏗️ Building frontend...
cd frontend
call npm run build
cd ..

REM Install Python dependencies
echo 🐍 Installing Python dependencies...
pip install -r requirements.txt

REM Create production database
echo 🗄️ Setting up production database...
python -c "from src.app.database.connection import create_tables; create_tables()"

REM Start production server
echo 🚀 Starting production server...
python start_backend.py

echo ✅ Production deployment complete!
echo 🌐 Application running on: http://localhost:8000
echo 📚 API Documentation: http://localhost:8000/docs
pause
