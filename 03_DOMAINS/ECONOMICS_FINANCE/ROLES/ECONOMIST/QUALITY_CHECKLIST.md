# Quality Checklist: Economist (`ECONOMIST` — `ROLE-FIN-001`)

- **Role ID:** `ROLE-FIN-001`
- **Canonical Role:** `ECONOMIST`
- **Parent Domain:** `ECONOMICS_FINANCE` ([DOMAIN_INDEX.md](../../DOMAIN_INDEX.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md))
- **Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)

> Pre-handoff verification checklist aligned with [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md). Every item must be verified via deterministic script output or primary source inspection before marking workstream status `PASS`.

## 1. Data Provenance & Accounting Identities
- [ ] Every macroeconomic or microeconomic series cites primary source agency (e.g., BEA, BLS, FRED, ECB, IMF, World Bank, or verified workspace file), release date/vintage, frequency, and seasonal-adjustment status.
- [ ] Nominal vs. real deflation basis (base year, price index such as Core PCE, CPI-U, or GDP deflator) and FX conversion basis (market FX vs. PPP) are explicitly stated and applied consistently.
- [ ] National income, balance-of-payments, or market-clearing identities ($Y = C + I + G + NX$; fiscal deficit $\rightarrow$ debt stock roll-forward) reconcile algebraically across all forecast periods.

## 2. Causal Identification & Econometric Rigor
- [ ] Target estimand (ATE, ATT, LATE, structural elasticity, or SVAR impulse response) is explicitly defined and separated from descriptive correlation.
- [ ] Endogeneity, omitted-variable bias, simultaneity (e.g., supply-demand identification), and reverse causality are addressed with documented identification assumptions.
- [ ] Time-series stationarity/order of integration ($I(0)$ vs. $I(1)$) and cointegration checks are executed prior to level regressions; lag lengths are justified via AIC/BIC or institutional frequency.
- [ ] Standard errors account for heteroskedasticity, serial correlation (HAC/Newey-West), or group clustering at the level of treatment assignment.

## 3. Robustness, Sensitivity & Scenario Coverage
- [ ] Diagnostic tests are reported where applicable: DiD pre-trend joint $F$-test, 2SLS first-stage $F$-statistic, RDD McCrary density/bandwidth sensitivity, or VAR stability eigenvalues.
- [ ] Sensitivity tables evaluate parameter variation across plausible elasticity, multiplier, lag, and policy-reaction bounds (`FIN-QG-05`).
- [ ] Coherent multi-variable macro scenarios (Baseline, Upside/Disinflation, Downside/Recession, Stagflation/Rate-Shock) model joint movements in output, inflation, rates, unemployment, and credit spreads (`FIN-QG-06`).

## 4. Uncertainty, Reproducibility & Governance Compliance
- [ ] Point estimates are accompanied by 95% confidence/prediction intervals, sample sizes ($N$, $T$), and explicit discussion of Lucas-critique or external-validity limits (`FIN-QG-08`).
- [ ] All numerical outputs were generated and verified via `run_command` scripts rather than mental arithmetic, with zero `TODO`/`TBD` placeholders or decorative "AI Sign" prose.
- [ ] Distributional welfare impacts and non-fiduciary regulatory disclosures (`FIN-QG-09`) are explicitly documented in the final deliverable.

## 5. Handoff & Governance Readiness
- [ ] Exclusive Write-Lock boundaries were strictly honored (`0` files modified outside assigned workstream paths).
- [ ] Deterministic `run_command` verification commands, script exit codes, and observed numerical outputs are recorded.
- [ ] Verified empirical facts, explicit model assumptions, and any `PARTIAL` or `NOT VERIFIED` items are cleanly separated.
- [ ] Internal relative Markdown links resolve cleanly on disk with zero `TODO`/`TBD` tokens or decorative prose.
- [ ] Structured 8-item Worker Handoff Report is complete and ready for `SA_GATE` and `PM_GATE` signoff.
