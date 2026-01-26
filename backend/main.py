"""FastAPI application entry point.

Provides:
- Health check endpoint at /health
- WebSocket endpoint for proctoring events at /ws/proctor (registered via register_websocket)
- Face detection endpoint at /detect_face
"""

import base64
import io
from fastapi import FastAPI, HTTPException
import cv2
import numpy as np

from .database import Base, engine
from . import models
from .websocket import register_websocket
from ..ai_engine.face_detection import FacePresenceDetector


def create_app() -> FastAPI:
    """Create and configure the FastAPI app."""
    # Ensure DB tables exist
    Base.metadata.create_all(bind=engine)

    app = FastAPI(title="AI Exam Proctoring API", version="0.1.0")

    # Initialize face detector
    face_detector = FacePresenceDetector()

    @app.get("/health")
    def health() -> dict[str, str]:
        """Health check endpoint."""
        return {"status": "ok"}

    @app.post("/detect_face")
    def detect_face(data: dict[str, str]) -> dict[str, str]:
        """Detect face presence in an image.

        Expects JSON with 'image' key containing base64 encoded JPEG image.
        Returns the presence status.
        """
        try:
            image_b64 = data.get("image")
            if not image_b64:
                raise HTTPException(status_code=400, detail="No image provided")

            # Decode base64
            image_data = base64.b64decode(image_b64)
            # Convert to numpy array
            nparr = np.frombuffer(image_data, np.uint8)
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            if frame is None:
                raise HTTPException(status_code=400, detail="Invalid image data")

            # Detect faces
            face_count = face_detector.detect_faces(frame)
            status = face_detector.evaluate_presence(face_count)

            return {"status": status, "face_count": face_count}

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    # Register WebSocket route
    register_websocket(app)
    return app


app = create_app()
