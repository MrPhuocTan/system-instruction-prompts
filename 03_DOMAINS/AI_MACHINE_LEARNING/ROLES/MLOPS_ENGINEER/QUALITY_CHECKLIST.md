# Quality Checklist: MLOps Engineer (`ROLE-AIML-007`)

- **Role:** [`MLOPS_ENGINEER`](./SYSTEM_PROMPT.md)
- **Domain Gates:** [`QUALITY_GATES.md`](../../QUALITY_GATES.md)

---

## 1. Lineage, Reproducibility & Supply-Chain Integrity
- [ ] Bound every registered model version immutably to `git_sha`, dependency lockfile/container digest, dataset/feature-view digest, hyperparameters, and evaluation report.
- [ ] Enforced safe weight deserialization (`safetensors`, `ONNX`, `weights_only=True`) and `SHA-256` checksum verification prior to serving load.

## 2. Offline-Online Parity & CI/CT Promotion Gates
- [ ] Verified feature-store and preprocessing parity via automated equivalence tests comparing batch offline features against online point-in-time lookups.
- [ ] Blocked automated Challenger promotion unless Challenger beats or matches Champion on locked golden + rolling evaluation splits AND passes latency, memory, and worst-slice guardrails.
- [ ] Placed upstream data-quality circuit breakers ahead of continuous training (`CT`) jobs to prevent poisoned model updates.

## 3. Serving Reliability, Warmup & Instant Rollback
- [ ] Configured readiness probes to pass ONLY after model weights load into memory and synthetic warmup forward passes complete (`JIT`/graph cache warmed).
- [ ] Bounded concurrency, request payload byte limits, dynamic-batching `max_queue_delay`, and inference timeouts; verified malformed requests return typed `4xx` errors without crashing workers.
- [ ] Verified deterministic shadow/canary traffic routing and tested `< 60s` rollback to the prior pinned Champion artifact.

## 4. Telemetry, Drift Calibration & Privacy Compliance
- [ ] Logged `(prediction_id, model_version, timestamp, latency_ms, confidence/abstention)` with `PII`/secret redaction to enable delayed ground-truth join and importance-weighted drift (`PSI`) alerting.
- [ ] Calibrated drift alert thresholds to top-importance features (`SHAP` rank) and prediction rate shifts to prevent alert fatigue.
- [ ] Protected host disk and RAM during local pipeline verification and gated any live cloud/production deployment behind explicit human approval.

## 5. Independent Verification & Handoff Completeness
- [ ] Executed automated `pytest` smoke tests covering DAG acyclicity, offline/online feature parity, malformed-payload `4xx` handling, readiness warmup, and Champion rollback.
- [ ] Documented deployment runbook, SLO thresholds, and rollback command sequence for [`SYSTEM_ARCHITECT`](../../../../02_CORE_ROLES/SYSTEM_ARCHITECT/SYSTEM_PROMPT.md).
- [ ] Explicitly separated empirically verified local serving checks from `NOT VERIFIED` multi-node cluster or live traffic load tests.
