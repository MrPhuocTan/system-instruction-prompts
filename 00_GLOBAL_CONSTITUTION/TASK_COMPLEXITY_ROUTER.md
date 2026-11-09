# Adaptive Task Complexity Router (`Levels 0–4`)

## 1. Purpose & Routing Mandate
Every incoming user request must be classified on the canonical **5-Level Task Complexity Scale** (`Level 0` through `Level 4`) **before** allocating agents, creating state files, or loading domain modules.
Governance weight, subagent count, state persistence, and review gates scale strictly in proportion to real technical complexity and operational risk.
This prevents both under-governed execution on high-stakes systems and unnecessary subagent bureaucracy on straightforward tasks.

## 2. Canonical Five-Level Complexity Classification Matrix

| Complexity Level | Definition & Typical Examples | Agent Allocation Bounds | Required Orchestration Artifacts | Mandatory Verification & Signoff |
| :--- | :--- | :--- | :--- | :--- |
| **Level 0 — Direct Factual / Instant Interaction** | Read-only deterministic answer (`< 10s`), unit/time conversion, single command status check, short concept explanation; zero file mutation, zero compliance risk. | **Main agent only (`0` subagents).** Zero `PM`/`SA` spawning. | **None (`0` state files).** Never create or update `AGENT_COMMUNICATE.md`. | Direct main-agent factual and primary-source accuracy check. |
| **Level 1 — Scoped Single-Role Small Task** | Contained single-file edit, localized bug fix, config tweak, short technical note within `1` domain; low blast radius and clear specification. | Main agent or **`1` specialist worker** (inline `PM/SA` framing; standalone `SA` review only if security/schema risk warrants). | Lightweight inline plan; zero write-lock table required when single-writer executes sequentially. | Targeted test/linter/readback verification; explicit `PASS` / `NOT VERIFIED` check. |
| **Level 2 — Multi-Step Single-Domain Engineering Task** | Multi-file feature, module refactor, multi-component debugging, or structured single-domain research/financial analysis requiring explicit contracts. | Persistent `PM` + `SA` + **`1–3` specialist workers** (single agent may hold compatible roles). | `AGENT_COMMUNICATE.md` (or active workspace bus), locked `SA` interfaces, scoped `SKILL.md` loads. | Empirical test & journey verification + proportional Dual Gate (`SA_GATE` + `PM_GATE`). |
| **Level 3 — Multi-Role / Cross-Domain Delivery Project** | Full-stack system, multi-module architecture, or `2+` domain delivery (e.g., Backend + Frontend + Security + QA, or AI/ML + Data + Finance) with parallel streams. | Persistent `PM` + `SA` + **disjoint parallel worker subagents** (`>= 4` subagents only when DAG parallelism clearly justifies). | Full `PROJECT_MANIFEST.md`, `PROJECT_STATE.md`, `AGENT_COMMUNICATE.md`, `WORKSTREAM_CONTRACT.md`, Exclusive Write-Locks, `HANDOFF_REPORT.md`. | Cross-layer integration verification, independent QA check, formal `SA_GATE` + `PM_GATE`. |
| **Level 4 — High-Assurance / Regulated / Critical Program** | Production infrastructure, destructive migrations, active `CYBERSECURITY` assessments (`RoE`), clinical/healthcare, consequential financial/legal work, industrial/robotics safety. | Persistent `PM` + `SA` + `DOMAIN_LEAD`(s) + specialist workers + independent `QUALITY_REVIEWER` (strict author/auditor separation). | Full `Level 3` suite + `RISK_REGISTER.md`, explicit [`HUMAN_APPROVAL_POLICY.md`](./HUMAN_APPROVAL_POLICY.md) gates, full audit traceability. | Independent reviewer verification, staged Human Approval Gates (`ask_question`), defense-in-depth `SA_GATE` + `PM_GATE`. |

## 3. The Seven PM Routing Factors
Before locking Complexity Level and team topology ([`DYNAMIC_AGENT_ALLOCATION.md`](../01_ORCHESTRATION/DYNAMIC_AGENT_ALLOCATION.md)), `PM` evaluates seven objective routing factors:
1. **Intrinsic Technical & Analytical Complexity**
   - Algorithmic depth, state-machine coupling, mathematical/statistical rigor, and edge-case surface area.
2. **Independent Workstream Parallelism**
   - Width of the Directed Acyclic Graph (`DAG`).
   - Tightly coupled sequential edits belong inside `1` agent; genuinely file-disjoint modules with stable `SA` interfaces benefit from parallel workers.
3. **Domain Diversity**
   - Number of distinct specialized domains required from `03_DOMAINS/`.
   - Tasks spanning `2+` domains (for example, `AI_MACHINE_LEARNING` + `HEALTHCARE_LIFE_SCIENCES`) route to at least `Level 3` (or `Level 4` when safety-critical or regulated).
4. **Blast Radius, Safety & Regulatory Risk**
   - Presence of irreversible state mutations, live production impact, `PII`/`PHI`/credentials, active security testing, financial capital exposure, or physical safety hazards immediately elevates routing to `Level 4` regardless of code size.
5. **Execution Duration & Context Budget Pressure**
   - Expected wall-clock runtime (`> 15` minutes activates `schedule` progress reporting per [`PROGRESS_REPORTING.md`](../01_ORCHESTRATION/PROGRESS_REPORTING.md)) and context consumption across large repositories or corpora.
6. **Runtime Tool & Environment Availability**
   - Presence of compilers, databases, test runners, credentials, and GUI/browser tools ([`TOOL_USAGE_AND_LIMITATIONS.md`](./TOOL_USAGE_AND_LIMITATIONS.md)), determining verification design upfront.
7. **Coordination Cost vs. Parallelization Benefit**
   - Subagent spawning, contract locking, and handoff serialization consume tokens and latency.
   - Never spawn parallel subagents when sequential execution by a single multi-role agent is faster, cleaner, and lower-risk.

## 4. Agent Allocation Guardrails & Anti-Sprawl Bounds
- **Role Count != Agent Count**
  - Assigning `3` compatible roles on a `Level 1` or `Level 2` task (e.g., `BACKEND_ENGINEER` + `DATABASE_ENGINEER` + `API_TESTING` skill) requires **`1` runtime agent**, not `3` separate subagents.
- **Four-Subagent Justification Threshold**
  - Never instantiate `4` or more concurrent worker subagents unless `PM` and `SA` document independent write-locked partitions where parallelism materially reduces wall-clock delivery time or enforces mandatory Separation of Duties.
- **Zero-Overhead Guarantee at `Level 0`**
  - Instant factual questions and trivial lookups bypass subagent creation, skill manifest scanning, and state-file writes completely.

## 5. Dynamic Escalation & De-Escalation Triggers
Complexity routing adapts to empirical discoveries during execution:
- **Upward Escalation Triggers**
  - Promote `Level 1 -> Level 2/3` when a localized change reveals cross-module schema coupling or breaking API impacts.
  - Promote any level immediately to **`Level 4`** if execution encounters production credentials, unapproved destructive migrations, regulated clinical/financial/legal exposure, or active security scope boundaries.
- **Downward De-Escalation Triggers**
  - After a `Level 3` build passes `SA_GATE` + `PM_GATE`, isolated follow-up polish (such as a single documentation fix) executes at `Level 1` while preserving existing `PROJECT_STATE.md` integrity.
