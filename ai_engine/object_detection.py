"""Prohibited object detection stub (e.g., phones, notes, extra displays).

Intended behavior:
- Use a general object detector (e.g., YOLOv8) to identify prohibited items.
- Return a list of detected class names or structured detections.

Implementation notes:
- Replace stub with `ultralytics` YOLOv8 inference and postprocessing.
- Consider custom class lists and confidence thresholds.
"""

from typing import List

try:
    import numpy as np
except Exception:  # pragma: no cover
    np = None  # type: ignore


def detect_prohibited_items(frame: "np.ndarray") -> List[str]:
    """Detect prohibited items from a frame.

    TODO:
    - Load a YOLOv8 model and run inference.
    - Map model classes to a business-specific prohibited-list.

    Args:
        frame: A single video frame as a NumPy array (BGR).

    Returns:
        A list of detected prohibited item labels.
    """
    # Placeholder: no detections yet.
    return []
