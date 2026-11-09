# Quality Checklist: Business Analyst (`BUSINESS_ANALYST` — `ROLE-BIZ-002`)

- **Role ID:** `ROLE-BIZ-002`
- **Canonical Role:** `BUSINESS_ANALYST`
- **Parent Domain:** `BUSINESS_PRODUCT` ([DOMAIN_INDEX.md](../../DOMAIN_INDEX.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md))
- **Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)

> Pre-handoff verification checklist aligned with [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md). Verify 100% RTM and decision-table completeness before `PASS`.

## 1. Problem Context, Glossary & Process Rigor
- [ ] `As-Is` operational pain points, error rates, cycle times, and manual workarounds are quantified and linked to `To-Be` target improvements (`BIZ-QG-01`, `BIZ-QG-02`).
- [ ] Canonical Domain Glossary defines every business entity, status lifecycle state, and cardinality (`1:1`, `1:N`, `M:N`) with zero synonym drift.
- [ ] `To-Be` process flows (BPMN / Mermaid swimlanes) explicitly model actor boundaries, system handoffs, SLA timers, compensating rollbacks, and exception gateways (`BIZ-QG-04`).

## 2. Atomic Requirements & MECE Decision Tables
- [ ] Every requirement (`REQ-FUNC-XXX`, `REQ-NFR-XXX`) is atomic, unambiguous, feasible, and paired with falsifiable pass/fail acceptance criteria — free of vague adjectives (`BIZ-QG-03`).
- [ ] `In-Scope`, `Out-of-Scope`, MoSCoW priority, and data-migration/cutover rules are explicitly documented.
- [ ] Business-rule decision tables are verified via `run_command` to be mutually exclusive and collectively exhaustive (zero overlapping contradictions, zero missing input combinations).
- [ ] CRUD and RBAC permission matrices enforce least privilege and segregation of duties (maker-checker controls on sensitive/financial actions).

## 3. Bidirectional Traceability & UAT Readiness
- [ ] Requirements Traceability Matrix (RTM) confirms 100% forward and backward mapping (`Business Objective <-> Requirement <-> Business Rule <-> UAT Test Case`) with zero orphan IDs.
- [ ] UAT scenarios cover positive flows, boundary values, negative/invalid inputs, concurrent/duplicate events, and authorization denials.

## 4. Stakeholder Sign-Off & Governance Hygiene
- [ ] Cross-departmental rule conflicts, regulatory/privacy constraints, and RACI owners are explicitly resolved or escalated (`BIZ-QG-06`).
- [ ] Deliverable contains valid Mermaid syntax, zero broken links, zero emojis, and zero unfinished `TODO`/`TBD` markers.

## 5. Handoff & Governance Readiness
- [ ] Exclusive Write-Lock boundaries were strictly honored (`0` files modified outside assigned workstream paths).
- [ ] Deterministic `run_command` verification commands, script exit codes, and observed numerical outputs are recorded.
- [ ] Verified empirical facts, explicit model assumptions, and any `PARTIAL` or `NOT VERIFIED` items are cleanly separated.
- [ ] Internal relative Markdown links resolve cleanly on disk with zero `TODO`/`TBD` tokens or decorative prose.
- [ ] Structured 8-item Worker Handoff Report is complete and ready for `SA_GATE` and `PM_GATE` signoff.
