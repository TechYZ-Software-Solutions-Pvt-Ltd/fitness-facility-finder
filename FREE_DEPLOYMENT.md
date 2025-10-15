# 🆓 Free Deployment Guide

This guide shows you how to deploy your Fitness Facility Finder for **FREE** on various cloud platforms.

## 🎯 Best Free Options

### 1. 🚀 **Railway** (Recommended - Easiest)

**Why Railway?**
- ✅ **Free tier**: $5 credit monthly (enough for small apps)
- ✅ **GitHub integration**: Auto-deploy from GitHub
- ✅ **Zero configuration**: Works out of the box
- ✅ **Custom domains**: Free subdomain included

**Steps:**
1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/fitness-facility-finder.git
   git push -u origin main
   ```

2. **Connect to Railway**:
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository

3. **Set Environment Variables**:
   - Go to your project → Variables
   - Add: `GOOGLE_PLACES_API_KEY` = your API key

4. **Deploy**: Railway automatically builds and deploys!

**Result**: `https://your-app-name.railway.app`

---

### 2. 🌟 **Render** (Great Alternative)

**Why Render?**
- ✅ **Free tier**: 750 hours/month
- ✅ **Auto-deploy**: From GitHub
- ✅ **Custom domains**: Free subdomain
- ✅ **SSL included**: Automatic HTTPS

**Steps:**
1. **Push to GitHub** (same as Railway)

2. **Connect to Render**:
   - Go to [render.com](https://render.com)
   - Sign up with GitHub
   - Click "New" → "Web Service"
   - Connect your repository

3. **Configure**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run src/app.py --server.port=$PORT --server.address=0.0.0.0`
   - **Environment**: Add `GOOGLE_PLACES_API_KEY`

4. **Deploy**: Click "Create Web Service"

**Result**: `https://your-app-name.onrender.com`

---

### 3. 🐳 **Heroku** (Classic Choice)

**Why Heroku?**
- ✅ **Free tier**: 550-1000 dyno hours/month
- ✅ **Easy deployment**: Git-based
- ✅ **Add-ons**: Many free add-ons available

**Steps:**
1. **Install Heroku CLI**:
   ```bash
   # Windows
   winget install Heroku.HerokuCLI
   
   # Or download from heroku.com
   ```

2. **Login and Create App**:
   ```bash
   heroku login
   heroku create your-app-name
   ```

3. **Set Environment Variables**:
   ```bash
   heroku config:set GOOGLE_PLACES_API_KEY=your_api_key
   ```

4. **Deploy**:
   ```bash
   git push heroku main
   ```

**Result**: `https://your-app-name.herokuapp.com`

---

### 4. ☁️ **Google Cloud Run** (Most Powerful)

**Why Google Cloud Run?**
- ✅ **Free tier**: 2 million requests/month
- ✅ **Serverless**: Pay only for usage
- ✅ **Global**: Deploy worldwide
- ✅ **Fast**: Google's infrastructure

**Steps:**
1. **Setup Google Cloud**:
   - Go to [console.cloud.google.com](https://console.cloud.google.com)
   - Create new project
   - Enable Cloud Run API

2. **Install Google Cloud CLI**:
   ```bash
   # Windows
   winget install Google.CloudSDK
   ```

3. **Build and Deploy**:
   ```bash
   # Build container
   gcloud builds submit --tag gcr.io/PROJECT-ID/fitness-finder
   
   # Deploy to Cloud Run
   gcloud run deploy fitness-finder \
     --image gcr.io/PROJECT-ID/fitness-finder \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --set-env-vars GOOGLE_PLACES_API_KEY=your_api_key
   ```

**Result**: `https://fitness-finder-xxx.run.app`

---

### 5. 🚀 **Vercel** (Fast & Modern)

**Why Vercel?**
- ✅ **Free tier**: Unlimited personal projects
- ✅ **Fast**: Global CDN
- ✅ **Easy**: GitHub integration
- ✅ **Modern**: Built for developers

**Steps:**
1. **Push to GitHub** (same as above)

2. **Connect to Vercel**:
   - Go to [vercel.com](https://vercel.com)
   - Sign up with GitHub
   - Import your repository

3. **Configure**:
   - **Framework Preset**: Other
   - **Build Command**: `pip install -r requirements.txt`
   - **Output Directory**: Leave empty
   - **Install Command**: `pip install -r requirements.txt`

4. **Add Environment Variables**:
   - `GOOGLE_PLACES_API_KEY` = your API key

**Result**: `https://your-app-name.vercel.app`

---

## 🎯 **Quick Comparison**

| Platform | Free Tier | Ease | Performance | Best For |
|----------|-----------|------|-------------|----------|
| **Railway** | $5 credit/month | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Beginners |
| **Render** | 750 hours/month | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Small apps |
| **Heroku** | 550-1000 hours/month | ⭐⭐⭐⭐ | ⭐⭐⭐ | Classic choice |
| **Google Cloud Run** | 2M requests/month | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Production |
| **Vercel** | Unlimited personal | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Modern apps |

## 🚀 **Recommended: Railway (Easiest)**

For beginners, I recommend **Railway** because:
- ✅ **Zero configuration** needed
- ✅ **Automatic deployment** from GitHub
- ✅ **Free tier** is generous
- ✅ **Works immediately** with your current structure

### Railway Quick Start:
```bash
# 1. Push to GitHub
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/fitness-facility-finder.git
git push -u origin main

# 2. Go to railway.app
# 3. Connect GitHub repo
# 4. Add GOOGLE_PLACES_API_KEY environment variable
# 5. Deploy automatically!
```

## 🔧 **Pre-Deployment Checklist**

Before deploying, make sure:

- [ ] **API Key Ready**: Get your Google Places API key
- [ ] **Code Pushed**: All code is in GitHub repository
- [ ] **Environment Variables**: Know what to set
- [ ] **Dependencies**: requirements.txt is complete
- [ ] **Port Configuration**: App uses PORT environment variable

## 🆘 **Troubleshooting**

### Common Issues:

1. **App Won't Start**:
   - Check environment variables are set
   - Verify requirements.txt is complete
   - Check build logs for errors

2. **API Key Issues**:
   - Ensure API key is correct
   - Check if Places API is enabled
   - Verify billing is set up

3. **Port Issues**:
   - Make sure app uses `$PORT` environment variable
   - Check if app binds to `0.0.0.0`

### Getting Help:
- Check platform documentation
- Look at build/deployment logs
- Test locally first with `python run.py`

## 💡 **Pro Tips**

1. **Start with Railway** - Easiest for beginners
2. **Test locally first** - Use `python run.py`
3. **Monitor usage** - Stay within free tier limits
4. **Use custom domains** - Most platforms offer free subdomains
5. **Set up monitoring** - Track your app's performance

## 🎉 **Success!**

Once deployed, your Fitness Facility Finder will be available at:
- **Railway**: `https://your-app-name.railway.app`
- **Render**: `https://your-app-name.onrender.com`
- **Heroku**: `https://your-app-name.herokuapp.com`
- **Google Cloud**: `https://your-app-name.run.app`
- **Vercel**: `https://your-app-name.vercel.app`

**Your app is now live and accessible worldwide! 🌍**

---

**Need help?** Check the platform-specific documentation or ask in their community forums.
