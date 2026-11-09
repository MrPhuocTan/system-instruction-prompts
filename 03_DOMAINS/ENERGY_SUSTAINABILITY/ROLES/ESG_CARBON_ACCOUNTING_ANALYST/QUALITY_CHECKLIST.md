# Quality Checklist: ESG & Carbon Accounting Analyst (`ROLE-ENG-004`)

- **Role:** [ESG_CARBON_ACCOUNTING_ANALYST](./SYSTEM_PROMPT.md)
- **Domain Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md) (`QG-ENG-004`, `QG-ENG-005`, `QG-ENG-006`)

## 1. Organizational, Operational & `Scope 3` Boundary Completeness
- [ ] Organizational consolidation approach (`operational control`, `financial control`, or `equity share`), base year, and structural recalculation threshold ($\ge 5\%$) are explicitly documented.
- [ ] `Scope 1` covers stationary combustion, mobile fleet, process emissions, and fugitive refrigerants/`SF6` verified via mass-balance top-up logs.
- [ ] `Scope 2` reports both `location-based` and `market-based` totals side-by-side in all summary disclosures.
- [ ] Market-based `Scope 2` contractual instruments (`RECs`, `GOs`, `PPAs`) satisfy GHG Protocol Scope 2 Quality Criteria (market boundary, vintage, retirement), and uncovered MWh apply regional residual mixes where published.
- [ ] All 15 `Scope 3` categories are screened; included categories state calculation tier (`supplier-specific`, `hybrid`, `average-data`, `spend-based`) and excluded categories provide quantitative materiality proof without omitting material categories (`Cat 1`, `Cat 3`, `Cat 11`, `Cat 15`).
- [ ] `Scope 3 Category 3` (`WTT` + `T&D` losses) is verified free of overlap with direct `Scope 1` combustion or `Scope 2` generation factors.

## 2. Emission Factor, `GWP` & `EEIO` Calculation Accuracy
- [ ] Every calculation row records exact `EF` source, publication year, geography, physical unit, and locked `IPCC GWP100` vintage (`AR6` default; fossil vs. biogenic `CH4` separated).
- [ ] Unit conversions (`therms`, `MMBtu`, `GJ`, `kWh`, `short tons` vs. `metric tonnes`, `t-km`) pass automated Python check scripts.
- [ ] Spend-based `EEIO` rows apply explicit FX conversion, `CPI/PPI` deflation to the `EEIO` model base year, and purchaser-to-producer margin alignment.
- [ ] Biogenic `CO2` emissions and land-sector (`FLAG`) removals are segregated from fossil inventory scopes per `GHG Protocol` rules.

## 3. `ISO 14040/14044` `LCA` & Anti-Greenwashing Verification
- [ ] Product `LCA`/`PCF` models specify functional unit, reference flow, system boundary, cut-off threshold, co-product allocation sensitivity, and multi-impact indicators beyond `GWP`.
- [ ] Foreground `LCA` unit processes pass mass, carbon-atom, and energy balance checks without unattributed elementary-flow leaks.
- [ ] Voluntary carbon credits/offsets, unmatched `RECs`, and avoided emissions are never subtracted from gross `Scope 1/2/3` totals.
- [ ] Retired credit claims verify registry serial numbers, vintage, additionality, permanence, and zero double-issuance.
- [ ] Comparative product assertions include `ISO 14044` boundary-equivalence and third-party critical-review disclosures.

## 4. Assurance Trail, Confidentiality & Signoff Readiness
- [ ] Reconciliation script confirms facility/category subtotals sum to consolidated totals ($\le 0.001\text{ tCO2e}$) with zero missing `EF` metadata cells.
- [ ] Data Quality Indicators (`DQI`) and uncertainty intervals are reported alongside point estimates in [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md).
- [ ] Confidential supplier BOMs and spend ledgers are protected, and external filings (`CSRD`, `ISSB`, `SEC`, `CBAM`, `CDP`) require mandatory human assurance signoff.
