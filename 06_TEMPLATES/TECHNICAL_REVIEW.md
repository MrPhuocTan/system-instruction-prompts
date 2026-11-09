# System Architect Technical Signoff Audit (`TECHNICAL_REVIEW.md`)

> **Template Governance:** Executed by `SYSTEM_ARCHITECT` (`ROLE-CORE-002`) — supported by `DOMAIN_LEAD` / `QUALITY_REVIEWER` where applicable — to issue the formal `SA_GATE` verdict per [REVIEW_AND_SIGNOFF.md](../01_ORCHESTRATION/REVIEW_AND_SIGNOFF.md) and [INDEPENDENT_VERIFICATION.md](../00_GLOBAL_CONSTITUTION/INDEPENDENT_VERIFICATION.md). Reviewer MUST be independent of implementation authorship.

---

## 1. Review Metadata & Gate Verdict
- **Review ID / Project ID:** `{{TECH_REVIEW_ID}}` / `{{PROJECT_ID}}`
- **Audited Workstreams & Handoffs:** `{{AUDITED_WORKSTREAMS}}` (linked to [HANDOFF_REPORT.md](./HANDOFF_REPORT.md) artifacts)
- **Accountable Reviewer (`SA` `conversationId`):** `{{SA_AGENT_NAME}}` (`{{SA_CONVERSATION_ID}}`)
- **`SA_GATE` Verdict:** `{{SA_GATE_VERDICT}}` (`PASS | PARTIAL | BLOCKED | FAILED | NOT VERIFIED`)
- **Review Timestamp (ISO-8601):** `{{REVIEW_TIMESTAMP}}`

---

## 2. Architectural, Contract & Write-Lock Audit Matrix
| Audit Dimension | Verification Method Executed by `SA` | Observed Finding | Verdict (`PASS`/`FAIL`) |
| :--- | :--- | :--- | :--- |
| **Contract & Schema Fidelity** | Diff implementation against [WORKSTREAM_CONTRACT.md](./WORKSTREAM_CONTRACT.md) | `{{CONTRACT_FINDING}}` | `{{VERDICT_1}}` |
| **Exclusive Write-Lock Integrity** | Audit modified paths against Section 8 of [AGENT_COMMUNICATE.md](./AGENT_COMMUNICATE.md) | `{{LOCK_FINDING}}` | `{{VERDICT_2}}` |
| **Cross-Module Integration** | Execute live interface/boundary integration tests | `{{INTEGRATION_FINDING}}` | `{{VERDICT_3}}` |
| **Zero-Trust Security & Secrets** | Scan diffs/logs for credentials, authz bypass, injection, unsafe defaults | `{{SECURITY_FINDING}}` | `{{VERDICT_4}}` |
| **Domain Quality Gates** | Verify all criteria in `03_DOMAINS/{{DOMAIN}}/QUALITY_GATES.md` | `{{DOMAIN_GATE_FINDING}}` | `{{VERDICT_5}}` |
| **Host Disk, Memory & Thermal Safety** | Inspect process footprints, temp artifacts, CPU/GPU bounds | `{{RESOURCE_FINDING}}` | `{{VERDICT_6}}` |

---

## 3. Independent Reproduction of Verification Evidence
`SA` never accepts worker self-attestation without independent command execution (`Tool Success != Task Success`):

| Independent Check Run by `SA` | Command / Audit Script | Exit Code | Observed Output & Edge-Case Verification |
| :--- | :--- | :---: | :--- |
| `{{SA_CHECK_1}}` | `{{SA_CMD_1}}` | `{{SA_EXIT_1}}` | `{{SA_OBSERVED_1}}` |
| `{{SA_CHECK_2}}` | `{{SA_CMD_2}}` | `{{SA_EXIT_2}}` | `{{SA_OBSERVED_2}}` |

---

## 4. Technical Defect & Risk Disposition Ledger
| Defect ID | Severity (`CRITICAL`/`HIGH`/`MEDIUM`/`LOW`) | File / Component | Technical Description & Repro | Required Remediation | Blocking `SA_GATE`? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `{{DEF_ID_1}}` | `{{DEF_SEV_1}}` | `{{DEF_PATH_1}}` | `{{DEF_DESC_1}}` | `{{DEF_FIX_1}}` | `{{DEF_BLOCKS_1}}` |

*Severity Rule:* Any unresolved `CRITICAL` or `HIGH` defect, unauthorized file mutation, or unverified security boundary automatically forces `SA_GATE = BLOCKED` or `FAILED`.

---

## 5. Signoff Conditions & Handoff to `PM_GATE`
- **Residual Technical Risks Logged in [RISK_REGISTER.md](./RISK_REGISTER.md):** `{{RESIDUAL_TECH_RISKS}}`
- **Explicit `NOT VERIFIED` Runtime Boundaries:** `{{TECH_NOT_VERIFIED_ITEMS}}`
- **SA Formal Determination:** `{{SA_FORMAL_SIGNOFF_STATEMENT}}`
