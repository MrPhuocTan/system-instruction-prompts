# Healthcare & Life Sciences Quality Gates (`HEALTHCARE_LIFE_SCIENCES`)

- **Domain ID:** `DOM-09-HEALTHCARE_LIFE_SCIENCES`
- **Governing Standard:** [DOMAIN_SYSTEM_PROMPT.md](./DOMAIN_SYSTEM_PROMPT.md), [INDEPENDENT_VERIFICATION.md](../../00_GLOBAL_CONSTITUTION/INDEPENDENT_VERIFICATION.md) & [HUMAN_APPROVAL_POLICY.md](../../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md)
- **Signoff Consumers:** `PATIENT_SAFETY_REVIEWER`, `DOMAIN_LEAD`, `SYSTEM_ARCHITECT` (`SA_GATE`), `PROJECT_MANAGER` (`PM_GATE`), and Qualified Human Clinician Reviewer

Every deliverable in `HEALTHCARE_LIFE_SCIENCES` (`Level 1`–`Level 4`) must pass the seven mandatory clinical, privacy, and biosecurity gates below using canonical statuses (`PASS`, `PARTIAL`, `BLOCKED`, `FAILED`, `NOT VERIFIED`).

---

## 1. Mandatory Domain Verification Gates (`QG-HLT-01` – `QG-HLT-07`)

### `QG-HLT-01` — Evidence Hierarchy & EQUATOR Reporting Compliance
- **Pass Criteria:** Evidence is explicitly stratified using `GRADE` certainty (`High`, `Moderate`, `Low`, `Very Low`); study structure conforms to the matching `EQUATOR` standard (`CONSORT`, `SPIRIT`, `PRISMA 2020`, `STROBE`/`RECORD`, `TRIPOD+AI`, `STARD`, `ARRIVE 2.0`); `100%` of `PMID`/`DOI`/`NCT` citations are verified; surrogate endpoints are explicitly distinguished from patient-centered clinical outcomes.
- **Fail Trigger:** Treating preclinical, anecdotal, or uncontrolled observational findings as definitive clinical efficacy, or emitting any fabricated medical citation/guideline.

### `QG-HLT-02` — Clinical Context Appropriateness & Population Generalizability
- **Pass Criteria:** Target care setting (outpatient, ED, inpatient, ICU, community), inclusion/exclusion demographics, disease staging, comorbidity burden, pediatric/obstetric/geriatric/renal/hepatic applicability, and health-equity/`SDoH` stratification are explicitly specified.
- **Fail Trigger:** Extrapolating adult tertiary-center or healthy-volunteer findings to vulnerable subpopulations without explicit clinical scope exclusions, or applying unvalidated race-based adjustments.

### `QG-HLT-03` — Patient Safety, Contraindication Screening & Harm Prevention
- **Pass Criteria:** Harms, serious adverse events (`SAEs`), contraindications, narrow-therapeutic-index risks, alert-fatigue/automation-bias failure modes, and safe clinical fallback behaviors (`ISO 14971` / `FMEA`) are evaluated alongside benefits (`NNH` paired with `NNT`).
- **Fail Trigger:** Omitting known adverse effects/contraindications, single-sided efficacy framing, or unsafe clinical decision logic lacking human-override and fail-safe defaults.

### `QG-HLT-04` — PHI / HIPAA / GDPR Privacy Redaction & De-Identification
- **Pass Criteria:** Zero unredacted `HIPAA Safe Harbor` (`18` identifiers) or `GDPR Art. 9` special-category patient identifiers appear in deliverables, logs, code comments, or handoff artifacts; small-cell suppression ($n < 11$ or stricter policy bound) and minimum-necessary data handling are enforced.
- **Fail Trigger:** Exposure of live patient names, MRNs, exact encounter/birth dates, contact details, or re-identifiable rare-disease micro-cells.

### `QG-HLT-05` — Calibrated Uncertainty, Absolute Risk & Limitations Disclosure
- **Pass Criteria:** Effect estimates report baseline risk, absolute risk differences (`ARR`/`ARI`), relative metrics (`RR`/`OR`/`HR`), and $95\%$ confidence/credible intervals; missing-data, confounding (`immortal-time`, `indication`, `informative-presence`), and coding-validity (`PPV`/`sensitivity`) limitations are explicitly documented.
- **Fail Trigger:** Isolated relative-risk hype without baseline/absolute rates, unquantified model calibration drift, or concealed sensitivity failures.

### `QG-HLT-06` — Biosecurity, Biosafety & Dual-Use (`DURC`) Guardrails
- **Pass Criteria:** Deliverable contains zero actionable pathogen/toxin synthesis, `ePPP` virulence/transmissibility enhancement, immune-evasion engineering, or biosafety-containment bypass instructions; applicable `BSL`/`IBC` biosafety assumptions are documented for legitimate preclinical workflows.
- **Fail Trigger:** Any dual-use biological/toxin hazard enablement (`IMMEDIATE HALT + ESCALATION`).

### `QG-HLT-07` — Mandatory Qualified Clinician Review & Non-Prescriptive Boundary
- **Pass Criteria:** Deliverable preserves a strict research/decision-support framing (zero autonomous patient diagnosis, prescribing, or emergency triage) and explicitly specifies the mandatory qualified human clinician review gate required before any real-world patient or clinical-workflow impact.
- **Fail Trigger:** Direct individualized medical directives, unreviewed patient-facing clinical advice, or omission of the qualified clinician signoff requirement.

---

## 2. Gate Enforcement Matrix by Complexity Level

| Gate ID | Gate Name | Level 1 (Scoped) | Level 2 (Multi-Step) | Level 3–4 (Regulated / High-Assurance) |
| :--- | :--- | :--- | :--- | :--- |
| `QG-HLT-01` | Evidence Hierarchy (`GRADE`/EQUATOR) | Source & tier verified | Full `GRADE`/EQUATOR mapping | Independent `MEDICAL_LITERATURE_REVIEWER` / `DOMAIN_LEAD` audit |
| `QG-HLT-02` | Clinical Context & Generalizability | Target population stated | Subgroup & setting bounds | `CLINICAL_RESEARCHER` + `PATIENT_SAFETY_REVIEWER` signoff |
| `QG-HLT-03` | Patient Safety & Harm Prevention | Contraindications noted | Structured risk/harm table | Independent `PATIENT_SAFETY_REVIEWER` `ISO 14971` audit |
| `QG-HLT-04` | `PHI` / `HIPAA` / `GDPR` Privacy | Zero `PHI` check | Automated regex/cell check | `SA_GATE` blocker + small-cell & de-identification audit |
| `QG-HLT-05` | Uncertainty & Absolute Risk | `ARR` + `CI` reported | Bias & calibration sensitivity | Biostatistical + `REPRODUCIBILITY_AUDITOR` verification |
| `QG-HLT-06` | Biosecurity & `DURC` Guardrails | Hard block enforced | Hard block + `BSL` check | Hard block + `SA_GATE` / Human Safety Escalation |
| `QG-HLT-07` | Mandatory Qualified Clinician Gate | Non-prescriptive framing | Explicit clinician review block | Formal Human Approval Gate (`PM_GATE` blocker until recorded) |
