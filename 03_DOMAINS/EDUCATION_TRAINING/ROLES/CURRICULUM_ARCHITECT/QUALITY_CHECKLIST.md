# Quality Checklist: Curriculum Architect (`ROLE-EDU-002`)

- **Role:** [CURRICULUM_ARCHITECT](./SYSTEM_PROMPT.md)
- **Domain Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md) (`QG-EDU-001`, `QG-EDU-002`, `QG-EDU-005`, `QG-EDU-006`)

## 1. Competency Framework & Program Outcome Alignment (`QG-EDU-001`)
- [ ] Program Learning Outcomes (`PLOs`) use observable Bloom action verbs and map cleanly to target job profiles or external frameworks (`SFIA`, `NICE`, `EQF`, `ABET`, `ISO/IEC 17024`).
- [ ] Every course/module maps to $\ge 1$ `PLO` with zero orphan survey modules disconnected from program outcomes.
- [ ] Every `PLO` is covered across `Introduce (I)`, `Reinforce (R)`, and summative `Master/Assess (M)` stages in the `I-R-M` matrix.
- [ ] Proficiency tier transitions (`Novice -> Practitioner -> Specialist`) define observable exit gates and integrative capstones.

## 2. Prerequisite `DAG` & Spiral Progression Integrity (`QG-EDU-002`)
- [ ] Programmatic topological sort confirms the course/module prerequisite graph is a strict Directed Acyclic Graph (`0` circular dependencies).
- [ ] Connected paths exist from every entry node through intermediate milestones to summative capstone modules.
- [ ] Zero hidden prerequisites exist: every tool, mathematical method, or domain concept consumed in Module $B$ is taught upstream in Module $A$ or verified via entry diagnostic.
- [ ] Bridge/remediation modules are specified for lateral-entry cohorts with heterogeneous baseline backgrounds.
- [ ] Shared core modules and role-specific elective tracks are factored cleanly to eliminate duplicated maintenance drift.
- [ ] Spiral curriculum reinforcement schedules spaced retrieval touchpoints across multi-week or multi-semester sequences.

## 3. Notional Workload, Credit Accounting & Lifecycle Governance
- [ ] Synchronous contact, reading/media, hands-on lab/debugging, independent study, and capstone hours are itemized per module.
- [ ] Credit-bearing programs reconcile notional learning hours accurately against `Carnegie` or `ECTS` (`25–30 hr/credit`) standards.
- [ ] Weekly notional hours match the target learner persona (`full-time cohort` vs. `part-time working professional`) without cognitive overload.
- [ ] Semantic curriculum versioning (`MAJOR.MINOR.PATCH`), deprecation rules, and technical/regulatory refresh triggers are documented.

## 4. Accessibility, Credential Honesty & Human Signoff (`QG-EDU-005`, `QG-EDU-006`)
- [ ] `UDL 3.0` accommodation pathways (flexible pacing, accessible capstone modalities without lowering construct standards) are specified.
- [ ] Mermaid pathway diagrams and adjacency tables render cleanly and match each other `1:1`.
- [ ] Exported JSON/CSV/Markdown curriculum schemas do not claim unexecuted mutations on live university `SIS` or enterprise `LXP` databases.
- [ ] Zero misleading academic-accreditation or statutory-licensure (`PE`, `RN`, `CPA`, `Bar`) representations exist.
- [ ] Verified standard mappings, workload assumptions, time-to-mastery estimates, and cohort pilot uncertainties are separated in [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md).
- [ ] Formal degree, credit, or certification specifications flag mandatory human academic-senate / accreditation-board signoff.
