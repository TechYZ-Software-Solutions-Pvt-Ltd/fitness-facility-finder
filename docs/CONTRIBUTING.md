# 🤝 Contributing to Fitness Facility Finder

Thank you for your interest in contributing to the Fitness Facility Finder! This document provides guidelines for contributing to this open source project.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Issue Guidelines](#issue-guidelines)
- [Coding Standards](#coding-standards)

## 📜 Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/fitness-facility-finder.git
   cd fitness-facility-finder
   ```
3. **Create a new branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 🛠️ Development Setup

### Prerequisites

- Python 3.8 or higher
- Google Places API key
- Git

### Local Development

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables**:
   ```bash
   cp env.example .env
   # Edit .env with your Google Places API key
   ```

3. **Run the application**:
   ```bash
   streamlit run app.py
   ```

4. **Access the app**: http://localhost:8501

### Docker Development

```bash
# Build and run with Docker
docker build -t fitness-finder .
docker run -p 8501:8501 -e GOOGLE_PLACES_API_KEY=your_key fitness-finder
```

## 🔄 How to Contribute

### Types of Contributions

- 🐛 **Bug fixes**
- ✨ **New features**
- 📚 **Documentation improvements**
- 🎨 **UI/UX enhancements**
- 🔧 **Performance optimizations**
- 🧪 **Tests**

### Contribution Process

1. **Check existing issues** and pull requests
2. **Create an issue** if you're planning a significant change
3. **Make your changes** following our coding standards
4. **Test your changes** thoroughly
5. **Submit a pull request**

## 📝 Pull Request Process

### Before Submitting

- [ ] Code follows the project's coding standards
- [ ] Self-review of your code has been performed
- [ ] Code has been commented, particularly in hard-to-understand areas
- [ ] Corresponding changes to documentation have been made
- [ ] Changes generate no new warnings
- [ ] New and existing unit tests pass locally

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tested locally
- [ ] All tests pass
- [ ] Manual testing completed

## Screenshots (if applicable)
Add screenshots to help explain your changes

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have performed a self-review
- [ ] I have commented my code
- [ ] I have made corresponding changes to documentation
```

## 🐛 Issue Guidelines

### Before Creating an Issue

1. **Search existing issues** to avoid duplicates
2. **Check if it's a known issue**
3. **Gather information** about your environment

### Issue Template

```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment:**
- OS: [e.g., Windows 10, macOS, Ubuntu]
- Python version: [e.g., 3.9.7]
- Streamlit version: [e.g., 1.28.0]

**Additional context**
Add any other context about the problem.
```

## 📏 Coding Standards

### Python Code Style

- Follow **PEP 8** style guidelines
- Use **type hints** where appropriate
- Write **docstrings** for functions and classes
- Keep functions **small and focused**
- Use **meaningful variable names**

### Code Organization

- **One feature per commit**
- **Clear commit messages**
- **Separate concerns** (UI, business logic, data)
- **Error handling** for all external API calls

### Documentation

- **Update README** for new features
- **Add docstrings** to new functions
- **Update deployment guides** if needed
- **Include examples** in documentation

## 🧪 Testing

### Manual Testing

- Test all user flows
- Verify error handling
- Check responsive design
- Test with different API keys

### Automated Testing (Future)

We plan to add automated testing. For now, please test manually:

```bash
# Test the application
streamlit run app.py
# Navigate through all features
# Test error scenarios
```

## 🚀 Deployment

### Testing Deployment

Before submitting changes that affect deployment:

1. **Test Docker build**:
   ```bash
   docker build -t fitness-finder .
   ```

2. **Test docker-compose**:
   ```bash
   docker-compose up
   ```

3. **Verify environment variables** work correctly

## 📞 Getting Help

- **GitHub Issues**: For bugs and feature requests
- **Discussions**: For questions and general discussion
- **Email**: Contact the maintainers for sensitive issues

## 🏆 Recognition

Contributors will be recognized in:
- **README.md** contributors section
- **Release notes**
- **GitHub contributors page**

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Fitness Facility Finder! 🎉
