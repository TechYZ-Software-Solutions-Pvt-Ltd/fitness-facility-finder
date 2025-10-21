# 🚀 JustList Deployment Guide

## 📋 Overview

This guide provides deployment instructions for both frontend (React) and backend (FastAPI) components of JustList.

**Version**: 2.0.0  
**Last Updated**: October 21, 2025  
**Status**: Production-ready with all bugs fixed

### ✅ **What's Working:**
- ✅ Search functionality (Google Places API)
- ✅ 29 comprehensive facility categories
- ✅ User registration & login
- ✅ Search history for logged-in users
- ✅ API key browser storage
- ✅ Detailed error messages
- ✅ All features tested and working locally

## 🎯 **Recommended: Netlify for Frontend**

Netlify works best with our monorepo structure and has automatic configuration via `netlify.toml`.

### ✅ Deploy Frontend to Netlify (5 Minutes)

1. **Go to**: https://app.netlify.com
2. **Sign in** with your GitHub account
3. **Click**: "Add new site" → "Import an existing project"
4. **Choose**: GitHub
5. **Select**: `TechYZ-Software-Solutions-Pvt-Ltd/justlist`
6. **Click**: "Deploy site" (Netlify auto-detects `netlify.toml`)

**Configuration (Auto-detected)**:
- Base directory: `frontend`
- Build command: `npm run build`
- Publish directory: `build`

**That's it!** Your frontend will be live in ~2 minutes.

---

## 🔧 Deploy Backend to Render (Free)

### ✅ Deploy FastAPI Backend to Render

1. **Go to**: https://render.com
2. **Sign in** with your GitHub account
3. **Click**: "New +" → "Web Service"
4. **Connect**: `TechYZ-Software-Solutions-Pvt-Ltd/justlist`
5. **Configure**:
   - **Name**: `justlist-backend`
   - **Root Directory**: *(leave empty)*
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python start_backend.py`
6. **Environment Variables** (click "Advanced"):
   - `GOOGLE_PLACES_API_KEY`: Your Google API key
   - `SECRET_KEY`: Generate a random secret (e.g., use `openssl rand -hex 32`)
7. **Click**: "Create Web Service"

**Your backend will be live at**: `https://justlist-backend.onrender.com`

---

## ⚙️ Connect Frontend to Backend

After deploying both:

1. **Get your backend URL** from Render (e.g., `https://justlist-backend.onrender.com`)
2. **Update frontend environment**:
   - In Netlify dashboard → Site settings → Environment variables
   - Add: `REACT_APP_API_URL` = `https://justlist-backend.onrender.com`
3. **Redeploy** frontend (Netlify will auto-rebuild)

---

## 🌐 Custom Domain (Optional)

### For Netlify (Frontend):
1. Go to: Site settings → Domain management
2. Click: "Add custom domain"
3. Follow the DNS configuration steps

### For Render (Backend):
1. Go to: Settings → Custom domains
2. Click: "Add custom domain"
3. Follow the DNS configuration steps

---

## 📊 Deployment Status

### Frontend (Netlify):
- ✅ Free tier: 100GB bandwidth/month
- ✅ Automatic HTTPS
- ✅ Continuous deployment from GitHub
- ✅ Build time: ~2 minutes

### Backend (Render):
- ✅ Free tier: 750 hours/month
- ✅ Automatic HTTPS
- ✅ Continuous deployment from GitHub
- ✅ Build time: ~3 minutes
- ⚠️ Free tier spins down after 15 min inactivity (first request takes ~30s)

---

## 🔍 Troubleshooting

### Frontend Build Fails:
- Check build logs in Netlify dashboard
- Verify `netlify.toml` is in repository root
- Ensure all dependencies are in `package.json`

### Backend Build Fails:
- Check build logs in Render dashboard
- Verify `requirements.txt` has all dependencies
- Check Python version (should be 3.8+)

### API Connection Fails:
- Verify `REACT_APP_API_URL` is set in Netlify
- Check backend is running (visit backend URL)
- Verify CORS is configured in backend

---

## 📝 Notes

- **Netlify** is better than Vercel for this monorepo structure
- **Render** free tier is truly free (unlike Railway which has limits)
- Both platforms auto-deploy when you push to GitHub
- SSL certificates are automatic on both platforms

---

## 🎉 Success!

Once deployed, your JustList app will be:
- **Frontend**: Live on Netlify with custom URL
- **Backend**: Live on Render with API endpoints
- **Database**: SQLite file on Render (persists across deployments)
- **Auto-deploy**: Enabled on both platforms

Enjoy your deployed app! 🚀

