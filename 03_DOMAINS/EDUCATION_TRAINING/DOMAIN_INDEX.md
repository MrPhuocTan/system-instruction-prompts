# Domain 15: Education & Training (`EDUCATION_TRAINING`)

- **Domain ID:** `DOM-15`
- **Precedence Layer:** Level 4 — Domain Governance (subordinate to [Global Constitution](../../00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md) and [PM + SA Orchestration](../../01_ORCHESTRATION/PERSISTENT_PM_SA.md))
- **Normative Binding:** [DOMAIN_SYSTEM_PROMPT.md](./DOMAIN_SYSTEM_PROMPT.md) and [QUALITY_GATES.md](./QUALITY_GATES.md)

## 1. Domain Scope & Purpose

The `EDUCATION_TRAINING` domain governs evidence-based instructional design, multi-course curriculum architecture, psychometric assessment engineering, executable technical workshops and hands-on labs, and empirical learning-effectiveness evaluation across academic, enterprise enablement, professional certification, and workforce upskilling contexts. Every specialist operating in this domain enforces Backward Design constructive alignment, Cognitive Load Theory scaffolding, `AERA/APA/NCME` measurement rigor, verified lab code/CLI executability, `UDL 3.0` / `WCAG 2.2 AA` accessibility, and strict `FERPA` / `COPPA` / `GDPR` learner-privacy protections.

## 2. Canonical Role Inventory (`5` Specialist Roles)

| Role ID | Canonical Role Directory | Specialist Prompt | Verification Checklist | Primary Pedagogical & Analytical Ownership |
| :--- | :--- | :--- | :--- | :--- |
| `ROLE-EDU-001` | `INSTRUCTIONAL_DESIGNER` | [SYSTEM_PROMPT.md](./ROLES/INSTRUCTIONAL_DESIGNER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/INSTRUCTIONAL_DESIGNER/QUALITY_CHECKLIST.md) | Action Mapping gap analysis, Backward Design alignment, Revised Bloom's `TLO`/`ELO` authoring, worked-example scaffolding, `UDL`/`WCAG` storyboards, and `SCORM`/`xAPI` specs |
| `ROLE-EDU-002` | `CURRICULUM_ARCHITECT` | [SYSTEM_PROMPT.md](./ROLES/CURRICULUM_ARCHITECT/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/CURRICULUM_ARCHITECT/QUALITY_CHECKLIST.md) | Multi-course pathway architecture, competency frameworks (`SFIA`, `NICE`, `EQF`, `ABET`), prerequisite `DAG` validation, spiral progression, and credit/time budgeting |
| `ROLE-EDU-003` | `ASSESSMENT_PSYCHOMETRIC_SPECIALIST` | [SYSTEM_PROMPT.md](./ROLES/ASSESSMENT_PSYCHOMETRIC_SPECIALIST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/ASSESSMENT_PSYCHOMETRIC_SPECIALIST/QUALITY_CHECKLIST.md) | Exam Tables of Specifications (`ToS`), diagnostic item banking, analytic rubrics, `CTT`/`IRT` calibration, Angoff cut-scores, reliability ($\alpha$/`KR-20`/`\kappa`), and `DIF` fairness |
| `ROLE-EDU-004` | `TECHNICAL_TRAINER` | [SYSTEM_PROMPT.md](./ROLES/TECHNICAL_TRAINER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/TECHNICAL_TRAINER/QUALITY_CHECKLIST.md) | Executable hands-on labs, reproducible sandbox/container setups, fault-injection troubleshooting scenarios, deterministic autograders, and facilitator runbooks |
| `ROLE-EDU-005` | `LEARNING_EXPERIENCE_EVALUATOR` | [SYSTEM_PROMPT.md](./ROLES/LEARNING_EXPERIENCE_EVALUATOR/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/LEARNING_EXPERIENCE_EVALUATOR/QUALITY_CHECKLIST.md) | `Kirkpatrick Levels 1–4` & `Phillips ROI` studies, `xAPI`/LMS funnel telemetry, normalized learning gain (`Hake's g`), cognitive walkthroughs, and remediation backlogs |

## 3. Task-to-Role Routing & Multi-Role Selection Matrix

