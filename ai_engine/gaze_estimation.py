"""Gaze estimation stub.

Intended behavior:
- Use face landmarks or eye region crops to estimate gaze direction.
- Output coarse categories (e.g., 'left', 'right', 'center', 'down').

Implementation notes:
- Replace with a lightweight gaze model or geometric heuristic.
- Consider latency and robustness to head pose changes.
"""

from typing import Literal

try:
    import numpy as np
except Exception:  # pragma: no cover
    np = None  # type: ignore


GazeDirection = Literal["left", "right", "center", "down", "unknown"]


def estimate_gaze(frame: "np.ndarray") -> GazeDirection:
    """Estimate coarse gaze direction from a frame.

    TODO:
    - Use detected face/eye regions to compute gaze vector.
    - Integrate with landmarks from MediaPipe Face Mesh if available.

    Args:
        frame: A single video frame as a NumPy array (BGR).

    Returns:
        A coarse gaze direction label.
    """
    # Placeholder: cannot infer without landmarks.
    return "unknown"
