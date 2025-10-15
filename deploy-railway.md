# 🚀 Railway Deployment - Step by Step

Railway is the **easiest** way to deploy your Fitness Facility Finder for free!

## 📋 Prerequisites

- GitHub account
- Google Places API key
- Your code ready in the project folder

## 🚀 Step-by-Step Deployment

### Step 1: Push to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Fitness Facility Finder"

# Create repository on GitHub first, then:
git remote add origin https://github.com/YOUR_USERNAME/fitness-facility-finder.git

# Push to GitHub
git push -u origin main
```

### Step 2: Deploy on Railway

1. **Go to Railway**: [railway.app](https://railway.app)

2. **Sign Up**: Click "Login" → "Login with GitHub"

3. **Create New Project**: 
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your `fitness-facility-finder` repository

4. **Configure Environment**:
   - Go to your project dashboard
   - Click on your service
   - Go to "Variables" tab
   - Add: `GOOGLE_PLACES_API_KEY` = your API key

5. **Deploy**: Railway automatically detects it's a Python app and deploys!

### Step 3: Access Your App

Your app will be available at: `https://your-app-name.railway.app`

## ✅ That's It!

Railway handles everything automatically:
- ✅ Detects Python/Streamlit app
- ✅ Installs dependencies from requirements.txt
- ✅ Runs your app
- ✅ Provides HTTPS URL
- ✅ Auto-deploys on code changes

## 🔧 Custom Configuration (Optional)

If you need custom settings, create a `railway.toml` file:

```toml
[build]
builder = "nixpacks"

[deploy]
startCommand = "streamlit run src/app.py --server.port=$PORT --server.address=0.0.0.0"
healthcheckPath = "/_stcore/health"
healthcheckTimeout = 100
restartPolicyType = "on_failure"
```

## 💰 Free Tier Limits

Railway's free tier includes:
- **$5 credit monthly** (usually enough for small apps)
- **512MB RAM**
- **1GB storage**
- **Custom domains**

## 🆘 Troubleshooting

### App Won't Start?
1. Check environment variables are set
2. Look at deployment logs
3. Ensure requirements.txt is complete

### API Key Issues?
1. Verify API key is correct
2. Check if Places API is enabled in Google Cloud
3. Ensure billing is set up

### Need Help?
- Railway Discord: [discord.gg/railway](https://discord.gg/railway)
- Railway Docs: [docs.railway.app](https://docs.railway.app)

## 🎉 Success!

Once deployed, share your app with the world! Your Fitness Facility Finder is now live and accessible to anyone with the URL.

**Example URL**: `https://fitness-finder-production.up.railway.app`
