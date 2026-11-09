# Runtime Worker & Role Allocation Registry (`WORKER_REGISTRY.md`)

> **Template Governance:** Enforces strict separation between static logical **Roles** (`02_CORE_ROLES/`, `03_DOMAINS/*/ROLES/`) and runtime **Agent** instances (`conversationId`) per [DYNAMIC_AGENT_ALLOCATION.md](../01_ORCHESTRATION/DYNAMIC_AGENT_ALLOCATION.md).

---

## 1. Registry Header & Allocation Budget
- **Project ID:** `{{PROJECT_ID}}`
- **Complexity Level:** `{{COMPLEXITY_LEVEL}}`
- **Active Parallel Subagent Count:** `{{ACTIVE_SUBAGENT_COUNT}}` (Rule: Do not spawn `>= 4` concurrent subagents unless independent workstream parallelism demonstrably justifies coordination cost.)
- **Session Parent `conversationId`:** `{{PARENT_CONVERSATION_ID}}`

---

## 2. Active & Reusable Subagent Instance Table
Reuse existing subagents within the active session via `send_message(Recipient=<conversationId>, ...)` instead of spawning duplicate workers per turn.

| Runtime Agent ID | `conversationId` | Primary Logical Role ID | Co-Located Compatible Role(s) | Domain(s) | Loaded Skill IDs | Active Write-Lock | Lifecycle State |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `{{AGENT_ID_1}}` | `{{CONV_ID_1}}` | `{{PRIMARY_ROLE_1}}` | `{{COMPAT_ROLES_1}}` | `{{DOMAIN_1}}` | `{{SKILL_IDS_1}}` | `{{WRITE_LOCK_1}}` | `{{STATE_1}}` |
| `{{AGENT_ID_2}}` | `{{CONV_ID_2}}` | `{{PRIMARY_ROLE_2}}` | `{{COMPAT_ROLES_2}}` | `{{DOMAIN_2}}` | `{{SKILL_IDS_2}}` | `{{WRITE_LOCK_2}}` | `{{STATE_2}}` |
| `{{AGENT_ID_3}}` | `{{CONV_ID_3}}` | `{{PRIMARY_ROLE_3}}` | `{{COMPAT_ROLES_3}}` | `{{DOMAIN_3}}` | `{{SKILL_IDS_3}}` | `{{WRITE_LOCK_3}}` | `{{STATE_3}}` |

*Allowed `Lifecycle State` values:* `INITIALIZING` | `ACTIVE_EXECUTING` | `IDLE_REUSABLE` | `BLOCKED_ESCALATED` | `COMPLETED_RELEASED`

---

## 3. Multi-Role Co-Location & Separation-of-Duties Audit
Before combining multiple logical roles inside one runtime subagent, `SA` + `PM` must verify zero conflict of interest:

| Runtime Agent ID | Combined Roles | Compatibility Justification | Separation-of-Duties Check (`PASS` / `REJECTED`) | Independent Reviewer Assigned |
| :--- | :--- | :--- | :--- | :--- |
| `{{AGENT_ID_1}}` | `{{COMBINED_ROLES_1}}` | `{{COLOCATION_RATIONALE_1}}` | `{{SOD_CHECK_1}}` | `{{REVIEWER_AGENT_ID_1}}` |
| `{{AGENT_ID_2}}` | `{{COMBINED_ROLES_2}}` | `{{COLOCATION_RATIONALE_2}}` | `{{SOD_CHECK_2}}` | `{{REVIEWER_AGENT_ID_2}}` |

**Non-Negotiable Separation Rules:**
1. An implementation author (`BACKEND_ENGINEER`, `FRONTEND_ENGINEER`, `MACHINE_LEARNING_ENGINEER`, `FINANCIAL_MODELING`) MUST NEVER act as its own `QUALITY_REVIEWER`, `SA_GATE` approver, or `PM_GATE` approver on `Level 2`–`Level 4` work.
2. Offensive security testers (`PENETRATION_TESTER`, `RED_TEAM_OPERATOR`) MUST NOT unilaterally approve scope expansions or compliance waivers (`SECURITY_GRC`, `PRIVACY_SPECIALIST`).
3. Sequential role transitions on a single agent require explicit write-lock updates in [AGENT_COMMUNICATE.md](./AGENT_COMMUNICATE.md).

---

## 4. Intra-Session `send_message` Reuse & Lock Transition Log
| Timestamp (ISO) | Runtime Agent ID | Action (`SPAWN` / `REUSE` / `LOCK_RELEASE`) | Workstream Slice | Handoff Artifact | Verified By |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `{{LOG_TIME_1}}` | `{{AGENT_ID_1}}` | `{{ACTION_1}}` | `{{SLICE_1}}` | `{{HANDOFF_PATH_1}}` | `{{VERIFIER_1}}` |
| `{{LOG_TIME_2}}` | `{{AGENT_ID_2}}` | `{{ACTION_2}}` | `{{SLICE_2}}` | `{{HANDOFF_PATH_2}}` | `{{VERIFIER_2}}` |
