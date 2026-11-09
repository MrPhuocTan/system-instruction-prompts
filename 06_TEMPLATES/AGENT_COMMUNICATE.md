# Central Multi-Agent Communication Bus (`AGENT_COMMUNICATE.md`)

> **Template Governance:** Canonical inter-agent state, write-lock, and sign-off ledger for `Level 2`–`Level 4` work per [AGENT_COMMUNICATION.md](../01_ORCHESTRATION/AGENT_COMMUNICATION.md) and [FILE_OWNERSHIP_AND_LOCKING.md](../01_ORCHESTRATION/FILE_OWNERSHIP_AND_LOCKING.md). Never instantiate for `Level 0`.

## 1. Project Identity
- **Project ID / Name:** `{{PROJECT_ID}}` — `{{PROJECT_NAME}}`
- **Workspace Root:** `{{WORKSPACE_ROOT_ABS_PATH}}`
- **Complexity Level & Active Domains:** `{{COMPLEXITY_LEVEL}}` | `{{ACTIVE_DOMAINS}}`
- **Library Reference:** `{{LIBRARY_ROOT_ABS_PATH}}` (`v1.0.0`)

## 2. Mission & Objectives
- **Primary User Objective:** `{{PRIMARY_USER_OBJECTIVE}}`
- **In-Scope Deliverables:** `{{IN_SCOPE_DELIVERABLES}}`
- **Explicit Out-of-Scope Boundaries:** `{{OUT_OF_SCOPE_BOUNDARIES}}`

## 3. PM & SA Ownership
| Governance Role | Accountable Agent Name | Active `conversationId` | State Hydration Pointer | Authority Scope |
| :--- | :--- | :--- | :--- | :--- |
| **Project Manager (`PM`)** | `{{PM_AGENT_NAME}}` | `{{PM_CONVERSATION_ID}}` | [PROJECT_STATE.md](./PROJECT_STATE.md) | Charter, scope, routing, UX cleanliness, `PM_GATE` |
| **System Architect (`SA`)** | `{{SA_AGENT_NAME}}` | `{{SA_CONVERSATION_ID}}` | [PROJECT_MANIFEST.md](./PROJECT_MANIFEST.md) | Contracts, security, write-locks, tests, `SA_GATE` |

## 4. Current Project Status
- **Lifecycle Phase:** `{{LIFECYCLE_PHASE}}` | **Overall Health:** `{{HEALTH_STATUS}}` (`ON_TRACK | AT_RISK | BLOCKED`)
- **Active Schedule / Progress Timer:** `{{ACTIVE_SCHEDULE_TASK_ID_OR_NONE}}` (20-min `schedule` cadence for tasks `> 15–20 min`; zero shell `sleep`)
- **Last Updated (ISO-8601):** `{{LAST_UPDATED_ISO}}`

## 5. Acceptance Criteria
- [ ] `AC-01`: `{{ACCEPTANCE_CRITERION_1}}` (Verification: `{{AC_1_VERIFICATION}}`)
- [ ] `AC-02`: `{{ACCEPTANCE_CRITERION_2}}` (Verification: `{{AC_2_VERIFICATION}}`)
- [ ] `AC-03`: `{{ACCEPTANCE_CRITERION_3}}` (Verification: `{{AC_3_VERIFICATION}}`)

## 6. Worker Registry
| Worker Agent ID | Assigned Role(s) (`02` / `03`) | Active `conversationId` | Loaded Skills (`04` / `05`) | Reuse / Lifecycle Status |
| :--- | :--- | :--- | :--- | :--- |
| `{{WORKER_ID_1}}` | `{{WORKER_ROLES_1}}` | `{{WORKER_CONV_ID_1}}` | `{{WORKER_SKILLS_1}}` | `{{WORKER_STATUS_1}}` |
| `{{WORKER_ID_2}}` | `{{WORKER_ROLES_2}}` | `{{WORKER_CONV_ID_2}}` | `{{WORKER_SKILLS_2}}` | `{{WORKER_STATUS_2}}` |

