# Education & Training Quality Gates (`QUALITY_GATES.md`)

- **Domain:** `EDUCATION_TRAINING` (`DOM-15`)
- **Enforcement Stage:** Mandatory pre-handoff verification by the accountable specialist and gate audit by [DOMAIN_LEAD](../../02_CORE_ROLES/DOMAIN_LEAD/SYSTEM_PROMPT.md), `SA_GATE`, and `PM_GATE` under [REVIEW_AND_SIGNOFF.md](../../01_ORCHESTRATION/REVIEW_AND_SIGNOFF.md).
- **Pass Rule:** Any `FAIL` on an applicable gate blocks `PASS` signoff until remediated or explicitly approved as an out-of-scope constraint by `PM + SA`.

## 1. Gate Matrix (`QG-EDU-001` through `QG-EDU-006`)

| Gate ID | Gate Name | Objective Pass Criteria | Deterministic Verification Method | Blocking Failure Trigger |
| :--- | :--- | :--- | :--- | :--- |
| `QG-EDU-001` | **Backward Design & Constructive Alignment** | 100% of `TLOs`/`ELOs` use observable Revised Bloom's verbs with conditions and mastery criteria; alignment matrix proves bidirectional `1:1` coverage across objectives, assessments, and practice activities. | Automated alignment-matrix completeness check (`0` unassessed objectives, `0` unpracticed exam skills, `0` banned vague verbs such as *"understand"* or *"know"* as terminal verb). | Unmeasurable objective verbs, orphan instructional content, or summative assessment testing skills never practiced. |
| `QG-EDU-002` | **Cognitive Load, Scaffolding & Prerequisite DAG** | Prerequisite dependencies form a valid Directed Acyclic Graph (`DAG`, `0` cycles); lessons progress via worked-example -> faded-practice -> independent transfer with realistic notional seat-time budgets and zero `"AI Sign"` clutter. | Topological sort / cycle-detection check on curriculum graph plus instructional-time budget audit (`reading + media + lab + assessment minutes <= allocated session window`). | Circular prerequisite loop, abrupt un-scaffolded jump to complex synthesis, or 3 hours of dense content packed into a 45-minute slot. |
| `QG-EDU-003` | **Psychometric Validity, Reliability & Rubric Fairness** | Assessments map to a weighted Table of Specifications (`ToS`); items pass structural item-writing rules with misconception-mapped distractors; rubrics use observable behavioral anchors; `CTT`/`IRT` and `DIF` stats verified when data exist. | Item-bank lint audit (single unambiguous key, distractor rationale present, zero `"all/none of the above"` cues) + Python psychometric script (`p`, $r_{pbis}$, $\alpha$/`KR-20`, `kappa`). | Ambiguous multi-key item, subjective adjective-only rubric (`"good/fair/poor"`), negative item-total discrimination ($r_{pbis} < 0$) left active, or biased item prompt. |
| `QG-EDU-004` | **Technical Accuracy & Hands-On Lab Executability** | Every code block, formula, dataset, lab starter state, fault-injection script, solution key, and autograder test suite executes cleanly in a reproducible environment with pinned versions and teardown steps. | `run_command` execution log confirming: (1) starter state fails target assertion as intended, (2) reference solution passes 100% of autograder tests (`exit code 0`), and (3) reset script restores clean state. | Unexecuted pseudocode presented as working lab, broken CLI flags/imports, autograder passable by trivial hardcoding, or destructive host side-effects. |
| `QG-EDU-005` | **Accessibility (`UDL 3.0` & `WCAG 2.2 AA`)** | Content provides multimodal representations, semantic heading order, $\ge 4.5:1$ text contrast, non-color-only cues, alt-text/captions/transcripts, keyboard-operable interactive widgets, and plain-language clarity. | Structural Markdown/HTML accessibility check (heading tree, alt-text presence, contrast ratios, keyboard focus order) + browser/GUI QA per `HUMAN_CENTRIC_APPLICATION_QA` when interactive UI exists. | Color-only pass/fail indicators, missing diagram alt-text, inaccessible drag-and-drop without keyboard alternative, or fabricated GUI test claims. |
| `QG-EDU-006` | **Learner Privacy (`FERPA`/`COPPA`/`GDPR`), IP & Human Oversight** | Zero student PII in datasets, `xAPI`/`SCORM` examples, or logs; minor age-gating (`COPPA`/`GDPR-K`) addressed; `OER`/copyright licenses verified; human review enforced on high-stakes grading/certification decisions. | PII regex/schema scan across sample datasets and telemetry payloads + license provenance table + explicit human signoff gate on high-stakes cutoffs. | Real learner PII leaked, unconsented minor tracking telemetry, unlicensed copyrighted material copied verbatim, or fully automated high-stakes credential denial without human appeal/review. |

