---
name: api-testing
description: "Use this skill when validating REST, GraphQL, gRPC, or WebSocket APIs for contract conformance, authentication and object-level authorization, idempotency, error handling, concurrency safety, and persisted state integrity."
---

# API Testing

## Skill Metadata
- **Skill ID:** `SKL-SPEC-003`
- **Name:** `api-testing`
- **Domain:** `IT_SOFTWARE, CYBERSECURITY`
- **Version:** `1.0.0`

## Purpose
Rigorously validate programmatic service interfaces (`REST`, `GraphQL`, `gRPC`, `WebSocket`, `Webhook`) beyond surface `HTTP 200` checks. This skill verifies strict request/response schema conformance, authentication and object/function-level authorization (`BOLA`/`IDOR`/`BFLA`), idempotency under retries, boundary/malformed payload rejection, concurrency race resistance, error-envelope hygiene, and underlying database/queue side effects.

## Required Competencies
- Interface contract verification (`OpenAPI 3.x`, `JSON Schema`, `Protobuf`, `GraphQL SDL`) including backward-compatibility breaking-change detection.
- Protocol semantics: HTTP method safety/idempotency (`GET`, `PUT`, `DELETE`, `POST + Idempotency-Key`), status code accuracy (`200/201/202/204/400/401/403/404/409/422/429`), caching headers, and content negotiation.
- Authorization matrix testing across unauthenticated callers, expired/tampered tokens, horizontal cross-tenant access (`BOLA`), and vertical privilege escalation (`BFLA`).
- Stateful lifecycle & concurrency testing (`Create -> Read -> Update -> Conflict/Retry -> Delete -> Confirm 404`) paired with persistence verification.

## Prerequisites
- Locked API contract (`OpenAPI`, schema definitions, or `SA` interface specification) and service source/routes inspected via `read_file`.
- Isolated local or staging service instance (or ASGI/WSGI/HTTP in-process test harness) runnable via `run_command`.
- Synthetic multi-role test fixtures (e.g., `Tenant_A_User`, `Tenant_B_User`, `ReadOnly_User`, `Admin_User`) for authorization isolation checks.

## Workflow
1. **Map Endpoint Contract & Invariants:** Extract every route/operation, HTTP verb, auth requirement, input field constraint, response schema, status code set, and side-effect invariant before writing assertions.
2. **Verify Positive Lifecycle & Persistence Parity:** Execute full stateful CRUD/workflow sequences; assert exact response headers (`Content-Type`, `Location`, `ETag`), schema types, field values, AND verify via subsequent `GET` or [DATABASE_VALIDATION](../DATABASE_VALIDATION/SKILL.md) that state actually persisted accurately.
3. **Execute Authentication & Authorization Matrix (`AuthN` / `AuthZ`):** Test every protected operation with missing credentials (`401`), expired/invalid signatures (`401`), insufficient role permissions (`403`), and cross-tenant object IDs (`403`/`404` preventing `BOLA`/`IDOR` leakage).
4. **Probe Schema Boundaries & Malformed Inputs:** Send missing required fields, wrong JSON types (`string` for `int`, `null`, arrays, deeply nested objects), unknown extra fields (mass-assignment check), oversized payloads (`413`), SQL/NoSQL metacharacters, and invalid pagination cursors (`limit=-1`, `limit=100000`).
5. **Test Idempotency, Concurrency & Rate Limits:** Replay identical mutating requests with the same `Idempotency-Key` and fire concurrent conflicting updates (`If-Match` / optimistic locking) to confirm zero duplicate charges/records or lost updates.
6. **Audit Error Envelopes & Information Leakage:** Confirm `4xx/5xx` responses follow a consistent machine-readable error schema (`code`, `message`, `request_id`) and never leak raw SQL queries, stack traces, file paths, or environment secrets.

