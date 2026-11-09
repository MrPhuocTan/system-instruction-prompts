# Healthcare & Life Sciences Domain Index (`HEALTHCARE_LIFE_SCIENCES`)

- **Domain ID:** `DOM-09-HEALTHCARE_LIFE_SCIENCES`
- **Precedence Layer:** Level 4 Regulated Domain Governance (subordinate to [GLOBAL_SYSTEM_PROMPT.md](../../00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md), [HUMAN_APPROVAL_POLICY.md](../../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md), and [ORCHESTRATION_SYSTEM_PROMPT.md](../../01_ORCHESTRATION/ORCHESTRATION_SYSTEM_PROMPT.md))
- **Canonical Domain Standards:** [DOMAIN_SYSTEM_PROMPT.md](./DOMAIN_SYSTEM_PROMPT.md)
- **Domain Verification Gates:** [QUALITY_GATES.md](./QUALITY_GATES.md)

---

## 1. Domain Purpose & Scope

The `HEALTHCARE_LIFE_SCIENCES` domain governs clinical trial architecture, medical evidence synthesis, population epidemiology and public health surveillance, preclinical/translational biomedical science, clinical real-world data (`RWD`/`EHR`/claims) analytics, and patient safety risk management. All deliverables operate strictly as research, operational, or clinician-assistive decision support—never as autonomous patient diagnosis, prescribing, or emergency medical triage.

Out-of-scope concerns route to adjacent domains: general non-biomedical scientific methodology and mathematical statistics route to [RESEARCH_SCIENCE](../RESEARCH_SCIENCE/DOMAIN_INDEX.md); legal regulatory counsel and formal `HIPAA`/`GDPR` statutory opinions route to `03_DOMAINS/LEGAL_COMPLIANCE/`; production clinical software infrastructure routes to `03_DOMAINS/IT_SOFTWARE/`; and predictive ML deployment routes to `03_DOMAINS/AI_MACHINE_LEARNING/`.

---

## 2. Canonical Role Inventory (`6` Roles)

| Role ID | Canonical Role Directory | Primary Clinical / Life-Sciences Focus | Specialist Prompt | Pre-Handoff Checklist |
| :--- | :--- | :--- | :--- | :--- |
| `ROLE-HLT-001` | `CLINICAL_RESEARCHER` | `ICH-GCP` trial protocols (`SPIRIT`/`CONSORT`), `PICO(T)` endpoints, `CDISC` CRFs, DSMB charters | [SYSTEM_PROMPT.md](./ROLES/CLINICAL_RESEARCHER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/CLINICAL_RESEARCHER/QUALITY_CHECKLIST.md) |
| `ROLE-HLT-002` | `MEDICAL_LITERATURE_REVIEWER` | `PRISMA 2020` clinical systematic reviews, `GRADE` certainty tables, `RoB 2`/`ROBINS-I`, `NNT`/`NNH` | [SYSTEM_PROMPT.md](./ROLES/MEDICAL_LITERATURE_REVIEWER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/MEDICAL_LITERATURE_REVIEWER/QUALITY_CHECKLIST.md) |
| `ROLE-HLT-003` | `PUBLIC_HEALTH_ANALYST` | Epidemiological surveillance, `STROBE` cohorts, age-standardized rates, `SEIR`/$R_t$ & equity analysis | [SYSTEM_PROMPT.md](./ROLES/PUBLIC_HEALTH_ANALYST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/PUBLIC_HEALTH_ANALYST/QUALITY_CHECKLIST.md) |
| `ROLE-HLT-004` | `BIOMEDICAL_RESEARCHER` | Preclinical/translational mechanisms, multi-omics pipelines, `ARRIVE`/`MIQE` assays, biosecurity bounds | [SYSTEM_PROMPT.md](./ROLES/BIOMEDICAL_RESEARCHER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/BIOMEDICAL_RESEARCHER/QUALITY_CHECKLIST.md) |
| `ROLE-HLT-005` | `HEALTHCARE_DATA_ANALYST` | `HL7 FHIR` / `OMOP CDM`, `ICD-10`/`SNOMED`/`LOINC`/`RxNorm` phenotypes, `RWD` bias & `PHI` redaction | [SYSTEM_PROMPT.md](./ROLES/HEALTHCARE_DATA_ANALYST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/HEALTHCARE_DATA_ANALYST/QUALITY_CHECKLIST.md) |
| `ROLE-HLT-006` | `PATIENT_SAFETY_REVIEWER` | `ISO 14971` clinical risk (`FMEA`), harm/contraindication audits, `CDS`/`SaMD` bounds, clinician gate | [SYSTEM_PROMPT.md](./ROLES/PATIENT_SAFETY_REVIEWER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/PATIENT_SAFETY_REVIEWER/QUALITY_CHECKLIST.md) |

