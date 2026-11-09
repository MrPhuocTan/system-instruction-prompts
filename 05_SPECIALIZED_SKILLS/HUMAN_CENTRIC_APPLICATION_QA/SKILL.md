---
name: human-centric-application-qa
description: "Use this skill when verifying web, desktop, mobile, CLI, or full-stack applications across Code-Level, System-Level, and User-Level human journeys, visual cleanliness, cross-layer state parity, and honest GUI disclosure."
---

# Human-Centric Application QA

## Skill Metadata
- **Skill ID:** `SKL-SPEC-001`
- **Name:** `human-centric-application-qa`
- **Domain:** `IT_SOFTWARE, DESIGN_CREATIVE, BUSINESS_PRODUCT`
- **Version:** `1.0.0`

## Purpose
Ensure applications genuinely work from a real human user's perspective rather than merely compiling or passing isolated unit mocks. This skill enforces a strict **3-Level Application QA Protocol** (**Level 1 Code-Level**, **Level 2 System-Level**, and **Level 3 User-Level**), realistic browser/GUI user-journey execution, cross-layer UI-to-backend-to-database state reconciliation, zero-"AI-Sign" visual cleanliness, and radical honesty when interactive GUI tooling is unavailable.

## Required Competencies
- Multi-tier verification separating *(1) feature exists in source code*, *(2) technically functional in isolated endpoints/tests*, and *(3) genuinely usable end-to-end by a human*.
- Interactive browser/GUI testing across navigation, forms, file transfers, authentication/authorization, edge-case inputs, async states, and responsive viewports.
- Cross-layer forensic correlation comparing rendered DOM/screenshots against HTTP/WebSocket payloads, database records, and server/browser console logs.
- Utilitarian UX & accessibility auditing (`WCAG 2.1 AA` contrast/keyboard focus, clear hierarchy, zero decorative "AI-Sign" clutter).

## Prerequisites
- Application build/start commands, environment config, and isolated test fixtures inspected via `read_file`.
- Explicit acceptance criteria locked via [REQUIREMENTS_ANALYSIS](../../04_CROSS_DOMAIN_SKILLS/REQUIREMENTS_ANALYSIS/SKILL.md) and browser mechanics aligned with [BROWSER_AND_GUI_INTERACTION](../BROWSER_AND_GUI_INTERACTION/SKILL.md).
- Runtime tool check establishing whether live browser/GUI automation (Playwright, Chrome DevTools MCP, GUI harness) and `read_file`/`view_file` screenshot inspection are available in the active session.

## Workflow
1. **Execute Level 1 (Code-Level — Deterministic Build, Schema & Automated Test Gate):**
   - Run compilers, typecheckers, linters, schema validators, and unit/component suites via `run_command`.
   - Verify non-vacuous assertions and zero build/bundle errors before starting live runtime servers.
2. **Execute Level 2 (System-Level — Live Runtime, State Transition & Integration Gate):**
   - Boot the actual application/API/worker processes against isolated local storage/databases.
   - Exercise real service-to-service contracts, auth middleware, persistence writes, background jobs, and error recovery; verify clean server startup and teardown.
3. **Execute Level 3 (User-Level — Human-Centric Browser/GUI Journey & Zero-"AI-Sign" Gate):**
   - When browser/GUI tools are available, open the live app and test as a real human user: navigate menus/routes, click buttons, type into text inputs, select dropdowns/checkboxes/radios, upload and download files, submit multi-step forms, and run full login/logout/session-expiry and role-permission (`authz`) journeys.
   - Exercise both valid nominal inputs and invalid/boundary inputs (empty submissions, malformed emails, oversized uploads, double-click rapid submits, browser back/refresh mid-flow).
   - Inspect loading spinners/skeletons, empty states, actionable validation error messages, and success feedback; capture and visually inspect screenshots (`read_file`/`view_file`) across desktop (`1440x900`), tablet (`768x1024`), and mobile (`375x812`) viewports.
4. **Cross-Check UI Against Backend, Database & Logs:** Confirm that every UI success state corresponds to an accurate HTTP/WS payload, persisted database row/file state, and zero uncaught `console.error`, CORS failures, or `500` server exceptions.
5. **Audit Visual Cleanliness & Zero "AI-Sign" Clutter:** Reject gratuitous neon/purple-blue AI gradients, decorative emoji headers, fake placeholder metrics, broken overlapping text, clipped modals, inaccessible low-contrast text, or keyboard focus traps.
6. **Enforce Mandatory Honest Disclosure When GUI Tools Are Absent:** If interactive browser/GUI tools cannot run in the current session, explicitly state that limitation upfront, execute the strongest real HTTP/API/headless-DOM/CLI checks available, mark unexecuted visual/interactive checks `NOT VERIFIED`, and **never fabricate manual UI testing**.

