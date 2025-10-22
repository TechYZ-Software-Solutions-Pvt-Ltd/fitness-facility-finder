"""
FastAPI main application for Facility Finder.
This is the backend API server.
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
import os
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import json

from .database.connection import create_tables
from .api import auth, facilities_simple, leads
from .api.delete_search_history import router as delete_history_router

# Create FastAPI app
app = FastAPI(
    title="Facility Finder API",
    description="A powerful API for finding facilities using Google Places API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Logging setup (file + console, JSON lines)
logs_dir = Path(__file__).resolve().parents[2] / "logs"
logs_dir.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("facility_finder")
if not logger.handlers:
    logger.setLevel(logging.INFO)
    class Tail50FileHandler(RotatingFileHandler):
        def emit(self, record: logging.LogRecord) -> None:
            super().emit(record)
            try:
                # Truncate file to last 50 lines to limit storage
                path = self.baseFilename
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()
                if len(lines) > 50:
                    with open(path, "w", encoding="utf-8") as f:
                        f.writelines(lines[-50:])
            except Exception:
                # Never let logging break the app
                pass

    file_handler = Tail50FileHandler(logs_dir / "app.log", maxBytes=256_000, backupCount=0, encoding="utf-8")
    console_handler = logging.StreamHandler()

    class JsonFormatter(logging.Formatter):
        def format(self, record: logging.LogRecord) -> str:
            payload = {
                "timestamp": self.formatTime(record, "%Y-%m-%dT%H:%M:%S%z"),
                "level": record.levelname,
                "message": record.getMessage(),
                "logger": record.name,
            }
            if record.exc_info:
                payload["exc_info"] = self.formatException(record.exc_info)
            return json.dumps(payload, ensure_ascii=False)

    json_formatter = JsonFormatter()
    file_handler.setFormatter(json_formatter)
    console_handler.setFormatter(json_formatter)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# Include API routers
app.include_router(auth.router)
app.include_router(facilities_simple.router)
app.include_router(leads.router)
app.include_router(delete_history_router)


@app.on_event("startup")
async def startup_event():
    """Initialize database tables on startup."""
    create_tables()
    logger.info("Database tables created successfully")


@app.get("/")
async def root():
    """Root endpoint."""
    resp = {
        "message": "Facility Finder API",
        "version": "1.0.0",
        "docs": "/docs",
        "status": "running"
    }
    logger.info("root endpoint hit")
    return resp


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    logger.info("health check")
    return {"status": "healthy", "timestamp": "2024-01-01T00:00:00Z"}


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Global HTTP exception handler."""
    try:
        body = await request.json()
    except Exception:
        body = None
    logger.warning(json.dumps({
        "event": "http_exception",
        "path": str(request.url),
        "method": request.method,
        "status_code": exc.status_code,
        "detail": exc.detail,
        "body": body,
    }, ensure_ascii=False))
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail, "status_code": exc.status_code}
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Global exception handler."""
    try:
        body = await request.json()
    except Exception:
        body = None
    logger.error(json.dumps({
        "event": "unhandled_exception",
        "path": str(request.url),
        "method": request.method,
        "body": body,
    }, ensure_ascii=False), exc_info=exc)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error", "status_code": 500}
    )


if __name__ == "__main__":
    # Run the server
    uvicorn.run(
        "main_api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Enable auto-reload for development
        log_level="info"
    )
