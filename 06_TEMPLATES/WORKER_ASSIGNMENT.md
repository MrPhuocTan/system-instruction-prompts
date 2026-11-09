# Worker Task Assignment Dispatch (`WORKER_ASSIGNMENT.md`)

> **Template Governance:** Issued by `PM` + `SA` when dispatching a new workstream slice or reusing an idle worker via `send_message` per [WORKSTREAM_MANAGEMENT.md](../01_ORCHESTRATION/WORKSTREAM_MANAGEMENT.md) and [SUBAGENT_CREATION_PROMPT.md](../07_SUBAGENT_PROMPTS/SUBAGENT_CREATION_PROMPT.md).

---

## 1. Assignment Dispatch Header
- **Assignment ID:** `{{ASSIGNMENT_ID}}`
- **Project ID / Workstream ID:** `{{PROJECT_ID}}` / `{{WORKSTREAM_ID}}`
- **Target Runtime Agent ID & `conversationId`:** `{{WORKER_AGENT_ID}}` (`{{WORKER_CONVERSATION_ID}}`)
- **Caller / Orchestrator `conversationId`:** `{{CALLER_CONVERSATION_ID}}`
- **Dispatch Mode:** `{{DISPATCH_MODE}}` (`INITIAL_INVOCATION | INTRA_SESSION_SEND_MESSAGE_REUSE`)
- **Bound Contract Reference:** `{{WORKSTREAM_CONTRACT_PATH}}` (derived from [WORKSTREAM_CONTRACT.md](./WORKSTREAM_CONTRACT.md))

---

## 2. Role, Domain & Skill Binding
- **Primary Role Prompt Loaded:** `{{PRIMARY_ROLE_SYSTEM_PROMPT_PATH}}`
- **Compatible Secondary Role(s):** `{{SECONDARY_ROLE_PATHS_OR_NONE}}`
- **Domain Standards & Gates Loaded:** `{{DOMAIN_SYSTEM_PROMPT_PATH}}`, `{{DOMAIN_QUALITY_GATES_PATH}}`
- **Procedural Skills Loaded (`04` / `05`):**
  1. `{{SKILL_1_ID}}` — `{{SKILL_1_PATH}}`
  2. `{{SKILL_2_ID}}` — `{{SKILL_2_PATH}}`
  3. `{{SKILL_3_ID}}` — `{{SKILL_3_PATH}}`

---

## 3. Scoped Objective, Inputs & Exclusive Write-Lock
- **Concrete Slice Objective:** `{{SLICE_OBJECTIVE}}`
- **Authoritative Input Artifacts (Read-Only):**
  - `{{INPUT_FILE_1}}` — `{{INPUT_1_PURPOSE}}`
  - `{{INPUT_FILE_2}}` — `{{INPUT_2_PURPOSE}}`
- **Exclusive Owned Paths (`Write-Lock` Registered in [AGENT_COMMUNICATE.md](./AGENT_COMMUNICATE.md)):**
  - `{{OWNED_WRITE_PATH_1}}`
  - `{{OWNED_WRITE_PATH_2}}`
- **Forbidden Paths & Out-of-Scope Operations:**
  - Never create, edit, or delete files outside the Exclusive Owned Paths listed above.
  - Explicit exclusions: `{{OUT_OF_SCOPE_EXCLUSIONS}}`

---

## 4. Interface Invariants & Resource Guardrails
- **Upstream / Downstream Interface Signatures (Immutable Without `SA` Approval):** `{{LOCKED_INTERFACE_SUMMARY}}`
- **Allowed Antigravity Tools:** `{{ALLOWED_TOOLS_LIST}}`
- **Security, Secret & Privacy Constraints:** Zero hardcoded credentials, API keys, tokens, or unredacted PII in code, logs, or handoffs.
- **Host Resource & Thermal Limits:** `{{RESOURCE_THERMAL_LIMITS}}`

---

## 5. Mandatory Verification & Handoff Protocol
1. Execute deterministic checks via `run_command`:
   - Build / Static / Schema Check: `{{VERIFY_CMD_STATIC}}`
   - Behavioral / Integration / Domain Check: `{{VERIFY_CMD_BEHAVIORAL}}`
   - Write-Lock Cleanliness Check: `{{VERIFY_CMD_DIFF_SCOPE}}`
2. Apply independent judgment (`Tool Success != Task Success`): inspect actual outputs, edge cases, and failure paths rather than exit codes alone.
3. Halt immediately and message `{{CALLER_CONVERSATION_ID}}` if blocked by missing prerequisites, contract ambiguity, or safety/scope boundaries.
4. Deliver a complete 8-item report formatted per [HANDOFF_REPORT.md](./HANDOFF_REPORT.md) to `{{HANDOFF_OUTPUT_PATH}}` and transmit the summary via `send_message(Recipient="{{CALLER_CONVERSATION_ID}}", ...)`.
