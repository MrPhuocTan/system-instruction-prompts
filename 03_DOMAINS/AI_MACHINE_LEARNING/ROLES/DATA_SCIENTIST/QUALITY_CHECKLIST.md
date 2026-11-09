# Quality Checklist: Data Scientist (`ROLE-AIML-009`)

- **Role:** [`DATA_SCIENTIST`](./SYSTEM_PROMPT.md)
- **Domain Gates:** [`QUALITY_GATES.md`](../../QUALITY_GATES.md)

---

## 1. Data Generating Process & Cohort Integrity
- [ ] Verified exact observation grain, exposure timestamp alignment, right-censoring windows, and missingness mechanism (`MCAR`/`MAR`/`MNAR`) prior to estimation.
- [ ] Confirmed zero survivorship bias, collider conditioning, or post-treatment filtering in cohort construction.
- [ ] Inspected heavy-tailed/skewed metrics and reported medians, quantiles, and winsorized/trimmed sensitivity alongside means.

## 2. Experimental & Causal Identification Validity
- [ ] Computed statistical power (`>= 80%`), Minimum Detectable Effect (`MDE`), and equivalence (`TOST`) bounds before interpreting `p > 0.05` null results.
- [ ] For `A/B` experiments: verified Sample Ratio Mismatch (`SRM` chi-squared `p >= 0.001`), pre-experiment covariate balance, `CUPED` pre-period cleanliness, and sequential/multiple-testing (`FDR`/FWER) adjustments.
- [ ] For observational causal claims: documented explicit causal DAG, passed pre-trend/placebo/negative-control falsification checks, and quantified unobserved-confounding sensitivity (`E-value`/Oster bounds).

## 3. Variance Estimation & Deterministic Reproducibility
- [ ] Matched standard errors (cluster-robust SEs, delta-method for ratio metrics, or block bootstrap) strictly to the unit of randomization or clustering.
- [ ] Verified every point estimate, confidence interval, and summary table regenerates deterministically from clean top-to-bottom script execution.

## 4. Decision Framing, Privacy & Epistemic Honesty
- [ ] Clearly separated verified empirical estimates from modeling assumptions, practical vs. statistical significance, and `NOT VERIFIED` external factors.
- [ ] Enforced small-cell (`k`-anonymity) privacy suppression and scrubbed `PII` from all exported summaries and diagnostic plots.
- [ ] Reported null or negative treatment findings faithfully without post-hoc subgroup cherry-picking.

## 5. Independent Verification & Handoff Completeness
- [ ] Validated estimator unbiasedness and `Type I` error calibration (`~5%` false positive rate at `alpha = 0.05`) on synthetic Monte Carlo data where custom statistical estimators were written.
- [ ] Reconciled cohort denominators (`N`) against upstream source tables (`0` unexplained attrition).
- [ ] Packaged clean, seed-locked reproduction commands and decision trade-off tables for [`PROJECT_MANAGER`](../../../../02_CORE_ROLES/PROJECT_MANAGER/SYSTEM_PROMPT.md).
