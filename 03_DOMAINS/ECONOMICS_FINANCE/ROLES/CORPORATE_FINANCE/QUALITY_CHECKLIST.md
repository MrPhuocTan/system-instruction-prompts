# Quality Checklist: Corporate Finance Specialist (`CORPORATE_FINANCE` — `ROLE-FIN-007`)

- **Role ID:** `ROLE-FIN-007`
- **Canonical Role:** `CORPORATE_FINANCE`
- **Parent Domain:** `ECONOMICS_FINANCE` ([DOMAIN_INDEX.md](../../DOMAIN_INDEX.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md))
- **Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)

> Pre-handoff verification checklist aligned with [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md). Verify every item before `PASS` handoff.

## 1. Cost of Capital & Hurdle Rate Rigor
- [ ] WACC uses market-value weights of debt, preferred stock, and equity (never book equity), risk-free rates matched to currency/duration, and peer-unlevered/relevered betas (`FIN-QG-01`, `FIN-QG-03`).
- [ ] Marginal pre-tax cost of debt reflects current market yields/credit spreads (not historical coupon rates), and after-tax cost of debt accounts for statutory tax rates and interest-deductibility caps.
- [ ] Divisional or M&A target cash flows are discounted at target/project-specific risk-adjusted hurdle rates rather than blended acquirer WACC.

## 2. Capital Allocation & M&A Value-Creation Math
- [ ] Incremental project cash flows exclude sunk costs and financing interest (already inside WACC), while explicitly incorporating working-capital changes, cannibalization, and opportunity costs (`FIN-QG-02`).
- [ ] M&A analysis separates **economic value creation** ($\text{PV}(\text{After-Tax Synergies} - \text{Integration Costs}) - \text{Premium Paid}$ and Deal ROIC vs. WACC) from **accounting/cash EPS accretion/dilution**.
- [ ] Pro-forma Sources & Uses, goodwill/PPA adjustments, financing fees, and pro-forma Balance Sheet reconcile with zero plugs (`FIN-QG-04`).
- [ ] Share buyback evaluation tests return at current vs. intrinsic share price rather than treating share-count reduction as automatic value creation.

## 3. Leverage, Liquidity & Stress Resilience
- [ ] Pro-forma leverage (`Total & Net Debt / EBITDA`), interest coverage, maturity wall, and debt covenant headroom are tested under trough-cycle / Bear / Stress scenarios (`FIN-QG-05`, `FIN-QG-06`, `FIN-QG-07`).
- [ ] Change-of-control debt acceleration clauses, rating-downgrade triggers, and minimum operating liquidity buffers are explicitly evaluated.

## 4. Confidentiality, Verification & Regulatory Disclaimers
- [ ] All NPV, IRR, WACC, and accretion/dilution tables are verified via `run_command` Python scripts with model uncertainties disclosed (`FIN-QG-08`).
- [ ] Confidential deal/MNPI data is protected, prose is free of emojis/placeholders, and non-fiduciary / licensed tax-and-legal review disclaimers (`FIN-QG-09`) are attached.

## 5. Handoff & Governance Readiness
- [ ] Exclusive Write-Lock boundaries were strictly honored (`0` files modified outside assigned workstream paths).
- [ ] Deterministic `run_command` verification commands, script exit codes, and observed numerical outputs are recorded.
- [ ] Verified empirical facts, explicit model assumptions, and any `PARTIAL` or `NOT VERIFIED` items are cleanly separated.
- [ ] Internal relative Markdown links resolve cleanly on disk with zero `TODO`/`TBD` tokens or decorative prose.
- [ ] Structured 8-item Worker Handoff Report is complete and ready for `SA_GATE` and `PM_GATE` signoff.
