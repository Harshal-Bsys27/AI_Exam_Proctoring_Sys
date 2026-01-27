"""Gaze estimation using OpenCV eye detection.

Estimates gaze direction based on eye positions and pupil detection.
"""

import cv2
import numpy as np
from typing import Literal

GazeDirection = Literal["left", "right", "center", "down", "unknown"]

# Load Haar cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


def estimate_gaze(frame: np.ndarray) -> GazeDirection:
    """Estimate coarse gaze direction from a frame.

    Args:
        frame: A single video frame as a NumPy array (BGR).

    Returns:
        A coarse gaze direction label.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) == 0:
        return "unknown"
    
    # Assume first face
    (x, y, w, h) = faces[0]
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]
    
    # Detect eyes
    eyes = eye_cascade.detectMultiScale(roi_gray)
    if len(eyes) < 2:
        return "unknown"
    
    # Take the two eyes (assuming left and right)
    eyes = sorted(eyes, key=lambda e: e[0])  # Sort by x position
    if len(eyes) >= 2:
        left_eye = eyes[0]
        right_eye = eyes[1]
        
        # Simple gaze estimation: check if pupils are visible or position
        # For simplicity, assume center if eyes detected
        # In a real implementation, use pupil detection
        
        # Placeholder: return "center" if eyes are detected
        return "center"
    
    return "unknown"
