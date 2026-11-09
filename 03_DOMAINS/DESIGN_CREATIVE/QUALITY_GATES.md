# Domain 08: Design & Creative (`DESIGN_CREATIVE`) — Mandatory Quality Gates

Every deliverable produced within `03_DOMAINS/DESIGN_CREATIVE/` must satisfy all **8 Domain Quality Gates** below prior to [`DOMAIN_LEAD`](../../02_CORE_ROLES/DOMAIN_LEAD/SYSTEM_PROMPT.md), `SA`, and `PM` sign-off under [`REVIEW_AND_SIGNOFF.md`](../../01_ORCHESTRATION/REVIEW_AND_SIGNOFF.md) and [`HUMAN_CENTRIC_APPLICATION_QA`](../../05_SPECIALIZED_SKILLS/HUMAN_CENTRIC_APPLICATION_QA/SKILL.md). Failure on any gate blocks sign-off (`STATUS = BLOCKED` or `FAILED`).

---

## Gate 1: User Requirements & Task Objective Alignment
- **Pass Criteria:**
  1. Every user flow, screen layout, visual asset, and copy block traces directly to locked user needs, target operator context, and `PM` acceptance criteria.
  2. Functional density matches user context (e.g., high-density keyboard-first data tables for daily power operators vs. guided progressive steps for infrequent consumer onboarding).
- **Fail Condition:** Designing unrequested features, mismatched workflow personas, or ornamental marketing splash sections when a functional workspace was requested.

## Gate 2: End-to-End User Journey & Information Architecture Clarity
- **Pass Criteria:**
  1. Entry triggers, primary navigation hierarchy, branching conditions, multi-step progress orientation, back/cancel preservation rules, and post-completion destinations are fully specified.
  2. Zero dead-end screens, orphan routes, unrecoverable destructive actions, or circular navigation traps exist.
- **Fail Condition:** Fragmented single-screen mockups lacking navigation context, entry/exit transitions, or error-recovery paths.

## Gate 3: Usability & Cognitive Load Minimization
- **Pass Criteria:**
  1. Applies progressive disclosure, Fitts's Law (proximate, adequately sized primary actions), Hick's Law (bounded choice sets, clear primary CTA per view), and sensible defaults.
  2. Forms enforce inline field validation on blur/submit, preserve user-entered input across errors, group related inputs logically, and avoid unnecessary modal interruptions.
- **Fail Condition:** Cluttered action bars with competing primary buttons, multi-level nested modals, or destructive error states that wipe user input.

## Gate 4: Accessibility Compliance (WCAG 2.2 Level AA Baseline)
- **Pass Criteria:**
  1. **Contrast:** Verified luminance contrast `>= 4.5:1` for normal text and `>= 3.0:1` for large text, UI control borders, icons, and focus indicators across both light and dark themes (where dark mode is in scope).
  2. **Keyboard & Focus:** Logical `Tab` order, visible `:focus-visible` indicator (`>= 2px` outline/offset contrast), Escape-key dismissal, focus trapping/restoration on dialogs, and `>= 24x24 CSS px` (`44x44px` touch) hit targets.
  3. **ARIA & Semantics:** Native semantic HTML elements prioritized (`<button>`, `<nav>`, `<main>`, `<label>`); custom widgets specify exact WAI-ARIA 1.2 roles, `aria-expanded` / `aria-invalid` / `aria-live` states, non-color-only status cues, and `prefers-reduced-motion` accommodations.
- **Fail Condition:** Low-contrast muted gray text, `div onClick` controls lacking keyboard/ARIA semantics, missing focus rings, color-only red/green status indicators, or vestibular motion hazards.

## Gate 5: Visual Hierarchy & Design System Token Consistency
- **Pass Criteria:**
  1. Clear 3-level visual hierarchy (primary focal action/headline -> secondary structural groups -> tertiary metadata) governed by disciplined modular typography and `4px`/`8px` spatial rhythm.
  2. All colors, spacing, radii, shadows, and breakpoints reference canonical **Primitive -> Semantic -> Component** design tokens with zero ad-hoc magic hex values or arbitrary pixel offsets.
- **Fail Condition:** Inconsistent spacing/padding, more than 2–3 competing font families, or raw untracked hex colors bypassing semantic tokens.

## Gate 6: Exhaustive Interaction States (`loading` / `empty` / `error` / `success`)
- **Pass Criteria:**
  1. View-level and component-level specs explicitly define: **Loading** (layout-stable skeleton/spinner without cumulative layout shift `CLS`), **Empty / Zero-Data** (clear explanation + primary creation CTA), **Error / Degraded** (plain-language cause + concrete recovery/retry action), **Overflow / Long-Content** (truncation, wrapping, virtualization across `320px`–`1440px+`), and **Success / Confirmation** states.
- **Fail Condition:** Happy-path-only designs that break under empty databases, slow networks, API `4xx/5xx` errors, or long localized strings.

## Gate 7: Pragmatic Minimalism & Zero "AI Sign" Clutter
- **Pass Criteria:**
  1. Interface and assets exhibit clean, purposeful, domain-authentic craft free of gratuitous purple-blue neon gradients, floating decorative blobs, sparkle icons, fake dashboard charts, dummy Latin placeholder text, or decorative emojis.
- **Fail Condition:** Any "AI Sign" visual cliche, stock filler text, or ornamental clutter that adds cognitive noise without functional utility.

## Gate 8: Deterministic Design Acceptance Criteria & QA Readiness
- **Pass Criteria:**
  1. Deliverable includes testable acceptance criteria (exact breakpoint behavior, contrast ratios, token names, keyboard steps, state transitions) executable by `FRONTEND_ENGINEER` and verifiable under the 3-level [`HUMAN_CENTRIC_APPLICATION_QA`](../../05_SPECIALIZED_SKILLS/HUMAN_CENTRIC_APPLICATION_QA/SKILL.md) protocol, with honest disclosure whenever live GUI browser tools are unavailable.
- **Fail Condition:** Subjective handoff notes ("make it look modern and sleek") lacking measurable layout, state, or accessibility criteria.
