# Fullstack Engineer Quality Checklist (`FULLSTACK_ENGINEER`)

- **Role ID:** `ROLE-IT-004`
- **Prompt Reference:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)
- **Domain Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md)

---

## 1. Pre-Handoff Verification Checklist

### 1.1 Client/Server Boundary & Authz Integrity
- [ ] **Strict Client/Server Boundary Isolation:** Server-only secrets, DB drivers, and signing keys are completely absent from client bundles (`server-only` guards verified on production build output).
- [ ] **Dual-Layer Validation & Server Authz:** Client forms provide accessible inline validation while server routes/actions independently enforce schema validation, authentication (`401`), and tenant/resource authorization (`403`).
- [ ] **Idempotency & Double-Submit Protection:** UI disables duplicate in-flight submissions AND backend handlers enforce idempotency/uniqueness constraints against concurrent retries.

### 1.2 End-to-End Persistence, SSR & UX Quality
- [ ] **Cross-Layer State Persistence:** End-to-end mutations verified across all three tiers—UI/client trigger, HTTP/RPC wire payload, and actual persisted database state—surviving full page reload.
- [ ] **SSR, Hydration & Timezone Determinism:** Server-rendered views hydrate with `0` console mismatch warnings and handle UTC-to-local timestamp formatting deterministically.
- [ ] **Complete UI State Matrix & Utilitarian UX:** Views cleanly render `loading`, `empty`, `validation-error`, `network-error`, and `success` states with WCAG 2.2 AA keyboard/contrast compliance and zero "AI Sign" clutter.
- [ ] **Migration & Query Safety:** Database changes include reversible forward/rollback steps, parameterized queries, and appropriate indexes without N+1 query loops.

### 1.3 Build, Runtime Hygiene & Write-Lock Compliance
- [ ] **Fullstack Build, Typecheck & Test Pass:** Unified typechecker, linter, backend integration tests, frontend component tests, and production build exit `0` via `run_command`.
- [ ] **Process & Log Hygiene:** Ephemeral dev servers/containers started via `manage_task` are terminated cleanly, and structured logs redact session cookies, tokens, and PII.
- [ ] **Exclusive Write-Lock & Honest QA Disclosure:** All edits remain inside assigned paths, and any unavailable live GUI/browser check is transparently marked `PARTIAL` or `NOT VERIFIED`.

---

## 2. Required Handoff Evidence & Gate Classification

1. Command outputs for fullstack typecheck, lint, migration check, automated test suite, and production build (`PASS` / `FAILED`).
2. Cross-layer verification trace demonstrating request payload, HTTP status, DB state query, and UI state behavior.
3. Explicit `PARTIAL` or `NOT VERIFIED` disclosure of environment/browser tool limitations and residual cross-stream touchpoints.
