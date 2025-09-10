from fastapi import APIRouter

# Custom imports
from ..config import get_logger

logger = get_logger(__name__)
router = APIRouter()

@router.get("/")
async def user_root():
    """Root of user endpoint path."""
    return {"user": "Sample User", 
            "message": "User endpoint is up and running!"}

@router.post("/preferences")
async def user_preferences(preferences: dict): # TODO: Define a Pydantic model for preferences
    """Upload user preferences."""
    logger.debug(f"Received user preferences: {preferences}")
    return {"status": "success", "preferences": preferences}