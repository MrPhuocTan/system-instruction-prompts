# Supply Chain & Logistics Quality Gates (`SUPPLY_CHAIN_LOGISTICS`)

All analytical models, inventory policies, network optimizations, and sourcing recommendations inside `03_DOMAINS/SUPPLY_CHAIN_LOGISTICS/` must pass the objective gates below prior to `DOMAIN_LEAD`, `SA`, and `PM` sign-off under [REVIEW_AND_SIGNOFF.md](../../01_ORCHESTRATION/REVIEW_AND_SIGNOFF.md) and [INDEPENDENT_VERIFICATION.md](../../00_GLOBAL_CONSTITUTION/INDEPENDENT_VERIFICATION.md). Any input lacking verified ERP/carrier actuals must be labeled `ASSUMED PARAMETER — SENSITIVITY TESTED`.

## 1. Mandatory Domain Quality Gates (`QG-SCM-01` – `QG-SCM-06`)

### `QG-SCM-01` — Demand Forecast Accuracy, Bias & `FVA` Gate
- **Pass Criteria:** Rolling-origin out-of-sample evaluation (`>= 3` folds or holdout horizon $\ge L + R$) with zero future data leakage; reports `WMAPE`, signed `Forecast Bias` (flagged if $|\text{Bias}| > 5\%$ persistent over/under-forecast), `MASE`, and positive **Forecast Value Added (`FVA > 0`)** over Seasonal Naive; intermittent SKUs (`ADI >= 1.32`) modeled via Croston/`SBA`/`TSB` or count distributions rather than raw `MAPE`; stockout-censored periods identified or imputed.
- **Required Evidence:** Executed Python backtest table (`run_command`) segmented by `ABC-XYZ` demand classes comparing candidate model vs. naive baseline.
- **Blocking Failure:** In-sample-only error reporting, unflagged persistent forecast bias, or dividing by zero actuals in unweighted `MAPE`.

### `QG-SCM-02` — Safety Stock, Service-Level & Working-Capital Trade-Off Gate
- **Pass Criteria:** Explicit selection between `CSL` (Type I) and `Fill Rate` (Type II, unit normal loss $G(z)$); protection window covers full `Lead Time + Review Period` ($L + R$); compound variance incorporates both forecast RMSE ($\sigma_e$) and lead-time standard deviation ($\sigma_L$); non-normal / intermittent tails validated via discrete/bootstrap simulation; efficient-frontier curve quantifies inventory working-capital dollars across service levels (`90%`, `95%`, `98%`, `99.5%`).
- **Required Evidence:** Executed Python inventory calculation + stochastic Monte Carlo service-level verification (`run_command`) confirming empirical fill rate matches analytical target within `+/- 1.0%`.
- **Blocking Failure:** Omitting lead-time variability ($\sigma_L = 0$ assumed without proof), conflating `CSL` with `Fill Rate`, or ignoring shelf-life/obsolescence write-off cost.

### `QG-SCM-03` — Network & Routing Physical Feasibility (`MILP` / `CVRPTW`) Gate
- **Pass Criteria:** `100%` mass/flow conservation across supply, DC, and customer nodes; enforces capacity caps, `MOQ`/lot-size constraints, dual **weight AND cubic volume** vehicle limits, customer time windows, and statutory driver Hours-of-Service (`FMCSA` / `EU EC 561/2006`); reports exact solver status and `MIP Optimality Gap %`.
- **Required Evidence:** Deterministic solver execution log (`run_command` via `scipy.optimize.milp` / `ortools`) verifying zero constraint violations (`max_violation < 1e-6`) plus baseline vs. optimized cost/miles/carbon delta.
- **Blocking Failure:** Unbalanced node flows, exceeding trailer weight/cube or driver shift hours, or claiming optimality from an unverified heuristic.

