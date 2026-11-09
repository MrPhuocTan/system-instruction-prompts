# Quality Checklist: Instructional Designer (`ROLE-EDU-001`)

- **Role:** [INSTRUCTIONAL_DESIGNER](./SYSTEM_PROMPT.md)
- **Domain Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md) (`QG-EDU-001`, `QG-EDU-002`, `QG-EDU-005`, `QG-EDU-006`)

## 1. Needs Analysis & Constructive Alignment (`QG-EDU-001`)
- [ ] Performance gap analysis explicitly separates genuine skill/knowledge deficits from environmental, UX, or incentive barriers.
- [ ] Lightweight job aids or workflow checklists are recommended in place of full courses wherever recall is non-critical on the job.
- [ ] Every `TLO` and `ELO` specifies observable Revised Bloom's action verb, workplace condition, and mastery criterion.
- [ ] Zero banned unobservable terminal verbs (*"understand"*, *"know"*, *"appreciate"*, *"learn about"*) appear in objective tables.
- [ ] Constructive Alignment Matrix proves `1:1` bidirectional coverage: every `ELO` maps to $\ge 1$ criterion-referenced check and $\ge 1$ practice activity.
- [ ] Zero orphan slides, tangential reading blocks, or unpracticed assessment topics remain in the storyboard.

## 2. Cognitive Load, Scaffolding & Seat-Time Realism (`QG-EDU-002`)
- [ ] Complex skills progress systematically from annotated worked examples -> faded completion problems -> independent transfer scenarios (`Sweller` / `Merrill`).
- [ ] Active practice and realistic workplace decision scenarios represent $\ge 40\%$ of total learner seat time.
- [ ] Passive click-to-reveal accordions and decorative gamification badges are never counted as authentic cognitive practice.
- [ ] Extraneous load is eliminated: callouts are integrated spatially onto diagrams (`zero split-attention`), narration complements rather than duplicates slide text, and `"AI Sign"` clutter is absent.
- [ ] Formative feedback branches explain *why* each distractor or decision fails/succeeds rather than returning bare `"Correct / Incorrect"` strings.
- [ ] Notional seat-time budget (`reading + media + practice + assessment`) fits within $\pm 10\%$ of session limits, budgeting novice practice at $2\times\text{--}3\times$ expert speed.

## 3. Accessibility (`UDL 3.0` / `WCAG 2.2 AA`), Privacy & Telemetry (`QG-EDU-005`, `QG-EDU-006`)
- [ ] Multimodal representations (`text`, `structured table/diagram`, `worked example`) and plain-language global English are provided.
- [ ] `WCAG 2.2 AA` specs (semantic heading order, $\ge 4.5:1$ contrast, non-color-only state cues, descriptive alt-text, captions/transcripts) are verified.
- [ ] Interactive components specify full keyboard navigation and screen-reader equivalents alongside pointer/drag interactions.
- [ ] `xAPI` / `SCORM` / `cmi5` telemetry statements capture only instructional state without exposing `FERPA`/`COPPA`/`GDPR` learner PII.
- [ ] All third-party/`OER` media carry verified license attribution (`CC-BY` / `CC-BY-SA`).

## 4. Verification & Handoff Readiness
- [ ] Automated alignment-script check confirms `0` unassessed objectives and `0` unpracticed exam skills.
- [ ] Readability and plain-language lexical clarity are checked for non-native English cohorts.
- [ ] Storyboard vs. live `LMS` execution scope is transparently disclosed without fabricating GUI playback.
- [ ] Verified telemetry facts, instructional assumptions, seat-time estimates, and unpiloted risks are separated in [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md).
- [ ] Mandatory human SME / safety-officer signoff gate is flagged for clinical, operational, or regulated compliance procedures.
