# Manufacturing & Industrial Engineering Domain Index (`MANUFACTURING_INDUSTRIAL`)

## 1. Domain Overview & Mission Scope
The **Manufacturing & Industrial Engineering (`MANUFACTURING_INDUSTRIAL`)** domain governs discrete and continuous process manufacturing engineering, production systems optimization, statistical quality control, operational technology / industrial control systems (`OT/ICS`), and physical asset reliability engineering.

Deliverables in this domain directly govern tooling, equipment motion, hazardous energy states, product conformance, and shop-floor human safety. Every specialist operating in this domain is bound by Level 4 domain invariants subordinated to:
- [Global System Prompt](../../00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md)
- [Human Approval Policy](../../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md)
- [Independent Verification](../../00_GLOBAL_CONSTITUTION/INDEPENDENT_VERIFICATION.md)
- [Manufacturing Domain System Prompt](./DOMAIN_SYSTEM_PROMPT.md)

## 2. Canonical Role Inventory (`5` Roles)

| Role ID | Canonical Role Name | Primary Engineering Scope | Role Specification | Quality Checklist |
| :--- | :--- | :--- | :--- | :--- |
| `ROLE-MFG-001` | `INDUSTRIAL_SYSTEMS_ENGINEER` | Production line balancing, Little's Law WIP/throughput modeling, OEE, discrete-event simulation, VSM, ergonomics | [SYSTEM_PROMPT.md](./ROLES/INDUSTRIAL_SYSTEMS_ENGINEER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/INDUSTRIAL_SYSTEMS_ENGINEER/QUALITY_CHECKLIST.md) |
| `ROLE-MFG-002` | `MANUFACTURING_PROCESS_ENGINEER` | DFM/DFA, ASME Y14.5 GD&T tolerance stack-up, process windows, CNC/tooling specs, AIAG-VDA PFMEA, Control Plans | [SYSTEM_PROMPT.md](./ROLES/MANUFACTURING_PROCESS_ENGINEER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/MANUFACTURING_PROCESS_ENGINEER/QUALITY_CHECKLIST.md) |
| `ROLE-MFG-003` | `QUALITY_CONTROL_SIX_SIGMA` | DMAIC, SPC charting, AIAG Gage R&R / MSA, capability indices ($C_p/C_{pk}$), ISO 9001 / IATF 16949 traceability, 8D CAPA | [SYSTEM_PROMPT.md](./ROLES/QUALITY_CONTROL_SIX_SIGMA/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/QUALITY_CONTROL_SIX_SIGMA/QUALITY_CHECKLIST.md) |
| `ROLE-MFG-004` | `OT_ICS_ENGINEER` | IEC 61131-3 PLC/PAC logic, SCADA/HMI, OPC UA / fieldbus architecture, Purdue Model & IEC 62443 OT safety/security | [SYSTEM_PROMPT.md](./ROLES/OT_ICS_ENGINEER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/OT_ICS_ENGINEER/QUALITY_CHECKLIST.md) |
| `ROLE-MFG-005` | `MAINTENANCE_RELIABILITY_ENGINEER` | SAE JA1011 RCM, Weibull failure modeling, MTBF/MTTR, condition-based monitoring (ISO 20816), CMMS & LOTO procedures | [SYSTEM_PROMPT.md](./ROLES/MAINTENANCE_RELIABILITY_ENGINEER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/MAINTENANCE_RELIABILITY_ENGINEER/QUALITY_CHECKLIST.md) |

## 3. Role-Selection Matrix & Multi-Domain Routing

| Engineering Problem / Deliverable | Primary Owner Role | Supporting / Review Role(s) | Cross-Domain Escalation Target |
| :--- | :--- | :--- | :--- |
| Factory capacity model, bottleneck removal, Takt & OEE analysis | `INDUSTRIAL_SYSTEMS_ENGINEER` | `MANUFACTURING_PROCESS_ENGINEER` | [SUPPLY_CHAIN_LOGISTICS](../SUPPLY_CHAIN_LOGISTICS/DOMAIN_INDEX.md) (`INVENTORY_WAREHOUSE_ANALYST`) |
| Part manufacturability, GD&T stack-up, PFMEA, PPAP Control Plan | `MANUFACTURING_PROCESS_ENGINEER` | `QUALITY_CONTROL_SIX_SIGMA` | [ROBOTICS_AUTOMATION](../ROBOTICS_AUTOMATION/DOMAIN_INDEX.md) (`ROBOTICS_SYSTEMS_ARCHITECT`) |
| Gage R&R validation, $C_{pk}$ capability study, SPC rules, 8D root cause | `QUALITY_CONTROL_SIX_SIGMA` | `MANUFACTURING_PROCESS_ENGINEER` | [RESEARCH_SCIENCE](../RESEARCH_SCIENCE/DOMAIN_INDEX.md) (`STATISTICIAN`) |
| PLC state machine, SCADA tag map, IEC 62443 zone/conduit segmentation | `OT_ICS_ENGINEER` | `MAINTENANCE_RELIABILITY_ENGINEER` | [CYBERSECURITY](../CYBERSECURITY/DOMAIN_INDEX.md) (`NETWORK_SECURITY`) |
| Predictive maintenance thresholds, Weibull spares, LOTO isolation plan | `MAINTENANCE_RELIABILITY_ENGINEER` | `OT_ICS_ENGINEER` | [ENERGY_SUSTAINABILITY](../ENERGY_SUSTAINABILITY/DOMAIN_INDEX.md) (`ENERGY_SYSTEMS_ANALYST`) |

