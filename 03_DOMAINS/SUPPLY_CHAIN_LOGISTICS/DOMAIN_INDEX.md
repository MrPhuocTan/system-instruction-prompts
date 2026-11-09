# Supply Chain & Logistics Domain Index (`SUPPLY_CHAIN_LOGISTICS`)

## 1. Domain Overview & Mission Scope
The **Supply Chain & Logistics (`SUPPLY_CHAIN_LOGISTICS`)** domain governs end-to-end supply chain architecture, Sales & Operations Planning (`S&OP` / `IBP`), statistical demand forecasting, mathematical network & vehicle routing optimization, strategic procurement & supplier risk management, multi-echelon inventory optimization (`MEIO`), warehouse operations, and international trade compliance.

Decisions in this domain commit working capital, supplier contracts, freight capacity, service-level promises, and cross-border customs declarations. All specialists in this domain operate under Level 4 domain invariants subordinated to:
- [Global System Prompt](../../00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md)
- [Human Approval Policy](../../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md)
- [Independent Verification](../../00_GLOBAL_CONSTITUTION/INDEPENDENT_VERIFICATION.md)
- [Supply Chain Domain System Prompt](./DOMAIN_SYSTEM_PROMPT.md)

## 2. Canonical Role Inventory (`5` Roles)

| Role ID | Canonical Role Name | Primary Engineering & Analytical Scope | Role Specification | Quality Checklist |
| :--- | :--- | :--- | :--- | :--- |
| `ROLE-SCM-001` | `SUPPLY_CHAIN_STRATEGIST` | `SCOR` architecture, `S&OP`/`IBP` governance, bullwhip mitigation, `TTS`/`TTR` resilience stress-testing, working-capital cash-to-cash trade-offs | [SYSTEM_PROMPT.md](./ROLES/SUPPLY_CHAIN_STRATEGIST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/SUPPLY_CHAIN_STRATEGIST/QUALITY_CHECKLIST.md) |
| `ROLE-SCM-002` | `DEMAND_FORECASTING_PLANNER` | Hierarchical time-series & intermittent demand (`Croston`/`TSB`), `WMAPE`/`Bias`/`MASE`/`FVA`, stockout censorship unbiasing, promo/price uplift | [SYSTEM_PROMPT.md](./ROLES/DEMAND_FORECASTING_PLANNER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/DEMAND_FORECASTING_PLANNER/QUALITY_CHECKLIST.md) |
| `ROLE-SCM-003` | `LOGISTICS_NETWORK_OPTIMIZER` | `MILP` facility location, `CVRPTW` vehicle routing, cube/weight & `FMCSA` Hours-of-Service constraints, multimodal freight & `Incoterms 2020` landed cost | [SYSTEM_PROMPT.md](./ROLES/LOGISTICS_NETWORK_OPTIMIZER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/LOGISTICS_NETWORK_OPTIMIZER/QUALITY_CHECKLIST.md) |
| `ROLE-SCM-004` | `PROCUREMENT_SOURCING_SPECIALIST` | Kraljic segmentation, `TCO` should-cost modeling, supplier `HHI` concentration risk, `RFx` scoring, `HTS`/origin/sanctions & `UFLPA` compliance | [SYSTEM_PROMPT.md](./ROLES/PROCUREMENT_SOURCING_SPECIALIST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/PROCUREMENT_SOURCING_SPECIALIST/QUALITY_CHECKLIST.md) |
| `ROLE-SCM-005` | `INVENTORY_WAREHOUSE_ANALYST` | `(s, Q)` / `(R, S)` safety-stock math (`CSL` vs. Fill Rate $G(z)$), `MEIO`, `ABC-XYZ` segmentation, `EOQ`/newsvendor, `WMS` slotting & wave picking | [SYSTEM_PROMPT.md](./ROLES/INVENTORY_WAREHOUSE_ANALYST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/INVENTORY_WAREHOUSE_ANALYST/QUALITY_CHECKLIST.md) |

## 3. Role-Selection Matrix & Multi-Domain Routing

