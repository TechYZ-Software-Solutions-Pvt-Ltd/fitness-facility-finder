# 🧪 Local Testing - Now Running

## ✅ Servers Started

### **Backend (FastAPI)**
- Running on: `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`
- Status: Check for "Uvicorn running on http://127.0.0.1:8000"

### **Frontend (React)**
- Running on: `http://localhost:3000`
- Should open automatically in browser
- Status: Check for "Compiled successfully!"

---

## 🧪 **Test Search Now**

### **Step 1: Wait for Servers** ⏳

**Backend Ready When You See:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**Frontend Ready When You See:**
```
Compiled successfully!

You can now view justlist-frontend in the browser.

  Local:            http://localhost:3000
```

### **Step 2: Open Browser**

If it doesn't open automatically:
- Open browser manually
- Go to: `http://localhost:3000`

### **Step 3: Try Searching**

1. **Enter your Google Places API Key** (it will be saved in browser)

2. **Try this test search:**
   - Country: **United States**
   - State: **California**
   - City: **Los Angeles**
   - Facility Category: **Fitness**
   - Facility Type: **Gym**
   - Max Results: **20**

3. **Click "Search Facilities"**

---

## 🔍 **What to Check**

### **If Search Works:**
- ✅ You'll see gyms in Los Angeles
- ✅ API key is valid and working
- ✅ Issue is with deployment, not code

### **If Search Fails:**

**Check Console:**
1. Press **F12** in browser
2. Go to **Console** tab
3. Try searching again
4. Look for **red error messages**
5. **Share what you see**

**Common Errors and Fixes:**

| Error | Cause | Fix |
|-------|-------|-----|
| "Network Error" | Backend not running | Check backend terminal |
| "API key is invalid" | Wrong key or restrictions | Check Google Console |
| "OVER_QUERY_LIMIT" | Billing not enabled | Enable billing |
| "ZERO_RESULTS" | No gyms in Mumbai | Try Los Angeles |

---

## 📊 **Backend Log Checking**

While searching, watch the backend terminal for logs like:

**Success:**
```
INFO: facilities.search:start user=anon city=Los Angeles type=Gym
INFO: facilities.search:done duration_ms=2345 total_found=15
```

**Failure:**
```
ERROR: Google Places API error: REQUEST_DENIED - This IP is not authorized
ERROR: Failed query: 'Gym in Mumbai, India'
```

---

## 🎯 **Test Cases**

Try these in order to narrow down the issue:

### **Test 1: Known Location**
- Los Angeles, CA, USA + Gym
- **Should work** - 100s of gyms

### **Test 2: Your Original Search**
- Whatever you were searching before
- Compare results with Test 1

### **Test 3: Different API Key**
- Try a different Google API key
- See if same issue occurs

---

## 📝 **What to Share**

After testing locally, tell me:

1. **Did Test 1 work?** (Los Angeles + Gym)
   - Yes → Original search had issues
   - No → API key or billing issue

2. **What do you see in browser console?** (F12 → Console)
   - Any red errors?
   - Copy the error text

3. **What do you see in backend logs?**
   - Any "ERROR:" lines?
   - What does it say?

4. **What were you originally searching for?**
   - Country, City, Facility Type

---

## ⏰ **Wait Time**

- **Backend**: 5-10 seconds to start
- **Frontend**: 30-60 seconds to compile
- **Browser**: Should auto-open at http://localhost:3000

**Once both say "ready", try the search!** 🚀

---

## 🛑 **To Stop Servers Later**

When done testing:
- Press **Ctrl+C** in both terminal windows
- Or close the terminals

