# 9-Item Locked Workstream Contract (`WORKSTREAM_CONTRACT.md`)

> **Template Governance:** Locked jointly by `PM` + `SA` **before** launching parallel worker subagents per [CONTRACT_AND_HANDOFF.md](../01_ORCHESTRATION/CONTRACT_AND_HANDOFF.md) and [FILE_OWNERSHIP_AND_LOCKING.md](../01_ORCHESTRATION/FILE_OWNERSHIP_AND_LOCKING.md). Zero silent interface drift is permitted once locked.

---

## Contract Header
- **Contract ID & Version:** `{{CONTRACT_ID}}` (`{{CONTRACT_VERSION}}`)
- **Contract Status:** `{{CONTRACT_STATUS}}` (`DRAFT | LOCKED | AMENDED_BY_SA_PM | SUPERSEDED`)
- **Locked Timestamp (ISO-8601):** `{{LOCKED_TIMESTAMP}}`

---

## 1. Workstream ID & Accountable Owner
- **Workstream ID:** `{{WORKSTREAM_ID}}`
- **Accountable Runtime Worker ID:** `{{WORKER_AGENT_ID}}` (Registered in [WORKER_REGISTRY.md](./WORKER_REGISTRY.md))
- **Assigned Domain & Role(s):** `{{DOMAIN_NAME}}` — `{{ASSIGNED_ROLES}}`

## 2. Objective & User-Value Context
- **Business / User Problem Solved:** `{{USER_VALUE_CONTEXT}}`
- **Technical / Analytical Mission:** `{{WORKSTREAM_MISSION}}`

## 3. Exact In-Scope & Out-of-Scope Boundaries
- **In-Scope Responsibilities:**
  1. `{{IN_SCOPE_ITEM_1}}`
  2. `{{IN_SCOPE_ITEM_2}}`
- **Explicit Out-of-Scope Exclusions (Owned by Adjacent Streams or Excluded):**
  1. `{{OUT_OF_SCOPE_ITEM_1}}`
  2. `{{OUT_OF_SCOPE_ITEM_2}}`

## 4. Exclusive Owned File / Module Paths (`Write-Lock`)
Cross-checked against Section 8 of [AGENT_COMMUNICATE.md](./AGENT_COMMUNICATE.md) (`0` overlapping writers):
- `{{EXCLUSIVE_PATH_1}}`
- `{{EXCLUSIVE_PATH_2}}`
- **Assigned Handoff Output Path:** `{{HANDOFF_ARTIFACT_PATH}}`

## 5. Locked Input / Output Interfaces
Any proposed deviation requires halting mutation and requesting an `SA + PM` contract amendment.
- **Consumed Inputs (Schemas / APIs / Files / Data Tables):** `{{CONSUMED_INTERFACES_SPEC}}`
- **Produced Outputs (Endpoints / Types / CLI Flags / Artifacts / Error Codes):** `{{PRODUCED_INTERFACES_SPEC}}`

## 6. Domain, Security, License & Hardware Constraints
- **Domain Standards & Regulatory Baselines:** `{{DOMAIN_REGULATORY_CONSTRAINTS}}`
- **Security, RoE & Secret Protection Rules:** `{{SECURITY_PRIVACY_CONSTRAINTS}}`
- **Dependency & License Restrictions:** `{{LICENSE_DEPENDENCY_CONSTRAINTS}}`
- **Host Disk, Memory & CPU/GPU Thermal Safeguards:** `{{HARDWARE_THERMAL_CONSTRAINTS}}`

## 7. Dependencies & Coordination Touchpoints
| Direction (`UPSTREAM` / `DOWNSTREAM`) | Counterparty Workstream | Shared Contract Artifact | Readiness / Sync Condition |
| :--- | :--- | :--- | :--- |
| `{{DEP_DIR_1}}` | `{{COUNTERPARTY_WS_1}}` | `{{SHARED_ARTIFACT_1}}` | `{{SYNC_CONDITION_1}}` |
| `{{DEP_DIR_2}}` | `{{COUNTERPARTY_WS_2}}` | `{{SHARED_ARTIFACT_2}}` | `{{SYNC_CONDITION_2}}` |

## 8. Required Verification Commands & Empirical Evidence
- **Deterministic Command 1:** `{{VERIFICATION_COMMAND_1}}` -> Expected Evidence: `{{EXPECTED_EVIDENCE_1}}`
- **Deterministic Command 2:** `{{VERIFICATION_COMMAND_2}}` -> Expected Evidence: `{{EXPECTED_EVIDENCE_2}}`
- **Behavioral / Edge-Case Proof (`Tool Success != Task Success`):** `{{BEHAVIORAL_PROOF_REQUIREMENT}}`

## 9. Explicit `PM` + `SA` Acceptance Criteria & Sign-Off Lock
- [ ] `{{CRITERION_SA_1}}` (*SA Technical Criterion*)
- [ ] `{{CRITERION_SA_2}}` (*SA Security & Boundary Criterion*)
- [ ] `{{CRITERION_PM_1}}` (*PM User Value, Domain Depth & Clean UX Criterion*)
- **Contract Lock Signatures:** `SA ({{SA_CONVERSATION_ID}})` + `PM ({{PM_CONVERSATION_ID}})`
