# Quality Checklist: Machine Learning Engineer (`ROLE-AIML-002`)

- **Role:** [`MACHINE_LEARNING_ENGINEER`](./SYSTEM_PROMPT.md)
- **Domain Gates:** [`QUALITY_GATES.md`](../../QUALITY_GATES.md)

---

## 1. Split Hygiene & Zero-Leakage Verification
- [ ] Verified split strategy matches data generating process (`GroupKFold` for repeated entities; chronological `walk-forward` + embargo gap for temporal targets) with automated disjointness assertions.
- [ ] Confirmed all stateful transformers (imputers, scalers, target/frequency encoders, feature selectors, oversamplers) fit strictly inside each training fold.
- [ ] Audited top `SHAP`/permutation features and ran adversarial validation (`train` vs. `test` `AUC`) to rule out post-outcome leakage or severe covariate shift.

## 2. Modeling Rigor, Baselines & Calibration
- [ ] Benchmarked final candidate against both a deterministic domain heuristic and a low-complexity linear/untuned baseline across `>= 3` seeds or CV folds.
- [ ] Evaluated probability calibration (`ECE`, Brier score, reliability curve) and applied Bayes prior correction if class weighting or downsampling was used during training.
- [ ] Selected operating threshold strictly on validation folds using explicit business/safety cost weights (`FP` vs. `FN`), keeping the held-out test split untouched until final lock.

## 3. Training-Serving Parity & Serialization Safety
- [ ] Exported model and preprocessing graph in safe, versioned formats (`ONNX`, native `LightGBM`/`XGBoost` `UBJ`/`JSON` + typed schema manifest) without untrusted `pickle` execution.
- [ ] Passed automated numerical parity tests (`atol <= 1e-6`) comparing training-pipeline predictions against standalone inference runtime outputs.
- [ ] Verified stateless batch invariance (`predict([x1, x2])[0] == predict([x1])[0]`) and edge-case resilience on all-null rows, unseen categorical tokens, extreme outliers, and `Inf`/`NaN` inputs.

## 4. Slice Fairness, Resource Footprint & Reproducibility
- [ ] Reported disaggregated metrics across cold-start entities, minority slices, and temporal windows without hiding regressions behind aggregate `ROC-AUC` or accuracy.
- [ ] Verified compliance with protected-attribute exclusions and monotonic/reason-code explainability requirements where applicable.
- [ ] Pinned random seeds, package versions, and dataset `SHA-256` hashes; verified local training memory and `p99` inference latency satisfy target serving SLAs.

## 5. Independent Verification & Handoff Completeness
- [ ] Executed full `pytest` suite from clean state verifying split disjointness, schema contracts, edge-case inputs, and `ONNX`/booster round-trip parity.
- [ ] Packaged reproducible evaluation summary and feature schema contract for [`MLOPS_ENGINEER`](../MLOPS_ENGINEER/SYSTEM_PROMPT.md) and [`AI_EVALUATION_ENGINEER`](../AI_EVALUATION_ENGINEER/SYSTEM_PROMPT.md).
- [ ] Explicitly separated empirically verified metrics from any `NOT VERIFIED` production traffic or delayed-label assumptions.
