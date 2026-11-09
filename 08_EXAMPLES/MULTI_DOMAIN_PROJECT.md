# End-to-End Walkthrough: Level 4 Multi-Domain Clinical Decision-Support SaaS (`MULTI_DOMAIN_PROJECT.md`)

> **Walkthrough Governance:** Demonstrates **Complexity Level 4** multi-domain coordination across **5 domains** (`HEALTHCARE_LIFE_SCIENCES`, `AI_MACHINE_LEARNING`, `LEGAL_COMPLIANCE`, `CYBERSECURITY`, `IT_SOFTWARE`), showcasing deterministic **Horizontal Conflict Resolution** ([AGENT_GOVERNANCE.md](../00_GLOBAL_CONSTITUTION/AGENT_GOVERNANCE.md)), staged Human Approval Gates ([HUMAN_APPROVAL_POLICY.md](../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md)), and dual `SA + PM` sign-off.

---

## 1. Realistic User Scenario
**User Prompt:**
> "Design and implement our FHIR R4 inpatient Sepsis Early-Warning Clinical Decision Support (CDS) module (`services/cds-sepsis/` + clinician EHR panel `apps/ehr-panel/`). The module scores hourly vitals/labs, explains risk factors to attending clinicians, logs audit trails, and must comply with HIPAA, GDPR, and FDA Non-Device CDS transparency criteria."

---

## 2. Multi-Domain Routing, Persistent Governance & Skill Loading
1. **Complexity Classification:** **Level 4** (patient-safety-adjacent clinical software + PHI/special-category health data + regulated ML inference).
2. **Governance Mesh ([AGENT_COMMUNICATE.md](../06_TEMPLATES/AGENT_COMMUNICATE.md)):** Persistent `PM` + `SA` coordinate alongside domain leads ([DOMAIN_LEAD](../02_CORE_ROLES/DOMAIN_LEAD/SYSTEM_PROMPT.md)) and load domain standards from all 5 domains:
   - **Healthcare & Patient Safety:** [HEALTHCARE_LIFE_SCIENCES/DOMAIN_SYSTEM_PROMPT.md](../03_DOMAINS/HEALTHCARE_LIFE_SCIENCES/DOMAIN_SYSTEM_PROMPT.md), [PATIENT_SAFETY_REVIEWER](../03_DOMAINS/HEALTHCARE_LIFE_SCIENCES/ROLES/PATIENT_SAFETY_REVIEWER/SYSTEM_PROMPT.md), [CLINICAL_RESEARCHER](../03_DOMAINS/HEALTHCARE_LIFE_SCIENCES/ROLES/CLINICAL_RESEARCHER/SYSTEM_PROMPT.md)
   - **AI / Machine Learning:** [AI_EVALUATION_ENGINEER](../03_DOMAINS/AI_MACHINE_LEARNING/ROLES/AI_EVALUATION_ENGINEER/SYSTEM_PROMPT.md) + [MODEL_EVALUATION](../05_SPECIALIZED_SKILLS/MODEL_EVALUATION/SKILL.md)
   - **Legal & Privacy Compliance:** [REGULATORY_ANALYST](../03_DOMAINS/LEGAL_COMPLIANCE/ROLES/REGULATORY_ANALYST/SYSTEM_PROMPT.md), [LEGAL_COMPLIANCE/PRIVACY_SPECIALIST](../03_DOMAINS/LEGAL_COMPLIANCE/ROLES/PRIVACY_SPECIALIST/SYSTEM_PROMPT.md)
   - **Cybersecurity:** [SECURITY_ARCHITECT](../03_DOMAINS/CYBERSECURITY/ROLES/SECURITY_ARCHITECT/SYSTEM_PROMPT.md) + [SECURITY_ASSESSMENT](../05_SPECIALIZED_SKILLS/SECURITY_ASSESSMENT/SKILL.md)
   - **Software & Human-Centric QA:** [FULLSTACK_ENGINEER](../03_DOMAINS/IT_SOFTWARE/ROLES/FULLSTACK_ENGINEER/SYSTEM_PROMPT.md) + [HUMAN_CENTRIC_APPLICATION_QA](../05_SPECIALIZED_SKILLS/HUMAN_CENTRIC_APPLICATION_QA/SKILL.md)

