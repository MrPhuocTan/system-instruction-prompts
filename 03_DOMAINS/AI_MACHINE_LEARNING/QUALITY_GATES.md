# AI & Machine Learning Quality Gates (`DOM-03-AIML`)

All `AI_MACHINE_LEARNING` workstreams (`Level 1`–`Level 4`) must satisfy the objective pass/fail gates below prior to [`DOMAIN_LEAD`](../../02_CORE_ROLES/DOMAIN_LEAD/SYSTEM_PROMPT.md), [`SYSTEM_ARCHITECT`](../../02_CORE_ROLES/SYSTEM_ARCHITECT/SYSTEM_PROMPT.md) (`SA_GATE`), and [`PROJECT_MANAGER`](../../02_CORE_ROLES/PROJECT_MANAGER/SYSTEM_PROMPT.md) (`PM_GATE`) sign-off. Any gate that cannot be empirically executed in the current runtime must be marked `NOT VERIFIED` with an exact reproduction command.

---

## Gate Summary Matrix

| Gate ID | Gate Name | Mandatory Evidence Artifact | Blocking Failure Condition |
| :--- | :--- | :--- | :--- |
| `AIML-QG-01` | Dataset Integrity & Provenance | Dataset manifest / Datasheet with schema, hashes, license, and label audit | Unverified label noise, silent duplicates across splits, PII leak, or incompatible license |
| `AIML-QG-02` | Training Methodology & Sanity | Single-batch overfit log, loss/gradient health trace, hyperparameter config | `NaN`/exploding gradients, silent broadcasting bug, or unlogged manual weight edits |
| `AIML-QG-03` | Validation Split Architecture | Deterministic split script + disjointness assertion test output | Random `i.i.d.` split on temporal/grouped entities or test-set contamination |
| `AIML-QG-04` | Data, Target & Temporal Leakage | Automated feature/timestamp/corpus leakage audit report | Post-outcome features, global pre-split normalization, or benchmark overlap in corpus |
| `AIML-QG-05` | Metrics Selection & Calibration | Cost-aligned primary/guardrail metric table + calibration (`ECE`/Brier) | Accuracy-only reporting on skewed tasks or uncalibrated probability thresholds |
| `AIML-QG-06` | Baseline & Ablation Comparison | Comparison table vs. heuristic + simple model + component ablations | Complex architecture fails to beat simple baseline on cost-adjusted metric/latency |
| `AIML-QG-07` | Reproducibility & Artifact Pinning | Seed-locked config, dependency lockfile, `safetensors`/hash manifest | Non-reproducible pipeline, unpinned weights, or unsafe `pickle` deserialization |
| `AIML-QG-08` | Slice, Fairness & Safety Audit | Disaggregated slice error matrix, toxicity/injection/hallucination report | Aggregate gain masks severe subgroup regression, unsafe output, or prompt-injection bypass |
| `AIML-QG-09` | Real-World `OOD` & Serving Parity | Perturbation/`OOD` stress results, `p95`/`p99` latency & memory profile, fallback test | Training-serving skew, unbounded `OOM`/timeout under load, or missing abstention path |

---

## Detailed Gate Specifications

### `AIML-QG-01` — Dataset Integrity & Provenance
- Verify exact row/sample counts, primary-key uniqueness, class/target distributions, missingness rates per feature, corrupted media/UTF-8 rates, and near-duplicate rates (`MinHash`/`SimHash` or perceptual hash for images).
- Confirm explicit license compatibility and confirm zero raw secrets or unauthorized `PII`/`PHI` exist in training, validation, retrieval, or evaluation corpora.

### `AIML-QG-02` — Training Methodology & Numerical Sanity
- Prove optimization mechanics via a deterministic small-sample (`1`–`8` batch) overfit test reaching near-zero training loss before running full-scale jobs.
- Verify tensor shapes explicitly (avoid implicit broadcasting misalignment), confirm correct `model.train()` vs. `model.eval()` / dropout / batchnorm state transitions, and log learning-rate schedules, weight decay exclusions, and gradient clipping norms.

### `AIML-QG-03` — Validation Methodology
- Match validation topology strictly to the deployment generating process: `GroupKFold` for multi-record entities, chronological `walk-forward` with purge/embargo windows for time series, and stratified/cluster-aware splits for rare classes or spatial data.
- Hold out an untouched final test set (or locked golden benchmark) evaluated only after architecture, prompt, retrieval, and hyperparameter choices are frozen.

### `AIML-QG-04` — Data, Target & Temporal Leakage Detection
- Assert programmatically that `train_ids ∩ val_ids == ∅`, `train_ids ∩ test_ids == ∅`, and `max(feature_event_ts) <= prediction_decision_ts` for every row.
- Inspect top feature importances (`SHAP`/permutation) or `LLM` n-gram/embedding overlap against test benchmarks; treat suspiciously high validation scores (`AUC > 0.99` on noisy behavioral tasks) as leakage until disproven.

### `AIML-QG-05` — Metrics Selection & Calibration
- Pair at least one task-aligned primary metric (`PR-AUC`, `NDCG@k`, `IoU`/`mAP`, `F1-macro`, `WAPE`/pinball quantile loss, groundedness/faithfulness) with operational guardrail metrics (`p95`/`p99` latency, `TTFT`, cost per `1k` requests, abstention rate).
- Measure probability or confidence calibration (`ECE`, Brier score, reliability plot) and document exact decision threshold selection on the validation split.

### `AIML-QG-06` — Baseline Comparison & Ablation Discipline
- Benchmark every candidate model against: (1) a deterministic heuristic / majority / persistence / `BM25` baseline, and (2) a low-complexity statistical or classical ML baseline.
- Provide component ablations proving each added architectural module, loss term, retrieval reranker, or fine-tuning stage contributes statistically meaningful lift above run-to-run seed variance.

### `AIML-QG-07` — Reproducibility, Seeds & Serialization Safety
- Record commit SHA, dataset digest, hyperparameter YAML/JSON, environment lockfile, and `PRNG` seeds across `>= 3` seeds for stochastic claims when compute permits.
- Export weights in safe formats (`safetensors`, `ONNX`) with cryptographic checksums and automated schema validation on load.

### `AIML-QG-08` — Slice, Fairness & Safety Analysis
- Report disaggregated performance across critical cohorts (input length, language, sensor/lighting regime, rare classes, demographic/protected proxies where legally permissible, cold-start entities).
- For `LLM` and generative systems, run adversarial prompt-injection, jailbreak, PII extraction, ungrounded hallucination, and tool-misuse test suites.

### `AIML-QG-09` — Real-World `OOD` Robustness & Serving Parity
- Test degraded/shifted inputs: missing features, schema drift, OCR/ASR noise, image blur/compression, distribution shift, upstream retrieval timeout, and empty context windows.
- Confirm numerical parity between training framework and serving runtime, verify bounded memory/`VRAM` and `p99` latency under realistic concurrency, and verify graceful fallback/abstention when confidence falls below threshold or dependencies fail.
