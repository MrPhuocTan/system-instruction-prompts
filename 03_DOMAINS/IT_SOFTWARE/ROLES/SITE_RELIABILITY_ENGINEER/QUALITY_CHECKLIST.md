# Site Reliability Engineer Quality Checklist (`SITE_RELIABILITY_ENGINEER`)

- **Role ID:** `ROLE-IT-011`
- **Prompt Reference:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)
- **Domain Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md)

---

## 1. Pre-Handoff Verification Checklist

### 1.1 SLI/SLOs, Burn-Rate Alerting & Cardinality Discipline
- [ ] **User-Centric SLI/SLO Definitions:** Availability, latency, freshness, or correctness SLIs map directly to user-observable outcomes with explicit measurement windows and error-budget thresholds.
- [ ] **Multi-Burn-Rate Actionable Alerting:** Paging alert rules use multi-window burn-rate logic (zero noisy raw CPU/memory threshold flaps), validate syntactically, and link 1:1 to actionable runbook procedures.
- [ ] **Bounded Metric Cardinality & OTel Correlation:** Metrics avoid high-cardinality labels (raw user IDs, UUIDs, unnormalized paths); logs and traces propagate `trace_id`/`span_id` and redact all secrets/PII.

### 1.2 Probes, Overload Protection & Fault Recovery
- [ ] **Decoupled Liveness vs. Readiness Probes:** Liveness (`/healthz`) checks local process health without downstream dependency calls (preventing cascading restart storms), while readiness (`/readyz`) governs traffic gating cleanly.
- [ ] **Retry-Storm & Overload Protection:** Outbound call chains enforce bounded deadlines, single-layer retry budgets with jitter, circuit breaking/load-shedding, and clean `SIGTERM` in-flight request draining.
- [ ] **Verified Dependency-Failure Behavior:** Automated or local fault simulation confirmed graceful degradation and bounded timeout responses when upstream dependencies stall or fail.

### 1.3 Runbooks, Chaos Safety & Runtime Honesty
- [ ] **Executable Runbooks & DR Clarity:** Operational and backup/restore runbooks specify exact diagnostic commands, RTO/RPO targets, escalation thresholds, and verified rollback steps.
- [ ] **Runtime & Chaos Safety:** Zero unapproved live fault-injection, traffic failover, or production state mutations occurred; persistent monitoring is codified in standard infra configs rather than assuming immortal IDE subagents.
- [ ] **Honest Environment Disclosure:** Cluster-level PromQL/Alertmanager/DR failover checks not runnable locally are explicitly marked `PARTIAL` or `NOT VERIFIED`.
- [ ] **Exclusive Write-Lock Compliance:** All modified telemetry, alerting, and runbook files reside strictly inside assigned write-lock paths.

---

## 2. Required Handoff Evidence & Gate Classification

1. Validated SLI/SLO specs, alert rule check outputs, and local probe/metrics/graceful-shutdown verification logs via `run_command` (`PASS` / `FAILED`).
2. Dependency-failure simulation results confirming absence of cascading hangs or retry storms.
3. Production Readiness Review (PRR) risk summary and any `PARTIAL` / `NOT VERIFIED` live-cluster checks escalated to `SA` + `PM`.
