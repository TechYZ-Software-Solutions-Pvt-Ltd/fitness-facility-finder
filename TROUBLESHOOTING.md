# 🔧 Troubleshooting Guide

## ✅ **RESOLVED: Critical Bug Fixed**

**The "No facilities found" issue was caused by a missing slash in the Google Places API URL.**
- ✅ **Fixed in latest version** (commit d80d97b)
- ✅ **Search now works** with valid Google API key
- ✅ **All 29 facility categories** functional

If you're still experiencing issues, see solutions below.

---

## Common Issues and Solutions

### 🔍 **Issue: "No facilities found. Try adjusting your search criteria."**

This error can occur for several reasons. Follow these steps to diagnose and fix:

---

#### **Possible Cause 1: Google API Key Not Set or Invalid**

**Symptoms:**
- Search returns "No facilities found" immediately
- Works for login/registration but not search

**Solution:**

1. **Check if API key is set in Render:**
   - Go to: https://dashboard.render.com
   - Click your backend service
   - Go to **Environment** tab
   - Check if `GOOGLE_PLACES_API_KEY` exists and has a value

2. **Verify API key is valid:**
   - Go to: https://console.cloud.google.com/apis/credentials
   - Check if your API key is active
   - Verify billing is enabled (Google requires it)
   - Check if Places API is enabled

3. **Add/Update API key in Render:**
   ```
   Key: GOOGLE_PLACES_API_KEY
   Value: Your_Google_API_Key_Here
   ```
   - Service will automatically restart

---

#### **Possible Cause 2: Backend Not Running or Not Connected**

**Symptoms:**
- Network errors in browser console
- Frontend can't reach backend

**Solution:**

1. **Check backend status:**
   - Go to Render dashboard
   - Verify service shows "Live" (green)
   - If "Suspended", wait 30 seconds for it to wake up

2. **Verify frontend has correct backend URL:**
   - Go to Netlify dashboard
   - Site settings → Environment variables
   - Check `REACT_APP_API_URL` exists
   - Value should be: `https://your-backend.onrender.com`

3. **Test backend directly:**
   - Visit: `https://your-backend.onrender.com/docs`
   - Should show FastAPI documentation
   - If error, backend has issues

---

#### **Possible Cause 3: Invalid Search Parameters**

**Symptoms:**
- Some searches work, others don't
- Specific locations return no results

**Solution:**

1. **Try a known location:**
   - Country: United States
   - State: California
   - City: Los Angeles
   - Facility: Gym

2. **Check facility type spelling:**
   - Must match Google Places types exactly
   - Examples: "gym", "hospital", "restaurant"
   - Avoid custom/misspelled types

3. **Simplify search:**
   - Start with fewer filters
   - Increase max results to 20
   - Try different facility categories

---

#### **Possible Cause 4: Google API Quota Exceeded**

**Symptoms:**
- Worked before, suddenly stopped
- Error in backend logs about quota

**Solution:**

1. **Check Google Cloud Console:**
   - Go to: https://console.cloud.google.com/apis/dashboard
   - Check "Quotas" tab
   - See if you've exceeded free tier

2. **Enable billing:**
   - Google Places requires billing enabled
   - Free tier: $200 credit per month
   - After credit: Pay per request

3. **Wait for quota reset:**
   - Daily quotas reset at midnight Pacific Time
   - Try again the next day

---

#### **Possible Cause 5: Network/CORS Issues**

**Symptoms:**
- Browser console shows CORS errors
- Network errors in browser

**Solution:**

1. **Check browser console:**
   - Press F12 → Console tab
   - Look for red errors
   - Note the specific error message

2. **Verify backend CORS settings:**
   - Backend should allow requests from Netlify domain
   - Check Render logs for CORS errors

3. **Clear browser cache:**
   - Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
   - Or clear browser cache completely

---

### 🌐 **Issue: Netlify Not Deploying**

**Symptoms:**
- Pushed to GitHub but Netlify not building
- Site shows old version

**Solution:**

1. **Check Netlify dashboard:**
   - Go to: https://app.netlify.com
   - Check "Deploys" tab
   - Look for latest commit

2. **Trigger manual deploy:**
   - Click "Trigger deploy" → "Deploy site"
   - Wait 2-3 minutes

3. **Check build logs:**
   - Click on the deployment
   - View logs for errors
   - Fix any build errors

4. **Verify GitHub connection:**
   - Site settings → Build & deploy
   - Check GitHub repository is connected
   - Verify branch is set to "main"

---

### 🔐 **Issue: Login/Registration Not Working**

**Symptoms:**
- Can't register new users
- Can't login

**Solution:**

1. **Check backend is running:**
   - Visit: `https://your-backend.onrender.com/docs`
   - Should show API documentation

2. **Verify environment variable:**
   - Netlify: `REACT_APP_API_URL` set correctly
   - Render: `SECRET_KEY` is set

3. **Check database:**
   - Render should have SQLite database
   - Check Render logs for database errors

4. **Clear local storage:**
   - Browser console: `localStorage.clear()`
   - Refresh page and try again

---

### 📊 **How to Check Backend Logs (Render)**

1. Go to: https://dashboard.render.com
2. Click your backend service
3. Click "Logs" tab
4. Look for errors when you try to search

**Common error messages:**
- `Google Places API key not found` → Add API key
- `Quota exceeded` → Enable billing or wait
- `Invalid request` → Check search parameters

---

### 🧪 **Testing Checklist**

Before reporting an issue, test these:

- [ ] Backend is "Live" in Render dashboard
- [ ] Backend docs accessible: `https://your-backend.onrender.com/docs`
- [ ] Google API key set in Render environment variables
- [ ] Frontend has correct `REACT_APP_API_URL` in Netlify
- [ ] Netlify deployed latest code (check deploy time)
- [ ] Try known location: Los Angeles, CA, USA
- [ ] Try simple facility: "Gym" or "Restaurant"
- [ ] Browser console has no red errors
- [ ] Billing enabled in Google Cloud Console

---

### 📞 **Still Not Working?**

If you've tried everything above:

1. **Check Render backend logs** for specific error
2. **Check Netlify deploy logs** for build errors
3. **Check browser console** (F12) for frontend errors
4. **Share the specific error message** for targeted help

---

### ✅ **Quick Fix Commands**

**Trigger Netlify Redeploy:**
```bash
cd "Facilty Search Production"
git commit --allow-empty -m "chore: Trigger redeploy"
git push
```

**Restart Render Backend:**
- Go to Render dashboard
- Click service → Manual Deploy → Deploy latest commit

**Clear Browser Cache:**
- Press Ctrl+Shift+Delete
- Select "Cached images and files"
- Click "Clear data"

---

### 🎯 **Most Common Fix**

**90% of "No facilities found" issues are solved by:**

1. Adding Google API key to Render environment variables
2. Enabling billing in Google Cloud Console
3. Waiting for Render backend to wake up (30 seconds)

Try these first before other troubleshooting steps!

