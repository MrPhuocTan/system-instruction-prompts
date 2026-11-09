# End-to-End Walkthrough: Level 1 / Level 2 Bugfix & Feature Task (`MODERATE_TASK.md`)

> **Walkthrough Governance:** Demonstrates adaptive escalation from **Level 1** to **Level 2**, focused specialist execution, and empirical runtime verification (`Tool Success != Task Success`) per [TASK_COMPLEXITY_ROUTER.md](../00_GLOBAL_CONSTITUTION/TASK_COMPLEXITY_ROUTER.md) and [INDEPENDENT_VERIFICATION.md](../00_GLOBAL_CONSTITUTION/INDEPENDENT_VERIFICATION.md).

---

## 1. Realistic User Scenario
**User Prompt:**
> "Customers see duplicate rows at page boundaries on `GET /v1/invoices?limit=25&cursor=...` when two invoices share the same `created_at` timestamp, and retries on `POST /v1/invoices` occasionally create duplicate invoices. Fix both issues cleanly with tests."

---

## 2. Complexity Routing (`Level 1 -> Level 2` Assessment)
1. **Initial Triage:** Fixing a single SQL cursor comparator in `src/api/invoices.py` alone would qualify as **Level 1** (single-file localized fix). However, adding stateful `Idempotency-Key` enforcement on `POST /v1/invoices` spans API middleware (`src/middleware/idempotency.py`), PostgreSQL unique constraints (`db/migrations/007_invoice_idempotency.sql`), route handlers (`src/api/invoices.py`), and concurrency integration tests (`tests/test_invoices_api.py`).
2. **Locked Classification (`Level 2 — Multi-Step Single-Domain Engineering Task`):**
   - **Active Domain:** `IT_SOFTWARE` ([DOMAIN_SYSTEM_PROMPT.md](../03_DOMAINS/IT_SOFTWARE/DOMAIN_SYSTEM_PROMPT.md), [QUALITY_GATES.md](../03_DOMAINS/IT_SOFTWARE/QUALITY_GATES.md))
   - **Governance Footprint:** `PM` locks acceptance criteria and `SA` locks the composite cursor + idempotency schema contract in target workspace `configs/agent_communicate.md` (derived from [AGENT_COMMUNICATE.md](../06_TEMPLATES/AGENT_COMMUNICATE.md)).
   - **Agent Allocation:** Because all 4 touched files sit in one tightly coupled backend slice, `PM + SA` allocate **1** specialist worker bound to [BACKEND_ENGINEER](../03_DOMAINS/IT_SOFTWARE/ROLES/BACKEND_ENGINEER/SYSTEM_PROMPT.md) (with compatible DB migration scope) plus **1** independent [QUALITY_REVIEWER](../02_CORE_ROLES/QUALITY_REVIEWER/SYSTEM_PROMPT.md) check — avoiding unnecessary 4-agent fragmentation.
   - **Loaded Skills:** [COGNITIVE_EXECUTION](../04_CROSS_DOMAIN_SKILLS/COGNITIVE_EXECUTION/SKILL.md), [API_TESTING](../05_SPECIALIZED_SKILLS/API_TESTING/SKILL.md), [DATABASE_VALIDATION](../05_SPECIALIZED_SKILLS/DATABASE_VALIDATION/SKILL.md).

---

## 3. SA Locked Technical Contract
- **Composite Keyset Cursor:** Base64URL-encoded JSON `{"created_at": "<ISO-8601-micros>", "id": "<uuidv7>"}` paired with deterministic SQL tuple comparison `(created_at, id) < (:cursor_ts, :cursor_id) ORDER BY created_at DESC, id DESC LIMIT :limit`.
- **Idempotency Contract (`POST /v1/invoices`):**
  - Require `Idempotency-Key` header (`1..128` ASCII chars); store `(tenant_id, idempotency_key, request_sha256, status_code, response_body, expires_at)` with a `UNIQUE (tenant_id, idempotency_key)` constraint.
  - Concurrent in-flight duplicate key returns `HTTP 409 Conflict` (`IDEMPOTENCY_REQUEST_IN_PROGRESS`); replayed key with mutated payload hash returns `HTTP 422 Unprocessable Entity` (`IDEMPOTENCY_PAYLOAD_MISMATCH`); exact retry returns cached `HTTP 201 Created` payload without inserting a second invoice row.

---

