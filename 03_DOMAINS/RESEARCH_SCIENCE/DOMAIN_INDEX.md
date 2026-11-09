# Scientific Research & Methodology Domain Index (`RESEARCH_SCIENCE`)

- **Domain ID:** `DOM-06-RESEARCH_SCIENCE`
- **Precedence Layer:** Level 4 Domain Governance (subordinate to [GLOBAL_SYSTEM_PROMPT.md](../../00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md) and [ORCHESTRATION_SYSTEM_PROMPT.md](../../01_ORCHESTRATION/ORCHESTRATION_SYSTEM_PROMPT.md))
- **Canonical Domain Standards:** [DOMAIN_SYSTEM_PROMPT.md](./DOMAIN_SYSTEM_PROMPT.md)
- **Domain Verification Gates:** [QUALITY_GATES.md](./QUALITY_GATES.md)

---

## 1. Domain Purpose & Scope

The `RESEARCH_SCIENCE` domain governs empirical, theoretical, observational, and computational scientific inquiry across natural, physical, behavioral, social, and formal sciences. It enforces falsifiable hypothesis formulation, bias-resistant study architecture, transparent statistical inference, verifiable bibliographic synthesis, and deterministic computational reproducibility across Complexity Levels 1 through 4.

Out-of-scope concerns route to adjacent domains: clinical trials, patient-level EHR analytics, and medical safety governance route to [HEALTHCARE_LIFE_SCIENCES](../HEALTHCARE_LIFE_SCIENCES/DOMAIN_INDEX.md); production ML serving and LLM engineering route to `03_DOMAINS/AI_MACHINE_LEARNING/`; enterprise warehouse pipelines route to `03_DOMAINS/DATA_ANALYTICS/`; and econometric market valuation routes to `03_DOMAINS/ECONOMICS_FINANCE/`.

---

## 2. Canonical Role Inventory (`6` Roles)

| Role ID | Canonical Role Directory | Primary Scientific Focus | Specialist Prompt | Pre-Handoff Checklist |
| :--- | :--- | :--- | :--- | :--- |
| `ROLE-SCI-001` | `RESEARCH_SCIENTIST` | Falsifiable hypotheses, mechanistic/theoretical modeling, empirical synthesis, IMRaD reporting | [SYSTEM_PROMPT.md](./ROLES/RESEARCH_SCIENTIST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/RESEARCH_SCIENTIST/QUALITY_CHECKLIST.md) |
| `ROLE-SCI-002` | `RESEARCH_METHODOLOGIST` | Causal identification (DAGs, DiD, IV, RDD), validity threats, bias control, preregistration | [SYSTEM_PROMPT.md](./ROLES/RESEARCH_METHODOLOGIST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/RESEARCH_METHODOLOGIST/QUALITY_CHECKLIST.md) |
| `ROLE-SCI-003` | `STATISTICIAN` | Frequentist/Bayesian inference, power/MDE, multiplicity control, hierarchical & missing-data models | [SYSTEM_PROMPT.md](./ROLES/STATISTICIAN/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/STATISTICIAN/QUALITY_CHECKLIST.md) |
| `ROLE-SCI-004` | `EXPERIMENTAL_DESIGNER` | Factorial/block/crossover DoE, randomization/blinding, control arms, measurement calibration | [SYSTEM_PROMPT.md](./ROLES/EXPERIMENTAL_DESIGNER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/EXPERIMENTAL_DESIGNER/QUALITY_CHECKLIST.md) |
| `ROLE-SCI-005` | `LITERATURE_REVIEWER` | Systematic/scoping reviews (PRISMA 2020), search strategies, RoB appraisal, citation verification | [SYSTEM_PROMPT.md](./ROLES/LITERATURE_REVIEWER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/LITERATURE_REVIEWER/QUALITY_CHECKLIST.md) |
| `ROLE-SCI-006` | `REPRODUCIBILITY_AUDITOR` | Independent code/data-to-figure regeneration, seed/environment determinism, FAIR audit | [SYSTEM_PROMPT.md](./ROLES/REPRODUCIBILITY_AUDITOR/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/REPRODUCIBILITY_AUDITOR/QUALITY_CHECKLIST.md) |

---

## 3. Role Selection Matrix by Scientific Task Archetype