### `QG-SCM-04` — Lead-Time Variability, Bullwhip & Resilience Stress-Test Gate
- **Pass Criteria:** Evaluates network/inventory performance under `P90/P95` lead-time tail spikes, port/lane closure (`TTS` vs. `TTR`), and `+20%` demand shock; computes multi-echelon **Bullwhip Ratio** and eliminates batching/promotion synchronization amplifiers.
- **Required Evidence:** Stress-test scenario matrix showing service-level degradation, expedite cost exposure, and recovery time (`TTR`) across disruption cases.
- **Blocking Failure:** Designing zero-slack single-lane just-in-time (`JIT`) flows based solely on mean transit time ($\bar{L}$) with zero disruption sensitivity check.

### `QG-SCM-05` — Supplier Concentration (`HHI`) & Total Cost of Ownership (`TCO`) Gate
- **Pass Criteria:** Landed `TCO` includes unit price, freight, `Incoterms 2020` insurance/handling, customs duties/tariffs, payment terms (`WACC` working-capital impact), inventory buffer cost, and quality/non-conformance cost; supplier **Herfindahl-Hirschman Index (`HHI`)** is audited at both Tier-1 vendor and geographic/sub-tier chokepoint levels with dual-sourcing or buffer plans where single-source share exceeds `50%` (`HHI > 0.25` high concentration).
- **Required Evidence:** Reproducible `TCO` waterfall comparison and Supplier Risk / `HHI` Matrix.
- **Blocking Failure:** Awarding `100%` volume on unit purchase price (`PPV`) alone while hiding tariff, lead-time buffer, or geographic single-point-of-failure exposure.

### `QG-SCM-06` — Customs, Trade Compliance & Commercial Approval Gate
- **Pass Criteria:** Explicit `Incoterms 2020` rule + named place (`FCAOrigin Terminal` vs. `FOB Port`), `HS`/`HTS` tariff & Rules-of-Origin assumptions flagged as provisional pending licensed customs broker sign-off, sanctioned-party (`OFAC`/`BIS`/`EU`) & forced-labor (`UFLPA`/`CSDDD`) screening checkpoints, Hazmat/cold-chain segregation (`IATA`/`IMDG`/`49 CFR`/`GDP`), and **Mandatory Human Approval** banner before any PO, tender, or ERP parameter commit.
- **Required Evidence:** Trade & Compliance Checklist in deliverable and [HANDOFF_REPORT.md](../../06_TEMPLATES/HANDOFF_REPORT.md).
- **Blocking Failure:** Misapplying maritime-only `FOB`/`CIF` Incoterms without flagging container terminal risk gaps, omitting sanctions/forced-labor due diligence on cross-border sourcing, or attempting live ERP/EDI execution without human sign-off.

## 2. Independent Verification & Separation-of-Duties Protocol
1. **Solver & Simulation Audit:**
   - Reviewers ([QUALITY_REVIEWER](../../02_CORE_ROLES/QUALITY_REVIEWER/SYSTEM_PROMPT.md), `DOMAIN_LEAD`, or `SA`) must re-execute optimization constraint checks and stochastic inventory simulations via `run_command` to verify that analytical claims hold under empirical simulation (`tool success != business feasibility`).
2. **Baseline Calibration Proof:**
   - Every network or routing optimization model must demonstrate a constrained `As-Is` baseline calibration run reconciled against historical volumes/spend before claiming optimization savings.
3. **Commercial & Legal Independence:**
   - On Level 3–4 sourcing awards, network closures, or cross-border tariff strategies, optimization authors may not self-approve commercial/legal compliance—independent audit and explicit human stakeholder sign-off are mandatory.
4. **Epistemic Tagging & Zero Live ERP Mutation:**
   - Distinguish **Verified ERP/WMS Actuals**, **Contracted Carrier/Supplier Tariffs**, **Statistical Forecasts**, and **Stress-Test Priors** in [HANDOFF_REPORT.md](../../06_TEMPLATES/HANDOFF_REPORT.md), confirming zero autonomous PO/EDI/ERP mutations occurred.
