# Quality Checklist: Product Designer (`ROLE-DES-001`)

Pre-handoff verification checklist aligned with [`SYSTEM_PROMPT.md`](./SYSTEM_PROMPT.md) and [`QUALITY_GATES.md`](../../QUALITY_GATES.md). Every item must pass prior to handoff.

## 1. Requirements Traceability & Information Architecture
- [ ] Every screen, workflow branch, and action maps directly to a locked user goal and `PM` acceptance criterion without scope creep or decorative bloat.
- [ ] Core domain objects, navigation hierarchy, URL/route structure, and role-based permission states (`unauthenticated`, `read-only`, `editor`, `admin`) are explicitly mapped.
- [ ] Layout density and interaction paradigm (keyboard-first power workspace vs. progressive guided wizard) match operator frequency and task criticality.

## 2. End-to-End Journey & Cognitive Load Discipline
- [ ] Every task flow specifies entry point, step orientation, back/cancel behavior (preserving unsaved work or warning on dirty forms), and post-completion destination.
- [ ] Zero dead-end views, circular redirect loops, or stacked modal-on-modal anti-patterns exist.
- [ ] Each view designates at most one unmistakable primary CTA; secondary and destructive actions are visually and spatially differentiated.
- [ ] Forms group related fields logically, provide sensible defaults, validate inline without wiping user input, and avoid premature error shaming before field blur/submit.

## 3. Exhaustive State & Accessibility Coverage
- [ ] All operational states are explicitly specified per view: `first-run empty`, `filtered zero-results`, `loading/skeleton` (zero `CLS`), `populated (1 to 10,000+ items)`, `long-string overflow`, `field/API error + recovery`, `offline/retry`, and `success`.
- [ ] Irreversible or high-impact actions include clear impact summaries, undo windows where feasible, or explicit confirmation safeguards.
- [ ] Keyboard navigation order, landmark regions, focus restoration rules, and WCAG 2.2 AA target-size/contrast constraints are integrated into the functional spec.

## 4. Zero "AI Sign" Hygiene & Engineering Handoff Readiness
- [ ] Design contains zero decorative "AI Sign" clutter (neon gradients, sparkle icons, fake KPI widgets, synthetic dummy text, or emoji headers).
- [ ] Testable Design Acceptance Criteria (breakpoints `320px`–`1440px+`, state triggers, keyboard expectations) are documented clearly for [`FRONTEND_ENGINEER`](../../../IT_SOFTWARE/ROLES/FRONTEND_ENGINEER/SYSTEM_PROMPT.md) and [`HUMAN_CENTRIC_APPLICATION_QA`](../../../../05_SPECIALIZED_SKILLS/HUMAN_CENTRIC_APPLICATION_QA/SKILL.md).
- [ ] Tool availability (live GUI browser vs. static specification) is honestly disclosed, and all relative Markdown links resolve cleanly.

## 5. Pre-Handoff Independent Verification Summary

| Verification Dimension | Evidence Inspected | Status |
| :--- | :--- | :--- |
| Goal Alignment & Route IA Topology | User requirements, permissions, and route graph (`0` dead ends) | `PASS / BLOCKED / FAILED` |
| Cognitive Load & Single Primary CTA | Progressive disclosure, Fitts/Hick check, inline error preservation | `PASS / BLOCKED / FAILED` |
| Exhaustive Operational State Matrix | `empty`, `loading` (`0` CLS), `error`, `overflow`, `success` defined | `PASS / BLOCKED / FAILED` |
| WCAG 2.2 AA Flow & Keyboard Linearity | Landmarks, focus restoration, and `24x24px`/`44x44px` target bounds | `PASS / BLOCKED / FAILED` |
| Zero "AI Sign" & Frontend Handoff Spec | Clean utilitarian layout + testable viewport/state criteria | `PASS / BLOCKED / FAILED` |
