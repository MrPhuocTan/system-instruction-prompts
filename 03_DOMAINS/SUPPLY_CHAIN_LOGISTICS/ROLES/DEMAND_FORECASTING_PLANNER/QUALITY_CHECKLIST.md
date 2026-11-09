# Quality Checklist — Demand Forecasting Planner (`ROLE-SCM-002`)

Verify every item below before submitting a handoff report under [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md):

## 1. Temporal Hygiene, Stockout Uncensoring & Segmentation
- [ ] Rolling-origin backtest enforces strict temporal causality (`train_end < forecast_origin`) across all lags, scalers, and `ABC-XYZ` classifications—zero future data leakage.
- [ ] Historical stockout windows, discontinued SKUs, and one-time tender spikes are audited and uncensored/flagged rather than treated as normal demand drops.
- [ ] Moving calendar events (holidays, fiscal month-ends, promotions) and post-promotion pantry-loading dips / cross-SKU cannibalization are explicitly modeled.
- [ ] SKUs are classified via `Syntetos-Boylan` (`ADI` vs. $CV^2$) so intermittent/lumpy items (`ADI >= 1.32`) use `Croston` / `SBA` / `TSB` or discrete count distributions—never median-zero point regressions.

## 2. Error Metrics, Bias, `FVA` & Horizon Alignment
- [ ] Evaluation horizon matches actual operational replenishment/procurement freeze lead time ($L + R$), not misleading `t+1` step-ahead error alone.
- [ ] Scorecard reports `WMAPE`, signed `Forecast Bias` ($\frac{\sum(F-A)}{\sum A}$), `MASE`/`RMSSE`, and `Pinball Loss`—never raw unweighted `MAPE` on zero-actual SKUs.
- [ ] **Forecast Value Added (`FVA`)** proves positive error reduction over Seasonal Naive / Moving Average at every pipeline stage (statistical model + any manual adjustments).
- [ ] Persistent bias ($|\text{Bias}| > 5\%$ over `3+` consecutive periods) triggers an automated root-cause flag.

## 3. Probabilistic Calibration & Hierarchical Coherence
- [ ] Cumulative lead-time demand quantiles (`P50/P90/P95/P98` over $L + R$) are empirically calibrated (`PICP` coverage checked) for downstream safety-stock sizing.
- [ ] Hierarchical forecasts reconcile coherently (`MinT` / `WLS` / `Bottom-Up` verified within `< 1e-6`) across SKU, DC, category, and total revenue rollups.

## 4. Reproducibility, Exception Monitoring & Governance Hygiene
- [ ] Backtest folds, baselines, and reconciliation math were executed deterministically via Python (`run_command`) with fixed random seeds.
- [ ] New-Product Introduction (`NPI`) and end-of-life (`EOL`) phase-out curves explicitly document analog cluster priors and ramp decay assumptions.
- [ ] Price-elasticity and promotional regressions check multicollinearity (`VIF`) and isolate baseline volume from temporary pantry-loading lifts.
- [ ] Forecast tracking signals (`CUSUM` / smoothed error ratio) define automated alert thresholds when structural regime shifts occur.
- [ ] Customer/POS transaction PII is redacted or aggregated prior to analysis and handoff logging.
- [ ] Model selection rejects complex ML architectures whenever out-of-sample `FVA` fails to beat simpler statistical baselines (`ETS` / `SBA`).
- [ ] Unit-of-measure conversions (`eaches`, `cases`, `pallets`, `tonnes`, currency) are reconciled consistently across historical and forecast horizons.
- [ ] Forecast residual autocorrelation (`Ljung-Box`) and heteroscedasticity across volume tiers are checked before generating parametric intervals.
- [ ] Verified POS/ERP actuals vs. imputed stockout adjustments are documented transparently in [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md).
- [ ] **Mandatory Human Approval** gate blocks autonomous publishing of forecast overrides into live `MRP` / `ERP` production schedules.
