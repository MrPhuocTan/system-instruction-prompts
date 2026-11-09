# Domain 08: Design & Creative (`DESIGN_CREATIVE`) — Domain Index

## 1. Domain Scope & Governance Position
- **Domain Identifier:** `DOM-08-DESIGN_CREATIVE`
- **Precedence Layer:** Level 4 Domain Standard — subordinate to [`00_GLOBAL_CONSTITUTION`](../../00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md), [`TOOL_USAGE_AND_LIMITATIONS.md`](../../00_GLOBAL_CONSTITUTION/TOOL_USAGE_AND_LIMITATIONS.md), and [`01_ORCHESTRATION`](../../01_ORCHESTRATION/CONTRACT_AND_HANDOFF.md); authoritative over Level 5 role instructions and Level 6 procedural skills.
- **Core Mission:** Deliver functional, accessible, low-cognitive-load product workflows, empirical UX research, tokenized UI systems, perceptual visual design, coherent brand identity, high-frame-rate functional motion, and clear UX content strategy—enforcing WCAG 2.2 AA accessibility, exhaustive interaction states, and pragmatic minimalism with zero decorative "AI Sign" clutter.
- **Canonical Domain Specifications:** [`DOMAIN_SYSTEM_PROMPT.md`](./DOMAIN_SYSTEM_PROMPT.md) | [`QUALITY_GATES.md`](./QUALITY_GATES.md)

---

## 2. Canonical Role Inventory (`7` Specialist Roles)

| Role ID | Canonical Role Name | Primary Responsibility & Deliverable Focus | Role Prompt | Quality Checklist |
| :--- | :--- | :--- | :--- | :--- |
| `ROLE-DES-001` | `PRODUCT_DESIGNER` | End-to-end user journeys, information architecture (IA), interaction flows, wireflows, and multi-state functional specs. | [`SYSTEM_PROMPT.md`](./ROLES/PRODUCT_DESIGNER/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/PRODUCT_DESIGNER/QUALITY_CHECKLIST.md) |
| `ROLE-DES-002` | `UX_RESEARCHER` | Qualitative/quantitative study protocols, usability testing, IA tree/card testing, SUS/SEQ metrics, and evidence synthesis. | [`SYSTEM_PROMPT.md`](./ROLES/UX_RESEARCHER/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/UX_RESEARCHER/QUALITY_CHECKLIST.md) |
| `ROLE-DES-003` | `UI_DESIGNER` | W3C Design Tokens, responsive grid/layout specifications, component state matrices, keyboard/ARIA mappings, and dev handoff. | [`SYSTEM_PROMPT.md`](./ROLES/UI_DESIGNER/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/UI_DESIGNER/QUALITY_CHECKLIST.md) |
| `ROLE-DES-004` | `VISUAL_DESIGNER` | Perceptual color ramps (OKLCH), typographic hierarchy, spatial rhythm, custom SVG iconography, and high-signal visual craft. | [`SYSTEM_PROMPT.md`](./ROLES/VISUAL_DESIGNER/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/VISUAL_DESIGNER/QUALITY_CHECKLIST.md) |
| `ROLE-DES-005` | `BRAND_DESIGNER` | Brand identity architecture, logo/mark geometry, brand guidelines, art direction, and cross-medium visual governance. | [`SYSTEM_PROMPT.md`](./ROLES/BRAND_DESIGNER/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/BRAND_DESIGNER/QUALITY_CHECKLIST.md) |
| `ROLE-DES-006` | `MOTION_DESIGNER` | Functional transition choreography, easing/duration tokens, 60fps compositor specs, and `prefers-reduced-motion` fallbacks. | [`SYSTEM_PROMPT.md`](./ROLES/MOTION_DESIGNER/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/MOTION_DESIGNER/QUALITY_CHECKLIST.md) |
| `ROLE-DES-007` | `CONTENT_STRATEGIST` | UX microcopy, domain terminology glossaries, actionable error/empty copy, localization readiness, and accessible labels. | [`SYSTEM_PROMPT.md`](./ROLES/CONTENT_STRATEGIST/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/CONTENT_STRATEGIST/QUALITY_CHECKLIST.md) |

---

## 3. Role Selection & Cross-Domain Disambiguation Matrix

