import fastapi
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from dotenv import load_dotenv

# Custom imports
from .config import get_logger
from .routes import user_router

# Load environment variables and initialize logger
load_dotenv()
logger = get_logger(__name__)

# Environment validation on startup
@asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    """"Lifespan context manager for startup and shutdown events."""
    logger.info("Starting up the Food API service...")
    try:
        # Perform startup actions
        # e.g., connect to databases, initialize resources, etc.
        # Add environment validation here if needed
        pass
        yield
    except Exception as e:
        logger.error(f"Error during startup: {e}")
        raise
    finally:
        logger.info("Shutting down the Food API service...")
        # Perform shutdown actions
        # e.g., close database connections, cleanup resources, etc.
        pass

app = fastapi.FastAPI(
    title="Food API",
    description="API for food suggestions and recommendations.",
    version="1.0.0",
    lifespan=lifespan
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# App routers
app.include_router(user_router, prefix="/user", tags=["User"])

@app.get("/", tags=["Root"])
async def root():
    """Root endpoint."""
    return {
        "message": "Welcome to the Food API!",
        "version": app.version,
        "docs": "/docs"
    }

@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint."""
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
