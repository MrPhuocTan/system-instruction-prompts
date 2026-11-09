# Backend Engineer Quality Checklist (`BACKEND_ENGINEER`)

- **Role ID:** `ROLE-IT-002`
- **Prompt Reference:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)
- **Domain Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md)

---

## 1. Pre-Handoff Verification Checklist

### 1.1 Contract, Authz & Domain Correctness
- [ ] **Contract Fidelity:** Endpoint paths, HTTP methods/RPC signatures, status codes, headers, pagination cursors, and error envelopes match the locked SA specification byte-for-byte.
- [ ] **Input Validation & Fail-Closed Authz:** Every handler validates request schemas at ingress and enforces both authentication (`401`) and object/tenant-level authorization (`403`) preventing BOLA/IDOR.
- [ ] **Atomicity & Idempotency:** Multi-step state mutations execute inside explicit database transactions or outbox boundaries; retriable write endpoints handle duplicate requests idempotently without double side effects.
- [ ] **Typecheck, Lint & Build Cleanliness:** Compiler, static typechecker, and linter exit with code `0` via `run_command` with zero suppressed safety rules or unhandled promise/error paths.

### 1.2 Persistence, Performance & Automated Testing
- [ ] **Bounded Timeouts & Pagination:** Every outbound HTTP/RPC call, DB query, stream consumer, and list endpoint enforces explicit timeouts, connection cleanup, and maximum page-size ceilings.
- [ ] **Zero N+1 & Safe Query Construction:** All persistence queries use parameterized bindings (zero string-interpolated SQL/NoSQL) and avoid N+1 query amplification inside loops.
- [ ] **Real Integration Test Coverage:** Automated tests verify happy paths, boundary values, malformed inputs, auth rejections, concurrency conflicts (`409`), and actual database state persistence.

### 1.3 Security, Telemetry & Runtime Hygiene
- [ ] **Secret & Log Hygiene:** Configuration loads exclusively from environment/secret providers; structured logs include trace/request IDs and redact tokens, passwords, keys, and PII.
- [ ] **Ephemeral Process Cleanup:** Any local test server or worker started during verification via `run_command` / `manage_task` has been cleanly terminated with zero orphaned background listeners.
- [ ] **Exclusive Write-Lock Compliance:** File audit confirms edits are strictly confined to owned backend paths with zero unapproved changes to shared contracts or sibling workstreams.

---

## 2. Required Handoff Evidence & Gate Classification

1. Exact test, typecheck, and lint commands executed via `run_command` with observed pass counts and exit codes (`PASS` / `FAILED`).
2. Sample verified request/response and persisted-state verification outputs for both valid and rejected (`4xx`) calls.
3. Explicit `PARTIAL` or `NOT VERIFIED` disclosure for any unavailable external third-party dependencies mocked during testing.
