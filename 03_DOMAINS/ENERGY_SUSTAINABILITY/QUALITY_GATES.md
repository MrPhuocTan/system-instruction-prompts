# Energy & Sustainability Quality Gates (`QUALITY_GATES.md`)

- **Domain:** `ENERGY_SUSTAINABILITY` (`DOM-14`)
- **Enforcement Stage:** Mandatory pre-handoff verification by the accountable specialist and gate audit by [DOMAIN_LEAD](../../02_CORE_ROLES/DOMAIN_LEAD/SYSTEM_PROMPT.md), `SA_GATE`, and `PM_GATE` under [REVIEW_AND_SIGNOFF.md](../../01_ORCHESTRATION/REVIEW_AND_SIGNOFF.md).
- **Pass Rule:** Any `FAIL` on an applicable gate blocks `PASS` signoff until remediated or explicitly documented as an out-of-scope boundary approved by `PM + SA`.

## 1. Gate Matrix (`QG-ENG-001` through `QG-ENG-007`)

| Gate ID | Gate Name | Objective Pass Criteria | Deterministic Verification Method | Blocking Failure Trigger |
| :--- | :--- | :--- | :--- | :--- |
| `QG-ENG-001` | **Thermodynamic & Mass/Energy Conservation** | Mass, enthalpy, carbon-atom, and electrical energy balances close within $\le 0.01\%$ across every node and timestep; `LHV`/`HHV` basis, auxiliary loads, and cyclic storage boundary ($SoE_T \ge SoE_0$) enforced. | Automated Python conservation assertion script summing nodal inflows, outflows, losses, and $\Delta SoE$ over full horizon. | Unexplained energy creation, Second-Law efficiency violation, mixed `LHV`/`HHV`, or storage depletion trick (`SoE_T < SoE_0`). |
| `QG-ENG-002` | **Power Flow, Interconnection & `N-1` Reliability** | Load-flow model matches declared AC/DC physics scope; bus voltages stay within statutory p.u. bands, branch `MVA` loadings $\le 100\%$ normal/emergency ratings under `N-0` and `N-1`, and fault/ride-through limits checked. | Power-flow solver convergence log, worst-case `N-1` contingency table, and voltage/thermal violation count $= 0$ (or documented mitigation). | Divergent AC solver ignored, copper-plate balance presented as grid interconnection approval, or unscreened `N-1` overload. |
| `QG-ENG-003` | **`LCOE` / `LCOS` Techno-Economic Parity** | Currency year, real vs. nominal `WACC`, tax/incentive assumptions, `CAPEX`/`OPEX`/augmentation schedules, degradation, and net post-curtailment `MWh` reconciled; sensitivity tornado executed. | Reproducible discounted cashflow/unit-cost script verifying NPV of revenues at `LCOE` equals NPV of lifecycle costs ($\pm \$0.01/\text{MWh}$). | Real cashflows discounted at nominal `WACC` (or vice versa), nameplate capacity used instead of net yield, or omitted BESS augmentation. |
| `QG-ENG-004` | **GHG Protocol Scope 1/2/3 & `EF` Traceability** | Consolidation boundary declared; Scope 1, dual Scope 2 (`location-based` + `market-based`), and 15 Scope 3 categories screened; `IPCC GWP` vintage locked; 100% of emission factors cite source, region, and year. | Tabular ledger cross-check confirming `Activity Data * EF * GWP = tCO2e` with zero orphan `EF` rows, unit mismatches, or missing Scope 2 pair. | Single Scope 2 figure reported without dual method, unattributed emission factors, mixed `AR4`/`AR5`/`AR6` `GWP`, or missing material Scope 3 category. |
| `QG-ENG-005` | **ISO 14040 / 14044 `LCA` Methodological Rigor** | Functional unit, reference flow, system boundary, cut-off threshold, co-product allocation rule, background LCI pedigree (`DQI`), and multi-impact sensitivity analysis documented in full. | Mass/element balance check on foreground unit processes plus allocation sensitivity comparison (`physical` vs. `economic` or system expansion). | Comparative product claim issued with asymmetric boundaries, single-indicator `GWP` tunnel vision, or missing critical-review disclosure. |
| `QG-ENG-006` | **Anti-Greenwashing & Claim Substantiation** | Gross Scope 1/2/3 inventory reported separately from carbon removals, offsets, and avoided emissions; contractual instruments meet market-boundary, vintage, additionality, and retirement rules. | Claim-to-evidence audit matrix mapping every public sustainability metric or net-zero statement to primary calculation rows and standard clauses. | Offsets subtracted from gross inventory totals, unbundled `RECs` applied across incompatible grid markets, or unsubstantiated "carbon neutral" label. |
| `QG-ENG-007` | **Environmental Permitting & Operational Safety** | Jurisdictional statutes, permit thresholds, receptor limits, monitoring (`CEMS`/sampling) QA, and mitigation hierarchy mapped accurately; human PE/regulatory/SCADA approval gates enforced. | Threshold comparison table (`modeled/measured concentration or discharge` vs. `statutory limit` with units and averaging period). | Wrong averaging period (`annual` vs. `1-hour`/`24-hour` NAAQS/BAT-AEL), uncited statutory limit, or live operational/filing action executed without human approval. |