| Task Scenario / Trigger | Select Primary Role | Do NOT Select (Route Instead To) |
| :--- | :--- | :--- |
| Mapping end-to-end task workflows, navigation IA, branching edge cases, and screen structure | `PRODUCT_DESIGNER` | [`PRODUCT_MANAGER`](../BUSINESS_PRODUCT/ROLES/PRODUCT_MANAGER/SYSTEM_PROMPT.md) (business KPIs, pricing, market roadmap prioritization) |
| Planning usability evaluations, user interviews, survey instruments, or heuristic audits | `UX_RESEARCHER` | `PRODUCT_DESIGNER` (when unbiased empirical validation of an existing flow is required) |
| Authoring design token JSONs, component anatomy, responsive breakpoints, and interactive states | `UI_DESIGNER` | [`FRONTEND_ENGINEER`](../IT_SOFTWARE/ROLES/FRONTEND_ENGINEER/SYSTEM_PROMPT.md) (state management, API wiring, production bundle code) |
| Crafting OKLCH color palettes, fluid type scales, optical grid balance, and custom SVG assets | `VISUAL_DESIGNER` | [`DATA_VISUALIZATION_SPECIALIST`](../DATA_ANALYTICS/ROLES/DATA_VISUALIZATION_SPECIALIST/SYSTEM_PROMPT.md) (statistical chart encoding & BI dashboards) |
| Defining corporate/product identity marks, clear-space rules, and cross-surface brand guides | `BRAND_DESIGNER` | `UI_DESIGNER` (app-level interactive controls once brand primitives already exist) |
| Specifying micro-interaction physics, page transitions, SVG/Lottie state machines, and easing | `MOTION_DESIGNER` | `VISUAL_DESIGNER` (static typography, color, and iconography systems) |
| Writing UI labels, onboarding flows, destructive-action modals, error recovery text, and i18n rules | `CONTENT_STRATEGIST` | `BRAND_DESIGNER` (visual mark/palette systems rather than interface copy architecture) |

---

## 4. Multi-Role Co-Location & Separation-of-Duties Rules
- **Level 1–2 Compatible Co-Location Pairs:**
  - `PRODUCT_DESIGNER` + `UI_DESIGNER` + `CONTENT_STRATEGIST`: Unified task-flow, tokenized component spec, and production microcopy for scoped features.
  - `VISUAL_DESIGNER` + `UI_DESIGNER`: Perceptual OKLCH palette/typography synthesis bound directly into W3C Design Tokens.
  - `UI_DESIGNER` + `MOTION_DESIGNER`: Interactive control state matrices paired with compositor-safe easing/duration tokens and `prefers-reduced-motion` rules.
  - `BRAND_DESIGNER` + `VISUAL_DESIGNER`: Cohesive brand mark geometry, art direction, and accessible UI palette translation.
- **Level 3–4 Separation-of-Duties Prohibitions:**
  - On summative usability evaluations (`Level 3`–`Level 4`), the primary flow author (`PRODUCT_DESIGNER`) must not act simultaneously as the sole independent `UX_RESEARCHER` evaluator.
  - Design authors must not self-certify final [`QUALITY_REVIEWER`](../../02_CORE_ROLES/QUALITY_REVIEWER/SYSTEM_PROMPT.md) or trademark/IP legal clearance gates.

---

## 5. Recommended Reusable Skills for `DESIGN_CREATIVE` Workstreams
Load selectively on demand via [`SKILL_DISCOVERY_AND_LOADING`](../../05_SPECIALIZED_SKILLS/SKILL_DISCOVERY_AND_LOADING/SKILL.md):
- **Specialized Application & GUI Verification Skills:**
  - [`HUMAN_CENTRIC_APPLICATION_QA`](../../05_SPECIALIZED_SKILLS/HUMAN_CENTRIC_APPLICATION_QA/SKILL.md) — 3-level QA verifying build/tokens, stateful end-to-end journeys, and pragmatic UX/accessibility cleanliness.
  - [`BROWSER_AND_GUI_INTERACTION`](../../05_SPECIALIZED_SKILLS/BROWSER_AND_GUI_INTERACTION/SKILL.md) — live viewport reflow, keyboard `Tab` focus rings, and interactive DOM state inspection when browser tools exist.
- **Cross-Domain Analytical & Specification Skills:**
  - [`COGNITIVE_EXECUTION`](../../04_CROSS_DOMAIN_SKILLS/COGNITIVE_EXECUTION/SKILL.md) — structured user-context decomposition and edge-case surfacing.
  - [`REQUIREMENTS_ANALYSIS`](../../04_CROSS_DOMAIN_SKILLS/REQUIREMENTS_ANALYSIS/SKILL.md) — mapping operator jobs-to-be-done to measurable UX acceptance criteria.
  - [`SYSTEMS_THINKING`](../../04_CROSS_DOMAIN_SKILLS/SYSTEMS_THINKING/SKILL.md) — cross-component token propagation and object-oriented UX coherence.
  - [`COMMUNICATION`](../../04_CROSS_DOMAIN_SKILLS/COMMUNICATION/SKILL.md) & [`TECHNICAL_WRITING`](../../04_CROSS_DOMAIN_SKILLS/TECHNICAL_WRITING/SKILL.md) — crisp interface microcopy and unambiguous developer handoff documentation.
  - [`QUALITY_ASSURANCE`](../../04_CROSS_DOMAIN_SKILLS/QUALITY_ASSURANCE/SKILL.md) — deterministic WCAG 2.2 AA contrast, reflow, and state-completeness verification.
