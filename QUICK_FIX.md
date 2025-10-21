# ⚡ Quick Fix: "No facilities found" Error

## 🎯 **Most Common Cause: Google API Key Not Set**

Follow these steps **in order**:

---

## **Step 1: Verify Backend is Running** ✅

1. **Check Render Dashboard:**
   - Go to: https://dashboard.render.com
   - Find your backend service
   - Status should show "Live" (green dot)
   - If "Suspended", wait 30 seconds (free tier spins down)

2. **Test Backend Directly:**
   - Open browser
   - Visit: `https://your-backend-name.onrender.com/docs`
   - You should see API documentation
   - If error page, backend has issues

---

## **Step 2: Add Google Places API Key** ⚠️ **MOST IMPORTANT**

### **A. Get Your Google API Key:**

1. **Go to Google Cloud Console:**
   - https://console.cloud.google.com/apis/credentials

2. **Create/Get API Key:**
   - Click "Create Credentials" → "API Key"
   - Copy the key

3. **Enable Places API:**
   - Go to: https://console.cloud.google.com/apis/library
   - Search "Places API"
   - Click "Enable"

4. **Enable Billing:** ⚠️ **REQUIRED**
   - Go to: https://console.cloud.google.com/billing
   - Link a billing account
   - **Note**: Google gives $200/month free credit
   - Places API won't work without billing enabled

### **B. Add Key to Render:**

1. **Go to Render Dashboard:**
   - https://dashboard.render.com

2. **Click your backend service**

3. **Go to "Environment" tab**

4. **Click "Add Environment Variable"**

5. **Enter:**
   ```
   Key:   GOOGLE_PLACES_API_KEY
   Value: [Paste your Google API key here]
   ```

6. **Click "Save"**

7. **Wait 30 seconds** for service to restart

---

## **Step 3: Verify Frontend Connection**

1. **Go to Netlify Dashboard:**
   - https://app.netlify.com

2. **Click your site**

3. **Go to: Site settings → Environment variables**

4. **Check if `REACT_APP_API_URL` exists**

5. **If missing, add it:**
   ```
   Key:   REACT_APP_API_URL
   Value: https://your-backend-name.onrender.com
   ```
   (Get the exact URL from your Render dashboard)

6. **If you added/changed it:**
   - Go to "Deploys" tab
   - Click "Trigger deploy" → "Deploy site"
   - Wait 2-3 minutes

---

## **Step 4: Test the Search**

After completing steps above:

1. **Wait 1 minute** for backend to be ready

2. **Open your Netlify site**

3. **Try this test search:**
   - Country: **United States**
   - State: **California**
   - City: **Los Angeles**
   - Facility Category: **Fitness**
   - Facility Type: **Gym**
   - Max Results: **20**

4. **Click "Search Facilities"**

5. **Expected Result:**
   - Should show gyms in Los Angeles
   - If still "No facilities found", continue below

---

## **Step 5: Check for Errors**

### **A. Check Browser Console:**

1. **Press F12** (or right-click → Inspect)
2. **Click "Console" tab**
3. **Try searching again**
4. **Look for RED errors**

**Common errors and fixes:**

| Error | Meaning | Fix |
|-------|---------|-----|
| `Network Error` | Can't reach backend | Check backend is running |
| `404 Not Found` | Wrong backend URL | Fix `REACT_APP_API_URL` in Netlify |
| `CORS Error` | Backend not allowing requests | Backend should be configured (it is) |
| `401 Unauthorized` | Not logged in | Login first |
| `500 Internal Server Error` | Backend crashed | Check Render logs |

### **B. Check Render Backend Logs:**

1. **Go to Render Dashboard**
2. **Click your backend service**
3. **Click "Logs" tab**
4. **Try searching again**
5. **Look for error messages**

**Common log errors:**

| Error in Logs | Fix |
|---------------|-----|
| `GOOGLE_PLACES_API_KEY not found` | Add API key (Step 2) |
| `Quota exceeded` | Enable billing in Google Cloud |
| `API key invalid` | Check key is correct |
| `Database error` | Restart service in Render |

---

## **Step 6: Alternative - Test Locally**

If the deployed version doesn't work, test locally:

1. **Start Backend:**
   ```bash
   cd "Facilty Search Production"
   python start_backend.py
   ```

2. **Start Frontend (new terminal):**
   ```bash
   cd "Facilty Search Production/frontend"
   npm start
   ```

3. **Create `.env` file in root:**
   ```
   GOOGLE_PLACES_API_KEY=your_api_key_here
   ```

4. **Try searching at** `http://localhost:3000`

---

## **🎯 Quick Checklist**

Before searching, verify:

- [ ] ✅ Backend shows "Live" in Render
- [ ] ✅ Google API key added to Render environment variables
- [ ] ✅ Billing enabled in Google Cloud Console
- [ ] ✅ Places API enabled in Google Cloud
- [ ] ✅ `REACT_APP_API_URL` set in Netlify
- [ ] ✅ Netlify deployed latest code
- [ ] ✅ Logged in to the app
- [ ] ✅ Waited 30 seconds after backend restart
- [ ] ✅ Using valid location (Los Angeles, CA works)
- [ ] ✅ Browser console has no errors

---

## **🚨 Still Not Working?**

### **90% of issues are solved by:**

1. **Adding Google API key to Render**
2. **Enabling billing in Google Cloud**
3. **Waiting for backend to wake up (30 seconds)**

### **If you've done all above:**

1. **Share the error from:**
   - Browser console (F12 → Console)
   - OR Render backend logs
   - OR exact error message shown

2. **Provide these details:**
   - Are you logged in?
   - What location are you searching?
   - What facility type?
   - Is backend "Live" in Render?
   - Is API key set in Render?

---

## **✅ Expected Behavior**

**When everything works:**

1. Select location (e.g., Los Angeles, CA)
2. Select facility (e.g., Gym)
3. Click "Search Facilities"
4. **First search might take 30 seconds** (backend waking up)
5. Results appear with gym names, addresses, ratings
6. Can click to see details
7. Search saved to history

**If you get results → Success!** 🎉

---

## **📞 Need More Help?**

See full troubleshooting guide: `TROUBLESHOOTING.md`

Or check these guides:
- `LOCAL_SETUP.md` - Run locally
- `CONNECT_FRONTEND_BACKEND.md` - Verify connection
- `DEPLOYMENT_GUIDE.md` - Redeploy everything

