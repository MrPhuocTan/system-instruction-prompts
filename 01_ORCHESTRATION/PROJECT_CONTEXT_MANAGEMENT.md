# Project Context Management & Progressive Disclosure

## 1. Context Budget Reality & Design Rationale
Large context windows degrade in instruction fidelity ("lost-in-the-middle" attention dilution) when flooded with irrelevant prompts, raw build logs, or unused domain rules.
Furthermore, Antigravity enforces a strict **`24 KB` (`24,576` bytes) per-file limit** and an aggregate **`20,000`-token always-on rule budget** across `.agents/rules/*.md`, `GEMINI.md`, and `AGENTS.md` ([`TOOL_USAGE_AND_LIMITATIONS.md`](../00_GLOBAL_CONSTITUTION/TOOL_USAGE_AND_LIMITATIONS.md)).
Progressive disclosure and small-batch checkpointing ([`AUTONOMOUS_ORCHESTRATION.md`](./AUTONOMOUS_ORCHESTRATION.md)) guarantee sharp domain adherence while keeping per-turn token consumption minimal.

## 2. Four-Tier Progressive Context Architecture

| Context Tier | Loaded Artifacts | Scope & Persistence | Budget & Loading Rule |
| :--- | :--- | :--- | :--- |
| **Tier 0 — Always-On Bootstrap** | Workspace `AGENTS.md` or `.agents/rules/framework-bootstrap.md` | Every turn in target workspace | Keep `< 4–8 KB` (`< 2,000` tokens). Never inline domain or role catalogs into Tier 0. |
| **Tier 1 — Active Orchestration State** | [`GLOBAL_SYSTEM_PROMPT.md`](../00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md), [`TASK_COMPLEXITY_ROUTER.md`](../00_GLOBAL_CONSTITUTION/TASK_COMPLEXITY_ROUTER.md), workspace `PROJECT_MANIFEST.md`, `PROJECT_STATE.md`, `AGENT_COMMUNICATE.md` | Orchestrator, `PM`, and `SA` on `Level 2`–`Level 4` tasks | Hydrate automatically at turn start; keep concise via checkpoint summarization. |
| **Tier 2 — Scoped Workstream Instruction** | Active domain `DOMAIN_SYSTEM_PROMPT.md` + `QUALITY_GATES.md`, assigned role `SYSTEM_PROMPT.md` + `QUALITY_CHECKLIST.md`, and `1–4` matched `SKILL.md` files | Scoped strictly to the assigned worker or sequential inline batch | Loaded on demand via `read_file` using paths resolved from [`LIBRARY_INDEX.md`](../LIBRARY_INDEX.md). |
| **Tier 3 — Ephemeral Batch Inspection** | Target source files, line-ranged log slices, test diffs, primary web sources | Local to immediate cognitive loop batch | Use line ranges (`StartLine`/`EndLine`) on large files; never dump multi-megabyte logs into messages. |

## 3. Strict Prohibition on Full-Library Preloading
1. **Zero Bulk Loading**
   - No orchestrator or subagent may bulk-read all `15` domains (`03_DOMAINS/`), all `112` roles, or all `22` skills (`04_CROSS_DOMAIN_SKILLS/`, `05_SPECIALIZED_SKILLS/`).
   - An `ECONOMICS_FINANCE` valuation task has zero reason to load `ROBOTICS_AUTOMATION` or `FRONTEND_ENGINEER` prompts.
2. **Index-First Routing**
   - Always resolve paths hierarchically without asking the user to know library paths:
     [`LIBRARY_INDEX.md`](../LIBRARY_INDEX.md) -> target `03_DOMAINS/<DOMAIN>/DOMAIN_INDEX.md` -> specific `ROLES/<ROLE>/SYSTEM_PROMPT.md`.
3. **Subagent & Batch Context Isolation**
   - When independent workstreams span distinct domains, spawning dedicated subagents ([`SUBAGENT_CREATION.md`](./SUBAGENT_CREATION.md))—or running sequential bounded batches when subagents are constrained—isolates each domain's context window cleanly.

## 4. State File Compaction, Checkpoints & Research Queues
Long-running `Level 3`–`Level 4` programs preserve continuity across turns and sessions without context overflow by maintaining structured state files:
- **`PROJECT_MANIFEST.md` ([Template](../06_TEMPLATES/PROJECT_MANIFEST.md))**
  - Stores stable charter, scope boundaries, active domain map, architectural invariants, and repository layout.
  - Modify only when user objectives or locked `SA` architecture formally evolve.
- **`PROJECT_STATE.md` ([Template](../06_TEMPLATES/PROJECT_STATE.md))**
  - Stores current internal lifecycle phase (`1–13`), active **`Checkpoint`** state (last verified batch, verified file inventory, resume cursor), prioritized **`Research Queue`** (pending domains, roles, modules, or open investigations), and active risks.
  - Reconciled automatically at the end of every verified batch so interrupted sessions auto-resume with zero lost work.
- **`AGENT_COMMUNICATE.md` ([Template](../06_TEMPLATES/AGENT_COMMUNICATE.md))**
  - Stores active worker registry, Exclusive Write-Locks, concise handoff summaries, and `SA_GATE` + `PM_GATE` verdicts.
  - Write verbose raw command outputs or benchmark dumps to dedicated workspace artifact paths (`logs/`, `reports/`, `configs/handoffs/`) and reference their paths rather than pasting multi-thousand-line transcripts into `AGENT_COMMUNICATE.md`.

## 5. Cross-Agent Context Passing Rules
When `PM` or the orchestrator dispatches a worker via `invoke_subagent` or `send_message`:
1. Pass **exact absolute file paths** and line ranges to inspect via `read_file` rather than copying whole source files into prompt text.
2. Explicitly enumerate the `2–6` library files the worker must load (`DOMAIN_SYSTEM_PROMPT.md`, `ROLE/SYSTEM_PROMPT.md`, `ROLE/QUALITY_CHECKLIST.md`, and assigned `SKILL.md` runbooks).
3. Include locked `SA` interface contracts and acceptance criteria verbatim so the worker never guesses cross-module contracts ([`CONTRACT_AND_HANDOFF.md`](./CONTRACT_AND_HANDOFF.md)).
4. Strip superseded intermediate debate from worker prompts—provide only authoritative locked decisions and active batch inputs.

## 6. Context Hygiene Failure Modes & Countermeasures
- **Rule Cap Overflow (`> 24 KB`):** Stuffing domain catalogs into `AGENTS.md` or `.agents/rules/` -> *Countermeasure:* Keep bootstrap pointers `< 8 KB` and load modules via `read_file` on demand.
- **Transcript Bloat in State Files:** Pasting full test stdout into `AGENT_COMMUNICATE.md` -> *Countermeasure:* Store verbose logs in `logs/` or `reports/` and link concise summaries.
- **Amnesia Across Interrupted Sessions:** Relying on transient chat memory without updating `PROJECT_STATE.md` -> *Countermeasure:* Reconcile `Checkpoint` and `Research Queue` at the end of every batch.
