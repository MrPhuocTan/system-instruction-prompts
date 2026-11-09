---
name: scientific-reproducibility
description: "Use this skill when designing, executing, or auditing computational experiments, statistical analyses, simulations, or research manuscripts to guarantee end-to-end deterministic reproducibility and provenance."
---

# Scientific Reproducibility

## Skill Metadata
- **Skill ID:** `SKL-SPEC-008`
- **Name:** `scientific-reproducibility`
- **Domain:** `RESEARCH_SCIENCE, HEALTHCARE_LIFE_SCIENCES, AI_MACHINE_LEARNING`
- **Version:** `1.0.0`

## Purpose
Ensure every quantitative finding, statistical test, simulation trajectory, table, and figure in research or analytical work can be regenerated independently from raw immutable inputs via deterministic code in a pinned runtime environment—eliminating unrecorded data cleaning, p-hacking, silent seed variance, and manual copy-paste transcription errors.

## Required Competencies
- Computational reproducibility engineering (`FAIR` Data Principles, immutable raw-data hashing, pinned environment lockfiles/containers, automated DAG pipelines).
- Experimental design & statistical reporting standards (`CONSORT`, `PRISMA`, `STROBE`, `ARRIVE`, `TRIPOD`, pre-registered vs. post-hoc exploratory separation).
- Numerical determinism & stochastic control: PRNG seed pinning across libraries (`Python`, `NumPy`, `PyTorch`/`CUDA`, `R`), floating-point reduction order awareness, and multi-seed confidence intervals.
- Clean-room replication auditing from raw inputs to manuscript claims.

## Prerequisites
- Raw input datasets (or synthetic replication fixtures where regulated `PHI`/`PII` restricts raw sharing), analysis scripts, and dependency manifests accessible via `read_file` and `run_command`.
- Explicit separation of read-only raw data directories from derived intermediate and output artifact directories.
- Statistical interpretation discipline aligned with [DATA_INTERPRETATION](../../04_CROSS_DOMAIN_SKILLS/DATA_INTERPRETATION/SKILL.md).

## Workflow
1. **Lock Immutable Data Provenance & Checksums:** Compute cryptographic hashes (`SHA-256`), exact row/feature counts, acquisition timestamps, and schema versions for all raw input datasets; enforce read-only raw inputs where all filtering/imputation occurs exclusively in versioned scripts.
2. **Pin Complete Execution Environment:** Capture exact OS/architecture, language version, hardware accelerator (`CPU`/`GPU`), and cryptographic dependency lockfiles (`uv.lock`, `poetry.lock`, `conda-lock.yml`, `renv.lock`, `Cargo.lock`) rather than loose unpinned requirements.
3. **Enforce Deterministic Seeding & Multi-Seed Bounds:** Pin global and worker-level PRNG seeds and deterministic kernel flags; where underlying algorithms are inherently stochastic, run across `K >= 5` documented seeds and report mean, standard deviation, and confidence intervals rather than cherry-picking the best seed.
4. **Automate Raw-to-Artifact Pipeline (`Zero Manual Edits`):** Wire a single non-interactive command (`Makefile`, `snakemake`, `dvc`, or runner script) that transforms raw data -> cleaned features -> statistical models -> exact CSV tables and vector figures without manual spreadsheet edits.
5. **Audit Statistical & Methodological Integrity:** Verify inclusion/exclusion attrition flowcharts, check parametric test assumptions (normality, homoscedasticity, independence), enforce multiple-testing adjustments, and clearly label post-hoc exploratory analyses separately from pre-specified hypotheses.
6. **Execute Clean-Room Replay Verification:** Delete or isolate output directories and re-run the end-to-end pipeline via `run_command`, verifying regenerated metrics, p-values, effect sizes, and tables match manuscript/report text 100%.