## 4. Specialist Cognitive Execution & Implementation
Following `Understand -> Reason -> Plan -> Execute -> Observe -> Independently Verify`:
1. **Reproduce Bugs First:** Worker writes a failing test in `tests/test_invoices_api.py` inserting `60` invoices where `10` rows share identical `created_at = '2026-11-08T10:00:00Z'`, reproducing `3` duplicated invoice IDs and `3` skipped IDs across 3 pages. Second test fires `8` concurrent `asyncio.gather` `POST /v1/invoices` calls with identical `Idempotency-Key`, reproducing `3` duplicate DB rows.
2. **Scoped Implementation (Within Exclusive Write-Lock):**
   - `db/migrations/007_invoice_idempotency.sql`: Adds composite index `idx_invoices_tenant_created_id ON invoices (tenant_id, created_at DESC, id DESC)` and `idempotency_records` table.
   - `src/middleware/idempotency.py`: Uses `INSERT ... ON CONFLICT (tenant_id, idempotency_key) DO NOTHING RETURNING ...` inside a short transaction to eliminate check-then-insert TOCTOU race conditions.
   - `src/api/invoices.py`: Implements keyset tuple pagination and binds idempotency middleware:
     ```sql
     SELECT id, tenant_id, amount_cents, currency, created_at
     FROM invoices
     WHERE tenant_id = :tenant_id
       AND (:cursor_ts IS NULL OR (created_at, id) < (:cursor_ts, :cursor_id))
     ORDER BY created_at DESC, id DESC
     LIMIT :limit;
     ```

---

## 5. Target Workspace `AGENT_COMMUNICATE.md` Write-Lock Excerpt
| Exclusive Owned Path (`Write-Lock`) | Lock Holder | Lock State | Post-Run Diff Check |
| :--- | :--- | :--- | :--- |
| `db/migrations/007_invoice_idempotency.sql` | `worker-backend-01` | `RELEASED` | Verified (`+28` lines) |
| `src/middleware/idempotency.py` | `worker-backend-01` | `RELEASED` | Verified (`+74` lines) |
| `src/api/invoices.py` | `worker-backend-01` | `RELEASED` | Verified (`+31/-14` lines) |
| `tests/test_invoices_api.py` | `worker-backend-01` | `RELEASED` | Verified (`+92` lines) |

---

## 6. Independent Verification Evidence (`Tool Success != Task Success`)
| Check | Command / Stimulus Executed | Observed Empirical Result | Status |
| :--- | :--- | :--- | :---: |
| **Static & Types** | `ruff check src tests && mypy --strict src` | `0` lint/type errors across modified modules | `PASS` |
| **Keyset Pagination** | `pytest tests/test_invoices_api.py -k pagination` | `60` rows paged in `limit=25` chunks -> `60` unique IDs, `0` duplicates, `0` drops | `PASS` |
| **Concurrency Race** | `pytest tests/test_invoices_api.py -k concurrent_idempotency` | `8` simultaneous POSTs -> `1` invoice row in PostgreSQL (`SELECT count(*) = 1`); payload-tampered retry -> `HTTP 422` | `PASS` |
| **Downstream Failure Rollback** | Simulated DB serialization error mid-handler | Idempotency lock row deleted cleanly on rollback so legitimate client retry succeeds | `PASS` |
| **Query Plan Audit** | `EXPLAIN (ANALYZE, BUFFERS) SELECT ...` | Index Scan using `idx_invoices_tenant_created_id` (`0` Seq Scan / Sort) | `PASS` |

---

## 7. Proportional Dual Gate Signoff & Residual Assumptions
- **`SA_GATE` (`PASS`):** Verified atomic `ON CONFLICT` locking, composite index usage, rollback cleanup on unhandled 5xx faults, and zero changes outside the 4 locked files ([TECHNICAL_REVIEW.md](../06_TEMPLATES/TECHNICAL_REVIEW.md)).
- **`PM_GATE` (`PASS`):** Confirmed deterministic pagination, clear `409`/`422` client error payloads, and clean handoff delivery ([FINAL_DELIVERY.md](../06_TEMPLATES/FINAL_DELIVERY.md)).
- **Documented Operational Assumption:** `idempotency_records.expires_at` defaults to `24 hours`; periodic TTL pruning via existing `pg_cron` job `prune_expired_idempotency` is logged as a deployment verification step.
