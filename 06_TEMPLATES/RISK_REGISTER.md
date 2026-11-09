# Project Risk, Assumption & Mitigation Register (`RISK_REGISTER.md`)

> **Template Governance:** Maintained jointly by `PM` + `SA` (+ `DOMAIN_LEAD` on `Level 3`–`Level 4` work) per [RISK_MANAGEMENT](../04_CROSS_DOMAIN_SKILLS/RISK_MANAGEMENT/SKILL.md) and [HUMAN_APPROVAL_POLICY.md](../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md). Synchronize critical items with Section 14 of [AGENT_COMMUNICATE.md](./AGENT_COMMUNICATE.md).

---

## 1. Register Metadata & Risk Appetite Thresholds
- **Project ID / Name:** `{{PROJECT_ID}}` — `{{PROJECT_NAME}}`
- **Complexity Level & Regulated Domains:** `{{COMPLEXITY_LEVEL}}` | `{{REGULATED_DOMAINS_OR_NONE}}`
- **Last Reviewed Timestamp:** `{{RISK_REVIEW_TIMESTAMP}}`
- **Mandatory Escalation Rule:** Any risk rated `CRITICAL` or implicating destructive operations, production infrastructure, offensive security scope, clinical/patient safety, legal/compliance exposure, or capital allocation MUST trigger an explicit Human Approval Gate via `ask_question` or direct user confirmation prior to execution.

---

## 2. Active Risk Matrix
*Scoring Scale:* `Likelihood` (`LOW | MEDIUM | HIGH`) $\times$ `Impact` (`LOW | MEDIUM | HIGH | CRITICAL`) $\rightarrow$ `Severity` (`LOW | MODERATE | HIGH | CRITICAL`).

| Risk ID | Category (`TECH`/`SEC`/`REG`/`DATA`/`OPS`) | Risk Event & Root Cause | Likelihood | Impact | Severity | Preventive Control | Contingency / Rollback Plan | Owner | Human Gate Required? | Status |
| :--- | :---: | :--- | :---: | :---: | :---: | :--- | :--- | :--- | :---: | :--- |
| `{{RSK_01}}` | `{{CAT_01}}` | `{{RISK_DESC_01}}` | `{{LIK_01}}` | `{{IMP_01}}` | `{{SEV_01}}` | `{{PREV_01}}` | `{{CONT_01}}` | `{{OWN_01}}` | `{{HG_01}}` | `{{STAT_01}}` |
| `{{RSK_02}}` | `{{CAT_02}}` | `{{RISK_DESC_02}}` | `{{LIK_02}}` | `{{IMP_02}}` | `{{SEV_02}}` | `{{PREV_02}}` | `{{CONT_02}}` | `{{OWN_02}}` | `{{HG_02}}` | `{{STAT_02}}` |
| `{{RSK_03}}` | `{{CAT_03}}` | `{{RISK_DESC_03}}` | `{{LIK_03}}` | `{{IMP_03}}` | `{{SEV_03}}` | `{{PREV_03}}` | `{{CONT_03}}` | `{{OWN_03}}` | `{{HG_03}}` | `{{STAT_03}}` |

---

## 3. Working Assumptions & Invalidation Triggers
Separate unverified working assumptions from empirical facts so downstream decisions remain auditable:

| Assumption ID | Assumption Statement | Dependent Workstream(s) | Validation Method | Consequence if Invalidated | Validation Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `{{ASM_01}}` | `{{ASSUMPTION_STATEMENT_01}}` | `{{ASM_STREAMS_01}}` | `{{ASM_VALIDATION_01}}` | `{{ASM_IMPACT_01}}` | `{{ASM_STATUS_01}}` |
| `{{ASM_02}}` | `{{ASSUMPTION_STATEMENT_02}}` | `{{ASM_STREAMS_02}}` | `{{ASM_VALIDATION_02}}` | `{{ASM_IMPACT_02}}` | `{{ASM_STATUS_02}}` |

---

## 4. Human Approval Gate & Escalation Tracking
Every risk with `Human Gate Required? = YES` must log explicit authorization state before consequential execution:

| Risk ID | Consequential Action Implicated | Approval Mechanism (`ask_question` / Written User Reply) | Approver Identity & Timestamp | Decision (`APPROVED`/`DENIED`/`SCOPED`) |
| :--- | :--- | :--- | :--- | :--- |
| `{{HG_RSK_01}}` | `{{HG_ACTION_01}}` | `{{HG_MECHANISM_01}}` | `{{HG_APPROVER_TS_01}}` | `{{HG_DECISION_01}}` |
| `{{HG_RSK_02}}` | `{{HG_ACTION_02}}` | `{{HG_MECHANISM_02}}` | `{{HG_APPROVER_TS_02}}` | `{{HG_DECISION_02}}` |

---

## 5. Early-Warning Indicators & Monitoring Triggers
- **Technical / Performance Thresholds:** `{{EARLY_WARNING_TECH_METRICS}}`
- **Security / Scope / Anomaly Triggers (Immediate Halt Conditions):** `{{IMMEDIATE_HALT_TRIGGERS}}`
- **Host Disk, Memory & CPU/GPU Thermal Ceilings:** `{{HOST_RESOURCE_CEILINGS}}`

---

## 6. Residual Risk & Signoff Disposition
- **Accepted Residual Risks at Delivery:** `{{ACCEPTED_RESIDUAL_RISKS}}`
- **Retired / Mitigated Risks:** `{{RETIRED_RISKS_SUMMARY}}`
- **Synchronized with `SA_GATE` & `PM_GATE` Reviews:** `{{GATE_SYNC_STATUS}}`
- **Disclosed in [FINAL_DELIVERY.md](./FINAL_DELIVERY.md) Section 5:** `{{FINAL_DELIVERY_DISCLOSURE_CHECK}}` (`YES | NO`)
