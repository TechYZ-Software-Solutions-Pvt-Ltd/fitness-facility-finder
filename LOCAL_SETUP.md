# 🖥️ Local Development Setup Guide

## 📋 Prerequisites

- Python 3.8 or higher
- Node.js 18 or higher
- npm (comes with Node.js)

## 🚀 Quick Start (Both Frontend & Backend)

### Step 1: Install Backend Dependencies

```bash
cd "C:\Users\roh90\Downloads\AI Projects\FacilitySearch.workspace\Facilty Search Production"
pip install -r requirements.txt
```

### Step 1.5: Initialize Database Tables ⚠️ **IMPORTANT**

Before running the app for the first time, create the database tables:

```bash
python init_database.py
```

**Expected output:**
```
✅ Database tables created successfully!
   - users
   - search_history
   - facilities

🎉 Database is ready! You can now start the application.
```

**Note:** Only run this once. The backend will handle the database after initial setup.

### Step 2: Set Up Environment Variables

Create a file named `.env` in the root directory:

```env
# Google Places API (Optional for testing registration/login)
GOOGLE_PLACES_API_KEY=your_api_key_here

# Security (Generate a random string)
SECRET_KEY=your-secret-key-here-use-random-string

# Database (SQLite - no setup needed)
DATABASE_URL=sqlite:///./data/facility_finder.db
```

### Step 3: Start Backend (Terminal 1)

```bash
cd "C:\Users\roh90\Downloads\AI Projects\FacilitySearch.workspace\Facilty Search Production"
python start_backend.py
```

**Expected output**:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

### Step 4: Start Frontend (Terminal 2 - New Terminal)

```bash
cd "C:\Users\roh90\Downloads\AI Projects\FacilitySearch.workspace\Facilty Search Production\frontend"
npm install
npm start
```

**Expected output**:
```
Compiled successfully!
You can now view justlist-frontend in the browser.
Local:            http://localhost:3000
```

### Step 5: Test Registration

1. Open browser: `http://localhost:3000`
2. Click "Register"
3. Fill in the form:
   - Full Name: Your Name
   - Email: test@example.com
   - Username: testuser
   - Password: TestPass123!
   - Confirm Password: TestPass123!
4. Click "Register"

**Expected**: Redirect to login page
**If fails**: Check console for errors

## 🔍 Troubleshooting

### Problem: "Network Error" or "Registration failed"

**Cause**: Backend is not running

**Solution**:
1. Open Terminal 1
2. Run: `python start_backend.py`
3. Verify you see: `Uvicorn running on http://127.0.0.1:8000`
4. Try registering again

### Problem: "CORS Error"

**Cause**: Frontend can't connect to backend

**Solution**:
1. Make sure backend is running on port 8000
2. Make sure frontend is running on port 3000
3. Restart both servers

### Problem: Database Error

**Cause**: Database file doesn't exist or can't be created

**Solution**:
```bash
# Create data directory
mkdir data

# Backend will create the database automatically on first run
python start_backend.py
```

### Problem: "Module not found" errors

**Cause**: Missing dependencies

**Solution**:
```bash
# Backend
pip install -r requirements.txt

# Frontend
cd frontend
npm install
```

## 📝 Notes

- **Registration** works offline (no Google API needed)
- **Login** works offline
- **Search** requires Google Places API key
- Database is stored in `data/facility_finder.db`
- User passwords are encrypted with bcrypt

## 🎯 Testing Workflow

1. **Start Backend** → Wait for "Uvicorn running"
2. **Start Frontend** → Wait for "Compiled successfully"
3. **Register User** → Should redirect to login
4. **Login** → Should see main search page
5. **Search** → Requires Google API key

## ✅ Success Indicators

**Backend Running**:
- Terminal shows: `INFO:     Uvicorn running on http://127.0.0.1:8000`
- Visit `http://localhost:8000/docs` → Shows API documentation

**Frontend Running**:
- Terminal shows: `Compiled successfully!`
- Browser opens at `http://localhost:3000`
- You see the JustList logo and search form

**Registration Works**:
- Form submits without errors
- Redirects to `/login` page
- Success message appears

## 🚀 Production (Netlify + Render)

For production deployment:
- Frontend: See `DEPLOYMENT_GUIDE.md`
- Backend: See `DEPLOYMENT_GUIDE.md`
- No local setup needed!

