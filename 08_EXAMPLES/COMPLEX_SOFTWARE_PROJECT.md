# End-to-End Walkthrough: Level 3 Multi-Workstream Software Build (`COMPLEX_SOFTWARE_PROJECT.md`)

> **Walkthrough Governance:** Demonstrates **Complexity Level 3** microservice subagent orchestration, 10-step skill discovery from [LIBRARY_INDEX.md](../LIBRARY_INDEX.md) and [skills.json](../skills.json), disjoint Exclusive Write-Locks, 3-Level Human-Centric QA, and persistent `PM + SA` dual sign-off.

---

## 1. Realistic User Scenario
**User Prompt:**
> "Build a multi-tenant B2B Purchase Order & Inventory Approval web application (PostgreSQL + FastAPI backend + React/TypeScript frontend). Buyers draft POs against supplier SKU catalogs, Approvers approve/reject POs over $5,000 with budget reservation locking, and Finance exports reconciled CSV ledgers."

---

## 2. Persistent `PM + SA` Initialization & 10-Step Skill Discovery
1. **Complexity Routing ([TASK_COMPLEXITY_ROUTER.md](../00_GLOBAL_CONSTITUTION/TASK_COMPLEXITY_ROUTER.md)):** Classified as **Level 3** (multi-module full-stack build across database, backend API, frontend UI, and end-to-end QA).
2. **Persistent Governance Instantiation ([PERSISTENT_PM_SA.md](../01_ORCHESTRATION/PERSISTENT_PM_SA.md)):**
   - Main orchestrator initializes [PROJECT_MANIFEST.md](../06_TEMPLATES/PROJECT_MANIFEST.md), [PROJECT_STATE.md](../06_TEMPLATES/PROJECT_STATE.md), and [AGENT_COMMUNICATE.md](../06_TEMPLATES/AGENT_COMMUNICATE.md) inside the target workspace `configs/` directory, spawning `pm-agent` ([PROJECT_MANAGER](../02_CORE_ROLES/PROJECT_MANAGER/SYSTEM_PROMPT.md)) and `sa-agent` ([SYSTEM_ARCHITECT](../02_CORE_ROLES/SYSTEM_ARCHITECT/SYSTEM_PROMPT.md)) once and reusing their `conversationId`s via `send_message` across all phases.
3. **10-Step Skill Discovery ([SKILL_DISCOVERY_AND_LOADING](../05_SPECIALIZED_SKILLS/SKILL_DISCOVERY_AND_LOADING/SKILL.md)):**
   - `PM + SA` query [LIBRARY_INDEX.md](../LIBRARY_INDEX.md) and [skills.json](../skills.json), selecting only task-relevant skills within token budgets:
     - `ws-db`: [DATABASE_VALIDATION](../05_SPECIALIZED_SKILLS/DATABASE_VALIDATION/SKILL.md), [COGNITIVE_EXECUTION](../04_CROSS_DOMAIN_SKILLS/COGNITIVE_EXECUTION/SKILL.md)
     - `ws-api`: [API_TESTING](../05_SPECIALIZED_SKILLS/API_TESTING/SKILL.md), [COGNITIVE_EXECUTION](../04_CROSS_DOMAIN_SKILLS/COGNITIVE_EXECUTION/SKILL.md)
     - `ws-ui`: [TECHNICAL_WRITING](../04_CROSS_DOMAIN_SKILLS/TECHNICAL_WRITING/SKILL.md), [COGNITIVE_EXECUTION](../04_CROSS_DOMAIN_SKILLS/COGNITIVE_EXECUTION/SKILL.md)
     - `ws-qa`: [HUMAN_CENTRIC_APPLICATION_QA](../05_SPECIALIZED_SKILLS/HUMAN_CENTRIC_APPLICATION_QA/SKILL.md), [BROWSER_AND_GUI_INTERACTION](../05_SPECIALIZED_SKILLS/BROWSER_AND_GUI_INTERACTION/SKILL.md), [API_TESTING](../05_SPECIALIZED_SKILLS/API_TESTING/SKILL.md), [DATABASE_VALIDATION](../05_SPECIALIZED_SKILLS/DATABASE_VALIDATION/SKILL.md)

---

## 3. Upfront SA Contract Lock & Disjoint Exclusive Write-Locks
Before spawning implementation workers via [SUBAGENT_CREATION_PROMPT.md](../07_SUBAGENT_PROMPTS/SUBAGENT_CREATION_PROMPT.md), `SA` locks `contracts/openapi_po_v1.yaml` and PostgreSQL Row-Level Security (`RLS`) policies in [WORKSTREAM_CONTRACT.md](../06_TEMPLATES/WORKSTREAM_CONTRACT.md) with zero overlapping file locks:

| Workstream | Runtime Agent | Bound Library Role(s) | Exclusive Owned Paths (`Write-Lock`) | Dependency Order |
| :--- | :--- | :--- | :--- | :--- |
| `ws-db` | `worker-db` | [DATABASE_ENGINEER](../03_DOMAINS/IT_SOFTWARE/ROLES/DATABASE_ENGINEER/SYSTEM_PROMPT.md) | `db/migrations/**`, `db/seeds/**`, `configs/handoffs/ws_db.md` | Wave 1 |
| `ws-api` | `worker-api` | [BACKEND_ENGINEER](../03_DOMAINS/IT_SOFTWARE/ROLES/BACKEND_ENGINEER/SYSTEM_PROMPT.md) | `services/api/**`, `tests/api/**`, `configs/handoffs/ws_api.md` | Wave 2 (after `ws-db` schema lock) |
| `ws-ui` | `worker-ui` | [FRONTEND_ENGINEER](../03_DOMAINS/IT_SOFTWARE/ROLES/FRONTEND_ENGINEER/SYSTEM_PROMPT.md) + [UI_DESIGNER](../03_DOMAINS/DESIGN_CREATIVE/ROLES/UI_DESIGNER/SYSTEM_PROMPT.md) | `apps/web/**`, `configs/handoffs/ws_ui.md` | Wave 2 (parallel against `openapi_po_v1.yaml`) |
| `ws-qa` | `worker-qa` | [QA_ENGINEER](../03_DOMAINS/IT_SOFTWARE/ROLES/QA_ENGINEER/SYSTEM_PROMPT.md) + [AUTOMATION_QA](../03_DOMAINS/IT_SOFTWARE/ROLES/AUTOMATION_QA/SYSTEM_PROMPT.md) | `tests/e2e/**`, `configs/QA_REPORT.md`, `configs/handoffs/ws_qa.md` | Wave 3 (independent non-author) |

---

## 4. Parallel Execution, Blocker Escalation & Reuse
- **Mid-Stream Interface Escalation (Zero Silent Drift):** While implementing CSV ledger export, `worker-ui` notices decimal currency precision (`NUMERIC(14,4)`) requires string serialization in JSON (`"total_amount": "5420.5000"`) rather than IEEE-754 floats. Instead of patching `services/api/**` across write-locks, `worker-ui` escalates via `send_message` to `sa-agent`. `SA` amends `contracts/openapi_po_v1.yaml` and messages `worker-api` (`send_message` reuse) to serialize decimals as exact strings.
- **Utilitarian UI Execution:** `worker-ui` delivers dense tabular PO queues, keyboard-accessible approval modals, explicit loading skeletons, empty-catalog states, inline field validation errors, and **zero decorative `"AI Sign"` emojis or marketing banners**.

---

## 5. Independent 3-Level Human-Centric QA (`QA_REPORT.md`)
Invoked via [QA_AGENT_PROMPT.md](../07_SUBAGENT_PROMPTS/QA_AGENT_PROMPT.md), `worker-qa` executes [QA_REPORT.md](../06_TEMPLATES/QA_REPORT.md):
- **GUI Tool Disclosure:** Playwright + headless Chromium browser automation + `read_file` screenshot inspection **AVAILABLE** and executed across desktop (`1440x900`) and mobile (`390x844`) viewports.

| QA Level | Verification Scenario | Stimulus / Journey Executed | Observed Cross-Layer Outcome | Tier / Verdict |
| :--- | :--- | :--- | :--- | :---: |
| **Level 1 (Code)** | Static types, lint, unit & OpenAPI schema | `mypy --strict`, `pytest tests/api`, `pnpm tsc --noEmit` | `0` errors; `100%` OpenAPI schema parity | `PASS` |
| **Level 2 (System)** | Concurrent double-approval race on `#PO-1042` (`$6,200` vs `$10,000` budget) | Simultaneous POST `/v1/pos/1042/approve` from two Approver sessions | PostgreSQL `SELECT ... FOR UPDATE` deducts `$6,200` once (`$3,800` left); second call gets `HTTP 409` | `PASS` |
| **Level 2 (Security)** | Cross-tenant horizontal isolation probe | Authenticated `tenant_b` JWT querying `GET /v1/pos/1042` (`tenant_a`) | PostgreSQL `RLS` + query filter return `HTTP 404`; audit event written | `PASS` |
| **Level 3 (User UX)** | Buyer draft -> `$5k+` routing -> Reject -> Edit -> Approve -> CSV export | Real browser clicks, form inputs, modal keyboard focus, CSV file download | CSV total reconciles to cent (`5420.5000`); loading/empty/error states clean; zero `"AI Sign"` | `Tier 3 (PASS)` |

---

## 6. Cross-Session Persistence & Progress Cadence Hygiene
- Because full-stack build + E2E Playwright execution ran `24 minutes`, `pm-agent` registered `schedule(DurationSeconds=1200, TimerCondition="never")`, delivered one factual 20-minute milestone update after Wave 2 completed, and cancelled the schedule via `manage_task(Action="kill", ...)` prior to final delivery.
- Updated `configs/PROJECT_STATE.md` so any follow-on session hydrates locked `RLS` invariants and `openapi_po_v1.yaml` contracts without re-discovery.

---

## 7. Dual Signoff (`SA_GATE` + `PM_GATE`)
- **`SA_GATE = PASS` ([TECHNICAL_REVIEW.md](../06_TEMPLATES/TECHNICAL_REVIEW.md)):** `sa-agent` independently verified `git diff` write-lock isolation across all 4 workstreams, PostgreSQL `RLS` enforcement, transactional budget locking, and clean container teardown.
- **`PM_GATE = PASS` ([BUSINESS_REVIEW.md](../06_TEMPLATES/BUSINESS_REVIEW.md)):** `pm-agent` confirmed `100%` Buyer/Approver/Finance requirement completion and zero `"AI Sign"` clutter, issuing the 6-part [FINAL_DELIVERY.md](../06_TEMPLATES/FINAL_DELIVERY.md).