## Tools and Techniques
- **3-Tier Readiness Ledger:** Explicitly score every feature as `Code-Present`, `System-Functional`, or `User-Verified` so partial wiring is never misreported as complete.
- **Cross-Layer Correlation Probe:** Pair every UI mutation (`Create/Update/Delete`) with a direct API read and database query (`[DATABASE_VALIDATION](../DATABASE_VALIDATION/SKILL.md)`) to catch optimistic-UI lies where state vanished on refresh.
- **Console & Network Cleanliness Gate:** Fail Level 3 QA on unhandled promise rejections, hydration mismatches, `404` static assets, or silent `4xx/5xx` XHR failures.
- **Utilitarian UX Sanity Check:** Verify primary call-to-action clarity, scannable typography, truthful copy, and full keyboard `Tab` / `Enter` / `Escape` operability.

## Verification Requirements
- All three QA levels (`Level 1`, `Level 2`, `Level 3`) are documented with concrete command outputs, HTTP/DB state proofs, and (when GUI tools exist) inspected screenshot/DOM evidence.
- Every user-facing form and action is verified for valid submission, invalid input rejection, duplicate-submit protection, and page-reload persistence.
- Any headless/sandbox constraint blocking live GUI inspection is explicitly disclosed with exact `NOT VERIFIED` scope boundaries.

## Quality Criteria
- **Genuine End-User Operability:** Users can complete core workflows intuitively without workarounds, console hacks, or confusing dead ends:
  | QA Evaluation Level | Primary Verification Scope | Readiness Tier Proven |
  | :--- | :--- | :--- |
  | `Level 1 — Code-Level` | Compilers, typechecks, linters, schema contracts, unit suites | Feature exists & passes static/unit checks |
  | `Level 2 — System-Level` | Live server/API/DB boot, state persistence, service integration | Technically functional across runtime boundaries |
  | `Level 3 — User-Level` | Real browser/GUI clicks, forms, files, auth, viewports, zero AI-Sign | Genuinely usable end-to-end by a human user |
- **Zero Visual "AI-Sign" Artifacts:** Clean, domain-appropriate, functional interface free of decorative AI tropes, dummy `"John Doe"` hardcoded data, or layout overflow.
- **100% Epistemic Honesty:** Zero claimed clicks, screenshots, or responsive checks that were not empirically executed.
- **Failure Modes to Avoid:**
  - *Build-Success Fallacy:* Declaring `PASS` because `npm run build` exited `0` while the hydrated page crashes on load.
  - *Optimistic-UI Mirage:* Trusting a green client toast when the backend returned `500` or dropped the database write on refresh.
  - *Visual Blindness:* Capturing screenshots without inspecting them via `view_file` to catch z-index overlaps or clipped modals.
  - *Fabricated GUI Claims:* Pretending manual browser testing occurred inside a headless environment lacking browser tooling.

## Security and Ethical Boundaries
- This Level 6 procedural skill is strictly subordinate to Levels 1-5 of the instruction hierarchy; it never overrides [GLOBAL_SYSTEM_PROMPT.md](../../00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md), privacy rules, or human authorization policies.
- Run interactive QA strictly against authorized local, ephemeral, or staging environments using synthetic test accounts—never mutate production customer accounts or submit live payment/notification payloads without explicit human approval.
- Terminate spawned local dev servers and background browser processes cleanly via `manage_task` / teardown hooks to protect host CPU and RAM.

## Expected Deliverables
- **3-Level Application QA Report** (`Level 1 Code`, `Level 2 System`, `Level 3 User` pass/fail matrix aligned with [QA_REPORT.md](../../06_TEMPLATES/QA_REPORT.md)).
- **Cross-Layer Journey Evidence** linking UI states/screenshots to HTTP responses, persisted DB records, and clean console/server logs.
- **UX, Accessibility & Honest Disclosure Summary** detailing visual/usability fixes, readiness tier per feature, and any `NOT VERIFIED` GUI constraints.