## Tools and Techniques
- **Contract-Driven Test Harness:** Use deterministic test runners (`pytest` + `httpx`/`schemathesis`, `supertest`/`vitest`, `go test httptest`, `grpcurl`) via `run_command` asserting both status code AND full payload schema.
- **`BOLA` / Mass-Assignment Probe:** Attempt injecting privileged fields (`role: "admin"`, `balance: 99999`, `tenant_id: "other"`) in `POST`/`PATCH` payloads and verify strict server-side allowlisting rejects or ignores them.
- **Parallel Race Burst:** Dispatch `10-20` simultaneous async requests against inventory/balance/uniqueness endpoints to expose missing database transactions or row locks.
- **Consumer-Driven Backward-Compatibility Check:** Verify optional/nullable field additions never break existing strict client deserializers.

## Verification Requirements
- Zero endpoints verified solely by status code (`assert resp.status_code == 200` without body and state assertions fails QA).
- Every mutating endpoint has explicit positive, validation-failure (`400/422`), unauthorized (`401/403`), not-found (`404`), and idempotency/conflict (`409`) coverage.
- Test suite runs deterministically in isolation with repeatable fixture setup/teardown and `0` live external network dependencies unless explicitly mocked or sandboxed.

## Quality Criteria
- **Strict Protocol & Schema Fidelity:** Status codes, headers, pagination cursors, timestamps (`ISO-8601 UTC`), and numeric precisions (string-encoded decimals for currency) match locked contracts 100%:
  | Test Dimension | Target Probe | Required Server Behavior |
  | :--- | :--- | :--- |
  | `AuthN` (Identity) | Missing, expired, `alg:none`, or tampered signature | `HTTP 401` + `WWW-Authenticate`; zero state read/write |
  | `AuthZ` (`BOLA` / `BFLA`) | Valid token accessing Tenant B ID or admin endpoint | `HTTP 403` or `404`; zero existence/metadata leakage |
  | Schema & Bounds | Wrong types, extra admin fields, negative limits | `HTTP 400/422` structured field errors; zero `500` crash |
  | Idempotency & Race | Duplicate `Idempotency-Key` or `20` parallel writes | Exact single mutation + replayed response or `409` lock |
- **Zero Cross-Tenant Leakage:** Horizontal and vertical authorization checks pass across both single-item and list/search/GraphQL-nested resolvers.
- **Clean Error Hygiene:** Zero unhandled `500` crashes on arbitrary malformed client input; malformed client input always yields `4xx` structured errors.
- **Failure Modes to Avoid:**
  - *Status-Only Assertions:* Checking `status == 200` while ignoring broken JSON schemas or unpersisted database writes.
  - *Middleware Bypass in Tests:* Calling controller functions directly in unit tests while skipping real auth/validation middleware.
  - *`HTTP 200` Error Masking:* Returning `200 OK` with `{ "success": false }` envelopes on REST failures, breaking HTTP caches and proxies.
  - *Nested Resolver Blindspot:* Securing top-level `/orders/:id` while leaving nested `/users/me?include=all_tenant_orders` wide open.

## Security and Ethical Boundaries
- This Level 6 procedural skill is strictly subordinate to Levels 1-5 of the instruction hierarchy; it never overrides [SECURITY_AND_PRIVACY.md](../../00_GLOBAL_CONSTITUTION/SECURITY_AND_PRIVACY.md) or authorized testing scope.
- Never send fuzzing bursts, authorization probes, or mutating payloads against unapproved third-party APIs or live production customer tenants.
- Use ephemeral test JWTs/keys generated at test runtime; never hardcode static production bearer tokens in test repositories.

## Expected Deliverables
- **Automated API Contract & Security Test Suite** covering lifecycle, schema boundaries, `AuthN`/`AuthZ`, idempotency, and concurrency.
- **Endpoint Coverage & Contract Conformance Matrix** mapping routes/operations to verified status codes and invariants.
- **API Defect & Breaking-Change Report** documenting reproducible `curl`/test payloads, observed vs. expected responses, and remediation fixes.
