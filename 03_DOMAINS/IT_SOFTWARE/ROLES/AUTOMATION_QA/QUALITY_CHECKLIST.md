# Automation QA Engineer Quality Checklist (`AUTOMATION_QA`)

- **Role ID:** `ROLE-IT-009`
- **Prompt Reference:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)
- **Domain Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md)

---

## 1. Pre-Handoff Verification Checklist

### 1.1 Determinism, Isolation & Selector Resilience
- [ ] **Zero Arbitrary Sleep Waits:** Test suite contains `0` hardcoded `sleep()` / `waitForTimeout()` delays, relying exclusively on deterministic readiness conditions, fake timers, or event assertions.
- [ ] **Hermetic State Isolation:** Every test initializes its own synthetic state (via factories/transactions/ephemeral DBs) and passes regardless of execution order or parallel worker count.
- [ ] **Repeat-Run Determinism:** Full test suite passed `100%` across consecutive/shuffled runs via `run_command` with `0` flaky retries or skipped assertions.
- [ ] **Accessible & Resilient Selectors:** UI/DOM tests query elements via accessible roles, labels, or explicit `data-testid` contracts rather than fragile CSS class chains or deep XPath indices.

### 1.2 Contract Depth & Non-Tautological Assertions
- [ ] **Real Boundary & Contract Assertions:** Integration and API suites assert status codes, response schemas, error envelopes (`400`/`401`/`403`/`404`/`409`/`422`), and persisted storage mutations without tautological mocks.
- [ ] **Non-Tautological Failure Verification:** Assertions check meaningful behavioral invariants (verified capable of failing when target logic breaks, `0` empty/assertion-free test bodies).
- [ ] **Outbound Side-Effect Blocking:** External third-party HTTP/SMTP/SMS/webhook endpoints are hermetically stubbed or blocked so test runs never leak traffic outside localhost.

### 1.3 Security, Teardown & Write-Lock Hygiene
- [ ] **Synthetic Secret & PII Hygiene:** Fixtures generate runtime dummy keys/tokens and synthetic records with `0` hardcoded real credentials or production PII.
- [ ] **Process, Temp-File & Disk Cleanup:** Teardown hooks close all DB pools, ephemeral servers, headless browsers, and temporary directories cleanly.
- [ ] **Exclusive Write-Lock & Fallback Honesty:** Edits stay strictly inside owned test/config paths, and any missing browser binary check is transparently reported as `PARTIAL` or `NOT VERIFIED`.

---

## 2. Required Handoff Evidence & Gate Classification

1. Exact test runner commands, execution duration, pass/fail/coverage counts, and repeat-run determinism output (`PASS` / `FAILED`).
2. Summary of newly automated layers (unit, contract/API, DB integration, E2E) and CI integration command.
3. Explicit `PARTIAL` or `NOT VERIFIED` disclosure of any runtime environment limitations (unavailable browser binaries or container daemons).
