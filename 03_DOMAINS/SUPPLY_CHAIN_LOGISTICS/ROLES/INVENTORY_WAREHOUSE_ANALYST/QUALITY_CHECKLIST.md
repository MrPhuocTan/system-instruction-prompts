# Quality Checklist — Inventory & Warehouse Analyst (`ROLE-SCM-005`)

Verify every item below before submitting a handoff report under [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md):

## 1. Safety-Stock, Service-Level & Replenishment Mathematics
- [ ] Service metric explicitly distinguishes **Cycle Service Level (`CSL` Type I)** from **Item Fill Rate (`FR` Type II)** and solves $G(z) = \frac{(1 - \beta)Q}{\sigma_{\text{DDLT}}}$ accurately so large-`MOQ` cycle stock is never double-buffered.
- [ ] Vulnerability horizon includes **both replenishment Lead Time AND Review Period** ($\bar{L} + R$), with compound variance $\sigma_{\text{DDLT}} = \sqrt{(\bar{L}+R)\sigma_e^2 + \bar{D}^2\sigma_L^2}$ driven by out-of-sample forecast error $\sigma_e$.
- [ ] Skewed, intermittent, or low-volume SKUs (`CV > 0.5` or mean DDLT `< 10` units) use Negative-Binomial, Gamma, or bootstrap quantiles rather than Gaussian approximations that allow negative demand.
- [ ] Order quantities respect `MOQ`, case/layer/pallet pack-rounding multiples, storage cube caps, and **Newsvendor** / `FEFO` shelf-life spoilage ceilings.
- [ ] Working-Capital (`$`) vs. Fill Rate (`90%`, `95%`, `98%`, `99.5%`) efficient-frontier table is generated with explicit annual carrying-cost rate (`h %`).

## 2. Stochastic Simulation Verification (`Monte Carlo`)
- [ ] Multi-seed daily discrete-time inventory simulation (`N >= 100` replications via `run_command`) confirms realized Fill Rate matches analytical target within `+/- 1.0%`.
- [ ] Simulation explicitly models backorder vs. lost-sales mechanics, stochastic lead times, pack rounding, and `FEFO` lot expiration write-offs.

## 3. Warehouse Slotting (`COI`), Ergonomics & Physical Rack Safety
- [ ] Forward-pick allocation (`Bartholdi-Hackman` $\sqrt{f_i c_i}$) satisfies total forward cubic capacity ($\sum v_i \le V_{\text{forward}}$) and balances restock labor against pick savings.
- [ ] Cube-per-Order Index (`COI`) slotting places heavy/fast picks in the ergonomic **Golden Zone** (`NIOSH` waist-to-shoulder window) AND disperses ultra-hot SKUs across aisles to prevent picker/forklift congestion.
- [ ] Slotting plan respects `ANSI MH16.1` rack beam/bay weight ratings, `NFPA 13` sprinkler flue spaces, cold-chain/Hazmat segregation, and `ABC` statistical cycle-count schedules.

## 4. Governance, Auditability & ERP/WMS Cutover Gate
- [ ] Excess & Obsolete (`E&O` / `SLOB`) exposure is quantified separately from active healthy cycle and safety stock.
- [ ] Multi-echelon (`MEIO`) upstream vs. downstream buffer placement verifies guaranteed/stochastic service propagation across DC tiers.
- [ ] Warehouse dock-to-stock receiving and wave-release cutoffs align realistically with carrier departure schedules.
- [ ] Forklift vs. pedestrian aisle separation (`OSHA 1910.178`) and dock-lock / wheel-chock safety rules are preserved in layout changes.
- [ ] Inventory Record Accuracy (`IRA`) tolerances and root-cause transaction audit triggers are specified for `ABC` cycle counts.
- [ ] All analytical safety-stock equations and Monte Carlo simulations were verified via deterministic Python scripts (`run_command`).
- [ ] Unit-of-measure consistency (`base unit` vs. `order pack` vs. `pallet layer`) is verified across `ROP`, `EOQ`, and cube calculations.
- [ ] Returns / reverse-logistics quarantine grading (`restock` vs. `refurbish` vs. `scrap`) prevents defective stock from inflating available-to-promise (`ATP`) inventory.
- [ ] Verified SKU master attributes vs. assumed carrying/shortage cost parameters are separated in [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md).
- [ ] **Mandatory Human Approval** gate blocks any direct parameter upload into live `ERP` / `WMS` production systems.