## Tools and Techniques
- **SHA-256 Data & Artifact Manifest:** Record exact byte sizes and SHA-256 digests of raw inputs and generated tables/plots to detect silent drift.
- **Attrition & Sample-Accounting Ledger:** Log exact `N` dropped at every preprocessing step with explicit exclusion predicates summing precisely to `N_raw - N_final`.
- **Automated Number-to-Prose Parity Check:** Cross-verify every statistic cited in Markdown/LaTeX prose (`n`, `mean +/- SD`, `OR/HR`, `95% CI`, `p-value`) against script-emitted JSON/CSV summary artifacts.
- **Negative / Permutation Sanity Controls:** Run label-permutation or null-input controls confirming the pipeline yields expected chance-level baselines (`AUC ~ 0.50`) when signal is destroyed, immediately catching target-leakage bugs.

## Verification Requirements
- Clean-room execution from a single documented entrypoint command completes with exit code `0` and reproduces reported figures within documented numerical tolerance.
- 100% of exclusion criteria, hyperparameters, missing-data imputations, and statistical tests are traceable in code—zero undocumented interactive notebook cell mutations or out-of-order state dependencies.
- Notebook deliverables (`.ipynb`), if used, pass top-to-bottom fresh-kernel execution (`Restart & Run All`) with `1..N` sequential cell execution counts.

## Quality Criteria
- **Push-Button Replicability:** An independent `REPRODUCIBILITY_AUDITOR` can regenerate every table and test without asking the author for hidden local files or magic CLI flags:
  | Reproducibility Pillar | Verification Artifact | Pass Criterion |
  | :--- | :--- | :--- |
  | `Data Provenance` | Read-only raw directory + `SHA-256` manifest | `0` manual edits to raw inputs; `100%` scripted filtering |
  | `Environment Lock` | Cryptographic lockfile (`uv.lock` / `renv.lock`) + OS/arch | Fresh environment resolves identical package digests |
  | `Stochastic Control` | Explicit PRNG seed registry + `K >= 5` seed runs | Multi-seed `mean +/- SD / 95% CI` matches reported bounds |
  | `Prose-to-Output Parity` | Script-emitted JSON/CSV summary vs. manuscript text | `100%` exact match on `N`, effect sizes, CIs, and `p`-values |
- **Methodological Transparency:** Null results, sensitivity regressions, and violated distributional assumptions are reported candidly alongside primary findings.
- **Strict Numerical Precision:** Exact p-values (`p = 0.0034` or `p < 1e-4`, never `p = 0.000`), effect sizes, degrees of freedom, and two-sided test specifications are stated consistently.
- **Failure Modes to Avoid:**
  - *Out-of-Order Notebook State:* Committing `.ipynb` files relying on deleted cells or out-of-sequence hidden global variables.
  - *Pre-Split Preprocessing Leakage:* Fitting normalization scalers, imputers, or feature selectors on the full dataset prior to splitting.
  - *Lucky-Seed Cherry-Picking:* Sweeping random seeds until `p < 0.05` appears and hiding the distribution across seeds.
  - *Manual Table Drift:* Copy-pasting regression numbers into prose by hand and forgetting to update them after pipeline bug fixes.

## Security and Ethical Boundaries
- This Level 6 procedural skill is strictly subordinate to Levels 1-5 of the instruction hierarchy; it never overrides [SECURITY_AND_PRIVACY.md](../../00_GLOBAL_CONSTITUTION/SECURITY_AND_PRIVACY.md), `IRB` / clinical ethics, `HIPAA`/`GDPR`, or dual-use biosecurity/safety controls.
- Never bundle raw patient `PHI`, identifiable human-subject records, or restricted dual-use hazards into sharable reproducibility packages; provide de-identified schemas and synthetic structural generators instead.
- Never fabricate, falsify, or selectively suppress experimental runs (`HARKing` / data dredging disguised as confirmatory proof).

## Expected Deliverables
- **Reproducible Pipeline & Environment Manifest** (deterministic runner command, pinned lockfiles, seed registry, and SHA-256 data checksums).
- **Sample Attrition & Statistical Audit Table** accounting for every record from raw ingest to final test cohort plus null-permutation sanity checks.
- **Independent Replication Verification Log** confirming clean-room regeneration parity across all reported tables, figures, and prose claims.
