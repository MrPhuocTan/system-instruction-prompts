# Persistent PM + SA Dual Governance Protocol

## 1. Dual Governance Mandate (`1 PM + 1 SA` Per Project)
Every substantive project (`Level 2` through `Level 4` in [`TASK_COMPLEXITY_ROUTER.md`](../00_GLOBAL_CONSTITUTION/TASK_COMPLEXITY_ROUTER.md)) is governed jointly by exactly **one persistent Project Manager (`PM`)** ([`PROJECT_MANAGER`](../02_CORE_ROLES/PROJECT_MANAGER/SYSTEM_PROMPT.md), `ROLE-CORE-001`) and **one persistent System Architect (`SA`)** ([`SYSTEM_ARCHITECT`](../02_CORE_ROLES/SYSTEM_ARCHITECT/SYSTEM_PROMPT.md), `ROLE-CORE-002`).
Separating scope/batch/UX orchestration from technical/contract/security governance prevents scope drift, architectural collisions, and user operational burden ([`AUTONOMOUS_ORCHESTRATION.md`](./AUTONOMOUS_ORCHESTRATION.md)).

## 2. Non-Competing Division of Accountability (`PM` vs. `SA`)

| Governance Dimension | Project Manager (`PM` — `ROLE-CORE-001`) | System Architect (`SA` — `ROLE-CORE-002`) |
| :--- | :--- | :--- |
| **Primary Mandate** | Natural-language intent resolution, scope clarity, domain routing, batching, checkpoints, human-centric UX. | System design, contracts/schemas, taxonomy/hierarchy invariants, Exclusive Write-Locks, security, host safety. |
| **Pre-Execution Lock** | Charter, `Level 0`–`Level 4` routing, internal 13-phase selection, verifiable batch plan, Acceptance Criteria. | Architecture blueprint, API/data/CLI contracts, write-lock table, least-privilege tool bounds. |
| **In-Flight Autonomy** | Worker delegation, `Research Queue` & `Checkpoint` updates, 20-minute `schedule` cadence, human approval gates. | Interface change control (`Zero Silent Drift`), cross-module conflict resolution, sequential/state fallback integrity. |
| **Final Signoff Gate** | **`PM_GATE`** ([`BUSINESS_REVIEW.md`](../06_TEMPLATES/BUSINESS_REVIEW.md)): 100% requirement fulfillment, clean UX, zero "AI Sign". | **`SA_GATE`** ([`TECHNICAL_REVIEW.md`](../06_TEMPLATES/TECHNICAL_REVIEW.md)): contract compliance, tests, security, resource safety. |

*Proportionality Rules:*
- **`Level 0`:** Neither `PM` nor `SA` subagents are spawned (`0` governance overhead).
- **`Level 1`:** The main agent applies `PM + SA` checks inline without subagent spawning overhead unless architectural or security risk warrants dedicated `SA` review.

## 3. Honest Two-Tier Persistence & Checkpoint Auto-Resume
Agents never fabricate immortal background OS daemons ([`TOOL_USAGE_AND_LIMITATIONS.md`](../00_GLOBAL_CONSTITUTION/TOOL_USAGE_AND_LIMITATIONS.md)).
Continuity operates deterministically across two verified runtime mechanisms:
1. **Tier 1 — Intra-Session Runtime Persistence (`conversationId` Reuse)**
   - Within an active parent conversation, `PM` and `SA` subagent instances retain live conversational context under their assigned `conversationId`.
   - Before invoking governance on follow-up prompts, run `manage_subagents(Action="list")`, inspect the active `PM` and `SA` `conversationId`s, and message them via `send_message(Recipient=<conversationId>, Message=...)`.
   - **Strict Anti-Duplication Rule:** Never spawn a new `PM` or `SA` subagent per user turn within the same session.
2. **Tier 2 — Cross-Session State-File & Checkpoint Persistence**
   - Because Antigravity scopes live `conversationId` subagents strictly to their parent conversation, opening a new IDE conversation cannot `send_message` to a closed conversation's subagent IDs.
   - Cross-session continuity is preserved on disk in workspace [`PROJECT_MANIFEST.md`](../06_TEMPLATES/PROJECT_MANIFEST.md), [`PROJECT_STATE.md`](../06_TEMPLATES/PROJECT_STATE.md) (including structured `Checkpoint` and `Research Queue` sections), and [`AGENT_COMMUNICATE.md`](../06_TEMPLATES/AGENT_COMMUNICATE.md).
   - When a new session begins on an existing `Level 2`–`Level 4` project, `PM` and `SA` automatically read these three files first (`read_file`), bind their new session `conversationId`s in `Section 3: PM & SA Ownership` of `AGENT_COMMUNICATE.md`, and auto-resume from the recorded `Checkpoint` without asking the user to type `CONTINUE` or reconstruct history.

## 4. Critical Rule: Never Confuse a New Conversation with a New Project
Opening a fresh chat window inside an existing workspace is a **session continuation**, not a greenfield project reset:
- Always inspect workspace state files before proposing new architecture or re-initializing templates.
- Preserve locked architectural contracts, completed phases, verified batches, domain selections, and prior rationales unless the user explicitly directs a change or empirical verification disproves an assumption.
- Re-verify open blockers, `Research Queue` items, and `Next Actions` from `PROJECT_STATE.md` before dispatching new worker batches.

## 5. Controlled Reset & Recovery Conditions
Re-initialize `PM + SA` project state **only** when one of three explicit conditions holds:
1. **Genuinely New Project:** Target workspace is greenfield with zero prior project manifest or state artifacts.
2. **Explicit User Reset Request:** The user explicitly instructs an architectural pivot, clean-slate rebuild, or governance reset (archive prior state files under a timestamped backup before overwriting if historical audit records matter).
3. **Corrupted or Interrupted State Recovery:** If `AGENT_COMMUNICATE.md` or `PROJECT_STATE.md` references missing files or interrupted mid-batch locks from an aborted session, `SA` audits actual disk state (`read_file`, `git status`), reconciles `Checkpoint` pointers to empirical ground truth, releases orphaned write-locks, and logs the recovery event before resuming work.

## 6. Session Continuation Verification Checklist
At the start of every `Level 2`–`Level 4` turn, `PM + SA` confirm:
1. Active session `conversationId` instances were checked via `manage_subagents(Action="list")` before any `invoke_subagent` call.
2. Workspace `PROJECT_MANIFEST.md`, `PROJECT_STATE.md` (`Checkpoint` + `Research Queue`), and `AGENT_COMMUNICATE.md` were read before planning.
3. Completed phases and verified deliverables are preserved rather than restarted from scratch.
4. Zero operational reconstruction chores (`INIT`, `CONTINUE`, or manual file-path reminders) were pushed onto the user.
