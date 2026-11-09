# IT & Software Engineering Quality Gates (`IT_SOFTWARE`)

- **Domain ID:** `DOM-01-IT_SOFTWARE`
- **Gate Authority:** Enforced by Domain Workers prior to handoff and audited by `SA` (`SA_GATE`) and `PM` (`PM_GATE`) per [REVIEW_AND_SIGNOFF.md](../../01_ORCHESTRATION/REVIEW_AND_SIGNOFF.md) and [INDEPENDENT_VERIFICATION.md](../../00_GLOBAL_CONSTITUTION/INDEPENDENT_VERIFICATION.md)
- **Domain Reference:** [DOMAIN_INDEX.md](./DOMAIN_INDEX.md) | [DOMAIN_SYSTEM_PROMPT.md](./DOMAIN_SYSTEM_PROMPT.md)

---

## 1. Gate Evaluation Protocol & Status Semantics

Every `IT_SOFTWARE` deliverable is evaluated against the eight testable gates below before delivery. Each gate receives an explicit status:
- `PASS`: Empirically verified with reproducible command, log, or test output.
- `PARTIAL`: Core subset verified locally; residual runtime gap documented transparently.
- `BLOCKED`: Halted by an external dependency, contract conflict, or pending human authorization.
- `FAILED`: Reproducible defect, contract mismatch, or security violation observed.
- `NOT VERIFIED`: Workspace lacks the required runtime daemon, cluster, or GUI tooling.

Claiming `PASS` without reproducible execution evidence is an automatic gate failure.

| Gate ID | Gate Category | Mandatory Verification Evidence | Pass Criteria (`PASS`) | Automatic Fail Triggers (`FAILED`) |
| :--- | :--- | :--- | :--- | :--- |
| `QG-IT-01` | **Architecture & Modularity** | Dependency graph inspection, ADR / contract diff against SA lock | Unidirectional module imports; zero edits outside Exclusive Write-Lock; interfaces match locked SA specs | Cyclic module dependencies; business logic embedded in transport/UI handlers; unauthorized cross-stream file edits |
| `QG-IT-02` | **Code Correctness & Static Analysis** | Compiler, typechecker, and linter exit codes via `run_command` | `0` syntax/compilation errors, `0` type errors, `0` high-severity lint defects; explicit error handling on all fallible calls | Suppressed type assertions hiding real mismatches (`any`/`ts-ignore` abuse), swallowed exceptions, race conditions, or unfinished stub code |
| `QG-IT-03` | **Unit & Integration Test Suite** | Full test runner output covering happy, boundary, and failure paths | `100%` passing deterministic tests; zero network-flaky sleeps; integration tests exercise real serialization and storage constraints | Tests passing only via tautological mocks, skipped/commented-out failing tests, or zero negative-path assertions |
| `QG-IT-04` | **API & Schema Contracts** | OpenAPI/Protobuf/GraphQL schema validation + live request/response checks | Status codes, headers, pagination, idempotency, and error payloads match spec; DB migrations run cleanly forward and backward | Undocumented breaking field changes, `HTTP 200` returning error payloads, or irreversible destructive schema migrations without approval |
| `QG-IT-05` | **Security & Secret Hygiene** | Secret scan, dependency audit, authn/authz boundary test cases | Zero hardcoded secrets/tokens/PII in code or logs; parameterized queries enforced; unauthorized/cross-tenant requests return `401`/`403` | Plaintext credentials in repo/logs, SQL/command/XSS injection vectors, missing object-level authorization checks, or unflagged critical CVEs |
| `QG-IT-06` | **Performance & Resource Bounds** | Query `EXPLAIN` plans, benchmark p95/p99 metrics, memory/timeout checks | Bounded query plans with appropriate indexes; explicit network/DB timeouts; zero unbounded loops, N+1 queries, or memory leaks | Unindexed full-table scans on hot paths, unbounded in-memory buffering of large payloads, or host disk/CPU exhaustion during verification |
| `QG-IT-07` | **Deployment & Observability Readiness** | Container/artifact build check, config validation, health/log inspection | Reproducible artifact build; externalized env configuration; health/readiness endpoints operational; structured logs include trace context | Environment-hardcoded URLs/ports, silent crash-loop startup on missing config, or opaque unstructured error logging |
| `QG-IT-08` | **End-to-End Human-Centric Journey** | Execution of [HUMAN_CENTRIC_APPLICATION_QA/SKILL.md](../../05_SPECIALIZED_SKILLS/HUMAN_CENTRIC_APPLICATION_QA/SKILL.md) Levels 1–3 | Verified user/CLI/API journey across valid, invalid, empty, loading, and error states; clean utilitarian UI free of decorative "AI Sign" clutter | Broken end-to-end state persistence, dead UI controls, raw stack traces exposed to users, or fabricated manual browser testing claims |

---

## 2. Proportional Gate Application by Task Complexity

1. **Level 1 (Scoped Single-Role Edit):**
   Apply `QG-IT-02`, `QG-IT-03`, and `QG-IT-05` at minimum, plus any gate directly touched by the modified surface (`QG-IT-08` for UI edits, `QG-IT-04` for endpoint/schema edits).
2. **Level 2 (Multi-Step Single-Domain Feature):**
   All applicable gates `QG-IT-01` through `QG-IT-08` require concrete command and runtime verification evidence recorded in `AGENT_COMMUNICATE.md` prior to `SA_GATE` and `PM_GATE`.
3. **Level 3–4 (Multi-Role / High-Assurance System):**
   Full 8-gate enforcement with independent `QA_ENGINEER` / `AUTOMATION_QA` verification, cross-workstream contract reconciliation, rollback dry-run evidence, and explicit human signoff before any production rollout or irreversible state mutation.

---

## 3. Honest Tool-Limitation Fallback Protocol

When a runtime environment lacks interactive browser tooling, Docker daemons, or target cloud credentials:
1. Mark the affected sub-check `PARTIAL` or `NOT VERIFIED` rather than `PASS`.
2. Execute the closest deterministic local substitute (headless DOM/component rendering, ASGI/WSGI/HTTP in-process test clients, SQLite/ephemeral local DB verification, or `terraform validate` / `helm template` static rendering).
3. Document exact verification commands for the user or downstream CI runner in the handoff report.

---

## 4. Escalation & Signoff Blocking Rules

- Any `FAILED` status on `QG-IT-01` through `QG-IT-08` blocks both `SA_GATE` and `PM_GATE` until remediated and independently re-verified.
- Any `SEV-1` security exposure (`QG-IT-05`) or unapproved destructive schema change (`QG-IT-04`) triggers immediate halt and escalation to `SA` and `PM`.
