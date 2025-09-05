import fastapi
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()  

# Environment validation and logging setup on startup
logging.basicConfig(
    level=logging.DEBUG, # Set to DEBUG for detailed output, change to INFO in production
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

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
## HERE: Add your API routers

@app.get("/", tags=["Root"])
async def read_root():
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
