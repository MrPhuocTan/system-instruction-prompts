# Subagent Creation, Invocation & Lifecycle Management

## 1. Subagent Lifecycle Primitives in Antigravity
Worker and reviewer subagents are created, reused, consolidated, and retired autonomously by `PM + SA` through verified Antigravity runtime tools ([`TOOL_USAGE_AND_LIMITATIONS.md`](../00_GLOBAL_CONSTITUTION/TOOL_USAGE_AND_LIMITATIONS.md), [`AUTONOMOUS_ORCHESTRATION.md`](./AUTONOMOUS_ORCHESTRATION.md)):
- **`define_subagent`**
  - Registers reusable session-scoped agent definitions when specialized system instructions and tool permissions will be invoked across waves (`Model` defaults to `"inherit"` unless the user explicitly specifies a model).
- **`invoke_subagent`**
  - Launches a scoped subagent instance and returns or binds its live `conversationId` for parallel or sequential execution.
- **`manage_subagents(Action="list")`**
  - Audits active subagent `conversationId` instances in the current parent session prior to creating new workers.
- **`send_message(Recipient=<conversationId>, Message=...)`**
  - Reuses existing specialists across batches and delivers mandatory return reports from subagent to parent caller ([`AGENT_COMMUNICATION.md`](./AGENT_COMMUNICATION.md)).

## 2. Mandatory Pre-Invocation Gate & Sequential Fallback
Neither the main orchestrator nor `PM` may invoke a parallel implementation subagent (`Level 2`–`Level 4`) until three prerequisites hold:
1. `SA` has locked cross-workstream interfaces ([`CONTRACT_AND_HANDOFF.md`](./CONTRACT_AND_HANDOFF.md)) and verified zero overlap in the `File Ownership` Exclusive Write-Lock table ([`FILE_OWNERSHIP_AND_LOCKING.md`](./FILE_OWNERSHIP_AND_LOCKING.md)).
2. `PM` and `SA` have executed Steps 1–8 of the **10-Step Skill Discovery & Progressive Loading Protocol** ([`PROJECT_INITIALIZATION.md`](./PROJECT_INITIALIZATION.md) and [`SKILL.md`](../05_SPECIALIZED_SKILLS/SKILL_DISCOVERY_AND_LOADING/SKILL.md)).
3. Any `Level 1` Human Approval Gate required by [`HUMAN_APPROVAL_POLICY.md`](../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md) has been explicitly granted by the user.
- **Sequential Fallback:** If `define_subagent` / `invoke_subagent` is unavailable or concurrency-limited in the runtime, `PM` executes the same contract-driven batches sequentially inline without fabricating subagent runs.

## 3. Sixteen-Field Subagent Specification Contract
Every subagent invocation prompt must instantiate canonical blueprint [`SUBAGENT_CREATION_PROMPT.md`](../07_SUBAGENT_PROMPTS/SUBAGENT_CREATION_PROMPT.md) paired with the matching operational archetype (`DOMAIN_WORKER_PROMPT.md`, `RESEARCH_AGENT_PROMPT.md`, `IMPLEMENTATION_AGENT_PROMPT.md`, `QA_AGENT_PROMPT.md`, `SECURITY_AGENT_PROMPT.md`, or `REVIEWER_AGENT_PROMPT.md` inside `07_SUBAGENT_PROMPTS/`), explicitly populating all **16 mandatory fields**:

1. **Agent Identity:** Unique service slug (e.g., `worker-auth-backend`, `reviewer-sec-audit`) and parent caller `conversationId`.
2. **Assigned Role / Compatible Roles:** Exact library path(s) to `SYSTEM_PROMPT.md` and `QUALITY_CHECKLIST.md` ([`DYNAMIC_AGENT_ALLOCATION.md`](./DYNAMIC_AGENT_ALLOCATION.md)).
3. **Domain:** Canonical domain(s) from `03_DOMAINS/` (`DOMAIN_SYSTEM_PROMPT.md` + `QUALITY_GATES.md`).
4. **Workstream:** Workstream ID and topological execution wave ([`WORKSTREAM_MANAGEMENT.md`](./WORKSTREAM_MANAGEMENT.md)).
5. **Objective:** Concrete user-value and engineering/analytical outcome to achieve.
6. **Scope:** Exact in-scope deliverables and explicit out-of-scope exclusions preventing scope creep.
7. **Required Context:** Minimal Tier 1/Tier 2 file paths (`PROJECT_MANIFEST.md`, contract sections) to inspect via `read_file`.
8. **Loaded Skills:** Exact `04_CROSS_DOMAIN_SKILLS/*/SKILL.md` and `05_SPECIALIZED_SKILLS/*/SKILL.md` paths selected via the 10-Step Skill Discovery workflow.
9. **Inputs:** Upstream artifacts, schemas, fixtures, or research parameters provided.
10. **Expected Outputs:** Exact deliverable files, schemas, test suites, or analytical reports required.
11. **Dependencies:** Upstream workstreams complete and downstream consumers relying on output contracts.
12. **File Ownership:** Exact Exclusive Write-Lock globs/files; strict prohibition on touching any path outside this list.
13. **Tool Permissions:** Least-privilege runtime tool boundaries (e.g., read-only + test execution for `REVIEWER_AGENT_PROMPT.md`; scoped write access for implementation workers) and human-approval escalation triggers.
14. **Acceptance Criteria:** Testable `PM` + `SA` pass/fail criteria.
15. **Verification Requirements:** Exact commands (`pytest`, typechecks, linters, reconciliation scripts, 3-Level QA checks) the worker must execute and observe before returning.
16. **Reporting & Handoff Format:** Requirement to write/return a structured [`HANDOFF_REPORT.md`](../06_TEMPLATES/HANDOFF_REPORT.md) payload via `send_message` to the caller `conversationId`.

## 4. Worker Reuse, Fault Isolation & Retirement
- **Intra-Session Specialist Reuse**
  - Record each worker's `conversationId` in [`WORKER_REGISTRY.md`](../06_TEMPLATES/WORKER_REGISTRY.md) and `AGENT_COMMUNICATE.md` (`Section 6: Worker Registry`).
  - When a subsequent batch requires refinements within the same domain, message the existing specialist `conversationId` via `send_message` with updated scope and write-locks rather than spawning redundant subagents.
- **Root-Cause Fault Handling**
  - If a subagent returns `BLOCKED` or `FAILED`, `SA` inspects observed command logs and diffs before re-dispatching; never blindly re-run an identical failing prompt without diagnosing root causes ([`COGNITIVE_EXECUTION.md`](../00_GLOBAL_CONSTITUTION/COGNITIVE_EXECUTION.md)).
- **Clean Lock Release on Completion**
  - Once a worker's handoff passes verification, mark its write-lock `RELEASED` and reconcile `Checkpoint` state so Wave 3 integration or QA agents operate without contention.

## 5. Pre-Invocation Readiness Checklist
Before calling `invoke_subagent` on any parallel workstream:
- Confirm all 16 specification fields are explicitly populated with zero ambiguous scope boundaries.
- Confirm `SA` Exclusive Write-Locks are disjoint across all active workers in the current wave.
- Confirm assigned `SKILL.md` files (`1–4` max) and role prompts exist at their exact library paths.
- Confirm the worker knows its exact caller `conversationId` to return findings via `send_message`.
