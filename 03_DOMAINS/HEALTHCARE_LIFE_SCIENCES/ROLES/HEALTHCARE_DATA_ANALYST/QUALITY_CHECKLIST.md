# Pre-Handoff Quality Checklist — `HEALTHCARE_DATA_ANALYST` (`ROLE-HLT-005`)

- **Governing Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)
- **Domain Quality Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md)

Verify every item below before issuing a worker handoff report:

## 1. PHI De-Identification & Data Governance Gate
- [ ] All `18` `HIPAA Safe Harbor` identifiers and `GDPR Art. 9` direct/quasi-identifiers (including free-text note/header leaks) are verified absent across outputs and logs (`QG-HLT-04`).
- [ ] Small-cell counts ($n < 11$ or stricter workspace policy) and complementary marginal totals that permit back-calculation are suppressed (`QG-HLT-04`).
- [ ] Raw input extracts remain read-only/unmodified with deterministic, versioned transformation scripts.

## 2. Terminology, Unit & Temporal Integrity
- [ ] Clinical code sets (`ICD-10`, `SNOMED CT`, `LOINC`, `RxNorm`, `CPT`) document exact vocabulary versions and distinguish validated phenotypes from raw single billing codes (`QG-HLT-01`).
- [ ] Laboratory `LOINC` measurements harmonize `UCUM` units (`mg/dL` vs. `mmol/L`, etc.), exclude cancelled/error statuses, and pass physiologic plausibility checks.
- [ ] Medication exposure distinguishes written orders from dispensed/administered fills and documents days-supply/`PDC` assumptions.
- [ ] Cohort timelines enforce strict pre-index lookback/continuous-enrollment windows and zero post-index lookahead or immortal-time bias (`QG-HLT-05`).
- [ ] Automated chronology checks (`death_date`, `admission`/`discharge`, `index_date`) and `RECORD` attrition waterfall sums pass via `run_command`.

## 3. Clinical Context, Equity & Clinician Gate
- [ ] Informative-presence, care-fragmentation, and insurance/access disparities are audited before interpreting utilization differences as biological risk (`QG-HLT-02`, `QG-HLT-05`).
- [ ] Adverse outcomes and phenotype misclassification (`PPV`/sensitivity) caveats are explicitly disclosed (`QG-HLT-03`).
- [ ] Mandatory qualified clinician review is specified prior to any clinical workflow or `CDS` use (`QG-HLT-07`).

## 4. Verification Evidence & Handoff Readiness
- [ ] SQL/Python data-quality assertions, `RECORD` waterfall checks, and `PHI`/small-cell scans executed cleanly via `run_command`.
- [ ] Synthetic vs. de-identified real-world dataset provenance and any `NOT VERIFIED` live `EHR` dependencies are explicitly disclosed.
- [ ] Cohort outputs and bias ledgers are prepared for independent `PATIENT_SAFETY_REVIEWER` audit.
- [ ] All created or modified files stay strictly inside the assigned Exclusive Write-Lock scope.
- [ ] Final handoff status (`PASS / PARTIAL / BLOCKED / FAILED / NOT VERIFIED`) aligns with observed data-quality verification.
