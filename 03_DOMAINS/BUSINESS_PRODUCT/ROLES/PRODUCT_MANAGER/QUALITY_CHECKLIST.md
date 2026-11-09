# Quality Checklist: Product Manager (`PRODUCT_MANAGER` — `ROLE-BIZ-001`)

- **Role ID:** `ROLE-BIZ-001`
- **Canonical Role:** `PRODUCT_MANAGER`
- **Parent Domain:** `BUSINESS_PRODUCT` ([DOMAIN_INDEX.md](../../DOMAIN_INDEX.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md))
- **Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)

> Pre-handoff verification checklist aligned with [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md). Every item must pass before engineering handoff or `PM_GATE` review.

## 1. Problem Evidence & Target User Clarity
- [ ] Target ICP/persona, trigger context, job-to-be-done, and baseline workaround cost are explicitly defined (`BIZ-QG-01`).
- [ ] Evidence is graded honestly (observed telemetry/interviews vs. untested hypotheses), with zero fabricated user quotes or survey numbers.

## 2. Metrics, Unit Economics & Scope Discipline
- [ ] Primary outcome KPIs specify exact baseline, target threshold, measurement window, and anti-gaming guardrail counter-metrics (`BIZ-QG-02`).
- [ ] Variable cost-to-serve (including cloud/API/LLM inference, payment processing, and support load) preserves positive contribution margin.
- [ ] Explicit `In-Scope`, `Out-of-Scope / Non-Goals`, prioritization trade-offs (RICE/WSJF inputs), and post-launch pivot/kill criteria are documented (`BIZ-QG-03`).

## 3. Specification Completeness, States & Utilitarian UX
- [ ] Every functional requirement maps to falsifiable `Given / When / Then` acceptance criteria with numeric performance/latency bounds.
- [ ] All UI/workflow states are specified: Empty/First-Run, Loading, Populated, Validation Error, Network/Server Failure, Offline/Retry, and Unauthorized/RBAC states.
- [ ] UX specification enforces utilitarian clarity with zero decorative "AI Sign" clutter, zero emojis in normative specs, and WCAG accessibility basics.
- [ ] Telemetry event names, properties, privacy/PII redaction rules, and staged rollout/feature-flag rollback steps are defined (`BIZ-QG-04`, `BIZ-QG-05`).

## 4. Cross-Functional Alignment & Ethical Compliance
- [ ] Cross-domain dependencies (Engineering, Design, Data, Legal/Privacy, Security, Support) and RACI ownership are locked (`BIZ-QG-06`).
- [ ] Zero deceptive dark patterns (coerced opt-ins, hidden fees, obstructed cancellation) exist; live commercial changes are gated on human approval.

## 5. Handoff & Governance Readiness
- [ ] Exclusive Write-Lock boundaries were strictly honored (`0` files modified outside assigned workstream paths).
- [ ] Deterministic `run_command` verification commands, script exit codes, and observed numerical outputs are recorded.
- [ ] Verified empirical facts, explicit model assumptions, and any `PARTIAL` or `NOT VERIFIED` items are cleanly separated.
- [ ] Internal relative Markdown links resolve cleanly on disk with zero `TODO`/`TBD` tokens or decorative prose.
- [ ] Structured 8-item Worker Handoff Report is complete and ready for `SA_GATE` and `PM_GATE` signoff.
