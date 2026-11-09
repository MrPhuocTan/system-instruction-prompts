# Quality Checklist: Assessment & Psychometric Specialist (`ROLE-EDU-003`)

- **Role:** [ASSESSMENT_PSYCHOMETRIC_SPECIALIST](./SYSTEM_PROMPT.md)
- **Domain Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md) (`QG-EDU-001`, `QG-EDU-003`, `QG-EDU-005`, `QG-EDU-006`)

## 1. Blueprint (`ToS`) & Constructive Validity (`QG-EDU-001`, `QG-EDU-003`)
- [ ] Table of Specifications (`ToS`) weights domains and Revised Bloom cognitive levels proportionally to job criticality and risk of error.
- [ ] Blueprint cell item counts sum exactly to total form length and match allocated examination time limits.
- [ ] Every assessment item/task traces to a declared `TLO`/`ELO` and measures authentic cognitive transfer rather than rote definition trivia.
- [ ] Construct-irrelevant variance (convoluted syntax, regional idioms, unstated assumptions, color-only figures) is stripped from all stems.

## 2. Item-Writing Hygiene & Behavioral Rubric Quality (`QG-EDU-003`)
- [ ] Selected-response items have a single verified defensible key (or explicit `Select N` count) independently verified via script/math execution where quantitative.
- [ ] Every distractor maps to a documented learner misconception or operational mistake (`100%` distractor rationale coverage).
- [ ] Zero `"all of the above"`, `"none of the above"`, double negatives, or unemphasized negative-stem traps exist.
- [ ] Key word-count length stays balanced ($0.7\times\text{--}1.4\times$ mean distractor length) with parallel grammatical phrasing across options.
- [ ] Enemy-item exclusion tags prevent inter-item cueing across items assembled onto the same test form.
- [ ] Performance/project rubrics use observable, countable behavioral anchors across all criteria and score levels (`0` subjective adjective-only scales).

## 3. Psychometric Calibration, Reliability & Fairness Verification
- [ ] Statistical model complexity matches sample size (`CTT` for $N \ge 30$; Rasch `1PL` for $N \ge 100$; `2PL/3PL` for $N \ge 300+$; unpiloted items labeled `PRE-PILOT`).
- [ ] When response matrices exist, Python scripts verify item difficulty ($p$), discrimination ($r_{pbis}$, flagging $< 0.15$ or negative values), $\alpha$/`KR-20`, conditional `SEM`, and rater `kappa`/`ICC`.
- [ ] Criterion-referenced cut-score rationale (`Modified Angoff` / `Bookmark`) and `Mantel-Haenszel` / logistic `DIF` fairness checks are documented where subgroup $N$ permits.

## 4. Exam Security, Learner Privacy & Human Oversight (`QG-EDU-006`)
- [ ] Live operational certification items are segregated from public practice banks to prevent item exposure compromises.
- [ ] Parallel test forms verify equivalence across domain weights, cognitive levels, and target Test Information curves.
- [ ] Examinee `FERPA`/`COPPA`/`GDPR` PII is stripped from response datasets prior to analysis or storage.
- [ ] `ADA` / `UDL` testing accommodations (`extended time`, `screen-reader tables`, `alt-text`) preserve target construct validity.
- [ ] Open-source Python vs. commercial `IRT` estimation scope, standard errors, and `PRE-PILOT` boundaries are separated in [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md).
- [ ] High-stakes pass/fail cutoffs and credentialing decisions enforce mandatory human board review (`EU AI Act` Annex III compliance).
