"""API routers to be included in the main FastAPI app."""

from .user_routes import router as user_router

__all__ = ["user_router"]