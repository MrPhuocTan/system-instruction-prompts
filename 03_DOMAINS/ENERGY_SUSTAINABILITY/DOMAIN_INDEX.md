# Domain 14: Energy & Sustainability (`ENERGY_SUSTAINABILITY`)

- **Domain ID:** `DOM-14`
- **Precedence Layer:** Level 4 — Domain Governance (subordinate to [Global Constitution](../../00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md) and [PM + SA Orchestration](../../01_ORCHESTRATION/PERSISTENT_PM_SA.md))
- **Normative Binding:** [DOMAIN_SYSTEM_PROMPT.md](./DOMAIN_SYSTEM_PROMPT.md) and [QUALITY_GATES.md](./QUALITY_GATES.md)

## 1. Domain Scope & Purpose

The `ENERGY_SUSTAINABILITY` domain governs macro- and micro-scale energy system optimization, electric power transmission and distribution engineering, renewable generation and storage plant yield modeling, corporate and product greenhouse gas (`GHG`) accounting, life cycle assessment (`LCA`), and statutory environmental permitting compliance. Every specialist operating in this domain enforces physical conservation laws, electrical network reliability margins, auditable techno-economic assumptions, source-traceable emission factors, and anti-greenwashing evidence standards.

## 2. Canonical Role Inventory (`5` Specialist Roles)

| Role ID | Canonical Role Directory | Specialist Prompt | Verification Checklist | Primary Engineering & Analytical Ownership |
| :--- | :--- | :--- | :--- | :--- |
| `ROLE-ENG-001` | `ENERGY_SYSTEMS_ANALYST` | [SYSTEM_PROMPT.md](./ROLES/ENERGY_SYSTEMS_ANALYST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/ENERGY_SYSTEMS_ANALYST/QUALITY_CHECKLIST.md) | Integrated capacity expansion (`CEM`), 8760 production cost dispatch (`UC/ED`), sector coupling, mass/energy/exergy balances, and `LCOE`/`LCOS` optimization |
| `ROLE-ENG-002` | `GRID_AND_POWER_SYSTEMS_ENGINEER` | [SYSTEM_PROMPT.md](./ROLES/GRID_AND_POWER_SYSTEMS_ENGINEER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/GRID_AND_POWER_SYSTEMS_ENGINEER/QUALITY_CHECKLIST.md) | AC/DC load flow, `N-1` contingency analysis, fault current duty, voltage/frequency stability, IEEE 1547/2800 `IBR` interconnection, and protection coordination |
| `ROLE-ENG-003` | `RENEWABLE_ENERGY_SPECIALIST` | [SYSTEM_PROMPT.md](./ROLES/RENEWABLE_ENERGY_SPECIALIST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/RENEWABLE_ENERGY_SPECIALIST/QUALITY_CHECKLIST.md) | Solar PV, wind, hydro, BESS, and green hydrogen resource assessment, `P50`/`P90` exceedance yield cascades, curtailment, and battery degradation sizing |
| `ROLE-ENG-004` | `ESG_CARBON_ACCOUNTING_ANALYST` | [SYSTEM_PROMPT.md](./ROLES/ESG_CARBON_ACCOUNTING_ANALYST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/ESG_CARBON_ACCOUNTING_ANALYST/QUALITY_CHECKLIST.md) | GHG Protocol Scope 1/2/3 inventories, ISO 14040/14044 & ISO 14067 `LCA`, `SBTi` pathway validation, CSRD/ESRS E1 & ISSB IFRS S2 disclosures, and anti-greenwashing audits |
| `ROLE-ENG-005` | `ENVIRONMENTAL_COMPLIANCE_SPECIALIST` | [SYSTEM_PROMPT.md](./ROLES/ENVIRONMENTAL_COMPLIANCE_SPECIALIST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/ENVIRONMENTAL_COMPLIANCE_SPECIALIST/QUALITY_CHECKLIST.md) | Environmental permitting (`NEPA`, `CAA`, `CWA`, `RCRA`, EU `EIA`/`IED`), dispersion exceedance screening, `CEMS` reconciliation, `CAPA`, and ISO 14001 controls |

## 3. Task-to-Role Routing & Multi-Role Selection Matrix

