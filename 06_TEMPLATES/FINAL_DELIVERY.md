# 6-Part Final Delivery Package (`FINAL_DELIVERY.md`)

> **Template Governance:** Canonical user-facing delivery structure for `Level 2`–`Level 4` engagements per [REVIEW_AND_SIGNOFF.md](../01_ORCHESTRATION/REVIEW_AND_SIGNOFF.md) and [INDEPENDENT_VERIFICATION.md](../00_GLOBAL_CONSTITUTION/INDEPENDENT_VERIFICATION.md). Issue only after proportional `SA_GATE` and `PM_GATE` completion and active `schedule` timer cleanup via `manage_task`.

---

## Pre-Delivery Integrity Checklist (Internal Gate)
- [ ] `100%` of user requirements satisfied and traced in [BUSINESS_REVIEW.md](./BUSINESS_REVIEW.md).
- [ ] `SA_GATE` ([TECHNICAL_REVIEW.md](./TECHNICAL_REVIEW.md)) and `PM_GATE` ([BUSINESS_REVIEW.md](./BUSINESS_REVIEW.md)) recorded in [AGENT_COMMUNICATE.md](./AGENT_COMMUNICATE.md).
- [ ] Independent verification confirms real behavior (`Tool Success != Task Success`).
- [ ] Verified facts, assumptions, estimates, and `NOT VERIFIED` items are explicitly separated.
- [ ] Zero leaked secrets/credentials, zero unintended dirty files, zero decorative `"AI Sign"` clutter, and all active `schedule` jobs cancelled.

---

## 1. Outcome & Dual Gate Status
- **Overall Delivery Status:** `{{OVERALL_DELIVERY_STATUS}}` (`PASS | PARTIAL | BLOCKED | FAILED | NOT VERIFIED`)
- **SA Technical Signoff (`SA_GATE`):** `{{SA_GATE_STATUS}}` — `{{SA_SIGNOFF_ONE_LINE}}`
- **PM Business & UX Signoff (`PM_GATE`):** `{{PM_GATE_STATUS}}` — `{{PM_SIGNOFF_ONE_LINE}}`
- **Executive Summary:** `{{EXECUTIVE_OUTCOME_SUMMARY}}`

---

## 2. Key Deliverables & Changes
Provide clickable `file://` absolute links for every delivered or modified workspace artifact:
- `[{{DELIVERABLE_1_BASENAME}}](file://{{DELIVERABLE_1_ABS_PATH}})` — `{{DELIVERABLE_1_SUMMARY}}`
- `[{{DELIVERABLE_2_BASENAME}}](file://{{DELIVERABLE_2_ABS_PATH}})` — `{{DELIVERABLE_2_SUMMARY}}`
- `[{{DELIVERABLE_3_BASENAME}}](file://{{DELIVERABLE_3_ABS_PATH}})` — `{{DELIVERABLE_3_SUMMARY}}`

---

## 3. Architecture, Domain & Governance Summary
- **Complexity Level & Active Domains:** `{{COMPLEXITY_LEVEL}}` | `{{ACTIVE_DOMAINS}}`
- **Specialist Roles & Skills Applied:** `{{APPLIED_ROLES_AND_SKILLS}}`
- **Key Architectural & Contract Decisions:** `{{KEY_ARCHITECTURE_SUMMARY}}`

---

## 4. Independent Verification Evidence
Summarize reproducible verification executed per [QA_REPORT.md](./QA_REPORT.md):

| Verification Tier | Command / Inspection Method | Observed Empirical Outcome | Result |
| :--- | :--- | :--- | :---: |
| **Code / Contract (`L1`)** | `{{VERIFY_L1_CMD}}` | `{{VERIFY_L1_OUTCOME}}` | `{{RES_L1}}` |
| **System / Runtime (`L2`)** | `{{VERIFY_L2_CMD}}` | `{{VERIFY_L2_OUTCOME}}` | `{{RES_L2}}` |
| **User / Domain (`L3`)** | `{{VERIFY_L3_METHOD}}` | `{{VERIFY_L3_OUTCOME}}` | `{{RES_L3}}` |

---

## 5. Assumptions, Limitations & Residual Risks
- **Verified Facts:** `{{FINAL_VERIFIED_FACTS}}`
- **Working Assumptions & Estimates:** `{{FINAL_ASSUMPTIONS_ESTIMATES}}`
- **Explicit `NOT VERIFIED` Items & Runtime Tool Constraints:** `{{FINAL_NOT_VERIFIED_ITEMS}}`
- **Residual Risks (from [RISK_REGISTER.md](./RISK_REGISTER.md)):** `{{FINAL_RESIDUAL_RISKS}}`

---

## 6. Next Steps & Operational Commands
1. **Run / Start / Inspect Command:** `{{OPERATIONAL_COMMAND_1}}`
2. **Test / Reproduce Verification Command:** `{{OPERATIONAL_COMMAND_2}}`
3. **Recommended Follow-On Actions:** `{{RECOMMENDED_NEXT_STEPS}}`
