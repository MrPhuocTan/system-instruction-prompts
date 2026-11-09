# Quality Checklist — Manufacturing Process Engineer (`ROLE-MFG-002`)

Verify every item below before submitting a handoff report under [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md):

## 1. GD&T, Datum Scheme & Tolerance Stack-Up
- [ ] Every stack-up references explicit `ASME Y14.5` / `ISO 1101` datums (`A | B | C`) and distinguishes bilateral, unilateral, geometric position/profile, and bonus/datum-shift terms accurately.
- [ ] Vector loop sign convention closes mathematically and is verified via executed Python calculation (`run_command`), reporting Worst-Case, `RSS` (with stated $C_p$/mean-shift factor), and Monte Carlo defect ppm.
- [ ] Thermal expansion ($\Delta L = \alpha L \Delta T$), tool wear drift, and clamping elastic deflection are included whenever dissimilar materials (e.g., aluminum housing + steel shaft) or tight tolerances (`< +/- 0.025 mm`) apply.
- [ ] Fixture locating scheme follows `3-2-1` kinematic constraint (e.g., planar 3-pad primary, 1 round + 1 diamond pin) with zero over-constraint part distortion.

## 2. Unit-Process Physics & CNC / Tooling Safety
- [ ] Cutting/forming/molding parameters (`SFM`/`Vc`, feed per tooth `fz`, clamping force, cure temp/pressure) are bounded within spindle power, tool deflection, and fixture slip safety factor (`SF >= 2.5`).
- [ ] Any CNC G-code snippet includes a mandatory safe startup header (`G17 G20/G21 G40 G49 G80 G90`), explicit work offset (`G54`), tool-length offset (`G43 H..`), clamp clearance `Z` plane, and **Offline CAM Collision + Dry-Run Single-Block Human Approval** notice.

## 3. AIAG-VDA PFMEA & Control Plan Traceability
- [ ] Process Flow Diagram, PFMEA, and Control Plan share identical Operation IDs (`OP10`, `OP20`, ...) with `100%` trace coverage of Critical (`CC`) and Significant (`SC`) characteristics.
- [ ] Every `Severity 9–10` and `AP = High` failure mode includes a physical/sensor `poka-yoke` prevention control rather than relying solely on visual inspection or operator training.
- [ ] Control Plan specifies exact measurement instrument, `MSA`/calibration expectation, sample size/frequency, SPC method, and concrete quarantine/containment reaction plan for out-of-spec events.

## 4. First Article / PPAP Readiness, LOTO & Governance Hygiene
- [ ] Ballooned drawing characteristics map `100%` to First Article Inspection (`AS9102` `FAI`) or `AIAG PPAP` dimensional results layouts.
- [ ] Gage selection achieves Test Uncertainty Ratio `TUR >= 4:1` against print tolerance and specifies `MSA` Gage R&R expectations.
- [ ] Setup and tool-change sheets specify `OSHA 1910.147` / `ISO 14118` `LOTO` energy isolation, bleed/block verification, and try-start steps.
- [ ] Coolant, mist, welding fume, or composite dust controls reference applicable Safety Data Sheet (`SDS`) ventilation and PPE requirements.
- [ ] Heavy fixture/die handling (`> 15–23 kg`) specifies hoist/eyebolt rated load limits and center-of-gravity rigging points.
- [ ] Known print dimensions, handbook material constants, and unvalidated shop-trial estimates are explicitly separated in [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md).
- [ ] Process capability run-at-rate trial plan (`>= 300` consecutive parts or `25+` subgroups) is specified prior to full production handover.
- [ ] Tool-life tracking counters and presetter wear-offset replacement thresholds are defined to prevent sudden tool fracture.
- [ ] Mandatory Human Approval Gate blocks direct execution of CNC G-code, press tonnage, or thermal cure recipes on physical equipment.
- [ ] Author vs. independent quality reviewer separation is preserved for Level 3–4 regulated part sign-offs.
- [ ] Zero unverified material substitutions or informal print-tolerance waivers appear in the process package.