| Task Archetype | Primary Accountable Role | Supporting / Review Role(s) | Mandatory Separation-of-Duties Rule |
| :--- | :--- | :--- | :--- |
| Decarbonization roadmap, microgrid sizing, or hydrogen/heat/power sector-coupling model | `ENERGY_SYSTEMS_ANALYST` | `RENEWABLE_ENERGY_SPECIALIST`, `ESG_CARBON_ACCOUNTING_ANALYST` | Keep LCOE/dispatch modeler separate from final investment valuation signoff on Level 3–4 tasks |
| Generator interconnection study, feeder hosting capacity, or substation fault/contingency study | `GRID_AND_POWER_SYSTEMS_ENGINEER` | `RENEWABLE_ENERGY_SPECIALIST` | Never issue live relay settings or energized switching orders without human PE approval |
| Utility-scale PV/wind/BESS bankable yield (`P50`/`P90`) and augmentation schedule | `RENEWABLE_ENERGY_SPECIALIST` | `ENERGY_SYSTEMS_ANALYST`, `GRID_AND_POWER_SYSTEMS_ENGINEER` | Separate plant yield authoring from independent lender technical review on Level 4 financings |
| Corporate Scope 1/2/3 inventory, product `LCA`, `SBTi` submission, or CSRD/ISSB climate report | `ESG_CARBON_ACCOUNTING_ANALYST` | `ENVIRONMENTAL_COMPLIANCE_SPECIALIST` | Author of GHG inventory or net-zero claim must not perform the independent assurance audit |
| Air/water/waste permit matrix, `NEPA`/`EIA` impact screening, or spill/exceedance `CAPA` | `ENVIRONMENTAL_COMPLIANCE_SPECIALIST` | `ESG_CARBON_ACCOUNTING_ANALYST` | Escalate statutory legal interpretation to Legal Compliance and require human regulatory signoff |

## 4. Recommended Cross-Domain & Specialized Skills

Load only task-relevant procedural skills on demand via progressive disclosure:
- **Cross-Domain Skills (`04_CROSS_DOMAIN_SKILLS/`):**
  - [SYSTEMS_THINKING](../../04_CROSS_DOMAIN_SKILLS/SYSTEMS_THINKING/SKILL.md) — coupled fuel, grid, storage, carbon, and permitting feedback loops.
  - [DATA_INTERPRETATION](../../04_CROSS_DOMAIN_SKILLS/DATA_INTERPRETATION/SKILL.md) — 8760 time-series meteorology, SCADA/AMI metering, and CEMS uncertainty analysis.
  - [RESEARCH_AND_SOURCE_VALIDATION](../../04_CROSS_DOMAIN_SKILLS/RESEARCH_AND_SOURCE_VALIDATION/SKILL.md) — verifying EPA eGRID, IEA, IPCC AR6, NREL ATB, and statutory code citations.
  - [DECISION_ANALYSIS](../../04_CROSS_DOMAIN_SKILLS/DECISION_ANALYSIS/SKILL.md) — multi-criteria cost, reliability, carbon abatement (`$/tCO2e`), and land/water trade-offs.
  - [RISK_MANAGEMENT](../../04_CROSS_DOMAIN_SKILLS/RISK_MANAGEMENT/SKILL.md) — extreme-weather dunkelflaute, curtailment, supply-chain, and permitting delay registers.
  - [TECHNICAL_WRITING](../../04_CROSS_DOMAIN_SKILLS/TECHNICAL_WRITING/SKILL.md) — engineering study reports, methodology appendices, and basis-of-design documents.
- **Specialized Skills (`05_SPECIALIZED_SKILLS/`):**
  - [SCIENTIFIC_REPRODUCIBILITY](../../05_SPECIALIZED_SKILLS/SCIENTIFIC_REPRODUCIBILITY/SKILL.md) — deterministic solver seeds, unit-checked physical balances, and scripted sensitivity runs.
  - [FINANCIAL_MODEL_VALIDATION](../../05_SPECIALIZED_SKILLS/FINANCIAL_MODEL_VALIDATION/SKILL.md) — real/nominal WACC reconciliation, tax-equity/ITC/PTC cashflows, and `LCOE`/`LCOS` parity checks.
  - [DATABASE_VALIDATION](../../05_SPECIALIZED_SKILLS/DATABASE_VALIDATION/SKILL.md) — activity-data ledger completeness, meter gap auditing, and emission-factor join integrity.

## 5. Cross-Domain Coordination Touchpoints

- **`ECONOMICS_FINANCE`:** Project finance debt sculpting (`DSCR`), PPA/tolling valuation, carbon credit pricing, and tax-credit monetization.
- **`MANUFACTURING_INDUSTRIAL` & `ROBOTICS_AUTOMATION`:** Industrial process heat electrification, `OT/ICS` SCADA telemetry boundaries, and hazardous-area (`ATEX`/`NFPA 855`) safety.
- **`SUPPLY_CHAIN_LOGISTICS`:** Scope 3 Category 1/4/9 upstream material and freight decarbonization (`GLEC` / ISO 14083) and critical-mineral traceability.
- **`LEGAL_COMPLIANCE`:** Statutory environmental law interpretation, PPA/interconnection contract clauses, and securities climate-disclosure liability.
