# Quality Checklist: Business Project Manager (`PROJECT_MANAGER` — `ROLE-BIZ-004`)

- **Role ID:** `ROLE-BIZ-004`
- **Canonical Role:** `PROJECT_MANAGER`
- **Parent Domain:** `BUSINESS_PRODUCT` ([DOMAIN_INDEX.md](../../DOMAIN_INDEX.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md))
- **Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)

> Pre-handoff verification checklist aligned with [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md). Distinct from Core Governance `02_CORE_ROLES/PROJECT_MANAGER` (`PM_GATE`).

## 1. Charter, Scope & Governance Boundary Clarity
- [ ] Deliverable explicitly scopes domain business project/program delivery without conflicting with Core Antigravity `PM` + `SA` session governance.
- [ ] Project objectives connect to validated customer/business outcomes and quantified ROI/budget baselines (`BIZ-QG-01`, `BIZ-QG-02`).
- [ ] WBS follows the 100% deliverable rule with explicit `In-Scope`, `Out-of-Scope`, and change-control trade-off triggers (`BIZ-QG-03`).

## 2. Critical Path, Resource & EVM Mathematical Integrity
- [ ] Dependency network is verified via `run_command` to be a valid Directed Acyclic Graph (zero circular dependencies).
- [ ] Forward/backward CPM pass (`ES`, `EF`, `LS`, `LF`, `Total Float`, `Free Float`) and critical-path identification (`Total Float == 0`) are mathematically exact.
- [ ] Resource utilization accounts for realistic productive capacity (`70%–80%`), holidays/blackout windows, and onboarding ramp (`BIZ-QG-04`).
- [ ] Where budget tracking applies, EVM metrics (`PV`, `EV`, `AC`, `CPI`, `SPI`, `EAC`, `TCPI`) are computed deterministically and reconciled to baseline totals.

## 3. RAID, RACI & Cutover Readiness
- [ ] RACI matrix assigns **exactly one** `Accountable (A)` owner and at least one `Responsible (R)` owner per deliverable (`BIZ-QG-06`).
- [ ] RAID register scores probability $\times$ impact, defines concrete leading-indicator triggers, contingency owners, and fallback actions (not generic `"monitor closely"`).
- [ ] Go/No-Go stage gates include explicit operational, security/compliance, training, and time-bounded rollback verification criteria (`BIZ-QG-04`, `BIZ-QG-05`).

## 4. Reporting Honesty & Hygiene
- [ ] Schedule slips, negative float, or budget overruns are surfaced transparently with concrete recovery options; Mermaid diagrams use supported `flowchart` syntax with zero emojis or unfinished placeholders.

## 5. Handoff & Governance Readiness
- [ ] Exclusive Write-Lock boundaries were strictly honored (`0` files modified outside assigned workstream paths).
- [ ] Deterministic `run_command` verification commands, script exit codes, and observed numerical outputs are recorded.
- [ ] Verified empirical facts, explicit model assumptions, and any `PARTIAL` or `NOT VERIFIED` items are cleanly separated.
- [ ] Internal relative Markdown links resolve cleanly on disk with zero `TODO`/`TBD` tokens or decorative prose.
- [ ] Structured 8-item Worker Handoff Report is complete and ready for `SA_GATE` and `PM_GATE` signoff.
