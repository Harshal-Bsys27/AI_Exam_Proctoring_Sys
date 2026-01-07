"""Pydantic schemas for request/response payloads."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class EventCreate(BaseModel):
    """Schema for creating a new proctoring event."""

    event_type: str = Field(..., max_length=50)
    payload: Optional[str] = None  # store as JSON string


class EventRead(BaseModel):
    """Schema for reading a stored proctoring event."""

    id: int
    created_at: datetime
    event_type: str
    payload: Optional[str]

    class Config:
        from_attributes = True  # Pydantic v2 style (alias for orm_mode)
