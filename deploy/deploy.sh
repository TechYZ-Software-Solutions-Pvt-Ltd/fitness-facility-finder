#!/bin/bash

# Fitness Facility Finder - Cloud Deployment Script
# This script helps deploy the application to various cloud platforms

echo "🚀 Fitness Facility Finder - Cloud Deployment"
echo "=============================================="

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if .env file exists
if [ ! -f .env ]; then
    echo "⚠️  .env file not found. Creating from template..."
    cp ../config/env.example .env
    echo "📝 Please edit .env file with your Google Places API key"
    echo "   Then run this script again."
    exit 1
fi

# Build Docker image
echo "🔨 Building Docker image..."
docker build -t fitness-finder .

if [ $? -eq 0 ]; then
    echo "✅ Docker image built successfully!"
else
    echo "❌ Docker build failed!"
    exit 1
fi

# Run with docker-compose
echo "🚀 Starting application with docker-compose..."
docker-compose up -d

if [ $? -eq 0 ]; then
    echo "✅ Application deployed successfully!"
    echo "🌐 Access your app at: http://localhost:8501"
    echo "📊 View logs with: docker-compose logs -f"
    echo "🛑 Stop with: docker-compose down"
else
    echo "❌ Deployment failed!"
    exit 1
fi
