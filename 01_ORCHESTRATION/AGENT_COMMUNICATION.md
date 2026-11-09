# Inter-Agent Communication Bus & Reactive Messaging

## 1. Dual-Channel Communication Architecture
Multi-agent coordination combines **live asynchronous runtime messaging** within an active session and **durable disk-backed state logging** across turns and sessions ([`PERSISTENT_PM_SA.md`](./PERSISTENT_PM_SA.md)):

1. **Live Session Messaging Channel (`send_message`)**
   - Point-to-point message delivery (`send_message(Recipient=<conversationId>, Message=...)`) between parent orchestrator, `PM`, `SA`, `DOMAIN_LEAD`, `QUALITY_REVIEWER`, and worker subagents.
   - Used to dispatch 16-field assignments ([`SUBAGENT_CREATION.md`](./SUBAGENT_CREATION.md)), resolve mid-flight clarifications, and transmit structured worker handoffs back to callers.
2. **Durable Shared Communication Bus (`AGENT_COMMUNICATE.md`)**
   - Instantiated in target workspaces (`Level 2`–`Level 4`) from canonical template [`AGENT_COMMUNICATE.md`](../06_TEMPLATES/AGENT_COMMUNICATE.md).
   - Preserves all **15 mandatory governance sections**:
     1. `Project Identity`
     2. `Mission & Objectives`
     3. `PM & SA Ownership`
     4. `Current Project Status`
     5. `Acceptance Criteria`
     6. `Worker Registry`
     7. `Workstream Ownership`
     8. `File Ownership`
     9. `Decisions & Rationale`
     10. `Dependencies & Blockers`
     11. `Event & Handoff Log`
     12. `Technical Signoff`
     13. `Business/UX Signoff`
     14. `Outstanding Issues`
     15. `Next Actions`

## 2. Single-Writer Bus Hygiene (Preventing `AGENT_COMMUNICATE.md` Races)
Because `AGENT_COMMUNICATE.md` is itself a workspace file subject to host filesystem writes ([`FILE_OWNERSHIP_AND_LOCKING.md`](./FILE_OWNERSHIP_AND_LOCKING.md)), parallel workers must **never** overwrite `AGENT_COMMUNICATE.md` concurrently:
- **Centralized Bus Coordinator**
  - During parallel waves, the main orchestrator (or designated `PM` coordinator) owns direct writes to `AGENT_COMMUNICATE.md`.
- **Per-Stream Handoff Artifacts**
  - Parallel worker subagents write detailed verification evidence to their own exclusive handoff path (e.g., `configs/handoffs/<stream_id>.md` or `reports/handoff_<stream_id>.md` structured per [`HANDOFF_REPORT.md`](../06_TEMPLATES/HANDOFF_REPORT.md)) and transmit the concise summary to their caller via `send_message`.
  - The coordinator then merges verified entries into `AGENT_COMMUNICATE.md` atomically.

## 3. Reactive Wakeup & Strict Ban on Polling Loops
Antigravity delivers subagent messages and background-task completion notifications **reactively**:
1. **Zero Busy-Wait Polling**
   - After launching parallel subagents (`invoke_subagent`) or messaging active workers (`send_message`), if no independent foreground work remains, end the turn cleanly by calling no more tools.
   - The runtime automatically wakes the caller agent as soon as a subagent sends a message or finishes execution.
2. **Absolute Ban on Shell `sleep` Waiting**
   - Never invoke `run_command` with `sleep 10`, `sleep 60`, or loop-polling scripts to wait for subagents or background tasks ([`TOOL_USAGE_AND_LIMITATIONS.md`](../00_GLOBAL_CONSTITUTION/TOOL_USAGE_AND_LIMITATIONS.md)).
   - For periodic `> 15`-minute progress updates, use exclusively `schedule` ([`PROGRESS_REPORTING.md`](./PROGRESS_REPORTING.md)).

## 4. Mandatory Subagent Return Protocol
Text generated privately by a subagent outside `send_message` is **not** relayed to its caller:
- Every subagent (`PM`, `SA`, `DOMAIN_LEAD`, `QUALITY_REVIEWER`, or specialist worker) **must** call `send_message(Recipient=<caller_conversationId>, Message=...)` before ending its turn.
- Every completion message follows a crisp five-part structure:
  1. `Workstream / Gate ID & Canonical Status` (`PASS | PARTIAL | BLOCKED | FAILED | NOT VERIFIED`)
  2. `Deliverables & Exact Absolute File Paths Created/Modified`
  3. `Contract & Exclusive Write-Lock Compliance Confirmation`
  4. `Executed Verification Commands & Observed Results`
  5. `Blockers, Assumptions, Unverified Items & Handoff File Path`

## 5. Confidentiality & Redaction on the Bus
All `AGENT_COMMUNICATE.md` entries and `send_message` payloads obey [`SECURITY_AND_PRIVACY.md`](../00_GLOBAL_CONSTITUTION/SECURITY_AND_PRIVACY.md): never record raw API keys, bearer tokens, private keys, database passwords, session cookies, or unmasked `PII`/`PHI` inside inter-agent logs.
