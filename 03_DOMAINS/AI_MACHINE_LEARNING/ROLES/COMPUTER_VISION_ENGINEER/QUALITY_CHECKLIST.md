# Quality Checklist: Computer Vision Engineer (`ROLE-AIML-004`)

- **Role:** [`COMPUTER_VISION_ENGINEER`](./SYSTEM_PROMPT.md)
- **Domain Gates:** [`QUALITY_GATES.md`](../../QUALITY_GATES.md)

---

## 1. Spatial/Temporal Split Hygiene & Dataset Integrity
- [ ] Grouped splits strictly by `video_id`, `scene_id`, `patient_id`, `document_id`, or `camera_id` and ran perceptual-hash (`pHash`/`dHash`) near-duplicate filtering across splits.
- [ ] Audited annotations for zero-area or out-of-bounds bounding boxes, self-intersecting polygons, EXIF orientation transpose mismatches, and truncated media files.

## 2. Coordinate Geometry & Preprocessing Parity
- [ ] Locked exact channel order (`RGB` vs. `BGR`), resize/interpolation kernel (`antialias` flag, `align_corners`), letterbox pad values, and normalization mean/std identically across training and serving code.
- [ ] Passed deterministic coordinate round-trip unit tests (`original sensor pixel -> letterbox/augment -> inverse unpad`) within `<= 1.0 px` error across boxes, masks, keypoints, and camera intrinsics `K`.
- [ ] Verified geometric augmentations preserve label semantics (no horizontal flips on chirality-sensitive objects, directional arrows, or OCR text).

## 3. Evaluation, Slice & Corruption Robustness
- [ ] Evaluated task-appropriate metrics (`mAP@50:95`, scale-stratified `AP_S`/`AP_M`/`AP_L`, boundary `IoU`, `HOTA`/`IDF1`, `CER`/`WER`) alongside confidence calibration and `NMS` threshold sensitivity.
- [ ] Audited disaggregated performance across object scale, occlusion severity, illumination (day/night/glare), camera angle, and compression/blur corruptions; visually inspected diagnostic failure overlays.

## 4. Stream Safety, Privacy & Serialization
- [ ] Verified exported `ONNX`/`safetensors`/`TensorRT` numerical parity against eager `PyTorch` (`IoU >= 0.99` on test fixtures).
- [ ] Bounded video decode/inference frame-queue backpressure (`drop-oldest` or rate limit) and measured `FPS`, host RAM, and `VRAM` headroom.
- [ ] Confirmed zero camera/`RTSP` credentials in code or logs, enforced decompression-bomb pixel/byte limits on untrusted uploads, and verified face/plate/biometric `PII` redaction compliance.

## 5. Independent Verification & Handoff Completeness
- [ ] Executed automated `pytest` suite covering coordinate transforms, channel/normalization parity, corrupt-image error handling, and `NMS` post-processing determinism.
- [ ] Verified batch-size invariance (`batch=1` vs. `batch=8`) and deterministic confidence scores across runs.
- [ ] Inspected rendered visual overlays on failure slices (`FP` and `FN` examples) via `view_file` where image outputs exist.
- [ ] Clearly separated empirically verified local benchmarks from `NOT VERIFIED` live camera or edge-accelerator metrics.
