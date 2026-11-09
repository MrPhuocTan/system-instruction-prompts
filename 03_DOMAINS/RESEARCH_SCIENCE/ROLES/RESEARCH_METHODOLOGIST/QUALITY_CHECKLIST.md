# Pre-Handoff Quality Checklist — `RESEARCH_METHODOLOGIST` (`ROLE-SCI-002`)

- **Governing Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)
- **Domain Quality Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md)

Verify every item below before issuing a worker handoff report:

## 1. Estimand & Identification Soundness
- [ ] Target estimand (`ATT`, `ATE`, `LATE`, descriptive association) is explicitly defined prior to estimator selection (`QG-SCI-01`).
- [ ] Causal `DAG` or formal structural assumption set explicitly classifies confounders, mediators, colliders, and unmeasured variables (`QG-SCI-03`).
- [ ] Adjustment set closes open backdoor paths without conditioning on post-treatment mediators, colliders, or downstream proxies (zero Table 2 fallacy).
- [ ] Eligibility, exposure assignment, and outcome follow-up `time zero` are aligned to eliminate immortal-time and prevalent-user bias.

## 2. Quasi-Experimental, Sampling & Measurement Rigor
- [ ] Core identification assumptions (`SUTVA`, positivity/overlap, parallel trends, exclusion restriction, continuity at cutoff) are explicitly stated and paired with empirical diagnostics.
- [ ] Sampling frame, non-response/attrition mechanisms, and construct operationalization (validity/reliability limits) are documented (`QG-SCI-04`).
- [ ] At least two orthogonal falsification or sensitivity checks (negative controls, placebo cutoffs/dates, E-values/partial-$R^2$ bounds) are pre-specified.
- [ ] Synthetic `DGP` simulation (when code execution applies) confirms unbiased recovery of known ground-truth parameters.

## 3. Preregistration, Ethics & Reporting Hygiene
- [ ] Confirmatory analysis plan locks covariate sets, subgroup rules, outlier handling, and primary endpoints before outcome modeling (`QG-SCI-05`).
- [ ] Unidentifiable causal pathways are downgraded to explicit associational claims with clear limitations (`QG-SCI-07`).
- [ ] Human-subjects ethics (`IRB`, informed consent, privacy/de-identification) and external validity boundaries are explicitly addressed.
- [ ] All cited methodological literature is verified with zero fabricated citations (`QG-SCI-02`).

## 4. Verification Evidence & Handoff Readiness
- [ ] `DAG` path checks, balance diagnostics, or synthetic `DGP` simulation commands and outputs are logged for independent review.
- [ ] Untestable identification assumptions (`exclusion restriction`, `unmeasured confounding`) are explicitly separated from empirically verified checks.
- [ ] All written or edited files reside strictly inside the assigned Exclusive Write-Lock scope.
- [ ] Unverified external datasets or institutional `IRB` approvals are marked `NOT VERIFIED` rather than `PASS`.
- [ ] Handoff status (`PASS / PARTIAL / BLOCKED / FAILED / NOT VERIFIED`) accurately reflects empirical verification evidence.
