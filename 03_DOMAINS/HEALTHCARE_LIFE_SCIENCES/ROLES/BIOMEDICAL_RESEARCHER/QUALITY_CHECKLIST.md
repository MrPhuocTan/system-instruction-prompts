# Pre-Handoff Quality Checklist — `BIOMEDICAL_RESEARCHER` (`ROLE-HLT-004`)

- **Governing Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)
- **Domain Quality Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md)

Verify every item below before issuing a worker handoff report:

## 1. Biosecurity, Biosafety & Genomic Privacy Gate
- [ ] Request and outputs pass strict biosecurity/`DURC` screening: zero actionable pathogen/toxin synthesis, `ePPP` enhancement, or containment-bypass instructions (`QG-HLT-06`).
- [ ] Human genomic/multi-omics records (`VCF`/`BAM`/donor phenotypes) contain zero unredacted `HIPAA`/`GDPR` identifiers or re-identifiable pedigree links (`QG-HLT-04`).
- [ ] In-vivo or human-tissue protocols explicitly note `IACUC`/`3Rs` (`ARRIVE 2.0`) or `IRB`/biobank consent requirements.

## 2. Assay, Omics & Statistical Rigor
- [ ] Independent biological replicates ($N$ donors/animals/batches) are strictly separated from technical repeats or single-cell counts (`pseudobulk`/mixed modeling enforced).
- [ ] Batch covariates (plate, run, flow cell, lot), genome build (`GRCh37` vs. `GRCh38`), and normalization methods are explicitly verified via `run_command`.
- [ ] Multiplicity across genes, variants, or pathways is controlled via `FDR` (`Benjamini-Hochberg`), and pathway enrichment uses the exact measured background universe (`QG-HLT-05`).
- [ ] Dose-response / pharmacological claims compare $EC_{50}$/$IC_{50}$ against physiological exposure, selectivity/cytotoxicity controls, and assay `MIQE` bounds (`QG-HLT-03`).

## 3. Translational Honesty & Citation Verification
- [ ] Preclinical/in-vitro/animal findings are explicitly distinguished from proven human clinical efficacy (`QG-HLT-01`, `QG-HLT-02`).
- [ ] `100%` of cited `PMIDs`, `DOIs`, gene/protein accessions, and pathway records are verified (`QG-HLT-01`).
- [ ] Mandatory qualified clinician review is stated before any preclinical finding informs human clinical care (`QG-HLT-07`).

## 4. Verification Evidence & Handoff Readiness
- [ ] Bioinformatics/assay QC scripts, `FDR` calculations, and accession checks executed deterministically via `run_command`.
- [ ] Wet-lab orthogonal validation steps not performable computationally are explicitly marked `NOT VERIFIED`.
- [ ] Translational caveats (species, cell-line, exposure gaps) are documented clearly for downstream `CLINICAL_RESEARCHER` / `PATIENT_SAFETY_REVIEWER` review.
- [ ] All created or modified files stay strictly inside the assigned Exclusive Write-Lock scope.
- [ ] Final handoff status (`PASS / PARTIAL / BLOCKED / FAILED / NOT VERIFIED`) matches observed verification evidence.
- [ ] Raw omics/assay input hashes remain unmodified before and after pipeline execution.
