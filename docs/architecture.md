# Architecture Overview

This project is intentionally minimal and production-like:

- Backend: FastAPI app with an HTTP health endpoint and a WebSocket endpoint for real-time proctoring events. Events are stored in SQLite using SQLAlchemy.
- Frontend: React + Vite app that accesses the user's webcam and monitors browser events (tab visibility changes, fullscreen enter/exit, window blur/focus). Events are sent to the backend over WebSockets.
- AI Layer: Python stubs in `ai_engine` with typed placeholders for face detection (OpenCV/MediaPipe), gaze estimation, prohibited object detection (YOLOv8), and a risk scoring utility.

## Data Flow
1. Frontend captures webcam and browser events.
2. Browser events are serialized and sent over WebSocket to the backend.
3. Backend persists events in SQLite for later analysis.
4. AI modules (currently stubs) will process frames or events to compute risk scores.

## Future Extensions
- Authentication/session management for real users and exams.
- Streaming frames to backend for server-side inference or using on-device models.
- Risk aggregation dashboards with alerting.
- Cloud deployment, monitoring, and scaling.
