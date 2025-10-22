#!/bin/bash

# Production Deployment Script for Facility Finder
echo "🚀 Starting Production Deployment..."

# Set production environment
export NODE_ENV=production
export FASTAPI_ENV=production

# Install dependencies
echo "📦 Installing dependencies..."
cd frontend
npm ci --production
cd ..

# Build frontend
echo "🏗️ Building frontend..."
cd frontend
npm run build
cd ..

# Install Python dependencies
echo "🐍 Installing Python dependencies..."
pip install -r requirements.txt

# Create production database
echo "🗄️ Setting up production database..."
python -c "from src.app.database.connection import create_tables; create_tables()"

# Start production server
echo "🚀 Starting production server..."
python start_backend.py

echo "✅ Production deployment complete!"
echo "🌐 Application running on: http://localhost:8000"
echo "📚 API Documentation: http://localhost:8000/docs"
