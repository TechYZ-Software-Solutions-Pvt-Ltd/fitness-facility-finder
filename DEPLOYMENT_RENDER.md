# Render Backend Deployment Guide

## 🆓 Deploying Backend to Render (100% Free)

### Prerequisites
- GitHub repository with your backend code
- Render account (free signup)

### Step 1: Prepare Backend for Render

Your backend is already configured with:
- ✅ `render.yaml` - Render deployment configuration
- ✅ `start_backend.py` - Backend startup script
- ✅ `requirements.txt` - Python dependencies
- ✅ Absolute imports - Fixed for deployment

### Step 2: Deploy to Render

#### Via Render Dashboard
1. **Go to [render.com](https://render.com)**
2. **Sign up/Login with GitHub**
3. **Click "New +" → "Web Service"**
4. **Connect your repository**: `TechYZ-Software-Solutions-Pvt-Ltd/fitness-facility-finder`
5. **Configure settings**:
   - **Name**: `facility-finder-backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python start_backend.py`
   - **Instance Type**: `Free`
6. **Add Environment Variables** (if needed):
   - `PYTHON_VERSION`: `3.11.0`
   - `PORT`: `10000`
7. **Click "Create Web Service"**

### Step 3: Get Your Backend URL
1. **Wait for deployment** (5-10 minutes)
2. **Copy your backend URL** from Render dashboard
3. **URL format**: `https://facility-finder-backend.onrender.com`

### Step 4: Update Frontend API URL
1. **In Vercel dashboard**, go to your project
2. **Navigate to "Environment Variables"**
3. **Update `REACT_APP_API_URL`** to your Render backend URL
4. **Redeploy** the frontend

### 🎉 Success!
Your backend will be available at:
- `https://your-backend-name.onrender.com`

### ⚠️ Important Notes

#### Free Tier Limitations:
- **Sleeps after 15 minutes** of inactivity
- **Takes 30-60 seconds** to wake up
- **750 hours/month** (enough for 24/7)
- **Perfect for development and small projects**

#### Wake-up Process:
- First request after sleep takes longer
- Subsequent requests are fast
- Consider this for user experience

### 🔧 Troubleshooting

#### Build Issues:
- Check `requirements.txt` has all dependencies
- Verify `start_backend.py` works locally
- Check Render build logs for errors

#### Runtime Issues:
- Check Render service logs
- Verify environment variables
- Ensure port configuration is correct

#### CORS Issues:
- Backend should handle CORS for your frontend domain
- Check CORS settings in FastAPI app

### 📊 Render vs Railway Comparison

| Feature | Render (Free) | Railway (Paid) |
|---------|---------------|----------------|
| **Cost** | ✅ 100% Free | ❌ $5/month |
| **Uptime** | ✅ 750 hours/month | ✅ 24/7 |
| **Sleep** | ⚠️ 15 min timeout | ✅ Always on |
| **Deployment** | ✅ Auto from GitHub | ✅ Auto from GitHub |
| **Custom Domain** | ✅ Free | ✅ Free |
| **SSL** | ✅ Automatic | ✅ Automatic |

### 🚀 Alternative: Fly.io (Also Free)
If you want always-on hosting:

1. **Go to [fly.io](https://fly.io)**
2. **Sign up** (free tier available)
3. **Install Fly CLI**
4. **Deploy with**: `fly deploy`

Fly.io offers:
- ✅ **Always-on** free tier
- ✅ **Global deployment**
- ✅ **Docker-based**
- ✅ **Generous limits**
