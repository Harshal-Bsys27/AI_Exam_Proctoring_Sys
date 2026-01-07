"""Face detection stubs using OpenCV/MediaPipe.

Intended behavior:
- Receive frames from the webcam pipeline.
- Detect faces and return bounding boxes.
- Optionally provide landmarks for downstream tasks (e.g., gaze).

Implementation notes:
- Replace placeholder logic with OpenCV/MediaPipe Face Detection.
- Consider performance trade-offs and model selection.
"""

from typing import List, Tuple

try:
    import numpy as np
except Exception:  # pragma: no cover - optional at scaffold time
    np = None  # type: ignore


def detect_faces(frame: "np.ndarray") -> List[Tuple[int, int, int, int]]:
    """Return a list of face bounding boxes (x, y, w, h).

    TODO:
    - Implement actual face detection with MediaPipe or OpenCV's DNN.
    - Calibrate thresholds and handle multiple faces.

    Args:
        frame: A single video frame as a NumPy array (BGR).

    Returns:
        List of bounding boxes as tuples (x, y, w, h).
    """
    # Placeholder: no detection yet.
    return []
