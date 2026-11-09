# Project Manifest (`PROJECT_MANIFEST.md`)

> **Template Governance:** Instantiate at project initialization (`Level 2`–`Level 4`) per [PROJECT_INITIALIZATION.md](../01_ORCHESTRATION/PROJECT_INITIALIZATION.md) and [PERSISTENT_PM_SA.md](../01_ORCHESTRATION/PERSISTENT_PM_SA.md). Store inside the target workspace state directory without copying static library prompts.

---

## 1. Project Identity & Complexity Classification
- **Project ID:** `{{PROJECT_ID}}`
- **Project Name:** `{{PROJECT_NAME}}`
- **Workspace Root:** `{{WORKSPACE_ROOT_ABS_PATH}}`
- **Library Source of Truth:** `{{LIBRARY_ROOT_ABS_PATH}}` (`v1.0.0`)
- **Complexity Level:** `{{COMPLEXITY_LEVEL}}` (`Level 2 | Level 3 | Level 4` — classified via [TASK_COMPLEXITY_ROUTER.md](../00_GLOBAL_CONSTITUTION/TASK_COMPLEXITY_ROUTER.md))
- **Primary & Secondary Domains:** `{{PRIMARY_DOMAIN}}`, `{{SECONDARY_DOMAINS}}`
- **Created / Last Updated (ISO-8601):** `{{CREATED_TIMESTAMP}}` / `{{UPDATED_TIMESTAMP}}`

---

## 2. Persistent Governance Bindings & State Pointers
Antigravity scopes live subagent `conversationId` processes to the active parent conversation. Intra-session turns reuse `conversationId` instances via `send_message`; cross-session continuity hydrates state from the canonical disk artifacts below.

| Governance Slot | Canonical Library Role | Active Session `conversationId` | Cross-Session State File Pointer | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Project Manager (`PM`)** | `ROLE-CORE-001` (`PROJECT_MANAGER`) | `{{PM_CONVERSATION_ID}}` | `{{STATE_DIR}}/PROJECT_STATE.md` | `{{PM_STATUS}}` |
| **System Architect (`SA`)** | `ROLE-CORE-002` (`SYSTEM_ARCHITECT`) | `{{SA_CONVERSATION_ID}}` | `{{STATE_DIR}}/AGENT_COMMUNICATE.md` | `{{SA_STATUS}}` |
| **Domain Lead(s)** | `ROLE-CORE-003` (`DOMAIN_LEAD`) | `{{DOMAIN_LEAD_CONVERSATION_IDS}}` | `{{STATE_DIR}}/WORKER_REGISTRY.md` | `{{DL_STATUS}}` |
| **Quality Reviewer** | `ROLE-CORE-004` (`QUALITY_REVIEWER`) | `{{QR_CONVERSATION_ID}}` | `{{STATE_DIR}}/QA_REPORT.md` | `{{QR_STATUS}}` |

---

## 3. Selected Domain & Specialist Role Inventory
List only roles justified by active workstreams. Do not allocate idle single-role agents where compatible roles can co-locate safely.

| Role ID | Canonical Role Name | Domain Folder (`03_DOMAINS/`) | Selection Rationale | Separation-of-Duties Constraint |
| :--- | :--- | :--- | :--- | :--- |
| `{{ROLE_ID_1}}` | `{{ROLE_NAME_1}}` | `{{DOMAIN_NAME_1}}` | `{{ROLE_1_RATIONALE}}` | `{{ROLE_1_SOD_CONSTRAINT}}` |
| `{{ROLE_ID_2}}` | `{{ROLE_NAME_2}}` | `{{DOMAIN_NAME_2}}` | `{{ROLE_2_RATIONALE}}` | `{{ROLE_2_SOD_CONSTRAINT}}` |
| `{{ROLE_ID_3}}` | `{{ROLE_NAME_3}}` | `{{DOMAIN_NAME_3}}` | `{{ROLE_3_RATIONALE}}` | `{{ROLE_3_SOD_CONSTRAINT}}` |

---

## 4. Discovered & Loaded Skills Manifest
Populated via the 10-step protocol in [SKILL_DISCOVERY_AND_LOADING](../05_SPECIALIZED_SKILLS/SKILL_DISCOVERY_AND_LOADING/SKILL.md) and inherited from [skills.json](../skills.json).

| Skill ID | Skill Name (`kebab-case`) | Version | Layer (`04` / `05`) | Prerequisite / Dependency Skills | Target Workstreams |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `{{SKILL_ID_1}}` | `{{SKILL_SLUG_1}}` | `1.0.0` | `{{SKILL_LAYER_1}}` | `{{SKILL_DEPS_1}}` | `{{SKILL_STREAM_1}}` |
| `{{SKILL_ID_2}}` | `{{SKILL_SLUG_2}}` | `1.0.0` | `{{SKILL_LAYER_2}}` | `{{SKILL_DEPS_2}}` | `{{SKILL_STREAM_2}}` |
| `{{SKILL_ID_3}}` | `{{SKILL_SLUG_3}}` | `1.0.0` | `{{SKILL_LAYER_3}}` | `{{SKILL_DEPS_3}}` | `{{SKILL_STREAM_3}}` |

---

## 5. Inspected Runtime Capabilities, Constraints & Fallbacks
- **Host OS, Shell & Toolchains:** `{{HOST_OS_SHELL_SUMMARY}}`
- **Verified Native Antigravity Tools:** `read_file`, `write_file`, `edit_file`, `run_command`, `define_subagent`, `invoke_subagent`, `send_message`, `manage_subagents`, `schedule`, `manage_task`, `search_web`, `ask_question`
- **Rules & Context Budget:** `.agents/rules/*.md`, `AGENTS.md`, and `GEMINI.md` obey the `24 KB` per-file cap and `20,000`-token always-on budget via selective on-demand loading.
- **Filesystem Locking Reality:** Host filesystem lacks per-subagent kernel ACL locks; write isolation is enforced via the SA Exclusive Write-Lock table in [AGENT_COMMUNICATE.md](./AGENT_COMMUNICATE.md) and post-execution `git status` / diff verification.
- **GUI / Browser Tooling Availability:** `{{GUI_BROWSER_AVAILABILITY_STATUS}}` (`AVAILABLE: {{TOOL_NAMES}}` | `UNAVAILABLE — fallback to HTTP/API/CLI/DOM verification without fabricating manual UI interaction`)
- **Hardware, Disk & Thermal Safeguards:** `{{DISK_CPU_GPU_LIMITS}}`
- **Human Approval Triggers Active:** `{{HUMAN_APPROVAL_TRIGGERS}}`
