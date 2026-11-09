# Quality Checklist: Grid and Power Systems Engineer (`ROLE-ENG-002`)

- **Role:** [GRID_AND_POWER_SYSTEMS_ENGINEER](./SYSTEM_PROMPT.md)
- **Domain Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md) (`QG-ENG-001`, `QG-ENG-002`)

## 1. Network Model & Per-Unit Data Integrity
- [ ] System `S_base` (`MVA`), bus nominal `V_base` (`kV`), and nominal frequency (`50 Hz` or `60 Hz`) are explicitly declared.
- [ ] Equipment per-unit impedance conversions (`transformers`, `lines`, `cables`, `reactors`) pass automated checks with zero $\sqrt{3}$ or base-MVA scaling errors.
- [ ] Positive-, negative-, and zero-sequence impedances, transformer vector groups, neutral grounding impedances, and `OLTC` tap bounds are populated for unbalanced and fault calculations.
- [ ] Conductor and transformer thermal limits distinguish continuous normal (`Rate A`) from short-term emergency (`Rate B` / ambient-adjusted) ratings.

## 2. Steady-State AC Load Flow & `N-1` Contingency Verification
- [ ] Full AC Newton-Raphson (or 3-phase unbalanced distribution) power flow converges within $< 10^{-6}\text{ p.u.}$ mismatch across peak load, minimum load / maximum DER export, and stressed transfer cases.
- [ ] System active ($P$) and reactive ($Q$) power balances close exactly (`Generation = Load + Shunt + Series Losses + Line Charging`).
- [ ] Every credible `N-1` single-element contingency (`line`, `transformer`, `generator`, `reactive bank`) is simulated across bounding dispatches.
- [ ] Non-convergent `N-1` contingencies are flagged explicitly as potential voltage-collapse hazards (`PV/QV` nose-curve margin failure) rather than omitted.
- [ ] Bus voltages remain within normal ($0.95\text{--}1.05\text{ p.u.}$) and post-contingency statutory bands, and branch `MVA` loadings stay $\le 100\%$ of applicable ratings (or engineered mitigations are re-solved and proven compliant).

## 3. Interconnection (`POI`), Fault Duty & Stability Screening
- [ ] Generator / `IBR` reactive power capability (`P-Q` curve / power factor) is verified strictly at the high-side Point of Interconnection (`POI`) after collector cable and GSU transformer reactive losses.
- [ ] Maximum symmetrical (`3LG`) and unbalanced (`SLG`, `LL`, `2LG`) fault currents are verified against switchgear interrupting and momentary peak duty ratings (`IEC 60909` / `ANSI C37`).
- [ ] Minimum fault MVA and Short-Circuit Ratio (`SCR` / `WSCR`) at the `POI` are calculated; weak-grid conditions (`SCR < 3.0`) explicitly flag mandatory `EMT` (`PSCAD`) and grid-forming (`GFM`) follow-up studies.
- [ ] `IEEE 1547` / `IEEE 2800` voltage/frequency ride-through, anti-islanding, and converter current-limited protection coordination issues (`blinding`, `sympathetic tripping`) are addressed.

## 4. Safety, `CEII` Confidentiality & Human PE Signoff
- [ ] Harmonic distortion (`IEEE 519` `THD`/`TDD`) and transformer energizing inrush / ferroresonance risks are screened where converter or capacitor banks connect.
- [ ] Islanded microgrid modes verify black-start capability, frequency/voltage droop sharing, and resynchronization phase-angle check (`ANSI 25`) limits.
- [ ] Proprietary `EMT` (`PSCAD`) and vendor black-box model boundaries are transparently disclosed alongside open-source (`pandapower`/`OpenDSS`) results.
- [ ] Zero `CEII` / `NERC CIP` secrets, substation IP addresses, or live SCADA credentials are exposed in outputs.
- [ ] Verified telemetry, standard impedance assumptions, simulation estimates, and unverified dynamic phenomena are separated in [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md).
- [ ] Deliverable explicitly requires licensed human `PE` review and utility operator approval prior to relay setting deployment, arc-flash labeling, or live switching execution.