---

## 3. Horizontal Conflict Resolution (Strictest Safety & Privacy Rule Wins)
During Phase 2 contract locking, three cross-domain design conflicts surfaced across Level 4/5 domain norms. Applying the mandatory conflict algorithm (**intersection of permitted actions** + **union of verification gates**):

| Contested Design Point | Initial Engineering / ML Proposal | Competing Safety / Legal / Security Rule | Locked `SA + PM` Resolution (Strictest Rule Wins) |
| :--- | :--- | :--- | :--- |
| **1. Clinical Actionability** | Auto-trigger STAT lactate & broad-spectrum antibiotic EHR order drafts on score `>= 0.75` | `PATIENT_SAFETY_REVIEWER` + `REGULATORY_ANALYST` (21st Century Cures Act Sec. 3060 Non-Device CDS): autonomous order triggering risks over-treatment & reclassifies software as regulated SaMD | **Advisory-Only Clinician-in-the-Loop:** Display calibrated risk tier, raw vital/lab trends (`MAP`, `Lactate`, `WBC`, `RR`), feature contributions, and SOFA reference criteria; require explicit attending physician review and independent order entry. |
| **2. Telemetry Retention for Retraining** | Log full FHIR `Patient` + `Observation` payloads for 180 days in ML feature store | `PRIVACY_SPECIALIST` + `SECURITY_ARCHITECT` (HIPAA Minimum Necessary + GDPR Art. 5/9): raw PHI duplication into ML logs violates minimization | **Zero Raw PHI in ML Logs:** Inference runs statelessly in-memory; audit log stores pseudonymized `encounter_hmac`, model version, input completeness hash, and clinician acknowledgment with KMS envelope encryption (`AES-256-GCM`). |
| **3. Missing Lab Imputation** | Silently median-impute missing arterial `Lactate` and `Bilirubin` | `PATIENT_SAFETY_REVIEWER`: silent normal-value imputation masks occult septic shock (false reassurance hazard) | **Explicit Uncertainty & Stale-Data Gating:** Reject silent median substitution on critical labs `> 6h` stale; render prominent `INCOMPLETE_LABS_UNCERTAINTY` indicator showing exact missing inputs and timestamps. |

---

## 4. Staged Human Approval Gates & Disjoint Implementation
1. **Human Gate #1 (Pre-Implementation Architecture & Regulatory Sign-Off):** Presented the 3 horizontal conflict resolutions, PHI threat model, and non-diagnostic clinical disclaimer boundary via `ask_question` -> `APPROVED` by clinical/product owner.
2. **Disjoint Workstream Execution:**
   - `ws-fhir-cds` (`services/cds-sepsis/**`): Stateless FHIR R4 `Observation` ingestion, mTLS + SMART-on-FHIR `system/Observation.read` scope enforcement, calibrated risk + explicit staleness/missingness evaluator, tamper-evident audit log.
   - `ws-ehr-panel` (`apps/ehr-panel/**`): High-contrast bedside clinical panel displaying timestamped vital trajectories, top contributing physiological drivers, confidence interval, stale-lab warning banner, and **zero decorative `"AI Sign"` badges or alarm-fatigue animations**.
   - `ws-clinical-qa` (`tests/**`, `reports/**`): Subgroup fairness & calibration audit across age/sex/ICU-vs-ward cohorts + 3-Level [QA_REPORT.md](../06_TEMPLATES/QA_REPORT.md).

