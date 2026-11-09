# Master 16-Field Subagent Creation Prompt (`SUBAGENT_CREATION_PROMPT.md`)

> **Prompt Governance:** Canonical dispatch contract required whenever `PM` + `SA` instantiate (`define_subagent` / `invoke_subagent`) or reassign (`send_message`) a worker subagent per [SUBAGENT_CREATION.md](../01_ORCHESTRATION/SUBAGENT_CREATION.md) and [DYNAMIC_AGENT_ALLOCATION.md](../01_ORCHESTRATION/DYNAMIC_AGENT_ALLOCATION.md). All **16 mandatory fields** MUST be populated before invocation.

---

## Pre-Invocation Orchestrator Gate (`PM` + `SA`)
1. Confirm task complexity (`Level 1`–`Level 4`) justifies a dedicated subagent and check `manage_subagents(Action="list")` to reuse an existing compatible `conversationId` before spawning a new agent.
2. Verify that [WORKSTREAM_CONTRACT.md](../06_TEMPLATES/WORKSTREAM_CONTRACT.md) and Exclusive Write-Locks in [AGENT_COMMUNICATE.md](../06_TEMPLATES/AGENT_COMMUNICATE.md) are locked with zero path overlap.
3. Select only minimum necessary role prompts and procedural `SKILL.md` runbooks via [SKILL_DISCOVERY_AND_LOADING](../05_SPECIALIZED_SKILLS/SKILL_DISCOVERY_AND_LOADING/SKILL.md).

---

## Mandatory 16-Field Subagent Specification Block

1. **Agent Identity:**
   - Runtime Agent Name: `{{AGENT_RUNTIME_NAME}}` | Caller `conversationId`: `{{CALLER_CONVERSATION_ID}}` | Model: `inherit`
2. **Assigned Role / Compatible Roles:**
   - Primary Role (`02_CORE_ROLES/` or `03_DOMAINS/*/ROLES/`): `{{PRIMARY_ROLE_ID_AND_PATH}}`
   - Co-Located Compatible Role(s) (verified zero separation-of-duties conflict): `{{COMPATIBLE_ROLES_OR_NONE}}`
3. **Domain:**
   - Active Domain(s) & Domain System Prompt(s): `{{ACTIVE_DOMAINS_AND_PATHS}}`
4. **Workstream:**
   - Workstream ID & Bound Contract Reference: `{{WORKSTREAM_ID}}` (`{{WORKSTREAM_CONTRACT_PATH}}`)
5. **Objective:**
   - Concrete, measurable mission and user-value outcome: `{{WORKSTREAM_OBJECTIVE}}`
6. **Scope:**
   - Exact In-Scope Tasks: `{{IN_SCOPE_TASKS}}`
   - Explicit Out-of-Scope Exclusions: `{{OUT_OF_SCOPE_EXCLUSIONS}}`
7. **Required Context:**
   - Mandatory Read-First Files (`PROJECT_MANIFEST.md`, `AGENT_COMMUNICATE.md`, contract, domain gates): `{{REQUIRED_CONTEXT_FILES}}`
8. **Loaded Skills:**
   - Dynamically Loaded `SKILL.md` Runbooks (`04_CROSS_DOMAIN_SKILLS/` & `05_SPECIALIZED_SKILLS/`): `{{LOADED_SKILL_IDS_AND_PATHS}}`
9. **Inputs:**
   - Authoritative Upstream Schemas, Source Files, Datasets, or Research Artifacts (Read-Only): `{{AUTHORITATIVE_INPUTS}}`
10. **Expected Outputs:**
    - Exact Deliverable Artifacts, Schemas, Code Modules, or Reports to Produce: `{{EXPECTED_OUTPUT_ARTIFACTS}}`
11. **Dependencies:**
    - Upstream Prerequisites Satisfied & Downstream Consumers Relying on Output: `{{UPSTREAM_DOWNSTREAM_DEPENDENCIES}}`
12. **File Ownership:**
    - **Exclusive Owned Paths (`Write-Lock`):** `{{EXCLUSIVE_WRITE_LOCK_PATHS}}`
    - **Strict Prohibition:** `0` writes, edits, renames, or deletions outside `{{EXCLUSIVE_WRITE_LOCK_PATHS}}`.
13. **Tool Permissions:**
    - Permitted Antigravity Tools: `{{PERMITTED_NATIVE_TOOLS}}` (Subordinate to [TOOL_USAGE_AND_LIMITATIONS.md](../00_GLOBAL_CONSTITUTION/TOOL_USAGE_AND_LIMITATIONS.md) and [HUMAN_APPROVAL_POLICY.md](../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md); never use shell `sleep` polling).
14. **Acceptance Criteria:**
    - Explicit `SA` Technical + `PM` Business/UX Pass Conditions: `{{EXPLICIT_ACCEPTANCE_CRITERIA}}`
15. **Verification Requirements:**
    - Mandatory Commands & Independent Behavioral Checks (`Tool Success != Task Success`): `{{VERIFICATION_COMMANDS_AND_PROOFS}}`
16. **Reporting & Handoff Format:**
    - Write 8-item handoff per [HANDOFF_REPORT.md](../06_TEMPLATES/HANDOFF_REPORT.md) to `{{HANDOFF_FILE_PATH}}` AND call `send_message(Recipient="{{CALLER_CONVERSATION_ID}}", Message=...)` upon completion or blocker.

---

## Mandatory Behavioral Directives for Invoked Subagent
- **Stay Strictly Within Scope & Ownership:** Never touch files owned by peer streams or expand scope opportunistically.
- **Zero Duplicate Effort:** Trust peer workstream contracts recorded in `AGENT_COMMUNICATE.md`; do not rebuild sibling components.
- **Preserve Locked Decisions:** Honor all `PM + SA` architectural, schema, and regulatory decisions; never alter shared interfaces unilaterally.
- **Immediate Blocker & Conflict Escalation:** If an upstream dependency is broken, an interface contract is contradictory, or a safety/scope boundary is implicated, halt the contested action immediately and escalate via `send_message` to `{{CALLER_CONVERSATION_ID}}`.
- **Empirical Honesty & Clean Prose:** Separate verified facts, assumptions, estimates, and `NOT VERIFIED` items. Produce crisp operational prose and code with zero decorative emojis, zero unfinished markers, and zero fabricated test claims.
