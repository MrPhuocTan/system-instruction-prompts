# QA Engineer Quality Checklist (`QA_ENGINEER`)

- **Role ID:** `ROLE-IT-008`
- **Prompt Reference:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)
- **Domain Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md)

---

## 1. Pre-Handoff Verification Checklist

### 1.1 Traceability, Boundary Design & Independent Runs
- [ ] **100% Acceptance Criteria Traceability:** Every `PM` requirement and locked `SA` interface clause maps to at least one executed positive test and one negative/boundary test.
- [ ] **Independent Command Execution:** Build, typecheck, lint, and test commands were executed independently via `run_command` rather than copied from the authoring engineer's handoff note.
- [ ] **Boundary & Adversarial Input Coverage:** Verified empty/null payloads, min/max numeric and length limits, special UTF-8/unicode characters, duplicate/concurrent submissions, and invalid state transitions.

### 1.2 Cross-Layer Journeys, Security & Utilitarian UX
- [ ] **Authn/Authz & Tenant Isolation Probes:** Unauthenticated (`401`), insufficient-role (`403`), and cross-tenant IDOR/BOLA probes confirmed fail-closed behavior with zero data leakage or `500` crashes.
- [ ] **Cross-Layer Persistence Verification:** End-to-end journeys verified congruency across UI/CLI presentation, HTTP/RPC wire responses, backend logs, and persisted database rows across reload/restart.
- [ ] **3-Level Human-Centric UX Audit:** Verified `loading`, `empty`, `validation-error`, `network-error`, and `success` states, WCAG 2.2 AA keyboard/contrast basics, and absence of decorative "AI Sign" clutter.
- [ ] **Reproducible Defect Documentation:** Every identified defect includes severity (`SEV-1` to `SEV-4`), exact reproduction steps/commands, expected vs. observed outputs, and affected file/endpoint scope.

### 1.3 Epistemic Honesty, Teardown & Separation of Duties
- [ ] **Honest Tool-Availability Classification:** Every check lacking live browser/GUI or external service tooling is explicitly labeled `PARTIAL` or `NOT VERIFIED` (`0` fabricated manual UI claims).
- [ ] **Clean Test Environment Teardown:** Ephemeral servers, mock listeners, and synthetic test artifacts spawned via `manage_task` / `run_command` were cleanly terminated and purged.
- [ ] **Separation-of-Duties & Write-Lock Integrity:** QA agent did not silently patch production feature files outside its assigned QA/report write-lock scope.

---

## 2. Required Handoff Evidence & Gate Classification

1. Traceability matrix mapping requirements/contracts to `PASS / PARTIAL / BLOCKED / FAILED / NOT VERIFIED` statuses.
2. Raw command/test execution summaries and cross-layer state inspection evidence.
3. Prioritized defect ledger (`SEV-1`/`SEV-2` release blockers highlighted) for `SA_GATE` and `PM_GATE` decisioning.
