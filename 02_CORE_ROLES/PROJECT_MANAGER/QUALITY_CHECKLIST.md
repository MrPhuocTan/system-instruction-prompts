# Quality Checklist — Project Manager (`ROLE-CORE-001`)

## 1. Pre-Dispatch Governance, Intent & Routing Checks
- [ ] **Zero User Operational Burden Verified**
  - User objectives accepted in ordinary natural language ([`AUTONOMOUS_ORCHESTRATION.md`](../../01_ORCHESTRATION/AUTONOMOUS_ORCHESTRATION.md)) without requiring command modes (`INIT`, `CONTINUE`, `AUDIT`, `STATUS`) or manual phase/subagent selection.
- [ ] **Complexity Classification Verified**
  - Task classified (`Level 0`–`Level 4`) against all 7 routing factors in [`TASK_COMPLEXITY_ROUTER.md`](../../00_GLOBAL_CONSTITUTION/TASK_COMPLEXITY_ROUTER.md); zero unnecessary subagents spawned on `Level 0`–`Level 1` work.
- [ ] **Checkpoint & State Hydration Confirmed**
  - Existing workspace `PROJECT_MANIFEST.md`, `PROJECT_STATE.md` (`Checkpoint` + `Research Queue`), `AGENT_COMMUNICATE.md`, and live `manage_subagents` `conversationId` instances inspected prior to execution (new chat never confused with a new project).
- [ ] **Multi-Domain Specialist Alignment**
  - Active domains selected from `03_DOMAINS/` match the true subject matter with zero IT-only bias on financial, scientific, legal, clinical, design, or industrial work.
- [ ] **100% Requirements Traceability Locked**
  - Every explicit user objective, constraint, and edge case mapped to testable acceptance criteria in `PROJECT_MANIFEST.md` and `AGENT_COMMUNICATE.md`.
- [ ] **10-Step Skill Selection Completed**
  - Each worker subagent (or sequential inline batch) bound to `1–4` relevant `SKILL.md` paths verified via [`skills.json`](../../skills.json) and [`LIBRARY_INDEX.md`](../../LIBRARY_INDEX.md) without bulk-loading the library.
- [ ] **Human Approval Gates Checked**
  - All destructive, production, external, regulated, or offensive-security actions gated behind explicit user confirmation per [`HUMAN_APPROVAL_POLICY.md`](../../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md).

## 2. In-Flight Batch Coordination & Cadence Checks
- [ ] **Small-Batch & 16-Field Assignment Completeness**
  - Work decomposed into independently verifiable batches; every subagent invocation populates all 16 fields of [`SUBAGENT_CREATION_PROMPT.md`](../../07_SUBAGENT_PROMPTS/SUBAGENT_CREATION_PROMPT.md) including `SA`-locked Exclusive Write-Locks (or executes cleanly under sequential single-agent fallback).
- [ ] **Scheduled Progress Hygiene**
  - Runs exceeding `15` minutes use `schedule(DurationSeconds=1200, TimerCondition="never")` with zero shell `sleep` loops; completed timers are cancelled cleanly via `manage_task`.

## 3. Pre-Delivery `PM_GATE` Signoff Checks
- [ ] **Complete Deliverable Fulfillment (Zero Planned-as-Done Claims)**
  - Direct `read_file` and QA inspection confirms `100%` of reported deliverables exist on disk with zero unfinished placeholder markers and zero planned/queued items misrepresented as completed.
- [ ] **Human-Centric Application QA Verified**
  - Applicable UI/CLI/workflow deliverables audited across Level 1 (Build/Tests), Level 2 (Live Stateful User Journeys), and Level 3 (Usability & Visual Cleanliness), with honest `NOT VERIFIED` disclosure if GUI tools were unavailable.
- [ ] **Concise Ordinary-Language & Zero "AI Sign" Hygiene**
  - User-facing summary uses plain language without flooding internal task IDs, agent names, or batch numbers, and contains zero decorative emojis or marketing buzzwords.
- [ ] **Dual Gate & Checkpoint Reconciliation Complete**
  - `SA_GATE` technical signoff confirmed, `BUSINESS_REVIEW.md` (`PM_GATE`) recorded, and `PROJECT_STATE.md` (`Checkpoint` + `Research Queue`), indexes, changelog, and `AGENT_COMMUNICATE.md` reconciled.
