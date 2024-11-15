from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.routes.data_routes import router as data_router

# Load environment variables
load_dotenv()

# Create FastAPI application
app = FastAPI(
    title="AI Data Extractor",
    description="An intelligent data extraction tool using AI and web search",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Conditionally import routes to avoid circular imports
try:
    from .routes import data_routes
    app.include_router(data_routes.router, prefix="/api")
except ImportError:
    print("Could not import routes")
