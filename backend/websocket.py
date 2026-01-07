"""WebSocket endpoint for receiving proctoring events in real time.

Clients send JSON (or plain text) describing events like visibility changes
or fullscreen exits. Messages are stored as `ProctorEvent` rows.
"""

from __future__ import annotations

import json
from typing import Any

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy.orm import Session

from .database import get_db
from .models import ProctorEvent


def register_websocket(app: FastAPI) -> None:
    """Attach the WebSocket route to the given FastAPI app."""

    @app.websocket("/ws/proctor")
    async def proctor_ws(websocket: WebSocket, db: Session = Depends(get_db)) -> None:  # type: ignore[call-arg]
        await websocket.accept()
        try:
            while True:
                message = await websocket.receive_text()

                event_type = "generic"
                payload_str = message
                try:
                    data: Any = json.loads(message)
                    if isinstance(data, dict) and "type" in data:
                        event_type = str(data["type"])[:50]
                except Exception:
                    # Not JSON; keep raw text payload
                    pass

                db_event = ProctorEvent(event_type=event_type, payload=payload_str)
                db.add(db_event)
                db.commit()
                db.refresh(db_event)

                await websocket.send_json({"ack": True, "id": db_event.id})

        except WebSocketDisconnect:
            # Client disconnected; end session gracefully
            return
