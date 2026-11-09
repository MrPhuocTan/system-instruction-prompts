# Quality Checklist: UI Designer (`ROLE-DES-003`)

Pre-handoff verification checklist aligned with [`SYSTEM_PROMPT.md`](./SYSTEM_PROMPT.md) and [`QUALITY_GATES.md`](../../QUALITY_GATES.md). Every item must pass prior to handoff.

## 1. Design Token & Visual System Integrity
- [ ] All colors, spacing (`4px`/`8px` grid), typography, border radii, elevation shadows, and z-index layers map cleanly to **Primitive -> Semantic -> Component** tokens (`0` raw magic hex codes or arbitrary pixel values).
- [ ] Semantic tokens resolve cleanly across light mode, dark mode (if in scope), and OS high-contrast (`forced-colors`) media queries without hardcoded overrides.
- [ ] Programmatic relative-luminance contrast checks confirm `>= 4.5:1` for all normal readable text and `>= 3.0:1` for large text, input/control borders, icons, and `:focus-visible` indicators.

## 2. Exhaustive Component States & Input Ergonomics
- [ ] Every interactive component specifies exact visual and token values for `default`, `hover`, `focus-visible`, `active/pressed`, `disabled`, `read-only`, `loading/busy`, and `invalid/error`.
- [ ] Form inputs always pair with persistent visible `<label>` elements (never placeholder-only labels), programmatic `aria-describedby` helper/error bindings, and non-color-only validation indicators.
- [ ] Loading states use dimension-matched skeletons or inline spinners that cause zero Cumulative Layout Shift (`CLS = 0`).
- [ ] Zero critical actions rely exclusively on pointer `:hover` without touch and keyboard parity.

## 3. WCAG 2.2 AA Keyboard, ARIA & Reflow Compliance
- [ ] Native HTML elements are prioritized; composite widgets (Tabs, Combobox, Menu, Dialog, Tree) specify complete W3C WAI-ARIA 1.2 roles, states, and arrow/Tab/Escape key maps.
- [ ] Interactive pointer targets meet `>= 24x24 CSS px` minimum (`WCAG 2.5.8`) and `>= 44x44 CSS px` on primary mobile/touch controls.
- [ ] Layouts reflow cleanly from `320px` (400% zoom) up to `1440px+`, support `200%` text resize, use CSS logical properties (`inline`/`block`) for RTL readiness, and handle `+40%` localized text expansion without clipping.

## 4. Pragmatic Minimalism & Handoff Verification
- [ ] Zero "AI Sign" clutter (gratuitous neon glows, glassmorphic blobs, decorative emojis, or stock filler strings) appears anywhere in tokens or component specs.
- [ ] Component prop APIs, token names, and QA acceptance steps are unambiguous for [`FRONTEND_ENGINEER`](../../../IT_SOFTWARE/ROLES/FRONTEND_ENGINEER/SYSTEM_PROMPT.md), with honest disclosure if live GUI browser verification was unavailable.
- [ ] All relative Markdown links resolve to existing canonical files.

## 5. Pre-Handoff Independent Verification Summary

| Verification Dimension | Evidence Inspected | Status |
| :--- | :--- | :--- |
| 3-Tier W3C Design Token Mapping | Primitive -> Semantic -> Component tokens (`0` magic hex/px values) | `PASS / BLOCKED / FAILED` |
| WCAG 2.2 AA Contrast & Target Math | `>= 4.5:1` text, `>= 3.0:1` borders/focus, `>= 24x24px` hit targets | `PASS / BLOCKED / FAILED` |
| Interactive & Asynchronous State Matrix | `default`, `hover`, `focus-visible`, `disabled`, `loading`, `invalid` | `PASS / BLOCKED / FAILED` |
| Semantic HTML, ARIA & `320px` Reflow | WAI-ARIA 1.2 key maps, `400%` zoom reflow, `+40%` i18n/RTL safety | `PASS / BLOCKED / FAILED` |
| Zero "AI Sign" & Runtime QA Disclosure | Utilitarian component craft + honest live-GUI vs. static disclosure | `PASS / BLOCKED / FAILED` |
