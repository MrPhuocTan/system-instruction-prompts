# Pre-Handoff Quality Checklist — `REPRODUCIBILITY_AUDITOR` (`ROLE-SCI-006`)

- **Governing Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)
- **Domain Quality Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md)

Verify every item below before issuing a reproducibility signoff report:

## 1. Environment, Lineage & Raw Data Integrity
- [ ] Auditor independence is preserved (separate from authoring worker on Level 3–4 tasks) and untrusted code was inspected before execution.
- [ ] Runtime interpreter versions, OS/hardware assumptions, and dependency lockfiles are documented and free of hardcoded user-local paths (`QG-SCI-06`).
- [ ] Raw input datasets have recorded `SHA-256` checksums that remain identical before and after full pipeline execution (`QG-SCI-04`).
- [ ] Preprocessing scripts log exact row counts at every filter/join/exclusion step and exhibit zero train/test or post-treatment leakage.

## 2. Clean-Run Execution & Determinism
- [ ] End-to-end pipeline was executed into a clean target directory via `run_command` without manual edits or undocumented steps (`QG-SCI-06`).
- [ ] `PRNG` seeds are explicitly pinned across all active stochastic libraries (`random`, `numpy`, `scipy`, `torch`/`jax`, R `set.seed`).
- [ ] Secondary seed or Monte Carlo SE check confirms substantive scientific conclusions are invariant to benign seed variation.
- [ ] Any HPC/hardware-constrained stages that could not be re-executed locally are explicitly tagged `NOT VERIFIED` rather than `PASS`.

## 3. Claim-to-Artifact Reconciliation & Hygiene
- [ ] `100%` of sample sizes ($N$), point estimates, confidence intervals, test statistics, and figures in the report reconcile with regenerated outputs within documented tolerance (`QG-SCI-05`).
- [ ] Summary statistics pass internal arithmetic/granularity consistency checks (`GRIM`/margin totals).
- [ ] Replication package contains zero leaked API keys, credentials, or unredacted human-subject PII (`QG-SCI-07`).

## 4. Audit Evidence & Signoff Determination
- [ ] Pre-run and post-run `SHA-256` checksum tables, exact `run_command` commands, exit codes, and runtime durations are recorded in the audit report.
- [ ] Numerical discrepancies exceeding tolerance are cataloged with exact file/line origin, severity, and remediation steps.
- [ ] Authoring source files were treated as read-only; audit outputs were written strictly inside assigned Exclusive Write-Lock paths.
- [ ] Final reproducibility gate determination (`PASS / PARTIAL / BLOCKED / FAILED / NOT VERIFIED`) is backed by deterministic evidence for `SA_GATE` and `PM_GATE`.
- [ ] Any residual environment differences (OS architecture, BLAS/GPU non-determinism) are explicitly documented.
