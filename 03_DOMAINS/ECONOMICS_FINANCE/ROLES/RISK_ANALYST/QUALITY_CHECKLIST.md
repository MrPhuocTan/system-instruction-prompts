# Quality Checklist: Risk Analyst (`RISK_ANALYST` — `ROLE-FIN-006`)

- **Role ID:** `ROLE-FIN-006`
- **Canonical Role:** `RISK_ANALYST`
- **Parent Domain:** `ECONOMICS_FINANCE` ([DOMAIN_INDEX.md](../../DOMAIN_INDEX.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md))
- **Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)

> Pre-handoff verification checklist aligned with [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md). Verify all risk metrics programmatically before handoff.

## 1. Exposure Completeness & Parameter Transparency
- [ ] All on-balance-sheet, off-balance-sheet, contingent commitment, and derivative exposures are inventoried with verified source cutoffs, currency, and seniority (`FIN-QG-01`).
- [ ] Confidence levels (e.g., `95%`, `99%`, `99.7%`), holding/liquidation horizons, lookback windows, decay factors, and distributional assumptions are documented in the Assumption Ledger (`FIN-QG-02`).

## 2. Tail, Credit & Liquidity Risk Mathematical Rigor
- [ ] Expected Shortfall ($\text{CVaR}$) is reported alongside $\text{VaR}$ so tail severity beyond the quantile cutoff is captured (`FIN-QG-03`, `FIN-QG-07`).
- [ ] Component VaR / CVaR contributions sum algebraically to diversified portfolio total risk, explicitly isolating diversification benefit.
- [ ] Non-linear positions (options, callable debt, caps/floors, prepayment convexity) are revalued via full revaluation or Delta-Gamma-Vega rather than linear Delta-only approximations.
- [ ] Credit risk models incorporate downturn LGD, EAD credit conversion on undrawn commitments, concentration/wrong-way risk, and IFRS 9 / CECL stage-migration sensitivities.
- [ ] Liquidity stress tests model cash survival horizon, LCR/runway troughs, revolver availability restrictions, and derivative variation-margin / collateral calls (`FIN-QG-04`).

## 3. Stress, Reverse-Stress & Backtest Validation
- [ ] Multi-factor stress scenarios test correlation breakdown ($\rho \to 1$ across risk assets), historical crisis replays, and hypothetical stagflation/rate/credit shocks (`FIN-QG-05`, `FIN-QG-06`).
- [ ] Reverse stress testing identifies the exact shock thresholds that breach debt covenants, regulatory capital minimums, or minimum operating cash.
- [ ] VaR/PD models include out-of-sample backtest diagnostics (Kupiec POF, Christoffersen independence, Brier/AUC calibration) where historical time series exist.

## 4. Independence, Uncertainty & Regulatory Compliance
- [ ] Independent model-validation findings explicitly record data limitations, fat-tail estimation uncertainty (`FIN-QG-08`), and separation of duties from model authors.
- [ ] Deliverable contains zero suppressed breaches, zero emojis/placeholders, and includes non-fiduciary regulatory/professional review disclaimers (`FIN-QG-09`).

## 5. Handoff & Governance Readiness
- [ ] Exclusive Write-Lock boundaries were strictly honored (`0` files modified outside assigned workstream paths).
- [ ] Deterministic `run_command` verification commands, script exit codes, and observed numerical outputs are recorded.
- [ ] Verified empirical facts, explicit model assumptions, and any `PARTIAL` or `NOT VERIFIED` items are cleanly separated.
- [ ] Internal relative Markdown links resolve cleanly on disk with zero `TODO`/`TBD` tokens or decorative prose.
- [ ] Structured 8-item Worker Handoff Report is complete and ready for `SA_GATE` and `PM_GATE` signoff.