| Primary Task Need | Primary Role | Supporting / Peer Role(s) | Mandatory Independent Gate (Level 3–4) |
| :--- | :--- | :--- | :--- |
| Formulate novel theory, mechanistic model, or full study manuscript | `RESEARCH_SCIENTIST` | `LITERATURE_REVIEWER`, `STATISTICIAN` | `REPRODUCIBILITY_AUDITOR` |
| Design observational causal study or critique study validity | `RESEARCH_METHODOLOGIST` | `STATISTICIAN` | `QUALITY_REVIEWER` / `DOMAIN_LEAD` |
| Design controlled lab, field, simulation, or A/B factorial protocol | `EXPERIMENTAL_DESIGNER` | `STATISTICIAN`, `RESEARCH_METHODOLOGIST` | `REPRODUCIBILITY_AUDITOR` |
| Execute inferential modeling, uncertainty quantification, or power plan | `STATISTICIAN` | `RESEARCH_SCIENTIST` | `REPRODUCIBILITY_AUDITOR` |
| Conduct systematic evidence synthesis or bibliographic gap map | `LITERATURE_REVIEWER` | `RESEARCH_METHODOLOGIST` | `QUALITY_REVIEWER` |
| Verify replication package, computational determinism, or p-hacking risk | `REPRODUCIBILITY_AUDITOR` | — (Must operate independently) | `SA_GATE` + `PM_GATE` |

---

## 4. Role-vs-Agent Allocation & Multi-Role Combination Rules

Per [DYNAMIC_AGENT_ALLOCATION.md](../../01_ORCHESTRATION/DYNAMIC_AGENT_ALLOCATION.md), a **Role** is a reusable specialist specification whereas an **Agent** is a runtime execution instance bound to an Exclusive Write-Lock:
1. **Level 1–2 Co-Location (Permitted):** One subagent may combine `RESEARCH_SCIENTIST` + `LITERATURE_REVIEWER` for exploratory framing, or `RESEARCH_METHODOLOGIST` + `EXPERIMENTAL_DESIGNER` (+ `STATISTICIAN` for sample-size sizing) when authoring a cohesive study protocol.
2. **Level 3–4 Separation of Duties (Mandatory):** Never assign the authoring `RESEARCH_SCIENTIST` or `STATISTICIAN` to serve as their own `REPRODUCIBILITY_AUDITOR`. Independent replication and statistical audit require a separate reviewer instance with read-only access to source analysis scripts and write-locks scoped strictly to audit artifacts.
3. **Domain Lead Coordination:** Multi-workstream Level 4 research programs appoint [DOMAIN_LEAD](../../02_CORE_ROLES/DOMAIN_LEAD/SYSTEM_PROMPT.md) alongside persistent `PM + SA` governance.

---

## 5. Recommended Cross-Domain & Specialized Skills

Load only task-relevant procedural skills on demand:
- **Primary Source & Citation Verification:** [RESEARCH_AND_SOURCE_VALIDATION/SKILL.md](../../04_CROSS_DOMAIN_SKILLS/RESEARCH_AND_SOURCE_VALIDATION/SKILL.md) (`SKL-CORE-004`) for provenance grading and zero-hallucination citation audits.
- **Hypothesis & Counterfactual Rigor:** [CRITICAL_THINKING/SKILL.md](../../04_CROSS_DOMAIN_SKILLS/CRITICAL_THINKING/SKILL.md) (`SKL-CORE-002`) and [COGNITIVE_EXECUTION/SKILL.md](../../04_CROSS_DOMAIN_SKILLS/COGNITIVE_EXECUTION/SKILL.md) (`SKL-CORE-001`).
- **Quantitative & Distributional Analysis:** [DATA_INTERPRETATION/SKILL.md](../../04_CROSS_DOMAIN_SKILLS/DATA_INTERPRETATION/SKILL.md) (`SKL-CORE-005`) for confounding, missingness, and effect-size interpretation.
- **Replication & Environment Determinism:** [SCIENTIFIC_REPRODUCIBILITY/SKILL.md](../../05_SPECIALIZED_SKILLS/SCIENTIFIC_REPRODUCIBILITY/SKILL.md) (`SKL-SPEC-008`) for deterministic seeds, lockfiles, and end-to-end figure/table regeneration.
- **Scholarly & Protocol Reporting:** [TECHNICAL_WRITING/SKILL.md](../../04_CROSS_DOMAIN_SKILLS/TECHNICAL_WRITING/SKILL.md) (`SKL-CORE-007`) for precise, jargon-calibrated scientific prose.
