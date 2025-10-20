"""
Main API router that combines all API endpoints.
"""

from fastapi import APIRouter
from .facilities_simple import router as facilities_router
from .auth import router as auth_router
from .delete_search_history import router as delete_history_router

# Create main API router
api_router = APIRouter()

# Include all API routers
api_router.include_router(facilities_router, prefix="/facilities", tags=["facilities"])
api_router.include_router(auth_router, prefix="/auth", tags=["authentication"])
api_router.include_router(delete_history_router, prefix="/search-history", tags=["search-history"])