## 7. Workstream Ownership
| Workstream ID | Accountable Worker ID | Contract Path | Upstream Dependencies | Gate Status |
| :--- | :--- | :--- | :--- | :--- |
| `{{WS_ID_1}}` | `{{WORKER_ID_1}}` | `{{WS_1_CONTRACT_PATH}}` | `{{WS_1_DEPENDENCIES}}` | `{{WS_1_STATUS}}` |
| `{{WS_ID_2}}` | `{{WORKER_ID_2}}` | `{{WS_2_CONTRACT_PATH}}` | `{{WS_2_DEPENDENCIES}}` | `{{WS_2_STATUS}}` |

## 8. File Ownership
Each mutated file or glob has at most `1` active writer. Cross-stream edits require `SA` contract amendment before mutation.

| Exclusive Owned Path / Glob (`Write-Lock`) | Lock Holder (`Worker ID`) | Lock State (`LOCKED` / `RELEASED`) | Post-Run Diff Audit |
| :--- | :--- | :--- | :--- |
| `{{OWNED_PATH_GLOB_1}}` | `{{WORKER_ID_1}}` | `{{LOCK_STATE_1}}` | `{{DIFF_AUDIT_1}}` |
| `{{OWNED_PATH_GLOB_2}}` | `{{WORKER_ID_2}}` | `{{LOCK_STATE_2}}` | `{{DIFF_AUDIT_2}}` |

## 9. Decisions & Rationale
| Decision ID | Timestamp | Owner (`PM`/`SA`) | Decision & Locked Interface Rule | Rationale & Rejected Alternatives |
| :--- | :--- | :--- | :--- | :--- |
| `{{DEC_ID_1}}` | `{{DEC_TIME_1}}` | `{{DEC_OWNER_1}}` | `{{DEC_SUMMARY_1}}` | `{{DEC_RATIONALE_1}}` |

## 10. Dependencies & Blockers
| Item ID | Type (`DEPENDENCY` / `BLOCKER`) | Affected Workstream | Description & Escalation Owner | Resolution Criteria |
| :--- | :--- | :--- | :--- | :--- |
| `{{BLK_ID_1}}` | `{{BLK_TYPE_1}}` | `{{BLK_STREAM_1}}` | `{{BLK_DESCRIPTION_1}}` | `{{BLK_RESOLUTION_1}}` |

## 11. Event & Handoff Log
- `{{EVENT_TIMESTAMP_1}}` — **`{{EVENT_ACTOR_1}}`**: `{{EVENT_SUMMARY_1}}` (Handoff/Artifact: `{{EVENT_ARTIFACT_PATH_1}}`)
- `{{EVENT_TIMESTAMP_2}}` — **`{{EVENT_ACTOR_2}}`**: `{{EVENT_SUMMARY_2}}` (Handoff/Artifact: `{{EVENT_ARTIFACT_PATH_2}}`)

## 12. Technical Signoff
- **`SA_GATE` Status:** `{{SA_GATE_STATUS}}` (`PASS | PARTIAL | BLOCKED | FAILED | NOT VERIFIED`) — Reference: [TECHNICAL_REVIEW.md](./TECHNICAL_REVIEW.md)
- **SA Verification Summary & Signoff Timestamp:** `{{SA_VERIFICATION_SUMMARY}}` (`{{SA_SIGNOFF_TIMESTAMP}}`)

## 13. Business/UX Signoff
- **`PM_GATE` Status:** `{{PM_GATE_STATUS}}` (`PASS | PARTIAL | BLOCKED | FAILED | NOT VERIFIED`) — Reference: [BUSINESS_REVIEW.md](./BUSINESS_REVIEW.md)
- **PM UX / Requirement Audit & Signoff Timestamp:** `{{PM_VERIFICATION_SUMMARY}}` (`{{PM_SIGNOFF_TIMESTAMP}}`)

## 14. Outstanding Issues
- **Known Limitations, Residual Risks & `NOT VERIFIED` Items:** `{{OUTSTANDING_ISSUES_SUMMARY}}` (Cross-reference [RISK_REGISTER.md](./RISK_REGISTER.md))

## 15. Next Actions
1. `{{NEXT_ACTION_1}}` — **Owner:** `{{NEXT_OWNER_1}}` | **Condition:** `{{NEXT_TRIGGER_1}}`
2. `{{NEXT_ACTION_2}}` — **Owner:** `{{NEXT_OWNER_2}}` | **Condition:** `{{NEXT_TRIGGER_2}}`
