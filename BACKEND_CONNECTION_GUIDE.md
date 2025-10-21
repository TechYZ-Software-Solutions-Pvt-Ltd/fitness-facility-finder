# 🔗 Connect Frontend to Backend - REQUIRED STEP

## ❌ **Current Issue:**

**"No search history yet"** message appears even after logging in and performing searches.

### **Root Cause:**
The GitHub Pages frontend is **NOT connected** to your Render backend. The frontend doesn't know where to send API requests.

---

## ✅ **Solution: Configure Backend URL**

You need to tell the frontend where your Render backend is deployed.

---

## 🚀 **Step 1: Get Your Render Backend URL**

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Find your "justlist-backend" service
3. Copy the URL (it looks like: `https://justlist-backend-xxxxx.onrender.com`)

---

## 🔧 **Step 2: Update Frontend Build Configuration**

### **Option A: Modify package.json (Recommended)**

1. Open `frontend/package.json`
2. Add your Render URL to the build script:

**Before:**
```json
"scripts": {
  "start": "react-scripts start",
  "build": "react-scripts build",
  ...
}
```

**After:**
```json
"scripts": {
  "start": "react-scripts start",
  "build": "REACT_APP_API_URL=https://your-render-url.onrender.com react-scripts build",
  ...
}
```

**For Windows users, use:**
```json
"scripts": {
  "start": "react-scripts start",
  "build": "set REACT_APP_API_URL=https://your-render-url.onrender.com&& react-scripts build",
  ...
}
```

### **Option B: Set Environment Variable Before Building**

#### **Windows:**
```bash
cd frontend
set REACT_APP_API_URL=https://your-render-url.onrender.com
npm run build
```

#### **Linux/macOS:**
```bash
cd frontend
export REACT_APP_API_URL=https://your-render-url.onrender.com
npm run build
```

---

## 📦 **Step 3: Rebuild and Redeploy**

After setting the backend URL:

### **Windows:**
```bash
cd "Facilty Search Production"
.\deploy-simple.bat
```

### **Linux/macOS:**
```bash
cd "Facilty Search Production"
./deploy-to-github-pages.sh
```

---

## 🎯 **Step 4: Verify Connection**

After 2-5 minutes:

1. **Open your app**: https://techyz-software-solutions-pvt-ltd.github.io/justlist/
2. **Open browser console** (F12 → Console tab)
3. **Login** to your account
4. **Open Settings** (gear icon)
5. **Click "Search History" tab**
6. **Check console logs**:
   - Should see: `[Search History] API URL: https://your-render-url.onrender.com`
   - Should NOT see: `API URL: http://localhost:8000`

---

## 🔍 **How to Debug:**

### **Check Current API URL:**

1. Open your app in browser
2. Press F12 (Developer Tools)
3. Go to Console tab
4. Type:
```javascript
console.log(process.env.REACT_APP_API_URL || 'http://localhost:8000')
```

**Expected:** Your Render URL  
**If you see:** `http://localhost:8000` → Backend not configured

### **Check Network Requests:**

1. Open Developer Tools (F12)
2. Go to Network tab
3. Try to search for a facility
4. Look for requests to `/facilities/search`
5. Check the request URL - should go to your Render backend

---

## 📋 **Common Issues:**

### **Issue 1: Still seeing "No search history"**

**Cause:** Environment variable not set during build

**Solution:**
1. Verify you set `REACT_APP_API_URL` before building
2. Rebuild the app
3. Redeploy to GitHub Pages

### **Issue 2: CORS errors in console**

**Cause:** Backend not allowing requests from GitHub Pages

**Solution:** Backend needs to allow your GitHub Pages domain in CORS settings

### **Issue 3: 404 errors when calling API**

**Cause:** Wrong backend URL or backend not deployed

**Solution:**
1. Verify Render backend is "Live" (green status)
2. Test backend directly: `https://your-render-url.onrender.com/health`
3. Should return: `{"status": "healthy"}`

---

## 🎊 **After Successful Connection:**

Once connected, all features will work:

- ✅ User registration and login
- ✅ Facility search
- ✅ Search history (up to 30 items)
- ✅ Delete search history
- ✅ Settings management
- ✅ Data sources configuration

---

## 💡 **Alternative: Local Development**

If you want to test everything locally without Render:

### **Terminal 1 - Backend:**
```bash
cd "Facilty Search Production"
python init_database.py
python start_backend.py
```

### **Terminal 2 - Frontend:**
```bash
cd frontend
npm start
```

**Access:** http://localhost:3000

This way, the frontend uses the default `http://localhost:8000` backend.

---

## 📊 **Architecture Reminder:**

```
┌─────────────────────────────────────┐
│  GitHub Pages                       │
│  (Frontend - Static Files)          │
│  ❌ NOT connected to backend yet    │
└────────────┬────────────────────────┘
             │
             │ Needs REACT_APP_API_URL
             │
             ▼
┌─────────────────────────────────────┐
│  Render                             │
│  (Backend - API Server)             │
│  ✅ Running at:                     │
│  https://your-render-url.onrender.com │
└─────────────────────────────────────┘
```

---

## ✅ **Quick Fix Checklist:**

1. [ ] Get Render backend URL
2. [ ] Modify `frontend/package.json` build script
3. [ ] Run `deploy-simple.bat` (or .sh)
4. [ ] Wait 2-5 minutes
5. [ ] Test search history in browser
6. [ ] Check browser console for API URL
7. [ ] Verify all features work

---

## 🎉 **Summary:**

**The frontend needs to know where the backend is.**

Without setting `REACT_APP_API_URL`:
- ❌ Frontend tries to call `http://localhost:8000`
- ❌ On GitHub Pages, this fails
- ❌ No search history, no login, no features

With `REACT_APP_API_URL` set:
- ✅ Frontend calls your Render backend
- ✅ All API requests work
- ✅ Search history appears
- ✅ All features functional

---

**Set the backend URL and rebuild to fix the search history issue!** 🚀
