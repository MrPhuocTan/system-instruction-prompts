# Quality Checklist: Energy Systems Analyst (`ROLE-ENG-001`)

- **Role:** [ENERGY_SYSTEMS_ANALYST](./SYSTEM_PROMPT.md)
- **Domain Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md) (`QG-ENG-001`, `QG-ENG-003`)

## 1. Physical & Thermodynamic Conservation Checks
- [ ] Every modeled node and energy carrier (`electricity`, `steam/heat`, `H2`, `fuel`, `CO2`) satisfies mass and energy balance closure ($\le 0.01\%$ numerical residual) across every timestep.
- [ ] Fuel heating values (`LHV` vs. `HHV`) and unit conversions (`MMBtu`, `GJ`, `MWh_th`, `kg`) are explicitly stated and applied consistently across fuel costs and heat rates.
- [ ] Parasitic auxiliary loads (compression, liquefaction, cooling pumps, inverter standby, CCS steam/power) are deducted from gross output.
- [ ] Thermal conversion efficiencies, heat-pump `COP` vs. temperature-lift curves, and electrolyzer specific energy obey Carnot and stoichiometric bounds.
- [ ] Storage state-of-energy (`SoE`) equations enforce separate charge/discharge efficiencies, standing losses, and usable `DoD` limits.
- [ ] Cyclic storage boundary closure ($SoE_{T} \ge SoE_{0}$) is enforced so the horizon does not extract unreplenished initial energy.
- [ ] Complementarity verified: zero non-physical simultaneous charging and discharging of the same storage asset during curtailment or negative-price hours.

## 2. Chronological Dispatch & Reliability Adequacy Checks
- [ ] Variable renewable generation, demand profiles, and ambient thermal derates use time-synchronized chronological (`8760` or sub-hourly) series rather than non-coincident averages.
- [ ] Optimization solver terminated with proven `OPTIMAL` status (or documented `MILP` optimality gap $\le 0.1\%$).
- [ ] Zero uninspected slack or artificial load-shedding variables distort dispatch; `EUE` and curtailment `%` are explicitly tabulated.
- [ ] Resource adequacy metrics (`LOLE`, `EUE`, reserve margin, peak net-load ramp) are tested across both typical and extreme-weather (`dunkelflaute` / drought) years.

## 3. Techno-Economic & `LCOE` / `LCOS` Parity Checks
- [ ] Currency code, base year, and `WACC` basis (`real` vs. `nominal`) match across all `CAPEX`, `FOM`, `VOM`, fuel, tax/incentive, augmentation, and decommissioning cashflows.
- [ ] `LCOE` and `LCOS` denominators use net meter-delivered energy after availability, degradation, round-trip storage loss, and curtailment.
- [ ] Portfolio comparisons report total annualized system cost (including firming, backup, and grid upgrades) alongside standalone asset `LCOE`.
- [ ] Sensitivity sweeps (`WACC`, `CAPEX`, fuel/carbon price, weather year) are executed and summarized with clear decision crossover points.

## 4. Reproducibility, Data Hygiene & Handoff Readiness
- [ ] Model scripts, solver tolerances, and parameter CSV/JSON inputs execute deterministically via `run_command` with zero hardcoded secrets.
- [ ] Independent audit script confirms `NPV(Net_MWh * LCOE) == NPV(Lifecycle_Costs)` within $\pm \$0.01/\text{MWh}$.
- [ ] Dual shadow prices (`LMPs`, marginal carbon abatement costs) are inspected for physical plausibility and unit consistency.
- [ ] Proprietary commercial tool gaps (`PLEXOS`/`AURORA` vs. `PyPSA`/LP) are transparently disclosed with exportable input schemas.
- [ ] Verified meter facts, literature/ATB assumptions, model estimates, and unmodeled AC grid stability boundaries are clearly separated in [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md).
- [ ] Mandatory human approval gate is flagged prior to capital procurement, tariff filing, or operational dispatch commitment.
