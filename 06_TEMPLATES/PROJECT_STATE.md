# Cross-Session Project State & Autonomous Continuity Snapshot (`PROJECT_STATE.md`)

> **Template Governance:** Maintained autonomously by `PM` + `SA` per [AUTONOMOUS_ORCHESTRATION.md](../01_ORCHESTRATION/AUTONOMOUS_ORCHESTRATION.md) and [PROJECT_CONTEXT_MANAGEMENT.md](../01_ORCHESTRATION/PROJECT_CONTEXT_MANAGEMENT.md) to guarantee zero-burden continuity across interrupted turns and separate Antigravity sessions. Pair with [PROJECT_MANIFEST.md](./PROJECT_MANIFEST.md) and [AGENT_COMMUNICATE.md](./AGENT_COMMUNICATE.md). Users interact strictly in natural language without operational mode commands.

---

## 1. Execution State
- **Project ID / Name:** `{{PROJECT_ID}}` — `{{PROJECT_NAME}}`
- **Snapshot Version & Timestamp (ISO-8601):** `{{STATE_VERSION}}` (`{{SNAPSHOT_TIMESTAMP_ISO}}`)
- **Last Active Parent Conversation ID:** `{{LAST_PARENT_CONVERSATION_ID}}`
- **Complexity Level & Active Scope:** `{{COMPLEXITY_LEVEL}}` — `{{ACTIVE_BATCH_SCOPE_SUMMARY}}`
- **Active Autonomous Internal Phase (`1`–`13`):** `{{ACTIVE_INTERNAL_PHASE}}`
  *(Selected automatically by `PM` across: `1. Project initialization` | `2. Domain discovery` | `3. Domain mapping` | `4. Role discovery` | `5. Role research` | `6. Competency modeling` | `7. Boundary modeling` | `8. Skill engineering` | `9. Prompt generation` | `10. Quality review` | `11. Integration` | `12. Coverage auditing` | `13. Incremental continuation`)*
- **Runtime Execution Mode:** `{{EXECUTION_MODE}}` (`PARALLEL_SUBAGENT_MESH | INTRA_SESSION_REUSE | SEQUENTIAL_SINGLE_AGENT_FALLBACK`)
- **Overall Health & Gate Readiness:** `{{HEALTH_STATUS}}` (`ON_TRACK | AT_RISK | BLOCKED`) | `SA_GATE = {{SA_GATE_STATUS}}` | `PM_GATE = {{PM_GATE_STATUS}}`

---

## 2. Latest Valid Checkpoint (`Checkpoint` Auto-Resume Pointer)
Enables `PM` to resume seamlessly on any natural-language continuation (e.g., `"Continue where we stopped"`) without re-running verified phases or asking the user to reconstruct prior progress:

- **Checkpoint ID & Timestamp:** `{{CHECKPOINT_ID}}` (`{{CHECKPOINT_TIMESTAMP_ISO}}`)
- **Completed Internal Phases (`1`–`13`):** `{{COMPLETED_INTERNAL_PHASES_LIST}}`
- **Last Independently Verified Batch:** `{{LAST_VERIFIED_BATCH_ID}}` — Verification Command & Exit Status: `{{LAST_BATCH_VERIFY_CMD_AND_RESULT}}`
- **Locked Contracts & Architectural Invariants ([WORKSTREAM_CONTRACT.md](./WORKSTREAM_CONTRACT.md)):** `{{LOCKED_CONTRACT_PATHS_AND_INVARIANTS}}`
- **Exact Next Atomic Resume Step:** `{{EXACT_NEXT_RESUME_BATCH_AND_ACTION}}`
- **Pending Human Approval Gate (Only if Constitutional Trigger Applies):** `{{PENDING_HUMAN_APPROVAL_OR_NONE}}`

---

## 3. Research Queue
Tracks pending domain, role, skill, architectural, implementation, and verification work units managed autonomously in bounded batches by `PM` + `SA`:

