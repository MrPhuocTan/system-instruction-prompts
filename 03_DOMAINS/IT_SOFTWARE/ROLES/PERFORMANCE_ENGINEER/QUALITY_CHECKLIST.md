# Performance Engineer Quality Checklist (`PERFORMANCE_ENGINEER`)

- **Role ID:** `ROLE-IT-010`
- **Prompt Reference:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)
- **Domain Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md)

---

## 1. Pre-Handoff Verification Checklist

### 1.1 Empirical Baseline, Profiling & Controlled Comparison
- [ ] **Empirical Baseline Captured First:** Reproducible pre-change baseline metrics (`p50`, `p95`, `p99` latency, RPS/ops-sec, peak RSS memory, DB query count) were recorded before code modification.
- [ ] **Profiler-Backed Root Cause:** Optimization targets a measured bottleneck evidenced by CPU/allocation profiles, event-loop telemetry, or SQL `EXPLAIN` plans rather than speculative micro-tuning.
- [ ] **Apples-to-Apples Multi-Trial Comparison:** Candidate benchmark ran under identical dataset cardinality, concurrency, warm-up separation, and runtime flags across `>= 3` trials via `run_command`.
- [ ] **Percentile & Error-Rate Integrity:** Reported gains evaluate `p50`/`p95`/`p99` tail latencies alongside `0%` unexpected error rate (never mean latency alone or fast failed `500` responses).

### 1.2 Memory Bounds, Cache Isolation & Regression Safety
- [ ] **Bounded Memory & Cache Safety:** Any introduced cache enforces strict max-entry/byte bounds, tenant-isolated cache keys, stampede protection, and explicit invalidation/TTL semantics.
- [ ] **Zero Functional or Security Regression:** Full existing + concurrency unit/integration suites pass `100%`, proving optimizations preserve data accuracy, isolation, and authz checks.

### 1.3 Host Thermal Protection, Scope & Write-Locks
- [ ] **Host Thermal, CPU & Disk Protection:** Local benchmark concurrency, duration, and temporary dataset sizes remained bounded without exhausting workspace disk or throttling the host OS; synthetic datasets and background processes were cleaned up.
- [ ] **Authorized Target Scope Only:** Zero load/stress traffic was sent to external third-party services or unapproved shared/production endpoints.
- [ ] **Honest Hardware Extrapolation Caveat:** Report distinguishes local loopback benchmark deltas from unverified multi-node production cluster capacity (`PARTIAL` / `NOT VERIFIED`).
- [ ] **Exclusive Write-Lock Compliance:** All benchmark scripts and code optimizations stay strictly inside assigned write-lock paths.

---

## 2. Required Handoff Evidence & Gate Classification

1. Exact benchmark/profiler commands and reproducible before-vs-after comparative table (`p50`, `p95`, `p99`, throughput, memory, query/allocation delta) (`PASS` / `FAILED`).
2. Functional regression test pass output post-optimization.
3. Documented dataset scale, hardware/runtime context, and any `PARTIAL` / `NOT VERIFIED` cluster capacity assumptions escalated to `SA`.
