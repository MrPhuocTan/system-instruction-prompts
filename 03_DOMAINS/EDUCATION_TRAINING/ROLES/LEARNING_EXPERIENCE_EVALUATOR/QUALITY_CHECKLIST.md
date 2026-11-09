# Quality Checklist: Learning Experience Evaluator (`ROLE-EDU-005`)

- **Role:** [LEARNING_EXPERIENCE_EVALUATOR](./SYSTEM_PROMPT.md)
- **Domain Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md) (`QG-EDU-003`, `QG-EDU-005`, `QG-EDU-006`)

## 1. Multi-Level Evaluation Design & Attribution Rigor (`QG-EDU-003`)
- [ ] Evaluation plan explicitly distinguishes `Kirkpatrick Level 1` (reaction), `Level 2` (objective mastery), `Level 3` (`30/60/90-day` workplace behavior transfer), and `Level 4` / `Phillips ROI` outcomes.
- [ ] Learner `CSAT` / `NPS` smile-sheet ratings are never conflated with verified skill retention or on-the-job transfer.
- [ ] Quasi-experimental controls (`DiD`, baseline ANCOVA, stepped cohort rollout) or explicit `Phillips` isolation/confidence discounts separate training effects from concurrent tooling, policy, or seasonal changes.
- [ ] Fully loaded `ROI` cost denominator includes instructional development, platform/delivery costs, AND learner/facilitator seat-time wage opportunity costs.
- [ ] Pre-deployment plans lacking live post-training telemetry are explicitly labeled `Evaluation Instrumentation Plan` or `Formative Pre-Pilot Audit`.

## 2. Funnel Conservation, Survivorship & Statistical Accuracy
- [ ] Python reconciliation script confirms exact cohort funnel closure (`Enrolled == Not_Started + Dropped + Failed + Mastered`).
- [ ] Intention-to-Treat (`ITT` across all enrolled learners) metrics are reported alongside completer-only metrics to prevent survivorship bias.
- [ ] Rapid-guessing responses (`< 3s`), test/instructor accounts, and duplicate `xAPI` / `Caliper` events are filtered deterministically before statistical aggregation.
- [ ] Pre/post analyses report `Hake's` normalized gain ($g$), paired effect sizes (`Cohen's d` / `Hedges' g`), `95%` confidence intervals, and baseline ceiling/floor flags.
- [ ] Every flagged drop-off or item-retry anomaly is traced to an actionable remediation owner (`scaffolding -> ROLE-EDU-001`, `prerequisite -> ROLE-EDU-002`, `flawed item -> ROLE-EDU-003`, `broken lab -> ROLE-EDU-004`).

## 3. Usability, Accessibility (`WCAG 2.2 AA`) & Learner Privacy (`QG-EDU-005`, `QG-EDU-006`)
- [ ] Formative UX reviews apply cognitive walkthroughs and 3-level `HUMAN_CENTRIC_APPLICATION_QA`, honestly disclosing if live browser/LMS player tools were unavailable in the runtime.
- [ ] `FERPA`, `COPPA`, and `GDPR` de-identification plus minimum cell-size suppression ($k \ge 5\text{--}10$) prevent individual learner re-identification in executive dashboards.
- [ ] Exploratory practice/hint telemetry is protected from punitive HR/employment misuse.

## 4. Independence, Reproducibility & Signoff Readiness
- [ ] Evaluation scripts (`funnel closure`, `Hake's g`, `effect sizes`, `ROI`) execute deterministically via `run_command` (`exit code 0`).
- [ ] Evaluator separation-of-duties from original course/lab authorship is explicitly confirmed on Level 3–4 program signoffs.
- [ ] Remediation backlog ranks fixes by quantified learner impact vs. engineering effort with concrete target role owners.
- [ ] Observed empirical telemetry, statistical isolation assumptions, `ROI` estimates, and uncollected longitudinal (`30/60/90-day`) gaps are separated in [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md).
- [ ] Mandatory human governance review is flagged before using training metrics in academic standing, certification, or workforce decisions.
