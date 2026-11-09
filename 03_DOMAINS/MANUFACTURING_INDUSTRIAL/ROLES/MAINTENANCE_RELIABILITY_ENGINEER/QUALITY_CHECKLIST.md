# Quality Checklist — Maintenance & Reliability Engineer (`ROLE-MFG-005`)

Verify every item below before submitting a handoff report under [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md):

## 1. Weibull Life-Data & Availability Mathematics
- [ ] Failure data is segregated by distinct physical failure mode (`ISO 14224`) rather than pooling unrelated failure mechanisms.
- [ ] Right-censored operating hours (surviving/suspended units) are explicitly included in Weibull MLE or median-rank regression calculations—never discarded.
- [ ] Weibull shape ($\beta$), scale ($\eta$), MTBF ($\eta \cdot \Gamma(1 + 1/\beta)$), and confidence bounds are verified via an executed Python script (`run_command`).
- [ ] System Reliability Block Diagram (`RBD`) and Operational Availability ($A_o$) account for repair downtime (`MTTR`), logistics/spares wait time, and imperfect switchover where applicable.

## 2. `SAE JA1011` RCM Logic & `CBM` Strategy Alignment
- [ ] Maintenance task selection matches Weibull $\beta$: zero scheduled intrusive tear-downs prescribed for $\beta \le 1.0$ failure modes.
- [ ] Every On-Condition (`CBM`) task defines the physical precursor signal (vibration `ISO 20816`, thermography, oil `ISO 4406`, ultrasound, `MCSA`), quantitative alert/trip thresholds, and inspection interval `<= P-F / 2`.
- [ ] Hidden protective functions (relief valves, standby trips, emergency backups) have mathematically calculated Failure-Finding Intervals (`FFI`) meeting target availability.
- [ ] Critical MRO spare-parts min/max levels are verified against lead-time Poisson demand and target stockout service level (`>= 95–99%` for bottleneck/safety spares).

## 3. `LOTO`, Statutory Compliance & Safety Execution
- [ ] Every intrusive `PM` or corrective job plan enumerates all hazardous energy sources (`OSHA 1910.147` / `ISO 14118`: electrical, pneumatic, hydraulic, gravity, thermal, chemical, spring/capacitor).
- [ ] Isolation device IDs, bleed/vent/mechanical-block steps, personal lock application, and **Try-Start / Zero-Energy Verification** are explicitly sequenced.
- [ ] Arc-flash boundaries (`NFPA 70E`), confined-space atmospheric checks, or hot-work permits are specified whenever energized or enclosed access applies.
- [ ] Precision maintenance acceptance tolerances (shaft laser alignment `<= 0.05 mm`, dynamic balance grade `ISO 21940`, fastener torque sequence) are included to prevent infant mortality.
- [ ] Statutory inspection intervals (`ASME` pressure vessels, `OSHA 1910.179` cranes/hoists, relief valves) remain intact unless escalated for certified authority sign-off.

## 4. Reproducibility, Spares & Handoff Governance
- [ ] Censored Weibull fits, `P-F / 2` intervals, RBD availability, and Poisson spares models were independently executed via `run_command`.
- [ ] Spare-parts shelf-life maintenance (motor shaft periodic rotation against false brinelling, capacitor reforming, desiccant seals) is specified for stored critical spares.
- [ ] Root-cause Defect Elimination (`RCFA`) distinguishes installation/alignment infant mortality from material fatigue wear-out.
- [ ] CMMS failure-code taxonomy (`ISO 14224` Equipment Class $\rightarrow$ Failure Mechanism $\rightarrow$ Failure Cause) is enforced for closed work orders.
- [ ] Field CMMS failure records are clearly distinguished from handbook failure-rate priors (`OREDA` / `IEEE 493`) in [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md).
- [ ] Mandatory Human Approval Gate is attached before modifying live `CMMS` schedules, alarm trip setpoints, or safety-device test intervals.
