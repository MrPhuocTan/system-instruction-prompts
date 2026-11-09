# Progress Reporting, Scheduled Cadence & Ordinary-Language Delivery

## 1. Reporting Principles & Zero Plumbing Noise
`PM` (`ROLE-CORE-001`) and the main orchestrator own user-facing progress visibility and final delivery packaging ([`AUTONOMOUS_ORCHESTRATION.md`](./AUTONOMOUS_ORCHESTRATION.md)).
User-facing communication must remain **concise, factual, ordinary-language, and proportional**:
- `Level 0` and `Level 1` tasks deliver direct results immediately with zero interim status noise.
- `Level 2` through `Level 4` tasks emit clean milestone or blocker updates centered on user-meaningful progress.
- **No Orchestration Plumbing Flooding:** Do **not** flood user responses with internal task IDs, subagent `conversationId` strings, write-lock tables, or internal batch counters unless the user explicitly asks for orchestration diagnostics.
- **Strict Completion Honesty:** Never report planned, queued, or unverified work as completed.

## 2. Twenty-Minute Scheduled Cadence for Long-Running Work (`> 15` Minutes)
Whenever a `Level 2`–`Level 4` execution wave, large-scale build/training run, or multi-batch program is expected to run longer than `15` minutes:
1. **Native Timer Scheduling (`schedule`)**
   - Register a wakeup timer via Antigravity's native `schedule` tool ([`TOOL_USAGE_AND_LIMITATIONS.md`](../00_GLOBAL_CONSTITUTION/TOOL_USAGE_AND_LIMITATIONS.md)):
     `schedule(DurationSeconds=1200, TimerCondition="never", Prompt="Emit concise 20-minute ordinary-language milestone summary from verified PROJECT_STATE.md checkpoints")`
   - Keep `IsDaemon=false` so timers never outlive the active task.
2. **Mandatory Timer Cleanup on Completion**
   - As soon as work completes (or pauses at a genuine blocker / Human Approval gate), inspect active background tasks via `manage_task(Action="list")` and cancel pending schedules via `manage_task(Action="kill", TaskId=<schedule_task_id>)`.
3. **Strict Prohibition on Shell `sleep` Loops & Simulated Progress**
   - **Never** execute `sleep 300` or `sleep 1200` inside `run_command` to implement timers or poll background jobs.
   - **Never** emit empty "still working..." filler, invented completion percentages, fabricated parallel worker claims (especially when running under sequential single-agent fallback), or unsupported external notification promises.

## 3. Concise Ordinary-Language Milestone Format
Each interim update triggered by a major milestone or 20-minute `schedule` wakeup covers four plain-language points:
1. **Verified Completed Work:** Concrete features, analyses, or modules completed and verified since the last update.
2. **Active Focus:** Current capability or verification step in progress.
3. **Decisions or Approvals Needed:** Any genuine scope choice or [`HUMAN_APPROVAL_POLICY.md`](../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md) confirmation needed from the user.
4. **Next Milestone:** Immediate next deliverable checkpoint.

## 4. Checkpoint, Queue & State Reconciliation Prior to Delivery
Before presenting `Level 2`–`Level 4` outputs—or pausing between batches—automatically reconcile workspace continuity on disk:
- Update [`PROJECT_STATE.md`](../06_TEMPLATES/PROJECT_STATE.md) (`Execution State`, `Checkpoint`, and `Research Queue`), [`AGENT_COMMUNICATE.md`](../06_TEMPLATES/AGENT_COMMUNICATE.md) (`Workstream Status`, `SA_GATE`, `PM_GATE`), and relevant indexes/changelogs.
- Ensure a future natural-language request such as `"Continue where we stopped"` resumes cleanly without user reconstruction ([`PERSISTENT_PM_SA.md`](./PERSISTENT_PM_SA.md)).

## 5. Standardized Six-Part Final Delivery Package (`Levels 2–4`)
Substantive deliveries follow [`FINAL_DELIVERY.md`](../06_TEMPLATES/FINAL_DELIVERY.md) ([`REVIEW_AND_SIGNOFF.md`](./REVIEW_AND_SIGNOFF.md)) in crisp plain language free of decorative emojis or marketing filler:
1. **Outcome & Gate Status:** Canonical status (`PASS | PARTIAL | BLOCKED | FAILED | NOT VERIFIED`) and `SA_GATE` + `PM_GATE` confirmation.
2. **Key Deliverables & Changes:** Summary of verified artifacts created or updated with exact workspace file paths.
3. **Architecture & Domain Summary:** Selected domain standards, key trade-offs resolved, and execution mode (parallel subagents or sequential fallback).
4. **Independent Verification Evidence:** Executed checks, test/reconciliation results, and 3-Level QA outcomes.
5. **Assumptions, Limitations & Residual Risks:** Clear separation of verified facts from working assumptions and any `NOT VERIFIED` items.
6. **Next Steps / Ready Commands:** Practical commands to run, inspect, or continue the project in natural language.

## 6. Reporting Anti-Patterns & Countermeasures
- **Plumbing Noise Dumping:** Exposing raw `conversationId` UUIDs, internal batch numbers, or write-lock tables in ordinary user updates -> *Countermeasure:* Keep internal orchestration metadata inside `AGENT_COMMUNICATE.md` and `PROJECT_STATE.md` unless requested.
- **Reporting Planned Work as Done:** Listing queued `Research Queue` items or unverified drafts under completed deliverables -> *Countermeasure:* Report strictly verified disk artifacts under completed outcomes.
- **Shell `sleep` Polling:** Blocking shell subshells with `sleep` -> *Countermeasure:* Use reactive subagent wakeup and native `schedule(DurationSeconds=1200, TimerCondition="never")`.
