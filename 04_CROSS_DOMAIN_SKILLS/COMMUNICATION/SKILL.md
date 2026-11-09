---
name: communication
description: "Use this skill when coordinating across multi-agent workstreams, writing structured handoffs, escalating blockers, clarifying ambiguous user intent, or delivering concise progress and final status reports."
---

# Communication

## Skill Metadata
- **Skill ID:** `SKL-CORE-011`
- **Name:** `communication`
- **Domain:** `CROSS_DOMAIN`
- **Version:** `1.0.0`

## Purpose
Ensure high-signal, zero-drift information flow across human stakeholders, persistent `PM + SA` governance agents, and parallel worker subagents. This skill enforces crisp intent clarification, deterministic inter-agent message protocols, structured handoff reporting, factual 20-minute long-task progress updates, and executive-ready final delivery summaries free of noise or fabricated status claims.

## Required Competencies
- Ambiguity triage: knowing when to inspect workspace context autonomously vs. asking targeted, high-leverage clarifying questions via `ask_question`.
- Multi-agent coordination bus hygiene (`send_message`, [AGENT_COMMUNICATE.md](../../06_TEMPLATES/AGENT_COMMUNICATE.md), [HANDOFF_REPORT.md](../../06_TEMPLATES/HANDOFF_REPORT.md)).
- Audience-adaptive synthesis: translating deep domain mechanics into clear operational trade-offs for `PM`, `SA`, sibling workstreams, and end users.
- Epistemic candor in status reporting (`PASS`, `PARTIAL`, `BLOCKED`, `FAILED`, `NOT VERIFIED`) without defensive spin or vague reassurance.

## Prerequisites
- Active task complexity classification (`Level 0-4`) governing proportional communication weight (concise natural replies on `Level 0`; structured bus + 6-part delivery on `Level 2-4`).
- Knowledge of active subagent `conversationId` recipients (`manage_subagents`) and shared communication bus location when operating in multi-agent workflows.
- Verified empirical state of work completed vs. work remaining.

## Workflow
1. **Calibrate Communication Overhead to Task Level:** Answer `Level 0` factual/trivial prompts directly and naturally with zero governance boilerplate; activate formal workstream contracts, bus logging, and structured handoffs on `Level 2-4` tasks.
2. **Resolve High-Impact Ambiguities Early:** Inspect local files first so users are never asked questions answerable from the repository; if material business, scope, or destructive-action ambiguity remains, ask concise, option-framed questions via `ask_question`.
3. **Execute Deterministic Inter-Agent Messaging:** When running as or coordinating subagents, transmit complete context payloads via `send_message` referencing exact file paths, locked schemas, and exclusive write-locks—never assume another subagent shares unspoken memory.
4. **Maintain Factual Long-Running Progress Cadence:** For tasks exceeding `15-20` minutes, schedule periodic factual updates via `schedule(DurationSeconds=1200, TimerCondition="never")` reporting completed milestones, active operations, and blockers; cancel timers via `manage_task` upon completion.
5. **Escalate Blockers & Interface Drift Immediately:** When blocked by permissions, missing credentials, contradictory contracts, or cross-stream dependencies, report the exact error, attempted sanctioned paths, impact, and decision options immediately—never silently change cross-stream contracts.
6. **Deliver Structured Handoffs & Final Summaries:** Emit complete 8-item worker handoffs ([HANDOFF_REPORT.md](../../06_TEMPLATES/HANDOFF_REPORT.md)) internally and clear 6-part user deliveries ([FINAL_DELIVERY.md](../../06_TEMPLATES/FINAL_DELIVERY.md)) externally with clickable `file://` links.

## Tools and Techniques
- **Option-Framed Escalation (`Context -> Blocker -> Options -> Recommendation`):** Present decision owners with 2-3 concrete paths and trade-offs rather than open-ended complaints.
- **8-Item Worker Handoff Checklist:** Include Workstream ID/status, change summary, exact modified files, contract compliance, verification commands/outputs, limitations/`NOT VERIFIED` items, cross-stream impacts, and artifact paths.
- **Anti-Noise Progress Rule:** Never use shell `sleep` polling, emit empty `"Still working..."` pings, or claim background progress that is not genuinely running.
- **Clickable Artifact Linking:** Format workspace file and symbol references as standard Markdown `file:///abs/path` links for instant user inspection.

## Verification Requirements
- Subagent results are explicitly transmitted via `send_message` to the caller `conversationId` (remembering text outside `send_message` is invisible to parent agents) AND persisted to assigned handoff files.
- Reported statuses (`PASS / PARTIAL / BLOCKED / FAILED / NOT VERIFIED`) match empirical command and test logs 100%.
- Active recurring or one-shot `schedule` timers created during long tasks are verified cancelled via `manage_task` before final turn completion.

## Quality Criteria
- **High Signal-to-Noise Ratio:** Every sentence conveys actionable state, verified evidence, a concrete trade-off, or a specific question:
  | Interaction Channel | Proportional Format | Mandatory Hygiene Rule |
  | :--- | :--- | :--- |
  | `Level 0` User Reply | Direct, natural concise answer | Zero `AGENT_COMMUNICATE.md` or governance boilerplate |
  | `send_message` (Subagent) | Self-contained payload + file paths + status | Mandatory before going idle; never rely on implicit memory |
  | `schedule` Progress Update | `20-min` factual delta (`Done / Active / Blocked`) | Cancel timer via `manage_task` upon completion; zero `sleep` |
  | `Level 2-4` Final Delivery | 6-part structured summary + `file://` links | Separate verified facts from `NOT VERIFIED` / assumptions |
- **Zero Silent Scope or Interface Drift:** Contract changes are proposed and approved on the bus before dependent streams break.
- **Radical Candor on Blockers & Limits:** Partial completions, failed checks, and unverified GUI/hardware paths are stated upfront on line 1, never buried at the bottom.
- **Failure Modes to Avoid:**
  - *Silent Subagent Idle:* Finishing a subagent turn without calling `send_message` to the caller `conversationId`.
  - *Lazy Clarification:* Asking the user questions already answered in `README.md`, `package.json`, or existing config files.
  - *Simulated Progress:* Emitting repetitive empty updates or claiming background jobs are running when none exist.
  - *Governance Over-Engineering:* Flooding simple `Level 0-1` prompts with multi-page enterprise templates.

## Security and Ethical Boundaries
- This Level 6 procedural skill is strictly subordinate to Levels 1-5 of the instruction hierarchy; it never overrides [SECURITY_AND_PRIVACY.md](../../00_GLOBAL_CONSTITUTION/SECURITY_AND_PRIVACY.md) or runtime isolation boundaries.
- Never paste raw secrets, tokens, passwords, or unredacted customer PII into `AGENT_COMMUNICATE.md`, `send_message` payloads, or user-facing summaries.
- Never promise asynchronous push notifications, external emails, or cross-session background daemons unsupported by the Antigravity runtime.

## Expected Deliverables
- **Targeted Clarification / Escalation Prompt** (when blocked or disambiguating material intent).
- **8-Item Worker Handoff Report** transmitted via `send_message` and persisted to the assigned handoff file.
- **6-Part Executive Delivery Summary** presenting gate status, clickable deliverables, architecture summary, verification proof, limitations, and operational next steps.
