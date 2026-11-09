# Frontend Engineer Quality Checklist (`FRONTEND_ENGINEER`)

- **Role ID:** `ROLE-IT-003`
- **Prompt Reference:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)
- **Domain Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md)

---

## 1. Pre-Handoff Verification Checklist

### 1.1 UX States, Accessibility & Utilitarian Craft
- [ ] **Complete UI State Coverage:** Every asynchronous screen and widget explicitly renders `loading`, `empty`, `validation-error`, `network-error` (with recovery action), and `success` states without raw stack traces or blank screens.
- [ ] **Zero Decorative "AI Sign" Clutter:** Interface uses clean utilitarian hierarchy, consistent spacing, and purposeful typography with zero decorative emojis, gratuitous neon gradients, fake metrics, or dead placeholder buttons.
- [ ] **WCAG 2.2 AA & Keyboard Accessibility:** All interactive elements use semantic `<button>`/`<a>`/`<input>` tags with programmatic labels, visible `:focus-visible` rings, logical Tab/Escape navigation, and `>= 4.5:1` text contrast.
- [ ] **Responsive Layout Integrity:** Layouts reflow cleanly across mobile (`375px`), tablet (`768px`), and desktop (`1440px`) breakpoints without horizontal scroll clipping or overlapping controls.

### 1.2 State Synchronization, Security & Build Quality
- [ ] **End-to-End API Wiring & Reload Persistence:** Interactive controls mutate/query real backend endpoints per locked SA contracts, guard against duplicate in-flight form submissions, and preserve expected state across page reload.
- [ ] **Race-Condition & Memory Hygiene:** Outbound requests cancel cleanly on unmount/re-query (`AbortController`), event listeners/timers are disposed, and derived values avoid redundant effect loops.
- [ ] **Client Bundle & Security Safety:** Production build succeeds (`0` type/lint/bundler errors), zero server secrets appear in client env vars, and untrusted strings are safely escaped against XSS.
- [ ] **Console & Network Cleanliness:** Zero uncaught runtime exceptions, React/Vue hydration/key warnings, or unexpected `4xx`/`5xx` waterfall loops during component/browser execution.

### 1.3 Runtime Honesty & Write-Lock Compliance
- [ ] **Honest Browser Verification Disclosure:** Live GUI/browser journey results include real observed evidence, or tool unavailability is explicitly disclosed as `PARTIAL` / `NOT VERIFIED` alongside automated DOM test outputs.
- [ ] **Exclusive Write-Lock & Dev-Server Cleanup:** Modified files stay strictly inside owned frontend paths and any background dev server started via `manage_task` has been terminated.

---

## 2. Required Handoff Evidence & Gate Classification

1. Typecheck, lint, automated component/DOM test, and production bundle build outputs (including bundle size summary) via `run_command`.
2. Real browser/GUI walkthrough findings (`PASS`), or explicit headless/DOM fallback disclosure (`PARTIAL` / `NOT VERIFIED`) if GUI tooling is unavailable.
3. List of verified user journeys (valid, invalid, empty, error) and any contract discrepancies escalated to `SA` + `PM`.
