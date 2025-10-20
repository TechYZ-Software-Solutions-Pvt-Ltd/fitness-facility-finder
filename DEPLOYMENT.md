# 🚀 Deployment Guide

This guide covers various deployment options for the Facility Finder application.

## 📋 Prerequisites

- Google Places API key
- Node.js 16+ and npm
- Python 3.8+
- Git

## 🌐 Deployment Options

### 1. Streamlit Cloud (Recommended for Quick Demo)

**Advantages:**
- Free hosting
- Easy setup
- Automatic updates from GitHub
- Built-in secrets management

**Steps:**
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Set the following secrets:
   - `API_BASE_URL`: Your backend API URL
   - `GOOGLE_PLACES_API_KEY`: Your Google Places API key
5. Deploy!

**Configuration:**
```yaml
# .streamlit/config.toml
[server]
port = 8501
headless = true

[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
```

### 2. Docker Deployment

**For Production:**

1. **Build the Docker image:**
   ```bash
   docker build -t facility-finder .
   ```

2. **Run with Docker Compose:**
   ```bash
   docker-compose up -d
   ```

3. **Access the application:**
   - Frontend: http://localhost:3000
   - Backend: http://localhost:8000

**Environment Variables:**
```env
GOOGLE_PLACES_API_KEY=your_api_key
FOURSQUARE_API_KEY=your_foursquare_key
YELP_API_KEY=your_yelp_key
DATABASE_URL=sqlite:///data/facility_finder.db
```

### 3. Manual Server Deployment

**Backend Setup:**
```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export GOOGLE_PLACES_API_KEY="your_api_key"
export DATABASE_URL="sqlite:///data/facility_finder.db"

# Start the backend
python start_backend.py
```

**Frontend Setup:**
```bash
cd frontend

# Install dependencies
npm install

# Build for production
npm run build

# Serve the build (using serve)
npm install -g serve
serve -s build -l 3000
```

### 4. Cloud Platform Deployment

#### Heroku

1. **Create Heroku app:**
   ```bash
   heroku create your-app-name
   ```

2. **Set environment variables:**
   ```bash
   heroku config:set GOOGLE_PLACES_API_KEY=your_api_key
   heroku config:set DATABASE_URL=sqlite:///data/facility_finder.db
   ```

3. **Deploy:**
   ```bash
   git push heroku main
   ```

#### Railway

1. Connect your GitHub repository
2. Set environment variables in Railway dashboard
3. Deploy automatically

#### DigitalOcean App Platform

1. Create a new app
2. Connect your GitHub repository
3. Configure build and run commands
4. Set environment variables
5. Deploy

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_PLACES_API_KEY` | Google Places API key | Yes |
| `FOURSQUARE_API_KEY` | Foursquare API key | No |
| `YELP_API_KEY` | Yelp API key | No |
| `DATABASE_URL` | Database connection string | Yes |
| `JWT_SECRET_KEY` | JWT signing key | Yes |
| `CORS_ORIGINS` | Allowed CORS origins | No |

### Database Setup

**SQLite (Default):**
```python
DATABASE_URL = "sqlite:///data/facility_finder.db"
```

**PostgreSQL:**
```python
DATABASE_URL = "postgresql://user:password@localhost/facility_finder"
```

**MySQL:**
```python
DATABASE_URL = "mysql://user:password@localhost/facility_finder"
```

## 🔒 Security Considerations

### Production Security Checklist

- [ ] Use HTTPS in production
- [ ] Set secure JWT secret key
- [ ] Configure CORS properly
- [ ] Use environment variables for secrets
- [ ] Enable database encryption
- [ ] Set up rate limiting
- [ ] Configure firewall rules
- [ ] Regular security updates

### API Key Security

1. **Never commit API keys to version control**
2. **Use environment variables or secrets management**
3. **Rotate keys regularly**
4. **Monitor API usage**
5. **Set up API key restrictions in Google Cloud Console**

## 📊 Monitoring and Logging

### Application Monitoring

**Backend Logging:**
```python
# Logs are automatically saved to logs/app.log
# Configure log level in start_backend.py
```

**Frontend Error Tracking:**
```javascript
// Add error boundary components
// Implement error reporting service
```

### Health Checks

**Backend Health Check:**
```bash
curl http://your-domain.com/health
```

**Expected Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T00:00:00Z"
}
```

## 🚨 Troubleshooting

### Common Issues

1. **CORS Errors:**
   - Check CORS configuration in backend
   - Verify frontend API URL

2. **Database Connection Issues:**
   - Check database URL
   - Verify database permissions
   - Check disk space

3. **API Key Issues:**
   - Verify API key is correct
   - Check API key restrictions
   - Monitor API quota

4. **Build Failures:**
   - Check Node.js version
   - Clear npm cache
   - Verify all dependencies

### Debug Commands

```bash
# Check backend logs
tail -f logs/app.log

# Test API endpoints
curl -X GET http://localhost:8000/health

# Check frontend build
cd frontend && npm run build

# Run tests
python -m pytest tests/
cd frontend && npm test
```

## 📈 Performance Optimization

### Backend Optimization

1. **Database Indexing:**
   ```sql
   CREATE INDEX idx_search_history_user_id ON search_history(user_id);
   CREATE INDEX idx_facilities_search_id ON facilities(search_id);
   ```

2. **Caching:**
   ```python
   # Implement Redis caching for frequent queries
   # Cache search results for 1 hour
   ```

3. **Connection Pooling:**
   ```python
   # Configure SQLAlchemy connection pool
   engine = create_engine(DATABASE_URL, pool_size=20, max_overflow=30)
   ```

### Frontend Optimization

1. **Code Splitting:**
   ```javascript
   // Implement lazy loading for components
   const LazyComponent = React.lazy(() => import('./Component'));
   ```

2. **Bundle Optimization:**
   ```bash
   # Analyze bundle size
   npm run build -- --analyze
   ```

3. **CDN Usage:**
   ```html
   <!-- Use CDN for static assets -->
   <script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
   ```

## 🔄 CI/CD Pipeline

### GitHub Actions

The project includes a CI/CD pipeline that:
- Runs tests on every push
- Builds the application
- Deploys to staging/production
- Runs security scans

### Manual Deployment

1. **Staging Deployment:**
   ```bash
   git push origin develop
   # Triggers staging deployment
   ```

2. **Production Deployment:**
   ```bash
   git push origin main
   # Triggers production deployment
   ```

## 📞 Support

For deployment issues:
1. Check the logs
2. Review this documentation
3. Create an issue on GitHub
4. Contact the development team

---

**Happy Deploying! 🚀**
