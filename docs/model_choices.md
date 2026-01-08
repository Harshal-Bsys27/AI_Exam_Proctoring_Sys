# Model Choices (Planned)

This project ships with placeholders instead of full ML models. Below are the intended choices and rationale:

- OpenCV: Efficient image operations and basic classical detection pipelines.
- MediaPipe: High-quality face detection/mesh landmarks suitable for gaze/pose estimation.
- YOLOv8 (ultralytics): General-purpose object detector for prohibited items (e.g., phones).

## Considerations
- Performance/latency: Balance accuracy with real-time constraints.
- Robustness: Handle poor lighting, occlusions, low-resolution webcams.
- Fairness: Validate across diverse faces and environments.
- Privacy: Minimize retained data and avoid unnecessary sharing/processing.

## Next Steps
- Replace `ai_engine` stubs with operational models and inference code.
- Add evaluation scripts and datasets with appropriate consent and licenses.
- Implement unit tests and golden-sample benchmarks.
