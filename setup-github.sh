#!/bin/bash

echo "🚀 Setting up GitHub repository for Fitness Facility Finder"
echo "========================================================"

echo ""
echo "📋 Prerequisites:"
echo "- GitHub account"
echo "- Git installed"
echo "- Google Places API key ready"
echo ""

read -p "Enter your GitHub username: " repo_name
read -p "Enter repository name (default: fitness-facility-finder): " app_name

if [ -z "$app_name" ]; then
    app_name="fitness-facility-finder"
fi

echo ""
echo "🔧 Setting up Git repository..."

# Initialize git if not already done
if [ ! -d ".git" ]; then
    echo "Initializing Git repository..."
    git init
else
    echo "Git repository already initialized."
fi

# Add all files
echo "Adding files to Git..."
git add .

# Create initial commit
echo "Creating initial commit..."
git commit -m "Initial commit: Fitness Facility Finder v1.0"

# Add remote origin
echo "Setting up remote origin..."
git remote add origin "https://github.com/$repo_name/$app_name.git"

echo ""
echo "✅ Git setup complete!"
echo ""
echo "📝 Next steps:"
echo "1. Go to https://github.com/new"
echo "2. Create repository named: $app_name"
echo "3. Don't initialize with README (we already have one)"
echo "4. Click 'Create repository'"
echo "5. Run: git push -u origin main"
echo ""
echo "🚀 Then deploy to Railway:"
echo "1. Go to https://railway.app"
echo "2. Sign up with GitHub"
echo "3. Deploy from GitHub repo"
echo "4. Add GOOGLE_PLACES_API_KEY environment variable"
echo ""

read -p "Press Enter to continue..."
