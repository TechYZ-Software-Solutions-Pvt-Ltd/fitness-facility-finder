# 🚀 Quick Cloud Deployment Guide

## 🎯 Choose Your Deployment Platform

### Option 1: Docker (Local/Any Cloud) - RECOMMENDED
```bash
# 1. Create .env file
copy env.example .env
# Edit .env with your Google Places API key

# 2. Deploy with Docker
deploy.bat
```

### Option 2: Heroku (Easiest)
1. Install Heroku CLI
2. Create Heroku app: `heroku create your-app-name`
3. Set API key: `heroku config:set GOOGLE_PLACES_API_KEY=your_key`
4. Deploy: `git push heroku main`

### Option 3: Railway (Simple)
1. Connect GitHub repo to Railway
2. Set environment variable: `GOOGLE_PLACES_API_KEY`
3. Deploy automatically

### Option 4: Google Cloud Run
```bash
# Build and deploy
gcloud builds submit --tag gcr.io/PROJECT-ID/fitness-finder
gcloud run deploy --image gcr.io/PROJECT-ID/fitness-finder --platform managed --allow-unauthenticated
```

### Option 5: AWS Elastic Beanstalk
```bash
# Install EB CLI
pip install awsebcli

# Deploy
eb init
eb create fitness-finder-env
eb deploy
```

## 🔑 Required: Google Places API Key
1. Go to Google Cloud Console
2. Enable Places API
3. Create API key
4. Set billing account
5. Add to environment variables

## 📱 Your App Will Be Available At:
- **Local Docker**: http://localhost:8501
- **Heroku**: https://your-app-name.herokuapp.com
- **Railway**: https://your-app-name.railway.app
- **Google Cloud**: https://your-app-name-xxx.run.app
- **AWS**: http://your-app-name.region.elasticbeanstalk.com

## 🛡️ Security Features Included:
- ✅ API key protection
- ✅ Rate limiting (10 requests/session)
- ✅ Input sanitization
- ✅ Secure logging
- ✅ Session management

## 📊 Monitoring:
- Health check: `/_stcore/health`
- Logs: `docker-compose logs -f`
- Metrics: Built-in Streamlit metrics

Ready to deploy! 🚀
