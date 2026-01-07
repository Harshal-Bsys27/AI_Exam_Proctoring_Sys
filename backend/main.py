"""FastAPI application entry point.

Provides:
- Health check endpoint at /health
- WebSocket endpoint for proctoring events at /ws/proctor (registered via register_websocket)
"""

from fastapi import FastAPI

from .database import Base, engine
from . import models
from .websocket import register_websocket


def create_app() -> FastAPI:
    """Create and configure the FastAPI app."""
    # Ensure DB tables exist
    Base.metadata.create_all(bind=engine)

    app = FastAPI(title="AI Exam Proctoring API", version="0.1.0")

    @app.get("/health")
    def health() -> dict[str, str]:
        """Health check endpoint."""
        return {"status": "ok"}

    # Register WebSocket route
    register_websocket(app)
    return app


app = create_app()