## 2. Mandatory Dimensional, Chronological & Uncertainty Verification

Before marking any workstream `PASS`, execute deterministic checks via `run_command` where quantitative calculations exist:
1. **Dimensional & Unit Closure:**
   - Verify explicit SI / industry unit labels on every column and equation (`MW` vs. `MWh`, `MW_ac` vs. `MW_dc`, `kWh_th` vs. `kWh_e`, `kg CO2e` vs. `tCO2e` vs. `MtCO2e`).
   - Confirm stack/effluent concentration normalization (`mg/Nm3` or `ppmvd` at explicit reference $O_2\%$, temperature, pressure, and dry/wet gas basis).
2. **Chronological Time-Series Hygiene:**
   - Confirm UTC vs. local standard time alignment, solar midpoint convention, leap-year (`8784` vs. `8760` hours) handling, and zero silent NaN/drop interpolation across weather (`TMY`/`ERA5`), load, and market price series.
3. **Uncertainty & Sensitivity Quantification:**
   - Validate `P50`/`P75`/`P90` exceedance bands, IPCC Tier 1/2/3 error propagation, or multi-parameter sensitivity tornadoes so decision-makers never receive false single-point precision.

## 3. Role-to-Checklist Traceability

Each specialist must attach its completed role checklist alongside domain gate evidence:
- `ENERGY_SYSTEMS_ANALYST`: [QUALITY_CHECKLIST.md](./ROLES/ENERGY_SYSTEMS_ANALYST/QUALITY_CHECKLIST.md) (`QG-ENG-001`, `QG-ENG-003`)
- `GRID_AND_POWER_SYSTEMS_ENGINEER`: [QUALITY_CHECKLIST.md](./ROLES/GRID_AND_POWER_SYSTEMS_ENGINEER/QUALITY_CHECKLIST.md) (`QG-ENG-001`, `QG-ENG-002`)
- `RENEWABLE_ENERGY_SPECIALIST`: [QUALITY_CHECKLIST.md](./ROLES/RENEWABLE_ENERGY_SPECIALIST/QUALITY_CHECKLIST.md) (`QG-ENG-001`, `QG-ENG-003`)
- `ESG_CARBON_ACCOUNTING_ANALYST`: [QUALITY_CHECKLIST.md](./ROLES/ESG_CARBON_ACCOUNTING_ANALYST/QUALITY_CHECKLIST.md) (`QG-ENG-004`, `QG-ENG-005`, `QG-ENG-006`)
- `ENVIRONMENTAL_COMPLIANCE_SPECIALIST`: [QUALITY_CHECKLIST.md](./ROLES/ENVIRONMENTAL_COMPLIANCE_SPECIALIST/QUALITY_CHECKLIST.md) (`QG-ENG-001`, `QG-ENG-007`)

## 4. Pre-Signoff Evidence Package Requirements

Every handoff submitted for `DOMAIN_LEAD` and `SA_GATE` review must attach verifiable artifacts:
1. **Executable Calculation Script or Workbook:** Deterministic Python/CLI verification output (`exit code 0`) demonstrating nodal balance closure, unit-conversion checks, and cashflow/inventory reconciliation.
2. **Primary Data & Factor Provenance Table:** Explicit citation of meteorological datasets, grid topology snapshots, emission-factor registries (`eGRID`, `IEA`, `DEFRA`, `USLCI`), `IPCC GWP` vintage, and statutory code sections.
3. **Assumption & Sensitivity Register:** Side-by-side separation of measured telemetry facts vs. parameterized assumptions, accompanied by sensitivity bounds (`P50`/`P90`, `WACC`, fuel/carbon trajectories, or allocation variants).
4. **Human Approval Gate Log:** Explicit signoff prompt whenever outputs feed regulatory filings, `PE`-stamped interconnection packages, financial carbon/REC retirements, or live operational setpoints.

## 5. Escalation & Signoff Recording

Record gate outcomes (`PASS`, `PARTIAL`, `BLOCKED`, `FAILED`, or `NOT VERIFIED`) with exact script outputs, solver logs, and citation tables in [HANDOFF_REPORT.md](../../06_TEMPLATES/HANDOFF_REPORT.md) per [INDEPENDENT_VERIFICATION.md](../../00_GLOBAL_CONSTITUTION/INDEPENDENT_VERIFICATION.md). Escalate any unresolved physical infeasibility, regulatory exceedance, or missing primary meter data to `PM + SA`.