| Queue Item ID | Category (`DOMAIN`/`ROLE`/`SKILL`/`ARCH`/`IMPL`/`QA`) | Work Item & Target Deliverable | Priority (`P0`–`P2`) | Upstream Dependency Readiness (`READY`/`WAITING`/`BLOCKED`) | Target Internal Phase & Batch | Status |
| :--- | :---: | :--- | :---: | :--- | :--- | :--- |
| `{{RQ_ID_1}}` | `{{RQ_CAT_1}}` | `{{RQ_ITEM_DESC_1}}` | `{{RQ_PRIO_1}}` | `{{RQ_DEP_READY_1}}` | `{{RQ_PHASE_BATCH_1}}` | `{{RQ_STATUS_1}}` |
| `{{RQ_ID_2}}` | `{{RQ_CAT_2}}` | `{{RQ_ITEM_DESC_2}}` | `{{RQ_PRIO_2}}` | `{{RQ_DEP_READY_2}}` | `{{RQ_PHASE_BATCH_2}}` | `{{RQ_STATUS_2}}` |
| `{{RQ_ID_3}}` | `{{RQ_CAT_3}}` | `{{RQ_ITEM_DESC_3}}` | `{{RQ_PRIO_3}}` | `{{RQ_DEP_READY_3}}` | `{{RQ_PHASE_BATCH_3}}` | `{{RQ_STATUS_3}}` |

---

## 4. Workstream Status & State Reconciliation Notes

### 4.1 Workstream Status Table
| Workstream ID | Assigned Role(s) | Exclusive Write-Lock Scope | Last Verified Handoff | Remaining Batch Slice / Blocker | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `{{WS_ID_1}}` | `{{WS_ROLES_1}}` | `{{WS_LOCK_PATHS_1}}` | `{{WS_HANDOFF_PATH_1}}` | `{{WS_REMAINING_1}}` | `{{WS_STATUS_1}}` |
| `{{WS_ID_2}}` | `{{WS_ROLES_2}}` | `{{WS_LOCK_PATHS_2}}` | `{{WS_HANDOFF_PATH_2}}` | `{{WS_REMAINING_2}}` | `{{WS_STATUS_2}}` |

### 4.2 Automatic `PM + SA` State Reconciliation Notes
Reconciled at every batch boundary without user intervention:
- **Artifact vs. Ledger Parity Check:** `{{DISK_VS_STATE_PARITY_SUMMARY}}` (*If interrupted mid-batch, `PM + SA` inspect on-disk files and `git status` against `Checkpoint` + `AGENT_COMMUNICATE.md`, quarantine or complete partial unverified writes, and advance `Checkpoint` only after verification passes.*)
- **Index, Changelog & Bus Sync Status:** `Indexes = {{INDEX_SYNC_STATUS}}` | `Changelog = {{CHANGELOG_SYNC_STATUS}}` | `AGENT_COMMUNICATE.md = {{BUS_SYNC_STATUS}}`
- **Epistemic Ledger & Active Risks ([RISK_REGISTER.md](./RISK_REGISTER.md)):**
  - Verified Facts: `{{VERIFIED_FACTS_SUMMARY}}`
  - Working Assumptions: `{{ACTIVE_ASSUMPTIONS_SUMMARY}}`
  - `NOT VERIFIED` Items & Top Risks: `{{NOT_VERIFIED_AND_TOP_RISKS}}`

---

## 5. Autonomous Session-Resume Hydration Protocol
Before acting on any follow-up or continuation turn in a new or resumed session:
1. Inspect `PROJECT_MANIFEST.md`, `PROJECT_STATE.md` (`Execution State`, `Latest Valid Checkpoint`, `Research Queue`), and `AGENT_COMMUNICATE.md` silently before spawning agents or editing files.
2. Run `{{BASELINE_VERIFICATION_COMMAND}}` via `run_command` to reconcile actual disk state against `{{CHECKPOINT_ID}}`.
3. Reuse active `PM`/`SA` `conversationId` handles via `send_message` when in-session, re-bind new `PM`/`SA` subagents when starting a new session, or execute via sequential single-agent fallback if subagents are unavailable.
4. Continue automatically from `{{EXACT_NEXT_RESUME_BATCH_AND_ACTION}}` and report outcomes in concise ordinary language.
