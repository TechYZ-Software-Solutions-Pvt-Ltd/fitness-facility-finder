# 🔍 API Key Debugging Guide

## Why "No facilities found" Even with Valid API Key?

The backend receives your API key and tries to use it, but the Google Places API might be rejecting it. Here's how to find out why:

---

## 📊 **Common Google API Error Responses**

| Status Code | Meaning | Solution |
|-------------|---------|----------|
| `REQUEST_DENIED` | API key invalid or restricted | Check key is correct + restrictions |
| `OVER_QUERY_LIMIT` | Quota exceeded | Enable billing or wait for reset |
| `INVALID_REQUEST` | Missing parameters | Check location is valid |
| `ZERO_RESULTS` | No places found | Try different location |
| `UNKNOWN_ERROR` | Server error | Try again later |

---

## 🔧 **Step-by-Step Debugging**

### **Step 1: Verify Your API Key Works**

Test your API key directly:

1. **Copy your API key**

2. **Open this URL in your browser** (replace `YOUR_API_KEY` and `LOS_ANGELES`):
   ```
   https://maps.googleapis.com/maps/api/place/textsearch/json?query=gym+in+Los+Angeles&key=YOUR_API_KEY
   ```

3. **Check the response:**

   **✅ Success** (status: "OK"):
   ```json
   {
     "status": "OK",
     "results": [...]
   }
   ```

   **❌ Failed** - See error:
   ```json
   {
     "status": "REQUEST_DENIED",
     "error_message": "This API project is not authorized to use this API"
   }
   ```

---

### **Step 2: Check API Key Restrictions**

Your API key might have restrictions that block the backend from using it:

1. **Go to Google Cloud Console:**
   - https://console.cloud.google.com/apis/credentials

2. **Click your API key**

3. **Check "API restrictions":**
   - **Option 1 (Recommended for testing)**: "Don't restrict key"
   - **Option 2**: Select "Restrict key" → Check "Places API" is selected

4. **Check "Application restrictions":**
   - **Option 1 (Recommended for testing)**: "None"
   - **Option 2**: If you have IP restrictions, add your Render backend IP

5. **Save changes**

6. **Wait 5 minutes** for restrictions to update

---

### **Step 3: Enable Required APIs**

Make sure these APIs are enabled:

1. **Go to:** https://console.cloud.google.com/apis/library

2. **Search and ENABLE these:**
   - ✅ **Places API** (New)
   - ✅ **Places API (Legacy)** - Sometimes needed
   - ✅ **Maps JavaScript API** - For geocoding
   - ✅ **Geocoding API** - For location lookup

3. **Click "ENABLE" on each**

---

### **Step 4: Enable Billing** ⚠️ **CRITICAL**

Google Places API **REQUIRES** billing to be enabled, even for free tier:

1. **Go to:** https://console.cloud.google.com/billing

2. **Link a billing account**
   - Credit card required
   - **You get $200/month FREE**
   - You won't be charged unless you exceed free tier

3. **Verify billing is active**

4. **Without billing, ALL requests fail** even with valid API key!

---

### **Step 5: Check Quota**

1. **Go to:** https://console.cloud.google.com/apis/dashboard

2. **Click "Places API"**

3. **Check "Quotas" tab**

4. **Look for:**
   - Daily quota used / total
   - If exceeded, wait until tomorrow or increase quota

---

## 🧪 **Test in Your Browser Console**

While on your deployed site:

1. **Press F12** → Console tab

2. **Paste this code** (replace `YOUR_API_KEY`):
   ```javascript
   fetch('https://maps.googleapis.com/maps/api/place/textsearch/json?query=gym+in+Los+Angeles&key=YOUR_API_KEY')
     .then(r => r.json())
     .then(data => console.log('Google API Response:', data))
     .catch(err => console.error('Error:', err));
   ```

3. **Check the response:**
   - If `status: "OK"` → API key works, issue is elsewhere
   - If `status: "REQUEST_DENIED"` → Fix API key restrictions
   - If `status: "OVER_QUERY_LIMIT"` → Enable billing or wait

---

## 🔍 **Check Backend Logs (Render)**

1. **Go to:** https://dashboard.render.com

2. **Click your backend service**

3. **Click "Logs" tab**

4. **Try searching** on your frontend

5. **Look for these log messages:**
   ```
   Google Places API error: REQUEST_DENIED
   ```
   or
   ```
   Google Places API error: OVER_QUERY_LIMIT
   ```

6. **Match error to solution above**

---

##  **Most Common Issues & Solutions**

### **Issue 1: "REQUEST_DENIED"**

**Cause:** API key has restrictions OR API not enabled

**Fix:**
1. Go to API key settings
2. Set "API restrictions" to "Don't restrict key"
3. Set "Application restrictions" to "None"
4. Save and wait 5 minutes

### **Issue 2: "OVER_QUERY_LIMIT"**

**Cause:** Billing not enabled OR quota exceeded

**Fix:**
1. Enable billing at: https://console.cloud.google.com/billing
2. Link credit card (you get $200 free/month)
3. Wait 5-10 minutes for billing to activate

### **Issue 3: Key works in browser but not in backend**

**Cause:** IP restriction or HTTP referrer restriction

**Fix:**
1. API key settings → Application restrictions
2. Select "None" (for testing)
3. Later, add your Render backend IP if needed

### **Issue 4: "INVALID_REQUEST"**

**Cause:** Missing or malformed parameters

**Fix:**
1. Try a simple location: "Los Angeles, California, USA"
2. Try a simple facility: "Gym"
3. Make sure you're logged in

### **Issue 5: "ZERO_RESULTS"**

**Cause:** No facilities of that type in that location

**Fix:**
1. Try "Los Angeles, CA, USA" + "Gym" (known to have results)
2. Try different facility type
3. Try larger city

---

## ✅ **Verification Checklist**

Before searching, verify ALL of these:

- [ ] Google Cloud project created
- [ ] **Billing enabled** ⚠️ (REQUIRED!)
- [ ] **Places API enabled**
- [ ] API key created
- [ ] API key has **NO restrictions** (for testing)
- [ ] Tested API key in browser (got "OK" status)
- [ ] Entered correct API key in frontend (check for typos)
- [ ] Logged in to the app
- [ ] Backend is "Live" in Render
- [ ] Backend URL set in Netlify (`REACT_APP_API_URL`)
- [ ] Tried known-good location (Los Angeles, CA)
- [ ] Tried known-good facility (Gym)

---

## 🎯 **Quick Test**

To verify everything works:

1. **Use this API key test URL:**
   ```
   https://maps.googleapis.com/maps/api/place/textsearch/json?query=gym+in+Los+Angeles&key=[YOUR_KEY]
   ```

2. **Expected response:**
   ```json
   {
     "status": "OK",
     "results": [
       {
         "name": "Gold's Gym",
         ...
       }
     ]
   }
   ```

3. **If you see "OK" but app still doesn't work:**
   - Check browser console for errors
   - Check Render backend logs
   - Make sure backend URL is correct in Netlify
   - Make sure you're logged in

---

## 📞 **Still Not Working?**

Share these details:

1. **Google API test URL response** (status field)
2. **Render backend logs** (copy the error)
3. **Browser console errors** (F12 → Console → copy errors)
4. **Exact search parameters** you're using
5. **Are you logged in?** (Yes/No)

This will help diagnose the exact issue!

---

## 💡 **Pro Tip**

**For testing, temporarily disable ALL restrictions:**

1. API key → Edit
2. API restrictions: "Don't restrict key"
3. Application restrictions: "None"
4. Save

This will tell you if restrictions are the problem. Once it works, you can add restrictions back one at a time.

