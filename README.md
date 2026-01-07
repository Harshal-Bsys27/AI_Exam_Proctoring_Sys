# AI-Based Online Exam Proctoring System

AI_Exam_Proctoring_Sys is a resume-quality, minimal yet production-like scaffold for an AI-powered online exam proctoring system. It includes a FastAPI backend with WebSocket support, a React + Vite frontend that accesses a webcam and monitors browser state, a stubbed AI engine layer (OpenCV/MediaPipe/YOLOv8 placeholders), and SQLite storage via SQLAlchemy.

This repository focuses on clean structure, typed Python stubs, and clear TODOs rather than full ML implementations.

## Features
- FastAPI backend with health check and WebSocket endpoint for real-time proctoring events
- SQLite database with SQLAlchemy models for storing events
- React + Vite frontend capturing webcam and monitoring browser/tab/fullscreen events
- AI engine stubs explaining intended CV/ML behavior (face detection, gaze estimation, object detection, risk scoring)
- Minimal, readable, and professional code with docstrings and type hints

## Quickstart

Prerequisites:
- Python 3.10+
- Node.js 18+

Install Python dependencies and run backend:

```bash
cd AI_Exam_Proctoring_Sys
python -m venv .venv
. .venv/Scripts/activate
pip install -r requirements.txt
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

Install frontend deps and run dev server (in another terminal):

```bash
cd AI_Exam_Proctoring_Sys/frontend
npm install
npm run dev
```

The frontend opens on Vite's dev URL (typically http://localhost:5173). The backend runs at http://localhost:8000 with a WebSocket at ws://localhost:8000/ws/proctor.

## Architecture

See [docs/architecture.md](docs/architecture.md) for a high-level view and [docs/model_choices.md](docs/model_choices.md) for AI/ML component notes.

Top-level structure:

```
AI_Exam_Proctoring_Sys/
├── ai_engine/
├── backend/
├── frontend/
├── docs/
├── requirements.txt
├── .gitignore
└── README.md
```

## Ethical & Privacy Disclaimer
- This project is for educational purposes. Real-world proctoring impacts privacy and must strictly comply with applicable laws and institutional policies.
- Disclose data collection practices to users and obtain explicit consent.
- Securely handle all media streams and derived data; minimize retention and access.
- Avoid biased or opaque decision-making. Keep a human in the loop for critical determinations.

## Next Steps
- Implement actual AI logic using OpenCV/MediaPipe/YOLOv8 inside the `ai_engine` module.
- Expand schema/models as needed (e.g., exams, participants, sessions).
- Add authentication, authorization, and audit logging when moving beyond prototypes.
- Add tests (unit/integration) and CI.
open cv based
A system for exam tracking 
and for user behaviour analysis 
 vs code connection