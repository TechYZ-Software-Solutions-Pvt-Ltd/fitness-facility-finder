# 🔗 Connect Frontend (Netlify) to Backend (Render)

This guide shows you how to connect your deployed frontend and backend.

## 📋 Prerequisites

- ✅ Frontend deployed on Netlify
- ✅ Backend deployed on Render
- ✅ Backend is running and accessible

---

## 🚀 Step-by-Step Connection

### **Step 1: Get Your Render Backend URL**

1. Go to: https://dashboard.render.com
2. Sign in with your account
3. Find your backend service (e.g., `justlist-backend`)
4. Click on it to open the service details
5. **Copy the URL** at the top (looks like):
   ```
   https://justlist-backend.onrender.com
   ```
   Or:
   ```
   https://your-service-name.onrender.com
   ```

**📸 Screenshot Location:**
- Dashboard → Your Service → Top of page → "Your service is live at [URL]"

---

### **Step 2: Add Backend URL to Netlify Environment Variables**

1. Go to: https://app.netlify.com
2. Click on your **justlist** site
3. Go to: **Site settings** (in the top menu)
4. In the left sidebar: Click **Environment variables**
5. Click: **Add a variable** (or **Add environment variable**)
6. Enter:
   - **Key**: `REACT_APP_API_URL`
   - **Value**: Your Render URL (from Step 1)
   
   Example:
   ```
   Key: REACT_APP_API_URL
   Value: https://justlist-backend.onrender.com
   ```

7. Click: **Save** or **Create variable**

**⚠️ Important Notes:**
- Must start with `REACT_APP_` (React requirement)
- **DO NOT** include trailing slash: ❌ `https://example.com/`
- **CORRECT** format: ✅ `https://example.com`

---

### **Step 3: Redeploy Frontend**

After adding the environment variable, Netlify needs to rebuild to use it:

**Option A: Manual Trigger (Fastest)**
1. Go to: **Deploys** tab
2. Click: **Trigger deploy** button
3. Select: **Deploy site**
4. Wait for build to complete (~2-3 minutes)

**Option B: Automatic (Git Push)**
- Any new commit to your repository will trigger a rebuild
- Environment variables will be included automatically

---

### **Step 4: Verify Connection**

Once Netlify finishes deploying:

1. **Open your Netlify site** (e.g., `https://your-site.netlify.app`)
2. **Try to Register**:
   - Click "Register"
   - Fill in the form
   - Submit
   - ✅ Should work without errors!
3. **Try to Login**:
   - Use the credentials you just created
   - ✅ Should redirect to main page
4. **Try to Search** (requires Google API key in Render):
   - Enter location and facility type
   - Click search
   - ✅ Should return results

---

## 🔍 Troubleshooting

### **Problem: "Network Error" when registering**

**Possible Causes:**
1. Environment variable not set correctly
2. Render backend not running
3. Frontend not rebuilt after adding variable

**Solutions:**
1. **Check Environment Variable:**
   - Netlify → Site settings → Environment variables
   - Verify `REACT_APP_API_URL` exists
   - Verify URL is correct (no trailing slash)

2. **Check Render Backend:**
   - Go to Render dashboard
   - Check if service is "Live" (green dot)
   - Click "Logs" to see if it's running
   - If "Suspended", it will wake up on first request (takes ~30 seconds)

3. **Redeploy Frontend:**
   - Netlify → Deploys → Trigger deploy
   - Wait for completion
   - Try again

### **Problem: "CORS Error" in browser console**

**Cause:** Backend CORS settings

**Solution:** 
The backend should already have CORS configured. If you see this error:
1. Check Render logs for errors
2. Verify backend is running
3. Ensure backend URL in Netlify matches exactly

### **Problem: Backend URL shows error page**

**Cause:** Render free tier spins down after 15 minutes of inactivity

**Solution:**
1. Wait 30 seconds for backend to wake up
2. Refresh the page
3. Try your action again
4. Backend will stay awake while in use

### **Problem: Search returns no results**

**Cause:** Google Places API key not set in Render

**Solution:**
1. Go to Render dashboard
2. Click your backend service
3. Go to: **Environment** tab
4. Add: `GOOGLE_PLACES_API_KEY` with your API key
5. Service will automatically restart

---

## ✅ Expected Behavior

### **Frontend (Netlify)**
- URL: `https://your-site.netlify.app`
- Loads: Login/Register pages
- Shows: Search form
- Works: All UI interactions

### **Backend (Render)**
- URL: `https://your-backend.onrender.com`
- Provides: API endpoints
- Handles: Authentication, searches, database
- Wakes: Within 30 seconds when called

### **Together**
- ✅ Registration works
- ✅ Login works
- ✅ Search works (with Google API key)
- ✅ Search history saves
- ✅ All features functional

---

## 📊 Environment Variables Summary

### **Netlify (Frontend)**
```
REACT_APP_API_URL=https://your-backend.onrender.com
```

### **Render (Backend)**
```
GOOGLE_PLACES_API_KEY=your_google_api_key_here
SECRET_KEY=your_random_secret_key_here
DATABASE_URL=sqlite:///./data/facility_finder.db
```

---

## 🎉 Success!

Once connected, your full JustList app is live:
- Frontend: Fast, responsive UI on Netlify
- Backend: Powerful API on Render
- Database: Persistent storage on Render
- Cost: **$0/month** (both free tiers)

**Test the full flow:**
1. Register → ✅ Creates account
2. Login → ✅ Authenticates user
3. Search → ✅ Finds facilities
4. View History → ✅ Shows past searches

Your app is production-ready! 🚀

---

## 📝 Quick Reference

**Netlify Dashboard:** https://app.netlify.com
**Render Dashboard:** https://dashboard.render.com

**Environment Variable Name:** `REACT_APP_API_URL`
**Environment Variable Value:** Your Render backend URL

**After adding variable:** Trigger deploy (Deploys → Trigger deploy)

