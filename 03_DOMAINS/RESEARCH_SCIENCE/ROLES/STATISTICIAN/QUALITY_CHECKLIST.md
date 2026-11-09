# Pre-Handoff Quality Checklist — `STATISTICIAN` (`ROLE-SCI-003`)

- **Governing Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)
- **Domain Quality Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md)

Verify every item below before issuing a worker handoff report:

## 1. Statistical Analysis Plan & Power Rigor
- [ ] Primary/secondary endpoints, covariate sets, and hypothesis families are locked in a clear `SAP` structure (`QG-SCI-01`).
- [ ] Sample-size, statistical power, or Minimum Detectable Effect (`MDE`) calculations document assumed variance, `ICC`, alpha, and attrition (`QG-SCI-05`).
- [ ] True independent experimental/observational unit ($N$) is modeled accurately; hierarchical clustering or repeated measures use mixed effects, `GEE`, or cluster-robust SEs (`QG-SCI-04`).
- [ ] Null findings (`p > 0.05`) are evaluated via confidence-interval width, `MDE`, or `TOST`/`ROPE` equivalence bounds—never asserted as proof of zero effect without bounds.

## 2. Model Diagnostics, Missingness & Multiplicity Control
- [ ] Likelihood family and link function match outcome support, dispersion, and censoring structure.
- [ ] Model diagnostics are executed and reported (residual/QQ/heteroscedasticity checks, `VIF`, proportional hazards, or Bayesian `R-hat <= 1.01`, `ESS`, zero divergences).
- [ ] Multiplicity across multiple endpoints, arms, subgroups, or interim looks is controlled via documented `FWER` or `FDR` methods (`QG-SCI-05`).
- [ ] Missingness frequencies and mechanisms (`MCAR`/`MAR`/`MNAR`) are audited; imputation (`MICE`) or sensitivity bounds are verified against complete-case baselines.

## 3. Numerical Verification & Reporting Integrity
- [ ] Every reported inference includes raw and standardized effect sizes, standard errors, exact test statistics, degrees of freedom, and $95\%$ CI/CrI (`SAMPL` standard).
- [ ] All statistics in prose/tables are deterministically computed via `run_command` with pinned `PRNG` seeds (`QG-SCI-06`)—zero mental-math or fabricated numbers.
- [ ] Small-cell disclosure controls prevent re-identification of sensitive human records, and unfavorable sensitivity results are transparently included (`QG-SCI-07`).

## 4. Verification Evidence & Handoff Readiness
- [ ] Exact `run_command` statistical script paths, `PRNG` seeds, and diagnostic logs are documented for independent `REPRODUCIBILITY_AUDITOR` rerun.
- [ ] Verified empirical quantities are explicitly separated from distributional assumptions and prior choices.
- [ ] All created or modified files stay strictly inside the assigned Exclusive Write-Lock scope.
- [ ] Compute-intensive runs not executed at full scale locally are explicitly labeled `NOT VERIFIED`.
- [ ] Final handoff status (`PASS / PARTIAL / BLOCKED / FAILED / NOT VERIFIED`) matches observed diagnostic results.
