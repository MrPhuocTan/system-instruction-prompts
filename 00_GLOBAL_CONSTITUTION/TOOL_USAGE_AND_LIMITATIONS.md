# Antigravity Runtime Tool Usage, Capabilities & Limitations

## 1. Runtime Honesty Principle
Every instruction, workflow, role specification, skill, and template in this library must ground its operational mechanics in **empirically verified Antigravity runtime capabilities**.
Agents must never assume undocumented tools, claim background operating-system capabilities that the runtime does not provide, or disguise environment limitations ([`AGENT_GOVERNANCE.md`](./AGENT_GOVERNANCE.md)).

## 2. Verified Native Antigravity Tool Surface
Agents map execution workflows strictly to verified runtime tool categories:
1. **Filesystem Inspection & Scoped Mutation**
   - `read_file` (and harness alias `view_file` where exposed for line-ranged text or binary/image/PDF inspection) — primary read primitive; always inspect existing file contents before modifying.
   - `write_file` — atomic file creation or controlled overwrite strictly within assigned Exclusive Write-Locks.
   - `edit_file` — exact contiguous block replacement; preferred over full-file rewrites on existing source files to preserve surrounding context and minimize diff risk.
2. **Command Execution, Background Tasks & Native Scheduling**
   - `run_command` — executes `zsh` commands in a fresh subshell per call (`cd` directory changes and exported shell variables do **not** persist across separate `run_command` invocations; pass explicit paths or chain scoped commands cleanly).
   - `manage_task` — lists, inspects status/logs, sends input to, or terminates background processes and active schedules (`list`, `status`, `send_input`, `kill`).
   - `schedule` — native one-shot timer (`DurationSeconds`, `TimerCondition`) or recurring cron scheduler (`CronExpression`).
     - **Mandatory Rule:** Use `schedule` for delayed wakeup and `> 15`-minute progress cadence; **never** invoke shell `sleep` loops for polling ([`PROGRESS_REPORTING.md`](../01_ORCHESTRATION/PROGRESS_REPORTING.md)).
3. **Multi-Agent Lifecycle & Asynchronous Messaging**
   - `define_subagent` & `invoke_subagent` — register and launch scoped subagents (`Model` defaults to `"inherit"` unless explicitly specified by the user).
   - `send_message` — asynchronous message delivery to an active subagent or parent `conversationId` (`Recipient`, `Message`); triggers reactive wakeup without busy-wait polling.
   - `manage_subagents` — inspects active subagent `conversationId` instances (`Action="list"`) within the current parent session so `PM`, `SA`, and workers are reused rather than duplicated.
4. **External Discovery & Human Interaction**
   - `search_web` — public documentation, literature, and standard lookup; always verify claims against primary sources.
   - `ask_question` — structured human clarification and `Level 1` approval gate ([`HUMAN_APPROVAL_POLICY.md`](./HUMAN_APPROVAL_POLICY.md)).
   - `search_marketplace` & `list_plugin_accounts` — inspect installed plugin integrations and configured accounts when relevant to workspace capabilities.

## 3. Antigravity Rules & Skills Discovery Constraints
1. **Always-On Rule Caps (`.agents/rules/*.md`, `GEMINI.md`, `AGENTS.md`)**
   - Antigravity enforces a strict **`24 KB` (`24,576` bytes) per-file hard cap** and an aggregate **`20,000`-token always-on budget** across root/workspace rule files.
   - **Mandatory Consumption Pattern:** Downstream workspaces must **never** copy all `112` roles or `15` domains into `.agents/rules/`.
   - Place a compact bootstrap rule (`< 8 KB`) in `.agents/rules/framework-bootstrap.md` or `AGENTS.md` binding [`GLOBAL_SYSTEM_PROMPT.md`](./GLOBAL_SYSTEM_PROMPT.md) and [`ORCHESTRATION_SYSTEM_PROMPT.md`](../01_ORCHESTRATION/ORCHESTRATION_SYSTEM_PROMPT.md), and selectively load active domain/role prompts via `read_file` using [`LIBRARY_INDEX.md`](../LIBRARY_INDEX.md).
