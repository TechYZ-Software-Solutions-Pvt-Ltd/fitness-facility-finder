#!/bin/bash

# GitHub Pages Deployment Script
# This script builds the React app and deploys it to GitHub Pages

echo "🚀 Starting GitHub Pages deployment..."

# Check if we're in the right directory
if [ ! -d "frontend" ]; then
    echo "❌ Error: frontend directory not found"
    echo "Please run this script from the project root directory"
    exit 1
fi

# Navigate to frontend directory
cd frontend

# Install dependencies
echo "📦 Installing dependencies..."
npm install

# Build the React app
echo "🔨 Building React app..."
npm run build

# Check if build was successful
if [ ! -d "build" ]; then
    echo "❌ Error: Build failed - build directory not found"
    exit 1
fi

echo "✅ Build successful!"

# Go back to project root
cd ..

# Create gh-pages branch if it doesn't exist
echo "🌿 Setting up gh-pages branch..."
git checkout -b gh-pages 2>/dev/null || git checkout gh-pages

# Copy build files to root
echo "📁 Copying build files..."
cp -r frontend/build/* .

# Add all files
git add .

# Commit changes
git commit -m "Deploy to GitHub Pages - $(date)"

# Push to gh-pages branch
echo "🚀 Pushing to GitHub Pages..."
git push origin gh-pages

# Switch back to main branch
git checkout main

echo "✅ Deployment complete!"
echo "🌐 Your site should be live at: https://techyz-software-solutions-pvt-ltd.github.io/justlist"
echo "⏰ It may take 5-10 minutes for changes to appear"
