# Quality Checklist: Financial Modeling Specialist (`FINANCIAL_MODELING` — `ROLE-FIN-005`)

- **Role ID:** `ROLE-FIN-005`
- **Canonical Role:** `FINANCIAL_MODELING`
- **Parent Domain:** `ECONOMICS_FINANCE` ([DOMAIN_INDEX.md](../../DOMAIN_INDEX.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md))
- **Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)

> Pre-handoff verification checklist aligned with [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md), [QUALITY_GATES.md](../../QUALITY_GATES.md), and [FINANCIAL_MODEL_VALIDATION](../../../../05_SPECIALIZED_SKILLS/FINANCIAL_MODEL_VALIDATION/SKILL.md).

## 1. Structural Architecture & Input Separation
- [ ] All exogenous drivers, tax rates, pricing/growth parameters, debt terms, and transaction assumptions reside in a dedicated Assumption Ledger with zero hardcoded constants inside formulas (`FIN-QG-02`).
- [ ] Historical actuals tie out to primary filings/ledgers (`FIN-QG-01`) and are visually/structurally separated from forecast periods with consistent column periodicity and unit scaling.
- [ ] Circularity (`Interest <-> Cash/Revolver`) is governed by an explicit `CIRC_SWITCH` (`0 = BOP acyclic`, `1 = iterative convergence`) tested for convergence stability.

## 2. Three-Statement & Schedule Reconciliation
- [ ] Balance Sheet balances (`abs(Assets - (Liabilities + Equity)) <= 1e-6`) in **every** historical and forecast period across **all** scenario switches with **zero** plug lines (`FIN-QG-04`).
- [ ] Cash Flow Statement ending cash equals Balance Sheet cash; Net Income links cleanly to Retained Earnings net of dividends/buybacks.
- [ ] Working-capital cash flow signs are verified (`-\Delta AR`, `-\Delta Inventory`, `-\Delta Prepaid`, `+\Delta AP`, `+\Delta Accrued/Deferred Revenue`).
- [ ] PP&E and Intangible BASE roll-forwards reconcile (`Ending = Beginning + Capex - D&A - Disposals`) and never depreciate net book value below salvage/zero.

## 3. Debt Waterfall, Taxes & Transaction Mechanics
- [ ] Sources & Uses table balances (`Total Sources == Total Uses`); purchase-price goodwill, deferred-tax step-ups, and capitalized financing fees flow accurately to the opening pro-forma Balance Sheet (`FIN-QG-03`).
- [ ] Revolver draws automatically when free cash falls below minimum operating cash, repays from excess cash before junior prepayments, and flags breaches if draws exceed revolver commitment.
- [ ] NOL carryforwards, interest-deductibility caps (e.g., IRC Sec. 163(j) awareness), and diluted equity waterfalls (options, warrants, management promote) calculate accurately.

## 4. Stress Testing, Sensitivity & Audit Hygiene
- [ ] 2D sensitivity matrices and Bull / Base / Bear / Severe Stress scenarios run cleanly without `#REF!`, `#DIV/0!`, `#VALUE!`, `NaN`, or `Inf` errors (`FIN-QG-05`, `FIN-QG-06`, `FIN-QG-07`).
- [ ] Master Error-Check summary block, model limitation disclosures (`FIN-QG-08`), and non-fiduciary notices (`FIN-QG-09`) are included with zero decorative emojis or unfinished placeholders.

## 5. Handoff & Governance Readiness
- [ ] Exclusive Write-Lock boundaries were strictly honored (`0` files modified outside assigned workstream paths).
- [ ] Deterministic `run_command` verification commands, script exit codes, and observed numerical outputs are recorded.
- [ ] Verified empirical facts, explicit model assumptions, and any `PARTIAL` or `NOT VERIFIED` items are cleanly separated.
- [ ] Internal relative Markdown links resolve cleanly on disk with zero `TODO`/`TBD` tokens or decorative prose.
- [ ] Structured 8-item Worker Handoff Report is complete and ready for `SA_GATE` and `PM_GATE` signoff.