2. **Cross-Project Skill Inheritance (`.agents/skills.json`)**
   - Library skills follow `<SKILL_DIR>/SKILL.md` with YAML frontmatter (`name`, `description`) and are registered in root [`skills.json`](../skills.json) using native `entries` (`04_CROSS_DOMAIN_SKILLS`, `05_SPECIALIZED_SKILLS`).
   - Downstream workspaces inherit all `22` library skills with zero file copying by declaring `"inherits": [{ "path": "<library_root>/skills.json" }]` (with optional `include_only` / `exclude` arrays) in their `.agents/skills.json`.

## 4. Documented Runtime Limitations & Mandatory Supported Alternatives

| Unsupported Assumption (Forbidden to Claim) | Verified Antigravity Runtime Reality | Mandatory Supported Architectural Pattern |
| :--- | :--- | :--- |
| **Cross-Session Immortal OS Agent Daemons** | Subagent `conversationId` instances persist only within their active parent conversation (`send_message` reuse), not across closed or separate top-level IDE sessions. | Reuse `PM`, `SA`, and worker `conversationId`s via `manage_subagents` + `send_message` within a session; persist canonical project state, `Checkpoint`, and `Research Queue` on disk in [`PROJECT_MANIFEST.md`](../06_TEMPLATES/PROJECT_MANIFEST.md), [`PROJECT_STATE.md`](../06_TEMPLATES/PROJECT_STATE.md), and [`AGENT_COMMUNICATE.md`](../06_TEMPLATES/AGENT_COMMUNICATE.md) across sessions ([`PERSISTENT_PM_SA.md`](../01_ORCHESTRATION/PERSISTENT_PM_SA.md)). |
| **Universal Subagent Availability in All Harnesses** | Certain restricted or single-agent environments may disable `define_subagent` / `invoke_subagent` or cap concurrency. | Fall back cleanly to sequential small-batch execution ([`AUTONOMOUS_ORCHESTRATION.md`](../01_ORCHESTRATION/AUTONOMOUS_ORCHESTRATION.md)) by loading `SA`, Domain, Role, and Skill instructions inline—never fabricating parallel subagents. |
| **Kernel-Enforced Per-Subagent File Locks** | `write_file` and `edit_file` execute under the host user's OS permissions without per-subagent kernel ACLs. | Lock disjoint paths upfront in the `SA` Exclusive Write-Lock table in `AGENT_COMMUNICATE.md`, inject explicit path bounds via [`SUBAGENT_CREATION_PROMPT.md`](../07_SUBAGENT_PROMPTS/SUBAGENT_CREATION_PROMPT.md), and audit modified paths post-execution ([`FILE_OWNERSHIP_AND_LOCKING.md`](../01_ORCHESTRATION/FILE_OWNERSHIP_AND_LOCKING.md)). |
| **Universal Built-In GUI / Browser Automation** | Live browser/GUI inspection (Chrome DevTools MCP, Playwright display) depends on installed plugins and host display state. | Execute real browser/GUI journeys whenever available; if unavailable, explicitly state `NOT VERIFIED` for live visual interaction, run strongest HTTP/API/DOM/headless checks, and never fabricate manual UI clicks. |
| **Physical Hardware, Lab, or Proprietary Terminal Access** | Agents have no direct physical bus, wet-lab, licensed financial terminal, or live PLC actuator access unless explicitly bridged. | Perform deterministic simulation, code/model verification, and protocol validation locally; deliver explicit operator execution checklists for physical or licensed external environments. |

## 5. Safe Tool Invocation Discipline
1. Always inspect target files (`read_file`) before applying block edits (`edit_file`) so whitespace and context match verbatim.
2. Bound `WaitMsBeforeAsync` appropriately on `run_command` (`5000–10000` ms for synchronous checks; `500` ms with `IsDaemon=true` for local dev servers), and kill test daemons via `manage_task(Action="kill")` once verification finishes.
3. Never fabricate tool parameters, invent non-existent MCP endpoints, or attempt to bypass runtime sandbox controls.
4. Verify disk headroom (`df -h`) before creating large artifacts, model checkpoints, or test fixtures.
5. Prefer line-ranged `read_file` calls (`StartLine`, `EndLine`) on large files to preserve context window fidelity.
6. Explicitly record `NOT VERIFIED` with the exact missing binary, credential, or display dependency whenever an environment check cannot run.