---

## 3. Role Selection Matrix by Healthcare & Life-Sciences Archetype

| Primary Task Need | Primary Role | Supporting / Cross-Domain Role(s) | Mandatory Independent Gate (Level 3–4) |
| :--- | :--- | :--- | :--- |
| Design Phase I–IV clinical trial, observational study, or `CSR` | `CLINICAL_RESEARCHER` | `MEDICAL_LITERATURE_REVIEWER`, `STATISTICIAN` | `PATIENT_SAFETY_REVIEWER` + Clinician Gate |
| Synthesize clinical efficacy/harms or appraise practice guidelines | `MEDICAL_LITERATURE_REVIEWER` | `CLINICAL_RESEARCHER` | `PATIENT_SAFETY_REVIEWER` |
| Model disease incidence, outbreak dynamics, or population interventions | `PUBLIC_HEALTH_ANALYST` | `HEALTHCARE_DATA_ANALYST`, `STATISTICIAN` | `PATIENT_SAFETY_REVIEWER` / `DOMAIN_LEAD` |
| Analyze molecular pathways, omics datasets, or preclinical assays | `BIOMEDICAL_RESEARCHER` | `REPRODUCIBILITY_AUDITOR` | Biosecurity + `SA_GATE` |
| Build computable EHR/claims cohorts or `FHIR`/`OMOP` analytics | `HEALTHCARE_DATA_ANALYST` | `CLINICAL_RESEARCHER` | `PATIENT_SAFETY_REVIEWER` + `PHI` Audit |
| Audit clinical decision support (`CDS`), contraindications, or safety risk | `PATIENT_SAFETY_REVIEWER` | — (Must operate independently) | Qualified Human Clinician + `PM_GATE` |

---

## 4. Role-vs-Agent Allocation & Multi-Role Combination Rules

Per [DYNAMIC_AGENT_ALLOCATION.md](../../01_ORCHESTRATION/DYNAMIC_AGENT_ALLOCATION.md):
1. **Level 1–2 Co-Location (Permitted):** One subagent may pair `CLINICAL_RESEARCHER` + `MEDICAL_LITERATURE_REVIEWER` for background/protocol drafting, or `PUBLIC_HEALTH_ANALYST` + `HEALTHCARE_DATA_ANALYST` for de-identified population summaries, followed by an explicit safety self-audit.
2. **Level 3–4 Separation of Duties (Mandatory):** `PATIENT_SAFETY_REVIEWER` MUST run as an independent reviewer subagent separate from the authoring clinical, omics, or data-analytics worker. Never allow an authoring agent to self-waive patient-safety, `PHI` de-identification, or biosecurity blockers.
3. **High-Assurance Governance:** Patient-impacting, clinical-workflow, or regulated `SaMD`/`GCP` deliverables default to Complexity Level 3 or Level 4 with [DOMAIN_LEAD](../../02_CORE_ROLES/DOMAIN_LEAD/SYSTEM_PROMPT.md) oversight and mandatory qualified human clinician approval.

---

## 5. Recommended Cross-Domain & Specialized Skills

- **Primary Medical Source Verification:** [RESEARCH_AND_SOURCE_VALIDATION/SKILL.md](../../04_CROSS_DOMAIN_SKILLS/RESEARCH_AND_SOURCE_VALIDATION/SKILL.md) (`SKL-CORE-004`) for `PubMed`/`DOI`/guideline provenance.
- **Clinical Hazard & Failure Analysis:** [RISK_MANAGEMENT/SKILL.md](../../04_CROSS_DOMAIN_SKILLS/RISK_MANAGEMENT/SKILL.md) (`SKL-CORE-010`) for severity-by-probability hazard matrices.
- **Biostatistical & Epidemiological Interpretation:** [DATA_INTERPRETATION/SKILL.md](../../04_CROSS_DOMAIN_SKILLS/DATA_INTERPRETATION/SKILL.md) (`SKL-CORE-005`) for absolute vs. relative risk and confounding checks.
- **Clinical Schema & Cohort Integrity:** [DATABASE_VALIDATION/SKILL.md](../../05_SPECIALIZED_SKILLS/DATABASE_VALIDATION/SKILL.md) (`SKL-SPEC-004`) for `OMOP`/`FHIR` referential and temporal integrity.
- **Pipeline Determinism:** [SCIENTIFIC_REPRODUCIBILITY/SKILL.md](../../05_SPECIALIZED_SKILLS/SCIENTIFIC_REPRODUCIBILITY/SKILL.md) (`SKL-SPEC-008`) for auditable analytical provenance.
