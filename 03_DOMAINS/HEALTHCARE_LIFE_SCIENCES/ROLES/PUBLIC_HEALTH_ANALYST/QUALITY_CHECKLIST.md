# Pre-Handoff Quality Checklist — `PUBLIC_HEALTH_ANALYST` (`ROLE-HLT-003`)

- **Governing Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)
- **Domain Quality Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md)

Verify every item below before issuing a worker handoff report:

## 1. Epidemiological Denominators, Standardization & Bias
- [ ] Case definitions, geographic/temporal frames, and exact population-at-risk / person-time denominators are explicitly documented (`QG-HLT-01`, `QG-HLT-02`).
- [ ] Comparisons across populations apply direct or indirect age/sex standardization (with named standard population weights summing to `1.0`) to prevent Simpson's paradox.
- [ ] Ascertainment bias, testing-volume changes, right-truncated reporting lags, and screening lead-time/length-time biases are explicitly audited (`QG-HLT-05`).
- [ ] Aggregate regional analyses explicitly avoid ecological-fallacy claims about individual-level causation.

## 2. Transmission / Burden Modeling & Equity Rigor
- [ ] Compartmental (`SIR`/`SEIR`) or regression models pass conservation/diagnostic checks via `run_command` and report wide scenario/parameter uncertainty intervals (`QG-HLT-05`).
- [ ] Fatality metrics clearly distinguish `CFR` from `IFR` and account for onset-to-outcome censoring.
- [ ] Health-equity / `SDoH` stratifications report both absolute rate differences and relative ratios without unvalidated biological-race assumptions (`QG-HLT-02`).
- [ ] Unintended harms and resource trade-offs of proposed public-health interventions are evaluated (`QG-HLT-03`).

## 3. Privacy Suppression, Biosecurity & Human Oversight
- [ ] Line-list `PHI` is completely redacted and small demographic-geographic cells ($n < 11$ or stricter policy bound) are suppressed (`QG-HLT-04`).
- [ ] Zero dual-use pathogen enhancement or biosecurity-sensitive dissemination detail is present (`QG-HLT-06`).
- [ ] All external surveillance sources (`WHO`/`CDC`/census) are verified (`QG-HLT-01`), and mandatory qualified public-health/clinician review is stated (`QG-HLT-07`).

## 4. Verification Evidence & Handoff Readiness
- [ ] Rate-standardization, conservation-law, and small-cell suppression verification scripts ran cleanly via `run_command`.
- [ ] Empirical surveillance observations are explicitly separated from stylized scenario assumptions and `NOT VERIFIED` external feeds.
- [ ] Policy/intervention outputs are queued for independent `PATIENT_SAFETY_REVIEWER` / `DOMAIN_LEAD` review where applicable.
- [ ] All created or modified files stay strictly inside the assigned Exclusive Write-Lock scope.
- [ ] Final handoff status (`PASS / PARTIAL / BLOCKED / FAILED / NOT VERIFIED`) matches observed verification evidence.
