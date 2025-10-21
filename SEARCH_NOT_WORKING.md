# 🔍 Search Not Working - Quick Diagnosis

## If API Key Works But Search Returns "No facilities found"

### **Most Common Reasons:**

---

## **1. Netlify Hasn't Deployed Latest Code Yet** ⚠️

We just pushed updates including localStorage for API key. Netlify needs to rebuild:

**Check Netlify Status:**
1. Go to: https://app.netlify.com
2. Click your site → "Deploys" tab
3. Check if latest deploy finished
4. **If still building**: Wait 2-3 minutes
5. **If failed**: Check build logs for errors

**Force Refresh Browser:**
- Windows: `Ctrl + Shift + R`
- Mac: `Cmd + Shift + R`

---

## **2. You're Not Logged In**

Some features require login:

**Solution:**
1. Click "Login" or "Register"
2. Create account or sign in
3. Try searching again

---

## **3. Invalid Location**

Google API might not recognize the location:

**Try this known-good search:**
- Country: `United States`
- State: `California`
- City: `Los Angeles`
- Facility Category: `Fitness`
- Facility Type: `Gym`

**If Los Angeles works:**
- Your original location might not be in Google's database
- Try a larger/well-known city

---

## **4. Facility Type Not Recognized by Google**

Some facility types in our 29 categories might not match Google's types.

**Google-compatible facility types (100% work):**
- Gym, Restaurant, Cafe, Hospital, School, Bank
- Hotel, Shopping Mall, Library, Park, Pharmacy
- Airport, Train Station, Museum, Theater, Zoo

**Types that might not work:**
- Very specific types (e.g., "Pilates Studio" might need to be "Gym")
- Software companies (Google mostly has physical locations)
- Very new business categories

**Solution:**
- Try a more general facility type
- Example: Instead of "Pilates Studio" try "Gym"
- Instead of "SaaS Company" try "Corporate Office"

---

## **5. Backend Not Connected**

**Check:**
1. **Browser Console** (F12 → Console tab)
2. Try searching
3. Look for errors like:
   - `Network Error` → Backend not reachable
   - `404 Not Found` → Wrong backend URL
   - `401 Unauthorized` → Not logged in

**Fix:**
- Check if `REACT_APP_API_URL` is set in Netlify
- Should be your Render backend URL
- If missing, add it and redeploy

---

## **6. Search Parameters Issue**

**Check your search:**
- City: Must not be empty
- Country: Must be selected
- Facility Type: Must be selected
- Max Results: Should be between 1-50

**If any field is empty:**
- Fill all required fields
- Try searching again

---

## **7. Google API Returning Zero Results**

Even with a valid API key and correct parameters, Google might return no results if:
- No facilities of that type exist in that location
- Location is too small/remote
- Facility type too specific

**Test:**
```
Try: "Restaurant in Paris, France"
Try: "Hospital in London, United Kingdom"
Try: "Gym in New York, United States"
```

These should ALWAYS return results if your API key works.

---

## 🧪 **Diagnostic Steps**

### **Step 1: Verify Deployment**
```
1. Check Netlify has deployed latest code
2. Hard refresh browser (Ctrl+Shift+R)
3. Check if API key field persists after refresh
```

### **Step 2: Check Backend Connection**
```
1. Press F12 → Network tab
2. Try searching
3. Look for request to your backend
4. Status should be 200 (success)
5. If 401: You need to login
6. If 404: Backend URL wrong
7. If 500: Backend error (check Render logs)
```

### **Step 3: Check API Key**
```
1. API key saved in browser (refresh page, should still be there)
2. API key is correct (no typos, no extra spaces)
3. API key has no restrictions (Google Cloud Console)
4. Billing enabled (Google Cloud Console)
```

### **Step 4: Test Known-Good Search**
```
Country: United States
State: California  
City: Los Angeles
Facility: Gym
```

If this works → Your original search had issues
If this fails → Problem with backend/API key

---

## 🎯 **Quick Checklist**

Before reporting "not working":

- [ ] Waited for Netlify to finish deploying
- [ ] Hard refreshed browser (Ctrl+Shift+R)
- [ ] Logged in to the app
- [ ] Tried "Gym in Los Angeles, USA"
- [ ] Checked browser console for errors (F12)
- [ ] API key is entered correctly
- [ ] Backend is "Live" in Render dashboard
- [ ] Backend URL set in Netlify

---

## 📊 **What to Share for Help**

If still not working, share:

1. **What you searched for:**
   - Country: ?
   - City: ?
   - Facility Type: ?

2. **Are you logged in?** (Yes/No)

3. **Browser console error** (F12 → Console → copy red errors)

4. **Netlify deploy status** (Building / Published / Failed)

5. **Did "Gym in Los Angeles, USA" work?** (Yes/No)

---

## 💡 **Most Likely Issue**

Based on timing, most likely:

**Netlify hasn't finished deploying the latest code yet!**

**Solution:**
1. Wait 2-3 minutes for Netlify to deploy
2. Check: https://app.netlify.com → Deploys tab
3. Once it says "Published" (green), try again
4. Hard refresh browser: Ctrl+Shift+R

---

## ✅ **Expected Behavior**

When everything works:

1. Enter Google API key (shows as dots ••••)
2. Select location (e.g., Los Angeles, CA, USA)
3. Select facility (e.g., Gym)
4. Click "Search Facilities"
5. **Loading** appears (first search might take 30 seconds if backend waking up)
6. **Results appear** with facility names, ratings, addresses
7. Can click facilities for details
8. Search saved to history

If you see this → Success! 🎉

If you see "No facilities found" → Follow steps above

