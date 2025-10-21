#!/bin/bash

echo "========================================"
echo "  JustList - Deploy to GitHub Pages"
echo "  with Backend Connection"
echo "========================================"
echo ""

# Check if backend URL is provided
if [ -z "$1" ]; then
    echo "ERROR: Backend URL not provided!"
    echo ""
    echo "Usage: ./deploy-with-backend.sh YOUR_RENDER_URL"
    echo "Example: ./deploy-with-backend.sh https://justlist-backend.onrender.com"
    echo ""
    echo "To get your Render URL:"
    echo "1. Go to https://dashboard.render.com/"
    echo "2. Find your 'justlist-backend' service"
    echo "3. Copy the URL"
    echo ""
    exit 1
fi

BACKEND_URL=$1

echo "Backend URL: $BACKEND_URL"
echo ""
echo "Building frontend with backend connection..."
echo ""

# Navigate to frontend
cd frontend

# Set environment variable and build
export REACT_APP_API_URL=$BACKEND_URL
echo "REACT_APP_API_URL is set to: $REACT_APP_API_URL"
echo ""

# Build the app
echo "Building React app..."
npm run build

if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: Build failed!"
    exit 1
fi

# Go back to root
cd ..

# Copy to docs folder
echo ""
echo "Copying to docs folder..."
cp -r frontend/build/* docs/

# Add and commit
echo ""
echo "Committing changes..."
git add docs/
git add frontend/
git commit -m "Deploy with backend: $BACKEND_URL"

# Push to GitHub
echo ""
echo "Pushing to GitHub..."
git push origin main

echo ""
echo "========================================"
echo "  Deployment Complete!"
echo "========================================"
echo ""
echo "Backend: $BACKEND_URL"
echo "Frontend: https://techyz-software-solutions-pvt-ltd.github.io/justlist/"
echo ""
echo "Wait 2-5 minutes for GitHub Pages to update."
echo ""

