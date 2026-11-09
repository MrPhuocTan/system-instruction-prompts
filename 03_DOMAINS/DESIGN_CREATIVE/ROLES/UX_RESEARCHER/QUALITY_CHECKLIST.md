# Quality Checklist: UX Researcher (`ROLE-DES-002`)

Pre-handoff verification checklist aligned with [`SYSTEM_PROMPT.md`](./SYSTEM_PROMPT.md) and [`QUALITY_GATES.md`](../../QUALITY_GATES.md). Every item must pass prior to handoff.

## 1. Methodological Fit & Bias Control
- [ ] Research method (contextual inquiry, usability test, card sort, tree test, survey, heuristic walkthrough) matches the stated decision objective (exploratory vs. evaluative; behavioral vs. attitudinal).
- [ ] Participant screener uses behavioral/contextual criteria with distractor options rather than transparent yes/no self-selection questions.
- [ ] Interview and survey instruments contain zero leading questions, zero double-barreled prompts, zero speculative future-purchase hypotheticals, and balanced rating scales.
- [ ] Usability task scenarios describe realistic user goals without leaking exact navigation labels or button names from the target UI, and task order is counterbalanced where sequence effects exist.

## 2. Empirical Integrity & Statistical Honesty (`ZERO FABRICATION`)
- [ ] Zero fabricated user quotes, synthetic interview transcripts, or invented task-completion numbers are presented as empirical findings (`[HYPOTHESIS]` vs. `[OBSERVED EVIDENCE]` strictly separated).
- [ ] Quantitative summaries report exact raw numerators/denominators (`k/n`) alongside any percentages, include confidence intervals (e.g., adjusted Wald / Wilson) where appropriate, and avoid claiming statistical significance on underpowered small-N samples.
- [ ] Standardized psychometric instruments (SUS, UMUX-Lite, SEQ, NASA-TLX) preserve validated item wording and exact scoring formulas.

## 3. Insight Traceability & Actionable Prioritization
- [ ] Every finding separates **Observed Behavior / Verbatim Evidence** -> **Root Usability Mechanism** -> **Severity Tier (`CRITICAL / HIGH / MEDIUM / LOW`)** -> **Concrete Product/UI Recommendation**.
- [ ] Heuristic or cognitive walkthrough findings cite the exact violated usability or WCAG 2.2 accessibility principle and affected workflow step.

## 4. Participant Privacy, Consent & Ethical Safeguards
- [ ] Study protocols include explicit informed-consent, recording-permission, data-retention, and right-to-withdraw disclosures.
- [ ] All participant PII/PHI is pseudonymized (`P01`, `P02`) across workspace artifacts, and vulnerable/clinical population triggers are escalated for IRB / legal privacy review.
- [ ] Deliverable contains zero decorative emojis, zero unfinished placeholders, and 100% valid relative Markdown links.

## 5. Pre-Handoff Independent Verification Summary

| Verification Dimension | Evidence Inspected | Status |
| :--- | :--- | :--- |
| Method Fit, Screener & Prompt Neutrality | Zero leading prompts, zero UI-label giveaways, counterbalanced tasks | `PASS / BLOCKED / FAILED` |
| Empirical Non-Fabrication Audit | 100% of quotes/counts traced to real data (`[HYPOTHESIS]` split) | `PASS / BLOCKED / FAILED` |
| Small-N & Psychometric Rigor | Raw `k/n` counts + confidence intervals + unmodified SUS/SEQ scales | `PASS / BLOCKED / FAILED` |
| Severity & Actionable Traceability | Evidence -> root mechanism -> `P0`–`P3` tier -> concrete UI fix | `PASS / BLOCKED / FAILED` |
| Informed Consent & PII Anonymization | Pseudonymized IDs (`P01`) + consent/IRB/privacy safeguards checked | `PASS / BLOCKED / FAILED` |
