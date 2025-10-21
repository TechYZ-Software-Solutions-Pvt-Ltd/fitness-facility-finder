"""
API endpoint to delete search history items.
"""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
import logging
from src.app.database.connection import get_db
from sqlalchemy.orm import Session
from src.app.database.models import SearchHistory, User
from src.app.auth.dependencies import get_current_user

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/search-history", tags=["search-history"])


class DeleteSearchHistoryRequest(BaseModel):
    """Request model for deleting search history."""
    search_id: int


class DeleteSearchHistoryResponse(BaseModel):
    """Response model for deleting search history."""
    success: bool
    message: str


@router.delete("/delete-search-history", response_model=DeleteSearchHistoryResponse)
async def delete_search_history(
    request: DeleteSearchHistoryRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Delete a specific search history item for the current user.
    
    Args:
        request: DeleteSearchHistoryRequest containing search_id
        db: Database session
        current_user: Current authenticated user
        
    Returns:
        DeleteSearchHistoryResponse with success status and message
    """
    try:
        # Find the search history item
        search_history = db.query(SearchHistory).filter(
            SearchHistory.id == request.search_id,
            SearchHistory.user_id == current_user.id
        ).first()
        
        if not search_history:
            raise HTTPException(
                status_code=404,
                detail="Search history item not found or you don't have permission to delete it"
            )
        
        # Delete the search history item
        db.delete(search_history)
        db.commit()
        
        logger.info(f"Deleted search history item {request.search_id} for user {current_user.id}")
        
        return DeleteSearchHistoryResponse(
            success=True,
            message="Search history item deleted successfully"
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting search history: {e}")
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Internal server error while deleting search history"
        )


@router.delete("/{search_id}", response_model=DeleteSearchHistoryResponse)
async def delete_search_history_by_id(
    search_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Delete a specific search history item by ID for the current user.
    
    Args:
        search_id: ID of the search history item to delete
        db: Database session
        current_user: Current authenticated user
        
    Returns:
        DeleteSearchHistoryResponse with success status and message
    """
    try:
        # Find the search history item
        search_history = db.query(SearchHistory).filter(
            SearchHistory.id == search_id,
            SearchHistory.user_id == current_user.id
        ).first()
        
        if not search_history:
            raise HTTPException(
                status_code=404,
                detail="Search history item not found or you don't have permission to delete it"
            )
        
        # Delete the search history item
        db.delete(search_history)
        db.commit()
        
        logger.info(f"Deleted search history item {search_id} for user {current_user.id}")
        
        return DeleteSearchHistoryResponse(
            success=True,
            message="Search history item deleted successfully"
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting search history: {e}")
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Internal server error while deleting search history"
        )


@router.delete("/delete-all-search-history", response_model=DeleteSearchHistoryResponse)
async def delete_all_search_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Delete all search history items for the current user.
    
    Args:
        db: Database session
        current_user: Current authenticated user
        
    Returns:
        DeleteSearchHistoryResponse with success status and message
    """
    try:
        # Find all search history items for the user
        search_histories = db.query(SearchHistory).filter(
            SearchHistory.user_id == current_user.id
        ).all()
        
        if not search_histories:
            return DeleteSearchHistoryResponse(
                success=True,
                message="No search history items found to delete"
            )
        
        # Delete all search history items
        for search_history in search_histories:
            db.delete(search_history)
        
        db.commit()
        
        logger.info(f"Deleted all search history items for user {current_user.id}")
        
        return DeleteSearchHistoryResponse(
            success=True,
            message=f"Deleted {len(search_histories)} search history items successfully"
        )
        
    except Exception as e:
        logger.error(f"Error deleting all search history: {e}")
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Internal server error while deleting all search history"
        )
