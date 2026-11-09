# Quality Checklist — Industrial Systems Engineer (`ROLE-MFG-001`)

Verify every item below before submitting a handoff report under [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md):

## 1. Takt, OEE & Capacity Mathematics
- [ ] Net available operating time explicitly deducts planned breaks, shift handovers, and scheduled preventive maintenance without hiding unplanned downtime.
- [ ] `Takt Time = Net Available Operating Time / Customer Demand` uses consistent time and unit dimensions across shifts.
- [ ] `OEE = Availability * Performance * Quality` reconciles exactly with `ISO 22400` six-big-losses breakdown (breakdowns, setup/adjustments, idling/minor stops, reduced speed, startup rejects, production rejects).
- [ ] Product-mix weighted cycle times account for sequence-dependent changeover matrices (`SMED` internal vs. external step split documented).

## 2. Stochastic Queueing, WIP & Line Balancing
- [ ] Task-to-station assignment satisfies `100%` of assembly precedence constraints (verified via DAG topological check).
- [ ] Bottleneck effective utilization stays within safe stochastic bounds (`<= 85–90%` unless decoupled and empirically simulated) with Kingman VUT or `DES` queue wait times reported.
- [ ] Blocking-after-service and starvation probabilities are modeled for finite inter-station buffers (`WIP` cap > 0 specified per buffer).
- [ ] Little's Law ($\text{WIP} = \text{Throughput} \times \text{Lead Time}$) holds within `< 1%` steady-state tolerance across simulated runs after warm-up period removal.
- [ ] Rework and scrap loops preserve mass/unit conservation without infinite-loop divergence.

## 3. Ergonomics, Layout & Physical Safety Compliance
- [ ] Manual handling tasks are evaluated against `NIOSH Lifting Index` (`LI <= 1.0` target; mechanical assist mandated above threshold) or `RULA`/`REBA` posture criteria.
- [ ] Cell layout preserves safety light-curtain minimum approach distances (`ISO 13855`), LOTO maintenance access envelopes, and emergency egress aisles.
- [ ] Forklift/AGV/pedestrian aisle intersections are separated or controlled rather than crossed blindly to save travel distance.

## 4. Reproducibility, Sensitivity & Governance Hygiene
- [ ] Discrete-event simulation (`DES`) or queueing script was executed via `run_command` with fixed random seeds ($N \ge 30$ replications).
- [ ] Steady-state throughput, WIP, and queue waiting times report `P10 / P50 / P90` percentiles and `95%` confidence intervals.
- [ ] Sensitivity analysis tests `+15%` demand surge, worst-case changeover sequence, and primary bottleneck machine downtime scenarios.
- [ ] Measured MES/stopwatch telemetry is explicitly separated from assumed operator pace, yield, or learning-curve parameters.
- [ ] CapEx, staffing, and buffer-footprint trade-offs are summarized without decorative filler or unsupported ROI claims.
- [ ] All internal links and artifact paths resolve cleanly for [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md).
- [ ] Mandatory Human Approval Gate notice is attached before any physical cell rearrangement, staffing change, or live MES schedule push.
