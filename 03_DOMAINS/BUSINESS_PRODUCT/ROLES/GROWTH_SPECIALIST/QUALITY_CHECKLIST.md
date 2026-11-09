# Quality Checklist: Growth Specialist (`GROWTH_SPECIALIST` — `ROLE-BIZ-006`)

- **Role ID:** `ROLE-BIZ-006`
- **Canonical Role:** `GROWTH_SPECIALIST`
- **Parent Domain:** `BUSINESS_PRODUCT` ([DOMAIN_INDEX.md](../../DOMAIN_INDEX.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md))
- **Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)

> Pre-handoff verification checklist aligned with [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md). Verify statistical power, SRM, and unit economics programmatically via `run_command` before `PASS`.

## 1. Funnel Diagnosis & Marginal Unit Economics
- [ ] Funnel bottleneck and user friction hypotheses are grounded in cohort/telemetry evidence rather than vanity top-of-funnel impressions (`BIZ-QG-01`).
- [ ] Unit economics separate **Marginal Paid CAC** from **Blended CAC**, weight LTV by **Gross Margin**, and verify CAC Payback Months and Net Dollar Retention (`BIZ-QG-02`).
- [ ] Cohort retention curves distinguish asymptotic flattening from ongoing linear decay before recommending paid acquisition scaling.

## 2. Experiment Design & Statistical Rigor
- [ ] Every experiment pre-specifies falsifiable hypothesis, randomization unit (checked for network/account spillover), baseline metric, Minimum Detectable Effect (MDE), $\alpha$, power ($1 - \beta \ge 0.80$), required sample size per arm, and full-week cycle duration (`BIZ-QG-05`).
- [ ] Post-experiment readouts run Sample Ratio Mismatch (SRM $\chi^2$) checks first and halt interpretation if traffic split deviates significantly ($p < 0.001$).
- [ ] Early-stopping rules use valid sequential boundaries (or fixed-horizon lock without peeking), and multi-variant / subgroup slices apply multiple-testing corrections (Bonferroni / Benjamini-Hochberg).
- [ ] Primary lift metrics are paired with mandatory guardrail metrics (refund/chargeback rate, unsubscribe/spam-complaint rate, D30 retention, latency, gross margin) (`BIZ-QG-03`).

## 3. Operational, Engineering & Legal Readiness
- [ ] Tracking instrumentation events, feature-flag kill switches, and support/billing load impacts are verified feasible (`BIZ-QG-04`, `BIZ-QG-06`).
- [ ] Zero manipulative dark patterns, zero non-consensual spam/scraping tactics, zero GDPR/CCPA/TCPA/CAN-SPAM violations, and zero emojis or unfinished placeholders exist.

## 4. Handoff & Governance Readiness
- [ ] Exclusive Write-Lock boundaries were strictly honored (`0` files modified outside assigned workstream paths).
- [ ] Deterministic `run_command` verification commands, script exit codes, and observed numerical outputs are recorded.
- [ ] Verified empirical facts, explicit model assumptions, and any `PARTIAL` or `NOT VERIFIED` items are cleanly separated.
- [ ] Internal relative Markdown links resolve cleanly on disk with zero `TODO`/`TBD` tokens or decorative prose.
- [ ] Structured 8-item Worker Handoff Report is complete and ready for `SA_GATE` and `PM_GATE` signoff.