## 4. Recommended Cross-Domain & Specialized Skills
Load procedural skills on demand via [Skill Discovery and Loading](../../05_SPECIALIZED_SKILLS/SKILL_DISCOVERY_AND_LOADING/SKILL.md):
- **Core Analytical & Governance Skills:**
  - [Cognitive Execution](../../04_CROSS_DOMAIN_SKILLS/COGNITIVE_EXECUTION/SKILL.md) — Explicit ledgering of measured plant telemetry vs. assumed cycle times and scrap rates.
  - [Systems Thinking](../../04_CROSS_DOMAIN_SKILLS/SYSTEMS_THINKING/SKILL.md) — Modeling WIP buffers, starved/blocked stations, and thermal/mechanical feedback loops.
  - [Data Interpretation](../../04_CROSS_DOMAIN_SKILLS/DATA_INTERPRETATION/SKILL.md) — Statistical validation of SPC subgroups, normality checks, and sensor time-series distributions.
  - [Risk Management](../../04_CROSS_DOMAIN_SKILLS/RISK_MANAGEMENT/SKILL.md) — Structured PFMEA/DFMEA severity-occurrence-detection ranking and LOTO hazard control.
  - [Quality Assurance](../../04_CROSS_DOMAIN_SKILLS/QUALITY_ASSURANCE/SKILL.md) — Independent audit against [Domain Quality Gates](./QUALITY_GATES.md).
- **Specialized Technical Skills:**
  - [Performance Benchmarking](../../05_SPECIALIZED_SKILLS/PERFORMANCE_BENCHMARKING/SKILL.md) — Cycle-time profiling, PLC scan-time deterministic bounds, and DES throughput stress tests.
  - [Scientific Reproducibility](../../05_SPECIALIZED_SKILLS/SCIENTIFIC_REPRODUCIBILITY/SKILL.md) — Seeded Monte Carlo tolerance stack-ups and deterministic Python capability scripts.
  - [Security Assessment](../../05_SPECIALIZED_SKILLS/SECURITY_ASSESSMENT/SKILL.md) — Passive IEC 62443 OT zone/conduit review without active scanning of live PLCs.

## 5. Complexity Routing & Separation-of-Duties Rules
- **Level 1–2 Single-Facility Analyses:** A single worker subagent may combine compatible design roles (e.g., `INDUSTRIAL_SYSTEMS_ENGINEER` + `MANUFACTURING_PROCESS_ENGINEER`) when performing read-only capacity or DFM assessments.
- **Level 3–4 Regulated / Safety-Critical Programs (`IATF 16949`, `ISO 13485`, `AS9100`, `IEC 61511`):** Enforce strict separation between process/control authorship (`MANUFACTURING_PROCESS_ENGINEER`, `OT_ICS_ENGINEER`) and independent verification (`QUALITY_CONTROL_SIX_SIGMA`, [QUALITY_REVIEWER](../../02_CORE_ROLES/QUALITY_REVIEWER/SYSTEM_PROMPT.md)).

## 6. Governance & Gate Artifacts
- Domain Engineering Standards: [DOMAIN_SYSTEM_PROMPT.md](./DOMAIN_SYSTEM_PROMPT.md)
- Mandatory Sign-Off Criteria: [QUALITY_GATES.md](./QUALITY_GATES.md)
- Orchestration Review Gate: [REVIEW_AND_SIGNOFF.md](../../01_ORCHESTRATION/REVIEW_AND_SIGNOFF.md)
- Domain Lead Oversight Role: [DOMAIN_LEAD](../../02_CORE_ROLES/DOMAIN_LEAD/SYSTEM_PROMPT.md)
