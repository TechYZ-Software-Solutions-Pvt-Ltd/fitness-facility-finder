# Fitness Facility Finder - Makefile
# Easy commands for development and deployment

.PHONY: help install run test clean docker-build docker-run deploy

help: ## Show this help message
	@echo "Fitness Facility Finder - Available Commands:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	pip install -r requirements.txt

run: ## Run the application locally
	python run.py

test: ## Test the application
	python -c "import streamlit; print('Streamlit version:', streamlit.__version__)"
	python -c "import pandas; print('Pandas version:', pandas.__version__)"
	python -c "import requests; print('Requests version:', requests.__version__)"

clean: ## Clean up temporary files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.log" -delete

docker-build: ## Build Docker image
	docker build -f deploy/Dockerfile -t fitness-finder .

docker-run: ## Run with Docker
	docker run -p 8501:8501 -e GOOGLE_PLACES_API_KEY=your_key fitness-finder

deploy: ## Deploy with docker-compose
	cd deploy && docker-compose up -d

setup-env: ## Setup environment file
	cp config/env.example .env
	@echo "Please edit .env file with your Google Places API key"

dev: setup-env install run ## Setup development environment and run

# Docker commands
docker-stop: ## Stop Docker containers
	cd deploy && docker-compose down

docker-logs: ## View Docker logs
	cd deploy && docker-compose logs -f

# Development commands
lint: ## Run code linting
	flake8 src/ --count --select=E9,F63,F7,F82 --show-source --statistics

format: ## Format code
	black src/
	isort src/

# Documentation
docs: ## Generate documentation
	@echo "Documentation is available in docs/ directory"

# Release commands
version: ## Show current version
	@python -c "import setup; print(setup.__version__)"

# Help for specific commands
help-docker: ## Show Docker help
	@echo "Docker Commands:"
	@echo "  make docker-build    - Build Docker image"
	@echo "  make docker-run      - Run with Docker"
	@echo "  make deploy          - Deploy with docker-compose"
	@echo "  make docker-stop     - Stop Docker containers"
	@echo "  make docker-logs     - View Docker logs"

help-deploy: ## Show deployment help
	@echo "Deployment Options:"
	@echo "  make deploy          - Docker Compose deployment"
	@echo "  make docker-run      - Simple Docker run"
	@echo "  See docs/DEPLOYMENT.md for cloud deployment options"
