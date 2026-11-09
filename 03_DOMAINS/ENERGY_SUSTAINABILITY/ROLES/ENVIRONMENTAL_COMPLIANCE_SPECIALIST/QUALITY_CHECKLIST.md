# Quality Checklist: Environmental Compliance Specialist (`ROLE-ENG-005`)

- **Role:** [ENVIRONMENTAL_COMPLIANCE_SPECIALIST](./SYSTEM_PROMPT.md)
- **Domain Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md) (`QG-ENG-001`, `QG-ENG-007`)

## 1. Statutory Scope, Jurisdiction & `PTE` Applicability
- [ ] Every numeric compliance threshold specifies exact jurisdiction (federal, state/provincial, local air-shed or watershed) and governing statutory/code citation.
- [ ] Air-shed attainment/non-attainment status, receiving waterbody designated uses, and nearby sensitive/protected receptors are explicitly documented.
- [ ] Permit applicability (`Major Source` `PSD`/`Title V` vs. minor) evaluates unconstrained `8,760 hr/yr` Potential-to-Emit (`PTE`) separately from historical actual emissions.
- [ ] Any synthetic-minor operational cap is verified for legal and practicable enforceability (continuous monitoring + recordkeeping conditions).
- [ ] Permitting matrix documents agency review lead times, public-comment windows, and cross-media interactions (`air`, `water`, `stormwater`, `wetlands`, `waste`, `noise`, `ecology`).

## 2. Normalization, Averaging Windows & Monitoring (`CEMS` / `DMR`) QA
- [ ] Stack concentrations are normalized accurately to reference dry/wet gas basis, standard temperature/pressure (`0 C` vs. `20 C`), and statutory reference $O_2\%$ ($C_{corr} = C_{meas} \cdot \frac{20.9 - O_{2,ref}}{20.9 - O_{2,meas}}$).
- [ ] Compliance evaluations test every applicable averaging window (`1-hr`, `3-hr`, `24-hr`, `30-day rolling`, `annual`) plus instantaneous `pH`/acute limits independently.
- [ ] Short-term spikes and excursions are never masked inside compliant monthly or annual means.
- [ ] `CEMS` / sampling data availability `%`, calibration drift (`QAL2/QAL3` / `Part 60/75`), and conservative missing-data substitution tiers pass automated script checks.

## 3. Containment, Mitigation Hierarchy & Spill/`CAPA` Controls
- [ ] Secondary containment (`SPCC` / tank bunds) verifies capacity $\ge 100\%$ of the largest single container plus design storm precipitation freeboard.
- [ ] Impact controls strictly follow `Avoid -> Minimize -> Restore -> Offset`; prohibited effluent/waste dilution (`40 CFR 403.6(d)`) is never proposed.
- [ ] Release/exceedance evaluations screen against `CERCLA`/`EPCRA`/`CWA` Reportable Quantities (`RQs`) and highlight urgent statutory reporting clocks (`immediate` / `24-hour`).

## 4. Verification, Non-Legal Disclaimer & Human Signoff Gate
- [ ] Hazardous waste streams (`RCRA` / `EU Waste List`) verify generator status, accumulation time limits, incompatibility segregation, and cradle-to-grave manifest reconciliation.
- [ ] `ISO 14001` aspect-impact scoring links every significant environmental aspect to an auditable operational control and monitoring KPI.
- [ ] Analytical Gaussian plume, mixing-zone dilution, and acoustic attenuation calculations are explicitly labeled as Tier-1 screening estimates vs. full regulatory `AERMOD`/`CORMIX` models.
- [ ] Verified monitoring logs, conservative screening assumptions, modeled receptor estimates, and legal-interpretation uncertainties are separated in [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md).
- [ ] Explicit non-legal-advice boundary is stated; statutory legal ambiguities are escalated to `LEGAL_COMPLIANCE`.
- [ ] Mandatory human EHS officer / licensed `PE` signoff gate is enforced before agency notifications, manifest signatures, or permit submissions.
