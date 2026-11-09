# Quality Checklist: Financial Analyst (`FINANCIAL_ANALYST` — `ROLE-FIN-002`)

- **Role ID:** `ROLE-FIN-002`
- **Canonical Role:** `FINANCIAL_ANALYST`
- **Parent Domain:** `ECONOMICS_FINANCE` ([DOMAIN_INDEX.md](../../DOMAIN_INDEX.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md))
- **Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)

> Pre-handoff verification checklist aligned with [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md). Verify every check programmatically before declaring `PASS`.

## 1. Source Tie-Out & Accounting Basis
- [ ] Historical revenue, gross profit, operating income, net income, total assets, total debt, and ending cash tie 100% to audited filings or verified workspace general-ledger exports (`FIN-QG-01`).
- [ ] Reporting basis (US GAAP vs. IFRS), currency, unit scale (`$000s` vs. `$M`), and fiscal year-end calendar are explicitly labeled on every schedule.
- [ ] Non-GAAP metrics (Adjusted EBITDA, Free Cash Flow) include a line-by-line bridge back to the closest GAAP/IFRS statutory measure, explicitly showing stock-based compensation and one-time adjustments.

## 2. Variance Bridge & Ratio Accuracy
- [ ] Budget-vs-Actual (BvA) and YoY/QoQ bridges (Price, Volume, Mix, FX, Cost) sum algebraically to exact total variance (`residual <= 1e-6`) with interaction terms explicitly assigned (`FIN-QG-03`).
- [ ] Segment, regional, and product-line schedules reconcile to consolidated totals after explicit corporate/unallocated overhead and intercompany eliminations.
- [ ] Return and turnover ratios (ROIC, ROE, Asset Turnover, DSO, DIO, DPO) pair flow numerators with consistent average stock denominators and matching day-count conventions (`365` vs. `360` days).
- [ ] Unit-economics metrics (LTV, CAC, CAC Payback, NDR, Gross Margin) apply gross-profit weighting rather than raw revenue and disclose exact cohort windows.

## 3. Forecast Realism, Liquidity & Sensitivity
- [ ] Driver-based forecast assumptions (headcount, pricing, churn, utilization, capex, NWC days) are cataloged in an Explicit Assumption Ledger (`FIN-QG-02`) with historical actuals for comparison.
- [ ] Balance Sheet and Cash Flow Statement reconcile across all forecast periods (`FIN-QG-04`), including intra-period seasonal working-capital troughs and minimum cash / revolver headroom.
- [ ] 2D sensitivity tables and Upside / Base / Downside operating scenarios quantify EBITDA, FCF, and liquidity runway impacts across key revenue and margin drivers (`FIN-QG-05`, `FIN-QG-06`, `FIN-QG-07`).

## 4. Verification, Confidentiality & Hygiene
- [ ] Independent Python verification (`run_command`) confirms zero division-by-zero errors, sign inversions on cost variances, or rounding discrepancies across summary and detail tables.
- [ ] Confidential payroll/customer PII is redacted, uncertainties are disclosed (`FIN-QG-08`), and non-fiduciary analytical disclaimers (`FIN-QG-09`) are included with zero emojis or unfinished placeholders.

## 5. Handoff & Governance Readiness
- [ ] Exclusive Write-Lock boundaries were strictly honored (`0` files modified outside assigned workstream paths).
- [ ] Deterministic `run_command` verification commands, script exit codes, and observed numerical outputs are recorded.
- [ ] Verified empirical facts, explicit model assumptions, and any `PARTIAL` or `NOT VERIFIED` items are cleanly separated.
- [ ] Internal relative Markdown links resolve cleanly on disk with zero `TODO`/`TBD` tokens or decorative prose.
- [ ] Structured 8-item Worker Handoff Report is complete and ready for `SA_GATE` and `PM_GATE` signoff.
