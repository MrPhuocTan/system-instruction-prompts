# Quality Checklist — Logistics & Network Optimizer (`ROLE-SCM-003`)

Verify every item below before submitting a handoff report under [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md):

## 1. Baseline Calibration & Mathematical Formulation (`MILP` / `CVRPTW`)
- [ ] A **Constrained As-Is Baseline** run is calibrated against historical spend/miles first so optimization savings are measured apples-to-apples without modeling-artifact inflation.
- [ ] Sets, decision variables, objective terms, `Big-M` tight physical bounds, solver status (`OPTIMAL` / `FEASIBLE`), and exact `MIP Optimality Gap %` are explicitly documented.
- [ ] Facility capacity, dock-door throughput, and fleet sizing satisfy **peak-week (`P95`) surge volume**—not merely `annual_volume / 365` averages.
- [ ] Mode-conversion models (`Air <-> Ocean`, `FTL <-> Intermodal/LTL`) include stepped weight/deficit-rating tariffs, fuel surcharges, detention/demurrage, AND in-transit pipeline + safety-stock carrying costs.

## 2. Physical, Vehicle & Regulatory Feasibility Constraints
- [ ] Independent post-solve audit script (`run_command`) confirms `100%` supply-DC-customer flow conservation (`max_error < 1e-6`) across all SKUs/commodities.
- [ ] Every vehicle/container load satisfies **both legal weight (`GVWR`/axle) AND cubic volume / non-stackable pallet floor-spot** limits simultaneously.
- [ ] Transit matrices apply realistic road circuity factors, urban/highway speed profiles, port/border dwell times, and customer delivery time windows.
- [ ] Every routed tour obeys statutory driver Hours-of-Service (`FMCSA 49 CFR 395` `11-hr` drive / `14-hr` shift / mandatory rest breaks or `EU EC 561/2006`).
- [ ] Hazmat segregation (`49 CFR` / `IMDG` / `IATA`) and `GDP` cold-chain temperature-zone constraints are strictly enforced where applicable.

## 3. Resilience Sensitivity, Emissions & Commercial Governance
- [ ] Sensitivity runs evaluate `+25%` fuel surcharge shocks, primary DC/port outage rerouting cost, and `+15%` peak volume stress.
- [ ] Transition / facility-closure one-time severance, lease exit, and inventory relocation costs are netted in multi-year NPV payback tables.
- [ ] Empty backhaul / deadhead miles and container repositioning imbalances are explicitly accounted for in dedicated fleet sizing.
- [ ] Freight `gCO2e / tonne-km` (`GLEC` / `ISO 14083` well-to-wheel factors) and `Incoterms 2020` cost/risk transfer points are reported accurately.
- [ ] Multi-stop drop-sequence unloading order (`LIFO` rear-door accessibility!) is checked so early stops are not blocked behind late-stop pallets.

## 4. Reproducibility & Dispatch Approval Gate
- [ ] Solver script and independent feasibility checker executed cleanly via `run_command` with zero constraint violations (`< 1e-6`).
- [ ] Carrier allocation diversification avoids `100%` single-carrier dependency on mission-critical high-volume lanes.
- [ ] Cross-border customs clearance lead-time variance and drayage chassis availability constraints are included on international lanes.
- [ ] Offline Haversine/circuity assumptions vs. turn-by-turn TMS truck-nav verification steps are disclosed in [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md).
- [ ] **Mandatory Human Approval** gate blocks any autonomous EDI `204` carrier load tender or live TMS route dispatch.
