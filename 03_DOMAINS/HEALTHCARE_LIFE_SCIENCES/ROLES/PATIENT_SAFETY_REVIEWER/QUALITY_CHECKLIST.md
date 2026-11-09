# Pre-Handoff Quality Checklist — `PATIENT_SAFETY_REVIEWER` (`ROLE-HLT-006`)

- **Governing Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)
- **Domain Quality Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md)

Verify every item below before issuing a patient-safety gate determination:

## 1. Reviewer Independence & Non-Prescriptive Boundary
- [ ] Safety audit was conducted independently of the authoring subagent (mandatory separation of duties on Level 3–4 deliverables).
- [ ] Deliverable contains zero autonomous patient diagnoses, individualized drug/dose prescriptions, or instructions that could delay emergency care (`QG-HLT-07`).
- [ ] Mandatory review and signoff by a licensed, qualified human clinician (`IRB`/pharmacist/specialist as applicable) is explicitly stated as a pre-deployment blocker (`QG-HLT-07`).

## 2. Clinical Hazard, Contraindication & Equity Audit (`ISO 14971` / `HFMEA`)
- [ ] `HFMEA` / hazard table evaluates foreseeable clinical misuse, false reassurance, missed red flags, and automation-bias failure modes (`QG-HLT-03`).
- [ ] Serious adverse events (`SAEs`), `NNH`, black-box warnings, drug interactions, and vulnerable-subgroup exclusions (pediatric, obstetric, geriatric, renal/hepatic impairment) are explicitly verified (`QG-HLT-02`, `QG-HLT-03`).
- [ ] Numerical expressions obey `ISMP` medication-safety rules (zero trailing `X.0` zeros, mandatory leading `0.X` zeros, unambiguous `UCUM` units) and pair relative risk with baseline/absolute risk (`QG-HLT-05`).
- [ ] Subgroup calibration/equity checks confirm zero unvalidated race-based physiological adjustments (`QG-HLT-02`).

## 3. Privacy, Biosecurity & Citation Verification
- [ ] Automated and manual checks confirm zero `HIPAA`/`GDPR` `PHI` identifiers and complete small-cell ($n < 11$) suppression (`QG-HLT-04`).
- [ ] Deliverable is `100%` clear of `DURC`/`ePPP`/toxin biosecurity hazards (`QG-HLT-06`) and fabricated `PMID`/`FDA`/guideline citations (`QG-HLT-01`).
- [ ] Referenced drug labels (`DailyMed`/`FDA`), black-box warnings, and guideline versions are current and free of retracted sources.
- [ ] Clinical decision support (`CDS`) outputs expose transparent clinical rationale, inputs, and uncertainty intervals rather than opaque risk scores (`QG-HLT-05`).

## 4. Safety Gate Determination & Escalation Evidence
- [ ] `ISO 14971` / `HFMEA` hazard register documents severity, likelihood, inline risk controls, and residual risk status for every identified clinical hazard.
- [ ] Boundary/unit/threshold audit scripts and authoritative drug-label/guideline checks are logged with reproducible evidence.
- [ ] Any unresolved severe harm, `PHI` leak, or prescriptive medical directive is set to `BLOCKED` or `FAILED` (`never` waived to `PASS`).
- [ ] Candidate authoring files remained read-only; safety audit artifacts were written strictly inside assigned Exclusive Write-Lock paths.
- [ ] Explicit human escalation checklist is ready for `SA_GATE`, `PM_GATE`, and Qualified Human Clinician signoff.
- [ ] Automated safety review explicitly discloses that it does not substitute for licensed clinical practitioner judgment.
