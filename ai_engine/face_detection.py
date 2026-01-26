"""Face presence detection using OpenCV Haar Cascade.

This module provides face presence detection for the AI exam proctoring system.
It uses OpenCV's Haar Cascade classifier for reliable face detection without deep learning.

Implementation notes:
- Uses Haar Cascade for face detection (frontal faces).
- Focuses on presence detection rather than detailed analysis.
- Designed for real-time performance with webcam input.

TODO:
- Consider switching to DNN-based detection for better accuracy.
- Add face tracking across frames for stability.
- Implement confidence scoring for detected faces.
- Handle different lighting conditions and angles.
"""

import cv2
import numpy as np
from typing import List, Tuple


class FacePresenceDetector:
    """Detector for face presence in video frames.

    Uses OpenCV Haar Cascade classifier to detect faces and evaluate presence status.
    """

    def __init__(self):
        """Initialize the face detector with Haar Cascade classifier."""
        # Load the pre-trained Haar Cascade classifier for frontal face detection
        cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        self.face_cascade = cv2.CascadeClassifier(cascade_path)

        # TODO: Add configuration for cascade parameters (scaleFactor, minNeighbors, etc.)

    def detect_faces(self, frame: np.ndarray) -> int:
        """Detect the number of faces in a given frame.

        Args:
            frame: A single video frame as a NumPy array (BGR format).

        Returns:
            The number of faces detected in the frame.

        TODO:
        - Add face size filtering to avoid false positives from small detections.
        - Implement face quality assessment.
        """
        # Convert frame to grayscale for Haar Cascade detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces using Haar Cascade
        # Parameters: scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        # These can be tuned for better performance/accuracy
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        return len(faces)

    def evaluate_presence(self, face_count: int) -> str:
        """Evaluate the presence status based on face count.

        Args:
            face_count: Number of faces detected.

        Returns:
            Status string: "FACE_MISSING", "OK", or "MULTIPLE_FACES".

        TODO:
        - Add hysteresis to prevent status flickering between frames.
        - Consider face position/pose for more sophisticated evaluation.
        """
        if face_count == 0:
            return "FACE_MISSING"
        elif face_count == 1:
            return "OK"
        else:  # face_count > 1
            return "MULTIPLE_FACES"


# Legacy function for backward compatibility (returns bounding boxes)
def detect_faces(frame: np.ndarray) -> List[Tuple[int, int, int, int]]:
    """Return a list of face bounding boxes (x, y, w, h).

    This is a legacy function. For presence detection, use FacePresenceDetector class.

    TODO:
    - Deprecate this function in favor of the class-based approach.
    - Implement actual face detection with improved accuracy.

    Args:
        frame: A single video frame as a NumPy array (BGR).

    Returns:
        List of bounding boxes as tuples (x, y, w, h).
    """
    # Placeholder: no detection yet.
    return []
