# 3-Level Human-Centric Application QA Report (`QA_REPORT.md`)

> **Template Governance:** Executed by an independent QA / Reviewer agent per [HUMAN_CENTRIC_APPLICATION_QA](../05_SPECIALIZED_SKILLS/HUMAN_CENTRIC_APPLICATION_QA/SKILL.md) and [BROWSER_AND_GUI_INTERACTION](../05_SPECIALIZED_SKILLS/BROWSER_AND_GUI_INTERACTION/SKILL.md). Enforces Code-Level, System-Level, and User-Level verification plus mandatory GUI tool availability disclosure.

---

## 1. QA Metadata & Runtime GUI Tool Availability Disclosure
- **QA Report ID / Project ID:** `{{QA_REPORT_ID}}` / `{{PROJECT_ID}}`
- **Independent QA Agent (`conversationId`):** `{{QA_AGENT_ID}}` (`{{QA_CONVERSATION_ID}}`) — *Confirmed non-author of code under test*
- **Target Build / Commit / Environment:** `{{TARGET_ENV_SUMMARY}}`
- **Mandatory GUI / Browser Tool Availability Disclosure:**
  - **Interactive Browser / GUI Automation Status:** `{{GUI_TOOL_STATUS}}` (`AVAILABLE: {{DETECTED_TOOLS}}` | `UNAVAILABLE IN CURRENT SESSION`)
  - **Verification Fidelity Attestation:** `{{GUI_ATTESTATION}}` (*If GUI tools are unavailable, explicitly disclose that limitation, record exact programmatic HTTP/API/DOM/CLI verification run, and NEVER claim manual UI clicks or visual checks that did not occur.*)
- **Overall QA Gate Status:** `{{QA_GATE_STATUS}}` (`PASS | PARTIAL | BLOCKED | FAILED | NOT VERIFIED`)

---

## 2. Level 1 — Code-Level & Deterministic Contract Evaluation
Validates static correctness, compilation, type safety, lint hygiene, schema parity, and isolated unit suites.

| Check Area | Command Executed | Exit Code | Coverage / Contract Result | Verdict |
| :--- | :--- | :---: | :--- | :--- |
| **Build & Typecheck** | `{{CMD_BUILD_TYPECHECK}}` | `{{L1_EXIT_1}}` | `{{L1_RESULT_1}}` | `{{L1_VERDICT_1}}` |
| **Lint & Static Security** | `{{CMD_LINT_SAST}}` | `{{L1_EXIT_2}}` | `{{L1_RESULT_2}}` | `{{L1_VERDICT_2}}` |
| **Unit & Schema Tests** | `{{CMD_UNIT_SCHEMA}}` | `{{L1_EXIT_3}}` | `{{L1_RESULT_3}}` | `{{L1_VERDICT_3}}` |

---

## 3. Level 2 — System-Level & Stateful Runtime Evaluation
Validates live runtime execution, cross-layer consistency (UI/CLI <-> HTTP/WS <-> Database/Filesystem), concurrency, and failure handling (`HTTP 200 != Business Logic Correct`).

| System Integration Flow | Stimulus / Payload | Observed API / CLI Response | Verified DB / Storage / Log State | Verdict |
| :--- | :--- | :--- | :--- | :--- |
| **Valid Stateful Mutation** | `{{L2_VALID_INPUT}}` | `{{L2_VALID_RESPONSE}}` | `{{L2_DB_STATE_1}}` | `{{L2_VERDICT_1}}` |
| **Invalid / Boundary Input** | `{{L2_INVALID_INPUT}}` | `{{L2_INVALID_RESPONSE}}` | `{{L2_DB_STATE_2}}` | `{{L2_VERDICT_2}}` |
| **Auth / Authz Isolation** | `{{L2_AUTHZ_PROBE}}` | `{{L2_AUTHZ_RESPONSE}}` | `{{L2_AUDIT_LOG_STATE}}` | `{{L2_VERDICT_3}}` |

---

## 4. Level 3 — User-Level & Human-Centric UX Evaluation
Distinguishes: `(1) Exists in Code` vs. `(2) Isolated Functional` vs. `(3) Genuinely Works for End User`.

| End-to-End User Journey | Navigation, Inputs & Controls Exercised | Loading / Empty / Error / Success States | Responsive / A11y / Zero `"AI Sign"` Check | Readiness Tier (`1`/`2`/`3`) |
| :--- | :--- | :--- | :--- | :---: |
| `{{JOURNEY_1_NAME}}` | `{{JOURNEY_1_CONTROLS}}` | `{{JOURNEY_1_STATES}}` | `{{JOURNEY_1_UX_CHECK}}` | `{{TIER_1}}` |
| `{{JOURNEY_2_NAME}}` | `{{JOURNEY_2_CONTROLS}}` | `{{JOURNEY_2_STATES}}` | `{{JOURNEY_2_UX_CHECK}}` | `{{TIER_2}}` |

---

## 5. Defect Ledger & Reproduction Evidence
| Bug ID | Severity | Layer (`L1`/`L2`/`L3`) | Reproducible Steps | Expected vs. Observed | Screenshot / Log Path | Status |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- |
| `{{BUG_ID_1}}` | `{{BUG_SEV_1}}` | `{{BUG_LAYER_1}}` | `{{BUG_STEPS_1}}` | `{{BUG_DIFF_1}}` | `{{BUG_EVIDENCE_1}}` | `{{BUG_STATUS_1}}` |

- **Linked Signoff Consumers:** [TECHNICAL_REVIEW.md](./TECHNICAL_REVIEW.md) (`SA_GATE`) and [BUSINESS_REVIEW.md](./BUSINESS_REVIEW.md) (`PM_GATE`).
