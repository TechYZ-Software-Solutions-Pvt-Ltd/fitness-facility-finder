# 🚀 Railway Deployment Guide

Deploy your Fitness Facility Finder to Railway in just a few steps!

## 📋 Prerequisites

- ✅ **Git repository** (already set up)
- ✅ **Google Places API Key** (get from Google Cloud Console)
- ✅ **Railway account** (free at railway.app)

## 🚀 Step-by-Step Deployment

### Step 1: Create GitHub Repository

1. **Go to GitHub**: [github.com/new](https://github.com/new)
2. **Repository name**: `fitness-facility-finder`
3. **Description**: `🏋️‍♂️ Open-source Streamlit app to find fitness facilities using Google Places API`
4. **Visibility**: Public
5. **Don't initialize** with README (we already have one)
6. **Click "Create repository"**

### Step 2: Push to GitHub

```bash
# Add remote origin (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/fitness-facility-finder.git

# Push to GitHub
git push -u origin main
```

### Step 3: Deploy on Railway

1. **Go to Railway**: [railway.app](https://railway.app)
2. **Sign up**: Click "Login" → "Login with GitHub"
3. **Create New Project**: 
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your `fitness-facility-finder` repository
4. **Railway will automatically detect** it's a Python/Streamlit app
5. **Wait for deployment** (usually 2-3 minutes)

### Step 4: Set Environment Variables

1. **Go to your project** in Railway dashboard
2. **Click on your service**
3. **Go to "Variables" tab**
4. **Add environment variable**:
   - **Key**: `GOOGLE_PLACES_API_KEY`
   - **Value**: Your Google Places API key
5. **Click "Add"**

### Step 5: Access Your App

Your app will be available at: `https://your-app-name.railway.app`

## ✅ That's It!

Railway handles everything automatically:
- ✅ Detects Python/Streamlit app
- ✅ Installs dependencies from requirements.txt
- ✅ Runs your app
- ✅ Provides HTTPS URL
- ✅ Auto-deploys on code changes

## 🔧 Configuration Details

### Railway Configuration (railway.toml):
```toml
[build]
builder = "nixpacks"

[deploy]
startCommand = "streamlit run src/app.py --server.port=$PORT --server.address=0.0.0.0"
healthcheckPath = "/_stcore/health"
healthcheckTimeout = 100
restartPolicyType = "on_failure"
```

### Environment Variables:
- `GOOGLE_PLACES_API_KEY`: Your Google Places API key
- `PORT`: Automatically set by Railway
- `STREAMLIT_SERVER_HEADLESS`: true (for production)

## 💰 Free Tier Limits

Railway's free tier includes:
- **$5 credit monthly** (usually enough for small apps)
- **512MB RAM**
- **1GB storage**
- **Custom domains**
- **Automatic deployments**

## 🆘 Troubleshooting

### App Won't Start?
1. **Check logs**: Go to Railway dashboard → Logs
2. **Verify environment variables**: Ensure API key is set
3. **Check requirements.txt**: All dependencies listed

### API Key Issues?
1. **Verify API key**: Check it's correct
2. **Enable Places API**: In Google Cloud Console
3. **Set up billing**: Required for Places API

### Build Errors?
1. **Check Python version**: Railway uses Python 3.11
2. **Verify file structure**: Ensure src/app.py exists
3. **Check dependencies**: All packages in requirements.txt

## 🔄 Updates

To update your app:
1. **Make changes** to your code
2. **Commit and push** to GitHub:
   ```bash
   git add .
   git commit -m "Update: description of changes"
   git push origin main
   ```
3. **Railway automatically deploys** the changes!

## 📊 Monitoring

### Railway Dashboard:
- **Deployments**: View deployment history
- **Logs**: Real-time application logs
- **Metrics**: CPU, memory usage
- **Variables**: Environment variables

### Health Check:
Your app includes a health check at: `/_stcore/health`

## 🎉 Success!

Once deployed, your Fitness Facility Finder will be:
- ✅ **Live and accessible** worldwide
- ✅ **Mobile responsive** on all devices
- ✅ **Secure** with environment variables
- ✅ **Auto-updating** on code changes
- ✅ **Monitored** with Railway's tools

## 📱 Mobile Testing

Test your deployed app on mobile:
1. **Open the Railway URL** on your phone
2. **Test all features**:
   - Form inputs
   - Search functionality
   - Data table scrolling
   - Download feature
3. **Verify responsiveness** on different screen sizes

## 🔗 Share Your App

Your app is now live at: `https://your-app-name.railway.app`

Share it with:
- **Social media**
- **Developer communities**
- **Potential users**
- **Portfolio/resume**

---

**Congratulations! Your Fitness Facility Finder is now live on Railway! 🎉**

Need help? Check Railway's documentation or community forums.