## 2. Interactive Learning Application QA Alignment

Whenever a deliverable includes an interactive web learning portal, quiz player, coding sandbox UI, or `SCORM`/`xAPI` package:
1. Apply the 3-level verification standard from [HUMAN_CENTRIC_APPLICATION_QA](../../05_SPECIALIZED_SKILLS/HUMAN_CENTRIC_APPLICATION_QA/SKILL.md):
   - **Level 1:** Build, schema (`imsmanifest.xml`, `QTI`, `xAPI` JSON), linter, and automated autograder unit tests pass.
   - **Level 2:** Live stateful learner journey verified (start attempt -> invalid input feedback -> hint progression -> valid submission -> score persistence -> retry/reset state).
   - **Level 3:** Clean utilitarian typography, uncluttered reading measure, keyboard navigation, responsive layout, and zero decorative `"AI Sign"` badges or artificial gamification noise.
2. Disclose honestly whenever interactive browser/LMS player tools are absent in the current session and execute the strongest programmatic DOM/API/schema checks available.

## 3. Role-to-Checklist Traceability

Each accountable role must complete and attach its specialist checklist prior to gate review:
- `INSTRUCTIONAL_DESIGNER`: [QUALITY_CHECKLIST.md](./ROLES/INSTRUCTIONAL_DESIGNER/QUALITY_CHECKLIST.md) (`QG-EDU-001`, `QG-EDU-002`, `QG-EDU-005`)
- `CURRICULUM_ARCHITECT`: [QUALITY_CHECKLIST.md](./ROLES/CURRICULUM_ARCHITECT/QUALITY_CHECKLIST.md) (`QG-EDU-001`, `QG-EDU-002`, `QG-EDU-005`)
- `ASSESSMENT_PSYCHOMETRIC_SPECIALIST`: [QUALITY_CHECKLIST.md](./ROLES/ASSESSMENT_PSYCHOMETRIC_SPECIALIST/QUALITY_CHECKLIST.md) (`QG-EDU-001`, `QG-EDU-003`, `QG-EDU-006`)
- `TECHNICAL_TRAINER`: [QUALITY_CHECKLIST.md](./ROLES/TECHNICAL_TRAINER/QUALITY_CHECKLIST.md) (`QG-EDU-001`, `QG-EDU-004`, `QG-EDU-005`)
- `LEARNING_EXPERIENCE_EVALUATOR`: [QUALITY_CHECKLIST.md](./ROLES/LEARNING_EXPERIENCE_EVALUATOR/QUALITY_CHECKLIST.md) (`QG-EDU-003`, `QG-EDU-005`, `QG-EDU-006`)

## 4. Pre-Signoff Evidence Package Requirements

Every handoff submitted for `DOMAIN_LEAD` and `SA_GATE` review must attach verifiable artifacts:
1. **Constructive Alignment & `DAG` Verification Output:** Deterministic script output confirming `1:1` objective-assessment-practice coverage, zero prohibited unobservable verbs, and zero circular prerequisite dependencies.
2. **Lab & Item Execution Evidence:** Command-line logs demonstrating starter-state failure, reference-solution `exit code 0`, clean environment reset, and independent verification of quantitative/code exam keys.
3. **Psychometric & Accessibility Audit Summary:** `ToS` blueprint weights, distractor misconception rationales, `CTT`/`IRT` or `PRE-PILOT` calibration tags, and `UDL 3.0` / `WCAG 2.2 AA` structural verification logs.
4. **Privacy & High-Stakes Governance Log:** Confirmation of zero `FERPA`/`COPPA`/`GDPR` student PII, verified `OER`/media licenses, and human signoff triggers on high-stakes certification, admissions, or safety-training decisions.

## 5. Escalation & Signoff Recording

Record gate outcomes (`PASS`, `PARTIAL`, `BLOCKED`, `FAILED`, or `NOT VERIFIED`) with exact alignment matrices, lab execution logs, and psychometric outputs in [HANDOFF_REPORT.md](../../06_TEMPLATES/HANDOFF_REPORT.md) per [INDEPENDENT_VERIFICATION.md](../../00_GLOBAL_CONSTITUTION/INDEPENDENT_VERIFICATION.md). Escalate any high-stakes accreditation, minor-privacy (`COPPA`), or unverified clinical/safety training hazard immediately to `PM + SA`.
