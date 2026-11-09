# Manufacturing & Industrial Engineering Quality Gates (`MANUFACTURING_INDUSTRIAL`)

All deliverables produced within `03_DOMAINS/MANUFACTURING_INDUSTRIAL/` must satisfy the objective quality gates below prior to `DOMAIN_LEAD`, `SA`, and `PM` sign-off under [REVIEW_AND_SIGNOFF.md](../../01_ORCHESTRATION/REVIEW_AND_SIGNOFF.md) and [INDEPENDENT_VERIFICATION.md](../../00_GLOBAL_CONSTITUTION/INDEPENDENT_VERIFICATION.md). Any gate lacking empirical plant telemetry must be explicitly labeled `NOT VERIFIED — PLANT TRIAL REQUIRED` rather than assumed passed.

## 1. Mandatory Domain Quality Gates (`QG-MFG-01` – `QG-MFG-07`)

### `QG-MFG-01` — Process Capability & Measurement System (`MSA`) Gate
- **Pass Criteria:** Gage R&R `%GRR < 10%` (`10–30%` conditionally acceptable with documented risk rationale; `> 30%` rejected) and `ndc >= 5`; zero active Western Electric / Nelson SPC out-of-control violations; $C_{pk} \ge 1.33$ for standard CTQs and $C_{pk} \ge 1.67$ for Critical/Safety characteristics (`CC`/`SC`).
- **Required Evidence:** Executed statistical audit (`n >= 25` subgroups / `>= 100` parts where available) reporting normality p-values, within-subgroup $\hat{\sigma}_{\text{within}}$ vs. overall $\hat{\sigma}_{\text{overall}}$, `95%` confidence bounds, and ANOVA Gage R&R variance components.
- **Blocking Failure:** Conflating $P_{pk}$ with $C_{pk}$, computing parametric capability on unstable/non-normal data without transformation, or ignoring `%GRR > 30%`.

### `QG-MFG-02` — DFMEA / PFMEA & Special Characteristics Gate
- **Pass Criteria:** Complete AIAG-VDA 7-step structure reporting Severity (`1–10`), Occurrence (`1–10`), Detection (`1–10`), and Action Priority (`AP`). `100%` of `Severity 9–10` and `AP = High` failure modes incorporate physical `poka-yoke` error-proofing or design prevention controls.
- **Required Evidence:** Bi-directional traceability matrix linking Design `CC`/`SC` callouts $\rightarrow$ PFMEA rows $\rightarrow$ Control Plan gaging, sample frequency, and out-of-control reaction plan.
- **Blocking Failure:** Using legacy RPN thresholds to waive `Severity 9–10` safety risks, or listing `"operator retraining / visual attention"` as sole prevention.

### `QG-MFG-03` — Dimensional & Tolerance Stack-Up Gate
- **Pass Criteria:** Explicit `ASME Y14.5` / `ISO 1101` datum reference frame, closed vector loop equations, thermal expansion correction ($\Delta L = \alpha L \Delta T$) where applicable, and verified Worst-Case (`> 0` margin for safety-critical fits) plus `RSS` / Monte Carlo defect projections.
- **Required Evidence:** Deterministic Python calculation output (`run_command`) verifying nominal gap, Worst-Case min/max, `RSS` bounds, and `%` variance contribution per feature.
- **Blocking Failure:** Unclosed vector loops, unverified bonus/datum-shift claims, or manual arithmetic without script verification.

### `QG-MFG-04` — OEE, Line Balance & Queueing Physics Gate
- **Pass Criteria:** Takt time accurately derived from net operating time; bottleneck utilization bounded (`<= 85–92%` under stochastic variance unless buffered and simulated); `OEE = Availability * Performance * Quality` reconciled with changeover (`SMED`) and scrap/rework losses; Little's Law ($\text{WIP} = \lambda \cdot W$) satisfied.
- **Required Evidence:** Reproducible queueing calculation or multi-seed Discrete-Event Simulation (`DES`) reporting `P10/P50/P90` throughput and station blocking/starvation percentages.
- **Blocking Failure:** Assuming `100%` deterministic utilization in multi-stage serial lines or manipulating OEE scheduled-time denominators.

### `QG-MFG-05` — IEC 62443 OT/ICS & PLC Determinism Gate
- **Pass Criteria:** Purdue Level `0–4` network segmentation with Level `3.5` IDMZ; zero direct Level `4`/cloud-to-Level `1` write paths; cyclic PLC routines free of unbounded loops/blocking calls; explicit safe fail states on `NAMUR NE 43` wire-break (`< 3.6 mA`), comms timeout, and power loss; `SIS` (`IEC 61511`) independent of `BPCS`.
- **Required Evidence:** `IEC 62443` Zone/Conduit table, Cause-and-Effect (`C&E`) interlock matrix, watchdog budget check, and offline Python state-transition verification log.
- **Blocking Failure:** Recommending active network scanning against live PLCs, double-coil output bugs, or crediting non-safety PLC code for `SIL 2+` / `PL d–e` protection.

### `QG-MFG-06` — ISO 9001 / IATF 16949 Traceability & Calibration Gate
- **Pass Criteria:** Controlled revision metadata, lot/serial genealogy schema, `ISO/IEC 17025` / NIST gage calibration traceability (`TUR >= 4:1` target), quarantine containment workflow, and `8D`/`CAPA` dual root-cause analysis (Occurrence + Escape).
- **Required Evidence:** Traceability audit table mapping specifications to shop-floor reaction plans and systemic `D5/D7` corrective actions.
- **Blocking Failure:** Closing `CAPA` records with `"human error"` as root cause or waiving suspect lots without formal `MRB` review.

### `QG-MFG-07` — Lockout/Tagout (`LOTO`) & Physical Safety Approval Gate
- **Pass Criteria:** Complete `OSHA 1910.147` / `ISO 14118` hazardous energy inventory, isolation devices, stored-energy bleed/blocking steps, zero-energy try-start check, PPE specification, and **Mandatory Human Approval Gate** banner on all PLC, SCADA, CNC, or actuator instructions.
- **Required Evidence:** Dedicated safety block in the deliverable and confirmation in [HANDOFF_REPORT.md](../../06_TEMPLATES/HANDOFF_REPORT.md) that zero autonomous hardware actuation occurred.
- **Blocking Failure:** Omitting pneumatic/hydraulic/gravity stored energy isolation, bypassing machine guards, or attempting live controller writes without human approval.

## 2. Independent Verification & Separation-of-Duties Protocol
1. **Executable Math Audit:** Reviewers (`QUALITY_REVIEWER`, `DOMAIN_LEAD`, or `SA`) must re-run or independently verify at least one governing calculation (stack-up margin, $C_{pk}$, Takt/WIP balance, or censored Weibull fit) via `run_command`.
2. **Author vs. Verifier Independence:** On Level 3–4 regulated deliverables, process/PLC authors (`MANUFACTURING_PROCESS_ENGINEER`, `OT_ICS_ENGINEER`) may never self-approve final quality/safety gates; independent sign-off by `QUALITY_CONTROL_SIX_SIGMA` or `QUALITY_REVIEWER` is mandatory.
3. **Epistemic Transparency:** Distinguish **Measured Plant Data**, **Standard/Handbook Constants**, **Model Estimates**, and **Unvalidated Shop Assumptions** in every handoff package.
