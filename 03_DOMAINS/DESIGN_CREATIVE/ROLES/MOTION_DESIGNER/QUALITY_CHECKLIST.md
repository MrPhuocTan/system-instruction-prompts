# Quality Checklist: Motion Designer (`ROLE-DES-006`)

Pre-handoff verification checklist aligned with [`SYSTEM_PROMPT.md`](./SYSTEM_PROMPT.md) and [`QUALITY_GATES.md`](../../QUALITY_GATES.md). Every item must pass prior to handoff.

## 1. Functional Purpose & Ergonomic Timing
- [ ] Every specified motion serves an explicit ergonomic purpose (causality feedback, spatial orientation, state continuity, or hierarchy focus)—zero purely decorative perpetual loops.
- [ ] High-frequency workspace actions complete in `<= 150–200ms`, standard overlays/drawers in `200–280ms`, and exit transitions run faster (`~20%–30%`) than entrances.
- [ ] Staggered list/grid entrances cap total cumulative stagger delay at `<= 150ms` and never block immediate pointer or keyboard interaction.
- [ ] Easing curves match physical intent (`ease-out` / critically damped spring for user-triggered entrances; `ease-in` for exits; `linear` reserved strictly for progress bars, spinners, or opacity crossfades).

## 2. Compositor Performance & Host Thermal Safety (`60fps / 120fps`)
- [ ] Animations mutate compositor-friendly properties (`transform`, `opacity`) and avoid main-thread layout/paint thrashing (`top`, `left`, `width`, `height`, `margin`, animated `blur`/`box-shadow`).
- [ ] Transitions are mid-flight interruptible without jarring snap-backs when a user rapidly toggles or cancels an action.
- [ ] `will-change` is scoped conservatively and torn down post-transition rather than applied globally across DOM trees, protecting GPU memory and host thermal limits.

## 3. Photosensitive & Vestibular Accessibility (`WCAG 2.2`)
- [ ] Zero flashing/strobing sequences exceed `3` flashes per second (**WCAG 2.3.1** Three Flashes or Below Threshold).
- [ ] Any essential animation lasting `> 5 seconds` provides an explicit user pause/stop control (**WCAG 2.2.2**).
- [ ] Every motion specification defines an explicit `@media (prefers-reduced-motion: reduce)` behavior replacing spatial translation/zoom/parallax with calm opacity crossfades (`<= 150ms`) or instant transitions without breaking `transitionend` listeners or hiding active loading indicators.

## 4. Zero "AI Sign" Restraint & Handoff Clarity
- [ ] Zero "AI Sign" motion gimmicks (pulsing neon borders, floating background orbs, distracting typewriter-effect delays on already-loaded UI text, or emoji confetti spam) appear in the specification.
- [ ] Motion tokens, `transform-origin` anchors, and QA verification steps are documented cleanly for [`FRONTEND_ENGINEER`](../../../IT_SOFTWARE/ROLES/FRONTEND_ENGINEER/SYSTEM_PROMPT.md), with honest disclosure if live browser frame profiling was unavailable.
- [ ] All relative Markdown links resolve cleanly.

## 5. Pre-Handoff Independent Verification Summary

| Verification Dimension | Evidence Inspected | Status |
| :--- | :--- | :--- |
| Ergonomic Timing & Interruptibility | `<= 150–280ms` workspace bounds, faster exits, non-blocking input | `PASS / BLOCKED / FAILED` |
| Compositor-Only `60fps` Property Audit | `transform`/`opacity` only (`0` layout-thrashing `width`/`top`) | `PASS / BLOCKED / FAILED` |
| Flash Safety (`WCAG 2.3.1` / `2.2.2`) | `<= 3` flashes/sec + pause/stop controls on `> 5s` sequences | `PASS / BLOCKED / FAILED` |
| `prefers-reduced-motion` Fallback Map | Opacity/instant replacements preserving JS lifecycle & spinners | `PASS / BLOCKED / FAILED` |
| Zero Perpetual Loops & Thermal Safety | Zero infinite decorative shaders/glows draining host CPU/GPU | `PASS / BLOCKED / FAILED` |