| Supply Chain Problem / Deliverable | Primary Owner Role | Supporting / Review Role(s) | Cross-Domain Escalation Target |
| :--- | :--- | :--- | :--- |
| End-to-end `S&OP` design, network resilience (`TTS`/`TTR`), bullwhip audit | `SUPPLY_CHAIN_STRATEGIST` | `DEMAND_FORECASTING_PLANNER`, `PROCUREMENT_SOURCING_SPECIALIST` | [ECONOMICS_FINANCE](../ECONOMICS_FINANCE/DOMAIN_INDEX.md) (`CORPORATE_FINANCE`) |
| SKU-location demand baseline, intermittent spare/long-tail forecast, `FVA` | `DEMAND_FORECASTING_PLANNER` | `INVENTORY_WAREHOUSE_ANALYST` | [AI_MACHINE_LEARNING](../AI_MACHINE_LEARNING/DOMAIN_INDEX.md) (`DATA_SCIENTIST`) |
| DC gravity-center / `MILP` design, `CVRPTW` fleet routing, lane freight optimization | `LOGISTICS_NETWORK_OPTIMIZER` | `SUPPLY_CHAIN_STRATEGIST` | [ENERGY_SUSTAINABILITY](../ENERGY_SUSTAINABILITY/DOMAIN_INDEX.md) (`ESG_CARBON_ACCOUNTING_ANALYST`) |
| Dual-sourcing split, landed `TCO` model, supplier `HHI` & customs/trade screening | `PROCUREMENT_SOURCING_SPECIALIST` | `LOGISTICS_NETWORK_OPTIMIZER` | [LEGAL_COMPLIANCE](../LEGAL_COMPLIANCE/DOMAIN_INDEX.md) (`COMPLIANCE_SPECIALIST`) |
| Safety-stock / reorder-point policy, Fill Rate vs. working capital curve, DC slotting | `INVENTORY_WAREHOUSE_ANALYST` | `DEMAND_FORECASTING_PLANNER` | [MANUFACTURING_INDUSTRIAL](../MANUFACTURING_INDUSTRIAL/DOMAIN_INDEX.md) (`INDUSTRIAL_SYSTEMS_ENGINEER`) |

## 4. Recommended Cross-Domain & Specialized Skills
Load procedural skills progressively via [Skill Discovery and Loading](../../05_SPECIALIZED_SKILLS/SKILL_DISCOVERY_AND_LOADING/SKILL.md):
- **Core Analytical & Governance Skills:**
  - [Cognitive Execution](../../04_CROSS_DOMAIN_SKILLS/COGNITIVE_EXECUTION/SKILL.md) — Explicit ledgering of ERP historical facts vs. lead-time, tariff, and elasticity assumptions.
  - [Systems Thinking](../../04_CROSS_DOMAIN_SKILLS/SYSTEMS_THINKING/SKILL.md) — Modeling multi-echelon bullwhip feedback loops, port congestion cascades, and capacity coupling.
  - [Data Interpretation](../../04_CROSS_DOMAIN_SKILLS/DATA_INTERPRETATION/SKILL.md) — Uncensoring stockout-truncated sales histories and testing fat-tailed lead-time distributions.
  - [Decision Analysis](../../04_CROSS_DOMAIN_SKILLS/DECISION_ANALYSIS/SKILL.md) — Multi-criteria cost vs. service-level vs. resilience efficient-frontier optimization.
  - [Risk Management](../../04_CROSS_DOMAIN_SKILLS/RISK_MANAGEMENT/SKILL.md) — Sub-tier concentration (`HHI`), geopolitical chokepoint, and cold-chain spoilage mitigation.
- **Specialized Technical Skills:**
  - [Financial Model Validation](../../05_SPECIALIZED_SKILLS/FINANCIAL_MODEL_VALIDATION/SKILL.md) — Working-capital carrying cost, landed `TCO`, and `Cash-to-Cash` reconciliation.
  - [Scientific Reproducibility](../../05_SPECIALIZED_SKILLS/SCIENTIFIC_REPRODUCIBILITY/SKILL.md) — Rolling-origin backtests, deterministic `MILP` solvers, and seeded Monte Carlo inventory simulations.

## 5. Complexity Routing & Separation-of-Duties Rules
- **Level 1–2 Tactical Planning Analyses:** One subagent may combine `DEMAND_FORECASTING_PLANNER` + `INVENTORY_WAREHOUSE_ANALYST` for cohesive forecast-to-safety-stock modeling.
- **Level 3–4 Enterprise Network Redesigns, Binding RFPs, or Customs Filings:** Enforce independent mathematical and compliance review ([QUALITY_REVIEWER](../../02_CORE_ROLES/QUALITY_REVIEWER/SYSTEM_PROMPT.md) or cross-role audit) plus explicit human commercial/legal sign-off.

## 6. Governance & Gate Artifacts
- Domain Engineering Standards: [DOMAIN_SYSTEM_PROMPT.md](./DOMAIN_SYSTEM_PROMPT.md)
- Mandatory Sign-Off Criteria: [QUALITY_GATES.md](./QUALITY_GATES.md)
- Orchestration Review Gate: [REVIEW_AND_SIGNOFF.md](../../01_ORCHESTRATION/REVIEW_AND_SIGNOFF.md)
- Domain Lead Oversight Role: [DOMAIN_LEAD](../../02_CORE_ROLES/DOMAIN_LEAD/SYSTEM_PROMPT.md)
