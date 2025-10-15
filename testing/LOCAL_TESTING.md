# 🧪 Local Testing Guide

Test your Fitness Facility Finder locally before deploying to Streamlit Cloud.

## 📋 Prerequisites

- ✅ **Python 3.8+** installed
- ✅ **All dependencies** installed (`pip install -r requirements.txt`)
- ✅ **Google Places API Key** (for full functionality testing)

## 🚀 Quick Start

### Method 1: Using run.py (Recommended)
```bash
python run.py
```

### Method 2: Direct Streamlit
```bash
streamlit run app.py
```

### Method 3: Using Make (if available)
```bash
make run
```

## 🌐 Access Your App

Once running, your app will be available at:
- **Local URL**: http://localhost:8501
- **Network URL**: http://192.168.1.109:8501 (accessible from other devices on your network)

## ✅ Testing Checklist

### 1. **UI/UX Testing**
- [ ] **Logo displays correctly** (GYM360 logo centered)
- [ ] **Header is properly centered** with "Fitness Facility Finder"
- [ ] **Form elements** are properly aligned
- [ ] **Search button** is right-aligned and styled
- [ ] **Footer** shows "Powered by Techyz Software Solutions Private Limited"

### 2. **Functionality Testing**
- [ ] **Country dropdown** works (select different countries)
- [ ] **City dropdown** updates based on country selection
- [ ] **Custom city input** works (type custom city name)
- [ ] **Fitness type selection** works (80+ predefined options)
- [ ] **Custom business type** works (select "Custom..." and enter custom type)
- [ ] **Form validation** works (try searching without API key)
- [ ] **Auto-focus** works (cursor focuses on required fields)
- [ ] **Search button** triggers search (with valid API key)

### 3. **Mobile Responsiveness Testing**
- [ ] **Resize browser window** to mobile size (375px width)
- [ ] **Form elements stack vertically** on mobile
- [ ] **Buttons are touch-friendly** (minimum 44px height)
- [ ] **Data table scrolls horizontally** on mobile
- [ ] **Text is readable** on small screens

### 4. **API Integration Testing**
- [ ] **Enter valid Google Places API key**
- [ ] **Search for facilities** in a known location
- [ ] **Results display correctly** in the table
- [ ] **Download functionality** works (CSV export)
- [ ] **Error handling** works (invalid API key, no results)

### 5. **Security Features Testing**
- [ ] **Logo cannot be right-clicked** (context menu disabled)
- [ ] **Logo cannot be dragged** (drag disabled)
- [ ] **Logo cannot be selected** (selection disabled)
- [ ] **Rate limiting** works (50 requests per 30 minutes)
- [ ] **Input validation** works (empty fields, invalid inputs)

## 🔧 Troubleshooting

### App Won't Start?
1. **Check Python version**: `python --version` (should be 3.8+)
2. **Install dependencies**: `pip install -r requirements.txt`
3. **Check port availability**: Port 8501 should be free
4. **Verify file paths**: Ensure `app.py` exists

### Logo Not Displaying?
1. **Check file path**: `assets/gym360_logo.png` should exist
2. **Verify image format**: Should be PNG format
3. **Check file permissions**: Image should be readable

### API Errors?
1. **Verify API key**: Should be valid Google Places API key
2. **Check API quotas**: Ensure you have remaining quota
3. **Enable Places API**: In Google Cloud Console
4. **Set up billing**: Required for Places API

### Mobile Issues?
1. **Clear browser cache**: Refresh with Ctrl+F5
2. **Test in different browsers**: Chrome, Firefox, Safari
3. **Use browser dev tools**: Toggle device toolbar
4. **Check CSS media queries**: Should respond to screen size

## 📱 Mobile Testing Tools

### Browser Dev Tools
1. **Open Dev Tools**: F12 or right-click → Inspect
2. **Toggle Device Toolbar**: Click device icon
3. **Select device**: iPhone, Android, iPad
4. **Test different orientations**: Portrait/landscape

### Online Testing Tools
- **BrowserStack**: Test on real devices
- **Responsive Design Checker**: Multiple screen sizes
- **Mobile-Friendly Test**: Google's tool

## 🎯 Performance Testing

### Load Testing
- [ ] **Multiple concurrent searches**
- [ ] **Large result sets** (100+ facilities)
- [ ] **Network latency simulation** (slow 3G)
- [ ] **Memory usage** monitoring

### Speed Testing
- [ ] **Page load time** < 3 seconds
- [ ] **Search response time** < 10 seconds
- [ ] **Download speed** for CSV files
- [ ] **Image loading time** for logo

## 🐛 Common Issues & Solutions

### Issue: "Module not found"
**Solution**: Install missing dependencies
```bash
pip install -r requirements.txt
```

### Issue: "Port already in use"
**Solution**: Kill existing process or use different port
```bash
streamlit run app.py --server.port 8502
```

### Issue: "API key invalid"
**Solution**: Check API key and enable Places API in Google Cloud Console

### Issue: "Logo not showing"
**Solution**: Verify file path and permissions
```bash
ls -la assets/gym360_logo.png
```

## 📊 Testing Results Template

```
Date: ___________
Tester: ___________
Browser: ___________
Device: ___________

UI/UX: ✅/❌
Functionality: ✅/❌
Mobile Responsive: ✅/❌
API Integration: ✅/❌
Security Features: ✅/❌
Performance: ✅/❌

Issues Found:
1. ________________
2. ________________
3. ________________

Overall Status: ✅ Ready for Deployment / ❌ Needs Fixes
```

## 🚀 Ready for Deployment?

If all tests pass:
1. **Commit any fixes**: `git add . && git commit -m "Fix: description"`
2. **Push to GitHub**: `git push origin main`
3. **Deploy to Streamlit Cloud**: Follow STREAMLIT_CLOUD_DEPLOY.md guide

## 📞 Support

If you encounter issues:
1. **Check logs**: Look for error messages in terminal
2. **Review documentation**: README.md, PROJECT_STRUCTURE.md
3. **Test step by step**: Follow this guide systematically
4. **Contact support**: info@techyz.net

---

**Happy Testing! 🎉**
