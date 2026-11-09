# Quality Checklist: Operations Manager (`OPERATIONS_MANAGER` — `ROLE-BIZ-005`)

- **Role ID:** `ROLE-BIZ-005`
- **Canonical Role:** `OPERATIONS_MANAGER`
- **Parent Domain:** `BUSINESS_PRODUCT` ([DOMAIN_INDEX.md](../../DOMAIN_INDEX.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md))
- **Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)

> Pre-handoff verification checklist aligned with [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md). Verify queueing, staffing, and unit-cost math programmatically before `PASS`.

## 1. Bottleneck Diagnosis & Unit Cost-to-Serve
- [ ] Root operational bottlenecks, defect/rework drivers, and baseline wait/cycle times are quantified from verified data or explicitly labeled assumptions (`BIZ-QG-01`).
- [ ] Time-Driven Activity-Based Costing (TDABC) captures fully loaded labor, shrinkage, tooling, and escalation rework per transaction (`BIZ-QG-02`).
- [ ] Speed/efficiency KPIs (AHT, throughput) are paired with mandatory quality counter-metrics (FCR, reopen rate, defect escape, CSAT).

## 2. Queueing, Peak Capacity & SLA Alignment
- [ ] Capacity models (`run_command`) verify server stability ($\rho = \frac{\lambda \tau}{c} < 1$) across **peak** arrival intervals (`p90`/`p95` volume + variance), not merely weekly averages (`BIZ-QG-04`).
- [ ] FTE headcount conversions explicitly incorporate operational shrinkage (breaks, PTO, training, attrition onboarding ramp).
- [ ] Internal SLOs and upstream vendor OLAs are strictly tighter than external customer-facing contractual SLAs (`Internal OLA + Processing < External SLA`).

## 3. Actionable SOPs, Exception Handling & Pilot Rigor
- [ ] SOPs use concise, testable checklists and deterministic decision/escalation tables covering edge cases, refunds, outages, and degraded-mode fallback (`BIZ-QG-03`).
- [ ] Process changes specify phased pilot rollout, baseline-vs-pilot metrics, and rollback triggers (`BIZ-QG-05`).

## 4. Governance, Privacy & Labor/Customer Ethics
- [ ] RACI ownership across Support, Ops, Engineering, Finance, and Vendors is unambiguous (`BIZ-QG-06`).
- [ ] Frontline/BPO access enforces customer PII masking, avoids abusive cancellation-obstruction ("sludge") scripts, and contains zero emojis or unfinished placeholders.

## 5. Handoff & Governance Readiness
- [ ] Exclusive Write-Lock boundaries were strictly honored (`0` files modified outside assigned workstream paths).
- [ ] Deterministic `run_command` verification commands, script exit codes, and observed numerical outputs are recorded.
- [ ] Verified empirical facts, explicit model assumptions, and any `PARTIAL` or `NOT VERIFIED` items are cleanly separated.
- [ ] Internal relative Markdown links resolve cleanly on disk with zero `TODO`/`TBD` tokens or decorative prose.
- [ ] Structured 8-item Worker Handoff Report is complete and ready for `SA_GATE` and `PM_GATE` signoff.
