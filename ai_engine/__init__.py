"""AI engine package stubs for the exam proctoring system.

This package contains placeholder implementations for computer-vision
and AI components such as face detection, gaze estimation, object
recognition, and risk scoring. Replace stubs with real models as the
project evolves.
"""

from .face_detection import detect_faces
from .gaze_estimation import estimate_gaze
from .object_detection import detect_prohibited_items
from .risk_scoring import RiskScorer

__all__ = [
    "detect_faces",
    "estimate_gaze",
    "detect_prohibited_items",
    "RiskScorer",
]
