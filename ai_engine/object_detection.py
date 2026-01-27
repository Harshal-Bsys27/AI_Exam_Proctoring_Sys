"""Prohibited object detection using YOLOv8.

Detects prohibited items like phones, books, etc.
"""

from typing import List
import numpy as np
from ultralytics import YOLO

# Load YOLOv8 model (nano for speed)
model = YOLO('yolov8n.pt')  # Will download if not present

# Prohibited classes (COCO dataset classes)
PROHIBITED_CLASSES = {
    67: 'cell phone',  # COCO class for cell phone
    73: 'book',        # book
    63: 'laptop',      # laptop
    62: 'tv',          # tv/monitor
    # Add more as needed
}


def detect_prohibited_items(frame: np.ndarray) -> List[str]:
    """Detect prohibited items from a frame using YOLOv8.

    Args:
        frame: A single video frame as a NumPy array (BGR).

    Returns:
        A list of detected prohibited item labels.
    """
    results = model(frame, conf=0.5)  # Confidence threshold
    
    detected = []
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls.item())
            if class_id in PROHIBITED_CLASSES:
                label = PROHIBITED_CLASSES[class_id]
                if label not in detected:
                    detected.append(label)
    
    return detected

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
