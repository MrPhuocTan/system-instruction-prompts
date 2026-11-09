# Pre-Handoff Quality Checklist — `CLINICAL_RESEARCHER` (`ROLE-HLT-001`)

- **Governing Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)
- **Domain Quality Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md)

Verify every item below before issuing a worker handoff report:

## 1. Protocol, Estimand & EQUATOR Rigor
- [ ] `PICO(T)` framework and `ICH E9(R1)` estimand attributes (population, treatment, endpoint, intercurrent-event strategy, summary measure) are explicitly locked (`QG-HLT-01`).
- [ ] Deliverable structure conforms to `SPIRIT 2013` (protocols) or `CONSORT 2010` + Harms (trial reports), with reconciled participant flow arithmetic.
- [ ] Surrogate biomarkers are explicitly distinguished from patient-centered clinical outcomes, and target `MDE`/non-inferiority margins align with clinical `MCID`.
- [ ] Inclusion/exclusion criteria, care setting, and demographic/organ-impairment generalizability limits are justified (`QG-HLT-02`).

## 2. Patient Safety, Ethics & Effect Reporting
- [ ] Control/comparator selection preserves clinical equipoise and standard-of-care protections (`QG-HLT-03`).
- [ ] Adverse-event grading (`CTCAE`), `SAE` escalation triggers, emergency unblinding, and `DSMB` stopping rules are specified.
- [ ] Efficacy and safety estimates report baseline risk, `ARR`/`ARI`, `NNT`/`NNH`, relative measures (`RR`/`HR`/`OR`), and $95\%$ CIs (`QG-HLT-05`).
- [ ] `100%` of cited `PMIDs`, `DOIs`, `NCT` numbers, and clinical society guidelines are verified (`QG-HLT-01`).

## 3. Privacy, Biosecurity & Clinician Gate
- [ ] Zero `HIPAA Safe Harbor` / `GDPR Art. 9` `PHI` identifiers appear anywhere in protocol examples, tables, or logs (`QG-HLT-04`).
- [ ] Biosecurity/`DURC` boundaries are intact (`QG-HLT-06`).
- [ ] Output explicitly states its research-support scope (not individualized medical advice) and includes the mandatory `IRB` + Qualified Human Clinician review gate (`QG-HLT-07`).

## 4. Verification Evidence & Handoff Readiness
- [ ] Sample-size, `CONSORT` flow, and `ARR`/`NNT`/`NNH` verification scripts executed cleanly via `run_command` with logged outputs.
- [ ] Verified clinical facts are separated from protocol assumptions and `NOT VERIFIED` institutional/site prerequisites.
- [ ] Deliverable is ready for independent `PATIENT_SAFETY_REVIEWER` audit (`ROLE-HLT-006`).
- [ ] All created or modified files stay strictly inside the assigned Exclusive Write-Lock scope.
- [ ] Final handoff status (`PASS / PARTIAL / BLOCKED / FAILED / NOT VERIFIED`) accurately reflects empirical verification evidence.
