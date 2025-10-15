# 🚀 Fitness Facility Finder - Cloud Deployment Guide

This guide will help you deploy the Fitness Facility Finder application to various cloud platforms.

## 📋 Prerequisites

- Google Places API Key
- Docker installed on your system
- Cloud platform account (AWS, Google Cloud, Azure, etc.)

## 🐳 Docker Deployment (Recommended)

### 1. Local Docker Deployment

```bash
# Clone or download the project
cd "Facility Search"

# Create environment file
cp env.example .env
# Edit .env file with your Google Places API key

# Make deployment script executable
chmod +x deploy.sh

# Run deployment
./deploy.sh
```

### 2. Manual Docker Commands

```bash
# Build the image
docker build -t fitness-finder .

# Run the container
docker run -d -p 8501:8501 -e GOOGLE_PLACES_API_KEY=your_api_key fitness-finder
```

## ☁️ Cloud Platform Deployment

### AWS Elastic Beanstalk

1. **Install EB CLI**:
   ```bash
   pip install awsebcli
   ```

2. **Initialize EB**:
   ```bash
   eb init
   eb create fitness-finder-env
   ```

3. **Deploy**:
   ```bash
   eb deploy
   ```

### Google Cloud Run

1. **Build and push to Google Container Registry**:
   ```bash
   gcloud builds submit --tag gcr.io/PROJECT-ID/fitness-finder
   ```

2. **Deploy to Cloud Run**:
   ```bash
   gcloud run deploy fitness-finder \
     --image gcr.io/PROJECT-ID/fitness-finder \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --set-env-vars GOOGLE_PLACES_API_KEY=your_api_key
   ```

### Azure Container Instances

1. **Build and push to Azure Container Registry**:
   ```bash
   az acr build --registry myregistry --image fitness-finder .
   ```

2. **Deploy to Container Instances**:
   ```bash
   az container create \
     --resource-group myResourceGroup \
     --name fitness-finder \
     --image myregistry.azurecr.io/fitness-finder \
     --ports 8501 \
     --environment-variables GOOGLE_PLACES_API_KEY=your_api_key
   ```

### Heroku

1. **Install Heroku CLI**

2. **Create Heroku app**:
   ```bash
   heroku create your-app-name
   ```

3. **Set environment variables**:
   ```bash
   heroku config:set GOOGLE_PLACES_API_KEY=your_api_key
   ```

4. **Deploy**:
   ```bash
   git add .
   git commit -m "Deploy fitness finder"
   git push heroku main
   ```

### Railway

1. **Connect your GitHub repository to Railway**

2. **Set environment variables in Railway dashboard**:
   - `GOOGLE_PLACES_API_KEY`: Your Google Places API key

3. **Deploy automatically from GitHub**

### Render

1. **Create a new Web Service on Render**

2. **Connect your GitHub repository**

3. **Configure**:
   - **Build Command**: `docker build -t fitness-finder .`
   - **Start Command**: `docker run -p 8501:8501 -e GOOGLE_PLACES_API_KEY=$GOOGLE_PLACES_API_KEY fitness-finder`
   - **Environment Variables**: Add your Google Places API key

## 🔧 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_PLACES_API_KEY` | Your Google Places API key | Yes |
| `DOMAIN` | Custom domain (optional) | No |
| `SSL_CERT_PATH` | SSL certificate path (optional) | No |
| `SSL_KEY_PATH` | SSL private key path (optional) | No |

## 🛡️ Security Considerations

1. **API Key Protection**: Never commit your API key to version control
2. **Environment Variables**: Use environment variables for sensitive data
3. **HTTPS**: Enable HTTPS in production
4. **Rate Limiting**: The app includes built-in rate limiting
5. **Input Validation**: All inputs are sanitized

## 📊 Monitoring and Logs

### Docker Logs
```bash
# View logs
docker-compose logs -f

# View specific service logs
docker-compose logs fitness-finder
```

### Health Check
The application includes a health check endpoint at `/_stcore/health`

## 🔄 Updates and Maintenance

### Update Application
```bash
# Pull latest changes
git pull

# Rebuild and redeploy
docker-compose down
docker-compose up -d --build
```

### Backup
```bash
# Backup logs
docker-compose exec fitness-finder tar -czf /app/logs/backup-$(date +%Y%m%d).tar.gz /app/logs/
```

## 🆘 Troubleshooting

### Common Issues

1. **Port 8501 already in use**:
   ```bash
   # Find and kill process
   lsof -ti:8501 | xargs kill -9
   ```

2. **API Key not working**:
   - Verify the API key is correct
   - Check if Places API is enabled in Google Cloud Console
   - Ensure billing is set up

3. **Docker build fails**:
   - Check Docker is running
   - Verify all files are present
   - Check internet connection for package downloads

### Support
For issues and support, check the application logs and ensure all prerequisites are met.

## 📈 Scaling

For high-traffic deployments, consider:
- Load balancers
- Multiple container instances
- Database for session storage
- CDN for static assets
- Monitoring and alerting systems
