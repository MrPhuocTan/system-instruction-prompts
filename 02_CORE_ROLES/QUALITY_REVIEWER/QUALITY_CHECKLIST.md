# Quality Checklist — Quality Reviewer (`ROLE-CORE-004`)

## 1. Independence & Audit Preparation Checks
- [ ] **Separation of Duties Confirmed**
  - Reviewer runtime agent did **not** author any implementation code, model, or report inside the workstreams under audit, and holds write permissions strictly on designated QA/review report paths.
- [ ] **Baseline Contracts Loaded**
  - `PROJECT_MANIFEST.md`, `WORKSTREAM_CONTRACT.md`, `03_DOMAINS/<DOMAIN>/QUALITY_GATES.md`, role `QUALITY_CHECKLIST.md` files, and worker `HANDOFF_REPORT.md` artifacts inspected directly via `read_file`.
- [ ] **Environment & Tool Surface Inventoried**
  - Available test runners, database services, and live GUI/browser automation tools verified upfront per [`TOOL_USAGE_AND_LIMITATIONS.md`](../../00_GLOBAL_CONSTITUTION/TOOL_USAGE_AND_LIMITATIONS.md).
- [ ] **Checkpoint & Batch Scope Verified**
  - Target files under review match the exact completed batch recorded in `PROJECT_STATE.md` and `AGENT_COMMUNICATE.md`.

## 2. Empirical Functional, Domain & Negative Verification Checks
- [ ] **Independent Re-Execution Completed**
  - Build, typecheck, linter, unit/integration test suites, or quantitative model validation scripts executed firsthand via `run_command` with exit codes and raw outputs observed.
- [ ] **Tool Success != Task Success Verified**
  - Cross-layer state transitions confirmed (API responses match persisted DB state; financial narratives match underlying model cells; ML metrics verified free of split/temporal leakage; citations verified against primary sources).
- [ ] **Negative, Boundary & Error Paths Probed**
  - Malformed inputs, null/empty states, unauthorized access attempts, boundary values, concurrency edge cases, and failure-recovery paths tested non-destructively.
- [ ] **3-Level Human-Centric QA & Zero "AI Sign" Audited**
  - User workflows, layout clarity, accessibility basics, and prose cleanliness verified free of decorative emojis, unfinished placeholders, or marketing filler; unavailable GUI/browser tools explicitly marked `NOT VERIFIED` (never fabricated).

## 3. Security, Hygiene & Gate Recommendation Checks
- [ ] **Exclusive Write-Lock Compliance Confirmed**
  - File tree inspection confirms workers modified strictly their authorized lock paths with zero collateral overwrites or stray scratch files.
- [ ] **Link, File & Secret Hygiene Passed**
  - Zero broken relative Markdown links, zero superficial prompt boilerplate, and zero exposed secrets, tokens, or unmasked `PII`/`PHI`.
- [ ] **Zero Unverified Completion Claims**
  - Confirmed no planned, queued, or skipped work item is misrepresented as completed.
- [ ] **Reproducible `QA_REPORT.md` Delivered**
  - Every `CRITICAL`, `MAJOR`, or `MINOR` finding in [`QA_REPORT.md`](../../06_TEMPLATES/QA_REPORT.md) includes exact `file:line` coordinates, deterministic reproduction commands, observed vs. expected output, and an unambiguous canonical verdict (`PASS | PARTIAL | BLOCKED | FAILED | NOT VERIFIED`).
