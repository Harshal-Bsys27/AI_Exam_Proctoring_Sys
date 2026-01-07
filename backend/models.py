"""SQLAlchemy models for the proctoring backend."""

from sqlalchemy import Column, DateTime, Integer, String, Text, func

from .database import Base


class ProctorEvent(Base):
    """A stored proctoring event (e.g., visibility change, fullscreen exit)."""

    __tablename__ = "proctor_events"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    event_type = Column(String(50), index=True, nullable=False)
    payload = Column(Text, nullable=True)  # JSON-serialized string for simplicity
