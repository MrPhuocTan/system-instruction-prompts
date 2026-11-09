# Workstream Management, Small-Batch Waves & Dependency Escalation

## 1. Workstream & Small-Batch Decomposition Principles
On `Level 2` through `Level 4` projects ([`TASK_COMPLEXITY_ROUTER.md`](../00_GLOBAL_CONSTITUTION/TASK_COMPLEXITY_ROUTER.md)), `PM` and `SA` autonomously decompose project scope into a **Directed Acyclic Graph (`DAG`)** of bounded workstreams executed in small, independently verifiable batches ([`AUTONOMOUS_ORCHESTRATION.md`](./AUTONOMOUS_ORCHESTRATION.md)).
Workstreams are indexed in [`AGENT_COMMUNICATE.md`](../06_TEMPLATES/AGENT_COMMUNICATE.md) (`Section 7: Workstream Ownership`) and formalized per workstream using [`WORKSTREAM_CONTRACT.md`](../06_TEMPLATES/WORKSTREAM_CONTRACT.md) and [`WORKER_ASSIGNMENT.md`](../06_TEMPLATES/WORKER_ASSIGNMENT.md).

Every valid workstream batch satisfies four structural invariants:
1. **Single Accountable Owner**
   - Exactly `1` runtime agent owns execution of a given workstream in any wave ([`DYNAMIC_AGENT_ALLOCATION.md`](./DYNAMIC_AGENT_ALLOCATION.md)).
2. **Acyclic Dependency Graph**
   - Upstream input artifacts and downstream consumer interfaces form a strict `DAG` with zero circular dependencies.
3. **Disjoint Mutable File Surface**
   - Parallel workstreams within the same wave share **zero** mutable file paths ([`FILE_OWNERSHIP_AND_LOCKING.md`](./FILE_OWNERSHIP_AND_LOCKING.md)).
4. **Independent Batch Verifiability & Checkpoint Safety**
   - Each batch is small enough to verify deterministically before advancing `PROJECT_STATE.md` (`Checkpoint` + `Research Queue`), guaranteeing zero lost progress if interrupted ([`CONTRACT_AND_HANDOFF.md`](./CONTRACT_AND_HANDOFF.md)).

## 2. Standard Topological Wave Execution Model
Projects execute in ordered waves so shared contracts stabilize before parallel fan-out:

| Execution Wave | Primary Engineering Objective | Active Owners | Gate Criteria to Advance |
| :--- | :--- | :--- | :--- |
| **Wave 0 — Framing & Contract Lock** | Hydrate checkpoints, classify `Level 0`–`Level 4`, lock charter, schemas, APIs, write-locks, and risk register. | `PM` + `SA` (+ `DOMAIN_LEAD` on `Level 4`) | `SA` contract lock + zero write-lock overlap + required Human Approval (`ask_question`) granted. |
| **Wave 1 — Shared Foundations** | Implement shared database schemas, core type packages, config scaffolding, or baseline datasets/protocols. | `1–2` foundational workers | Deterministic schema, typecheck, and build verification `PASS` + checkpoint saved. |
| **Wave 2 — Parallel Domain & Feature Batches** | Concurrent microservice, UI, data, analytical, financial, or research batches across disjoint directories. | Parallel specialist subagents (or sequential inline batches under fallback) | `100%` of Wave 2 [`HANDOFF_REPORT.md`](../06_TEMPLATES/HANDOFF_REPORT.md) artifacts validated against locked contracts. |
| **Wave 3 — Integration, QA & Coverage Audit** | Wire shared entrypoints/indexes, execute end-to-end 3-Level QA, cross-domain tie-outs, and security/compliance review. | Integration owner + independent `QUALITY_REVIEWER` / QA / Security agent | Integration tests, [`QA_REPORT.md`](../06_TEMPLATES/QA_REPORT.md), and domain quality gates `PASS`. |
| **Wave 4 — Dual Signoff & Delivery** | Final `SA_GATE` technical review, `PM_GATE` business/UX review, checkpoint/changelog reconciliation, and plain-language report. | `SA` + `PM` + Main Orchestrator | Both `SA_GATE = PASS` and `PM_GATE = PASS` (or explicit `PARTIAL` disclosure approved). |

## 3. Critical Path & Shared-Bottleneck Elimination
- **Shared Root Manifests & Barrel Files**
  - Root indexes (`LIBRARY_INDEX.md`, `package.json`, `pyproject.toml`, router registries, migration sequences) are scheduled strictly in **Wave 1** (pre-locked skeleton) or **Wave 3** (post-feature aggregation) under a single owner—never inside concurrent Wave 2 workers.
- **Deterministic Contract Fixtures for Parallel Unblocking**
  - When a frontend, analytics, or valuation stream depends on a backend API or upstream data pipeline, `SA` locks exact JSON schemas or CSV column contracts in Wave 0.
  - Both streams build concurrently against deterministic contract fixtures in Wave 2 and verify live cross-layer integration in Wave 3.

## 4. Blocker, Conflict & Scope Escalation Protocol
When a worker encounters an upstream defect, missing input, environment failure, or contract contradiction:
1. **Never Work Around Contracts Silently**
   - Never mutate files outside Exclusive Write-Locks or invent undocumented schema fields to mask an interface mismatch.
2. **Immediate Structured Escalation**
   - Set affected workstream status to `BLOCKED` (or `PARTIAL` for completed orthogonal items) and notify the orchestrator/`PM` via `send_message` with:
     - Blocking dependency or contract clause ID.
     - Observed empirical error output or failing assertion.
     - Concrete technical options for `SA` resolution.
3. **Controlled DAG Re-Sequencing**
   - `PM` and `SA` update `Section 10: Dependencies & Blockers` in `AGENT_COMMUNICATE.md`, issue a formal Contract Amendment if justified ([`CONTRACT_AND_HANDOFF.md`](./CONTRACT_AND_HANDOFF.md)), and re-dispatch impacted batches cleanly.
4. **Deadlock Prevention**
   - Never allow Wave 2A to wait synchronously on live runtime mutations from concurrent Wave 2B; any live runtime coupling must be split into sequential waves (`Wave N -> Wave N+1`).

## 5. Wave Transition & Checkpoint Readiness Gate
Before advancing from Wave $N$ to Wave $N+1$:
- Verify `100%` of Wave $N$ deliverables exist on disk and pass pre-integration tests.
- Update `PROJECT_STATE.md` (`Checkpoint` and `Research Queue`) and release completed Wave $N$ Exclusive Write-Locks.
- Confirm Wave $N+1$ inputs match actual verified Wave $N$ outputs with zero silent schema drift.