| Task Archetype | Primary Accountable Role | Supporting / Review Role(s) | Mandatory Separation-of-Duties Rule |
| :--- | :--- | :--- | :--- |
| Course module design, e-learning storyboard, performance job aid, or lesson scaffolding | `INSTRUCTIONAL_DESIGNER` | `TECHNICAL_TRAINER`, `ASSESSMENT_PSYCHOMETRIC_SPECIALIST` | Separate high-stakes certification item validation from lesson content authoring on Level 3–4 programs |
| Degree/bootcamp roadmap, role competency matrix, accreditation mapping, or prerequisite graph | `CURRICULUM_ARCHITECT` | `INSTRUCTIONAL_DESIGNER`, `LEARNING_EXPERIENCE_EVALUATOR` | Require independent `DOMAIN_LEAD` / accreditation audit before locking formal credit/credential standards |
| Certification exam blueprint, item bank calibration, grading rubric, or cut-score study | `ASSESSMENT_PSYCHOMETRIC_SPECIALIST` | `CURRICULUM_ARCHITECT` | Item authors must not single-handedly approve final cut-scores or `DIF` bias signoff on high-stakes exams |
| Engineering workshop, live-coding bootcamp, cloud/security sandbox lab, or CLI autograder | `TECHNICAL_TRAINER` | `INSTRUCTIONAL_DESIGNER` | Every lab starter, broken state, and solution script must pass independent automated execution checks |
| Post-training impact study, LMS drop-off audit, A/B pedagogy analysis, or usability review | `LEARNING_EXPERIENCE_EVALUATOR` | `ASSESSMENT_PSYCHOMETRIC_SPECIALIST` | Course authors must not serve as sole effectiveness auditor (`ROLE-EDU-005`) on Level 3–4 ROI signoffs |

## 4. Recommended Cross-Domain & Specialized Skills

Load only active procedural runbooks on demand via progressive disclosure:
- **Cross-Domain Skills (`04_CROSS_DOMAIN_SKILLS/`):**
  - [REQUIREMENTS_ANALYSIS](../../04_CROSS_DOMAIN_SKILLS/REQUIREMENTS_ANALYSIS/SKILL.md) — distinguishing genuine skill/knowledge gaps from tooling, process, or incentive barriers.
  - [COGNITIVE_EXECUTION](../../04_CROSS_DOMAIN_SKILLS/COGNITIVE_EXECUTION/SKILL.md) — structured pedagogical decomposition and misconception anticipation.
  - [TECHNICAL_WRITING](../../04_CROSS_DOMAIN_SKILLS/TECHNICAL_WRITING/SKILL.md) — crisp, plain-language learner instructions, lab guides, and rubrics free of decorative filler.
  - [COMMUNICATION](../../04_CROSS_DOMAIN_SKILLS/COMMUNICATION/SKILL.md) — audience-calibrated tone across novice, practitioner, and executive cohorts.
  - [DATA_INTERPRETATION](../../04_CROSS_DOMAIN_SKILLS/DATA_INTERPRETATION/SKILL.md) — psychometric item telemetry, `xAPI` event funnels, and pre/post effect-size analysis.
  - [RESEARCH_AND_SOURCE_VALIDATION](../../04_CROSS_DOMAIN_SKILLS/RESEARCH_AND_SOURCE_VALIDATION/SKILL.md) — primary domain accuracy and peer-reviewed learning-science citation verification.
- **Specialized Skills (`05_SPECIALIZED_SKILLS/`):**
  - [HUMAN_CENTRIC_APPLICATION_QA](../../05_SPECIALIZED_SKILLS/HUMAN_CENTRIC_APPLICATION_QA/SKILL.md) — 3-level QA across interactive learning apps, LMS packages, keyboard navigation, and visual clarity.
  - [BROWSER_AND_GUI_INTERACTION](../../05_SPECIALIZED_SKILLS/BROWSER_AND_GUI_INTERACTION/SKILL.md) — real learner-journey inspection of web-based labs, quizzes, and responsive viewports.
  - [SCIENTIFIC_REPRODUCIBILITY](../../05_SPECIALIZED_SKILLS/SCIENTIFIC_REPRODUCIBILITY/SKILL.md) — deterministic lab container/environment execution and statistical psychometric scripts.

## 5. Cross-Domain Coordination Touchpoints

- **`IT_SOFTWARE`, `AI_MACHINE_LEARNING`, `CYBERSECURITY`, & `DATA_ANALYTICS`:** Subject-matter technical accuracy, safe isolated lab sandboxes (zero live offensive payloads outside authorized ranges), and autograder CI pipelines.
- **`DESIGN_CREATIVE`:** Visual hierarchy, instructional diagrams (`dual coding`), interactive UI states, and `WCAG 2.2 AA` contrast/typography systems.
- **`LEGAL_COMPLIANCE` & `HEALTHCARE_LIFE_SCIENCES`:** `FERPA`/`COPPA`/`GDPR` student data governance, `EU AI Act` high-risk educational system compliance, copyright licensing, and continuing medical/legal education (`CME`/`CLE`) accreditation rules.
