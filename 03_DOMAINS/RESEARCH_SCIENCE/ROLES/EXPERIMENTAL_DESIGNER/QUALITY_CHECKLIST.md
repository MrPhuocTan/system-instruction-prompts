# Pre-Handoff Quality Checklist — `EXPERIMENTAL_DESIGNER` (`ROLE-SCI-004`)

- **Governing Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)
- **Domain Quality Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md)

Verify every item below before issuing a worker handoff report:

## 1. Design Matrix, Resolution & Orthogonality
- [ ] Controllable factors, levels/ranges, held-constant variables, nuisance factors, and primary/guardrail responses are explicitly tabulated (`QG-SCI-01`).
- [ ] Design architecture (full/fractional factorial, block, split-plot, crossover, `RSM`) avoids naive `OFAT` and documents exact alias/confounding relations (`QG-SCI-03`).
- [ ] Matrix orthogonality, `VIF`, center-point curvature checks, and error degrees of freedom are verified programmatically via `run_command`.
- [ ] Split-plot or hard-to-change factors explicitly separate whole-plot and subplot error strata.

## 2. Randomization, Controls & Measurement Calibration
- [ ] Run order and unit allocation are generated with a documented, deterministic `PRNG` seed to prevent batch/temporal drift confounding (`QG-SCI-06`).
- [ ] Positive controls, negative/sham controls, and instrument calibration/drift check runs are embedded at specified intervals (`QG-SCI-04`).
- [ ] True biological/experimental replicates ($N$) are clearly separated from repeated technical measurements ($k$).
- [ ] Allocation concealment, blinding roles, and Sample Ratio Mismatch (`SRM`) diagnostics are specified where applicable.

## 3. Power, Stopping Rules & Safety Envelopes
- [ ] Sample-size / replicate count is justified against target `MDE`, variance estimates, and multiplicity adjustments (`QG-SCI-05`).
- [ ] Interim monitoring or early-stopping rules lock alpha-spending boundaries or pre-outcome quality exclusions (zero optional-stopping `peeking`).
- [ ] Physical, thermal, compute, ethical (`IRB`/`IACUC`), and dual-use safety limits are verified across all factor corners (`QG-SCI-07`).

## 4. Verification Evidence & Handoff Readiness
- [ ] Design-matrix generation scripts, orthogonality/`VIF` checks, and power simulations executed cleanly via `run_command`.
- [ ] Run-order table (`CSV`/Markdown), `PRNG` seed value, and alias structure are saved for independent `REPRODUCIBILITY_AUDITOR` verification.
- [ ] Physical benchtop or field-execution steps not performable in software are explicitly labeled `NOT VERIFIED` pending lab execution.
- [ ] All created or modified files stay strictly inside the assigned Exclusive Write-Lock scope.
- [ ] Final handoff status (`PASS / PARTIAL / BLOCKED / FAILED / NOT VERIFIED`) accurately reflects empirical verification evidence.
- [ ] Cross-stream dependencies with `STATISTICIAN` or `RESEARCH_SCIENTIST` are documented clearly.
