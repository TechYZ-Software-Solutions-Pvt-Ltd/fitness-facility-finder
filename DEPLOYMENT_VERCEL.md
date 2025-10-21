# Vercel Deployment Guide

## 🚀 Deploying React App to Vercel

### Prerequisites
- GitHub repository with your React app
- Vercel account (free)

### Step 1: Prepare Repository
1. Ensure your React app is in the `frontend/` directory
2. The app is already built and ready for deployment

### Step 2: Deploy to Vercel

#### Option A: Via Vercel Dashboard
1. Go to [vercel.com](https://vercel.com)
2. Sign up/Login with GitHub
3. Click "New Project"
4. Import your repository: `TechYZ-Software-Solutions-Pvt-Ltd/fitness-facility-finder`
5. Configure build settings:
   - **Framework Preset**: Create React App
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `build`
6. Add Environment Variables:
   - `REACT_APP_API_URL`: Your backend URL (e.g., `https://your-backend.railway.app`)
7. Click "Deploy"

#### Option B: Via Vercel CLI
```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy from project root
vercel

# Follow the prompts:
# - Set up and deploy? Y
# - Which scope? (your account)
# - Link to existing project? N
# - Project name: facility-finder
# - Directory: frontend
# - Override settings? N
```

### Step 3: Configure Environment Variables
In Vercel dashboard:
1. Go to your project settings
2. Navigate to "Environment Variables"
3. Add:
   - `REACT_APP_API_URL`: `https://your-backend-name.onrender.com`

### Step 4: Deploy Backend (Render - 100% Free)
1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Create new Web Service from GitHub repo
4. Select your repository
5. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python start_backend.py`
   - Instance Type: Free
6. Get your backend URL from Render dashboard

### Step 5: Update Frontend API URL
1. In Vercel dashboard, update `REACT_APP_API_URL` to your Render backend URL
2. Redeploy the frontend

### 🎉 Success!
Your React app will be available at:
- `https://your-app-name.vercel.app`

### Custom Domain (Optional)
1. In Vercel dashboard, go to "Domains"
2. Add your custom domain
3. Update DNS settings as instructed

## 🔧 Troubleshooting

### Build Issues
- Ensure all dependencies are in `package.json`
- Check that `npm run build` works locally
- Verify `frontend/` directory structure

### API Connection Issues
- Verify backend URL is correct
- Check CORS settings in backend
- Ensure backend is deployed and running

### Environment Variables
- Variables must start with `REACT_APP_`
- Redeploy after changing environment variables
- Check Vercel function logs for errors
