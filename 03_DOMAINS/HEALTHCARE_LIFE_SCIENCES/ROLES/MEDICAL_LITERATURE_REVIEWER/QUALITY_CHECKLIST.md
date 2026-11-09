# Pre-Handoff Quality Checklist — `MEDICAL_LITERATURE_REVIEWER` (`ROLE-HLT-002`)

- **Governing Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)
- **Domain Quality Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md)

Verify every item below before issuing a worker handoff report:

## 1. PRISMA Search & Citation Integrity
- [ ] Clinical `PICO(T)` scope, eligible study designs, and prioritized efficacy + harm outcomes are explicitly defined (`QG-HLT-01`).
- [ ] `MEDLINE`/`PubMed`/`ClinicalTrials.gov` search strings, retrieval dates, and reconciled `PRISMA 2020` flow counts are documented.
- [ ] `100%` of cited `PMIDs`, `DOIs`, `NCT` numbers, authors, and publication years are verified against primary sources—zero fabricated citations (`QG-HLT-01`).
- [ ] Retractions, errata, non-peer-reviewed `medRxiv` preprints, and `ABSTRACT_ONLY_INSPECTED` paywalled studies are explicitly flagged.

## 2. Risk-of-Bias & GRADE Synthesis Rigor
- [ ] Validated study-appropriate appraisal tools (`RoB 2`, `ROBINS-I`, `QUADAS-2`, `PROBAST`, `AGREE II`) are applied per included study/guideline.
- [ ] `GRADE` certainty (`High`, `Moderate`, `Low`, `Very Low`) is justified per outcome across bias, inconsistency ($\tau^2$/$I^2$), indirectness, imprecision, and publication bias.
- [ ] Randomized trials and observational cohorts are stratified rather than naively pooled together.
- [ ] Summary-of-Findings tables report baseline control risk, `ARR`/`ARI`, `NNT`/`NNH`, relative effects, and $95\%$ CIs verified from raw counts (`QG-HLT-03`, `QG-HLT-05`).

## 3. Clinical Context, Safety & Non-Prescriptive Framing
- [ ] Target care setting, demographic inclusions/exclusions, and surrogate-vs-clinical endpoint distinctions are clear (`QG-HLT-02`).
- [ ] Adverse events, contraindications, and discordant specialty guidelines are transparently reported (`QG-HLT-03`).
- [ ] Zero `PHI` is present (`QG-HLT-04`), and mandatory qualified human clinician review is prominently stated (`QG-HLT-07`).

## 4. Verification Evidence & Handoff Readiness
- [ ] `PMID`/`DOI`/`NCT` verification logs, search strings, and `NNT`/`NNH` recomputation scripts are saved for independent audit.
- [ ] `ABSTRACT_ONLY_INSPECTED` and `UNVERIFIED_EXTERNAL_CITATION` items are explicitly segregated from full-text verified evidence.
- [ ] Synthesis is ready for independent `PATIENT_SAFETY_REVIEWER` hazard check on Level 3–4 clinical tasks.
- [ ] All created or modified files stay strictly inside the assigned Exclusive Write-Lock scope.
- [ ] Final handoff status (`PASS / PARTIAL / BLOCKED / FAILED / NOT VERIFIED`) aligns with observed verification evidence.