### Disjoint Exclusive Write-Lock Registry (`AGENT_COMMUNICATE.md` Section 8 Excerpt)
| Workstream ID | Primary Role(s) | Exclusive Owned Paths (`Write-Lock`) | Lock State | Diff Audit |
| :--- | :--- | :--- | :---: | :--- |
| `ws-reg-safety` | `PATIENT_SAFETY_REVIEWER` + `REGULATORY_ANALYST` | `docs/hazard_log.md`, `docs/cures_act_cds_traceability.md` | `RELEASED` | `0` out-of-lock edits |
| `ws-sec-privacy` | `SECURITY_ARCHITECT` + `PRIVACY_SPECIALIST` | `docs/hipaa_gdpr_dpia.md`, `services/cds-sepsis/crypto/**` | `RELEASED` | `0` out-of-lock edits |
| `ws-fhir-cds` | `FULLSTACK_ENGINEER` (Backend FHIR/ML Runtime) | `services/cds-sepsis/api/**`, `services/cds-sepsis/scoring/**` | `RELEASED` | `0` out-of-lock edits |
| `ws-ehr-panel` | `FULLSTACK_ENGINEER` (Clinician Bedside UI) | `apps/ehr-panel/**` | `RELEASED` | `0` out-of-lock edits |
| `ws-clinical-qa` | `AI_EVALUATION_ENGINEER` + `QUALITY_REVIEWER` | `tests/**`, `reports/QA_REPORT.md`, `reports/subgroup_eval.md` | `RELEASED` | `0` out-of-lock edits |

---

## 5. Multi-Domain Verification Matrix (Union of Domain Quality Gates)
Per the horizontal conflict resolution rule, the final build had to pass the **union** of all 5 domains' quality gates simultaneously:

| Domain Lens | Quality Gate / Standard Audited | Independent Verification Executed | Outcome |
| :--- | :--- | :--- | :---: |
| **`HEALTHCARE_LIFE_SCIENCES`** | [HEALTHCARE_LIFE_SCIENCES/QUALITY_GATES.md](../03_DOMAINS/HEALTHCARE_LIFE_SCIENCES/QUALITY_GATES.md) (False-reassurance suppression & raw vital provenance) | Simulated `8h` stale lactate + borderline MAP (`64 mmHg`) -> verified green low-risk state suppressed & `INCOMPLETE_LABS_UNCERTAINTY` rendered | `PASS` |
| **`AI_MACHINE_LEARNING`** | Calibration (`ECE <= 0.02`) & demographic subgroup parity across age/sex/ward | Holdout sensitivity `86.4%`, PPV `41.2%`, `ECE = 0.014`; max subgroup false-negative gap `1.8%` (`< 3.0%` threshold) | `PASS` |
| **`LEGAL_COMPLIANCE`** | 21st Century Cures Act Sec. 3060 Criterion 1–4 + HIPAA Minimum Necessary + GDPR Art. 9 | Confirmed clinician can independently review underlying FHIR vitals, SOFA logic, and cohort study citations without black-box lock-in | `PASS` |
| **`CYBERSECURITY`** | SMART-on-FHIR authz, mTLS, `AES-256-GCM` audit log encryption, zero PHI in stdout | `pytest tests/security/test_phi_redaction.py` -> `0` MRN/name/DOB strings in logs; expired/wrong-ward scopes -> `HTTP 401`/`403` | `PASS` |
| **`IT_SOFTWARE` (3-Level QA)** | [QA_REPORT.md](../06_TEMPLATES/QA_REPORT.md) (`p99` latency `< 250ms`, WCAG AAA bedside legibility, zero `"AI Sign"`) | Load test `200 RPS` -> `p99 = 142ms`; contrast `>= 7.4:1`; full keyboard navigation; zero ornamental AI badges | `PASS` |

---

## 6. Staged Human Gate #2, Clinical Disclaimers & Dual Signoff
- **Human Gate #2 (Pre-Release Clinical Governance Review):** Presented subgroup calibration report, hazard log, and clinician panel screenshots to clinical safety lead via `ask_question` -> `APPROVED FOR SANDBOX PILOT ONLY`.
- **Explicit `NOT VERIFIED` Clinical Boundary:** Prospective multi-hospital clinical outcomes trial, local hospital lab analyzer reference-range calibration, and IRB approval remain mandatory external human prerequisites (`NOT VERIFIED` in software sandbox) logged in [RISK_REGISTER.md](../06_TEMPLATES/RISK_REGISTER.md).
- **`SA_GATE = PASS` ([TECHNICAL_REVIEW.md](../06_TEMPLATES/TECHNICAL_REVIEW.md)) & `PM_GATE = PASS` ([BUSINESS_REVIEW.md](../06_TEMPLATES/BUSINESS_REVIEW.md)):** Issued complete 6-part [FINAL_DELIVERY.md](../06_TEMPLATES/FINAL_DELIVERY.md) with full 5-domain traceability.
