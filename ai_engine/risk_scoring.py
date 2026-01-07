"""Risk scoring stub for proctoring events.

Intended behavior:
- Combine signals (face presence, gaze, objects, browser events) into a
  normalized risk score (e.g., 0.0 to 1.0).

Implementation notes:
- Start with a rule-based approach; later replace with a trained model.
"""

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class RiskScorer:
    """Placeholder risk scoring class.

    TODO:
    - Add tunable weights for each signal.
    - Log intermediate contributions for explainability.
    """

    def score_event(self, event: Dict[str, Any]) -> float:
        """Return a simple placeholder risk score.

        Args:
            event: A dictionary describing a proctoring event.

        Returns:
            A float in [0.0, 1.0] representing risk magnitude.
        """
        # Placeholder heuristic: unknown events are low risk.
        event_type = event.get("type", "unknown")
        if event_type in {"visibilityhidden", "fullscreen_exit", "suspicious_object"}:
            return 0.7
        return 0.1
