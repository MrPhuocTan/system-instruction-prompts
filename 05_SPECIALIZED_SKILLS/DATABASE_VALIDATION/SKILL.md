---
name: database-validation
description: "Use this skill when verifying database schemas, forward and rollback migrations, ACID transaction isolation, referential constraints, query execution plans, data backfills, and backup-restore integrity."
---

# Database Validation

## Skill Metadata
- **Skill ID:** `SKL-SPEC-004`
- **Name:** `database-validation`
- **Domain:** `IT_SOFTWARE, DATA_ANALYTICS`
- **Version:** `1.0.0`

## Purpose
Guarantee data durability, schema integrity, zero-downtime migration safety, transactional consistency, and query scalability across relational (`PostgreSQL`, `MySQL`, `SQLite`), document/key-value, and analytical data stores. This skill prevents silent data corruption, destructive table rewrites, production metadata locks, `N+1` query storms, and unrecoverable migrations.

## Required Competencies
- Relational and analytical data modeling: primary/surrogate keys, foreign keys, `UNIQUE`/`CHECK`/`NOT NULL` constraints, temporal/audit columns, and money/decimal precision (`NUMERIC` over `FLOAT`).
- Online zero-downtime schema migration engineering (expand-and-contract pattern, concurrent index creation, lock-timeout guards, forward + rollback idempotency).
- Transaction isolation & concurrency validation (`READ COMMITTED`, `REPEATABLE READ`, `SERIALIZABLE`, `SELECT ... FOR UPDATE`, optimistic version counters, deadlock avoidance).
- Physical execution-plan analysis (`EXPLAIN (ANALYZE, BUFFERS)`) covering index selectivity, join strategies, sort spills, and write amplification.

## Prerequisites
- Migration scripts, ORM models, DDL files, and data-access queries inspected via `read_file`.
- Ephemeral local database instance, containerized test DB, or embedded engine (`sqlite3`, `duckdb`, local `postgres`) accessible via `run_command`.
- Explicit human approval gate (`[HUMAN_APPROVAL_POLICY.md](../../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md)`) verified prior to touching any shared staging or production datastore.

## Workflow
1. **Audit Schema Invariants & Data Types:** Verify that domain invariants are enforced in the database layer (not solely in application code): `NOT NULL`, `FOREIGN KEY` cascade/restrict semantics, `CHECK` bounds, `UNIQUE` partial/composite indexes, timezone-aware timestamps (`TIMESTAMPTZ`), and exact `NUMERIC` currency types.
2. **Test Migration Lifecycle (`Up -> Seed -> Down -> Up`):** Run forward migration on a non-empty seeded fixture dataset, verify schema and existing rows survive intact, run rollback (`down`) migration cleanly, and re-apply forward migration to prove idempotency and reversibility.
3. **Screen for Locking & Zero-Downtime Hazards:** Inspect DDL statements for operations acquiring prolonged `ACCESS EXCLUSIVE` / table-rewrite locks on hot tables (e.g., non-concurrent index builds, adding `NOT NULL` with volatile defaults, column renames breaking live readers); enforce expand-migrate-contract sequencing and `lock_timeout`.
4. **Validate ACID Transactions & Concurrent Contention:** Simulate partial multi-step failures to confirm full atomic rollback (`0` orphaned partial records), and execute concurrent read-modify-write transactions to verify isolation prevents lost updates, double-spends, or constraint races.
5. **Analyze Query Plans (`EXPLAIN ANALYZE`):** Run critical read/write/pagination queries against realistic data volumes and distribution skew; verify composite index column ordering, eliminate unintended sequential scans and `OFFSET` deep-page blowups, and catch ORM `N+1` query loops via query-count assertions.
6. **Reconcile Data Backfills & Backup-Restore:** For data transformations or migrations, compare pre- and post-migration row counts, null counts, cryptographic/aggregate checksums (e.g., sum of balances per tenant), and verify backup dumps actually restore cleanly into a fresh schema.

## Tools and Techniques
- **`Up / Down / Up` Migration Harness:** Automated CLI/test check verifying schema diff parity (`pg_dump --schema-only` / ORM autogenerate diff = `0` drift between migrations and models).
- **Query-Count & `EXPLAIN` Guardrails:** Wrap integration tests with SQL statement counters (`assert query_count <= k` independent of list size `N`) and capture `EXPLAIN (ANALYZE, BUFFERS)` plans.
- **Expand-and-Contract Pattern:** Split breaking column changes into (1) add nullable column + dual-write, (2) batched throttled backfill + `NOT VALID` constraint + `VALIDATE CONSTRAINT`, (3) switch reads, (4) drop legacy column in a later release.
- **Row & Financial Checksum Reconciliation:** Reconcile source vs. target aggregates across partition keys before declaring any ETL or backfill complete.

## Verification Requirements
- Zero drift between committed migration history and application ORM/schema definitions.
- Every constraint (`FK`, `UNIQUE`, `CHECK`, `NOT NULL`) is tested with an explicit negative write proving the database rejects invalid state directly.
- Data backfills include deterministic row-count and domain-invariant reconciliation queries showing `0` unattributed drops or duplicates.

## Quality Criteria
- **Database-Enforced Truth:** Application bugs cannot persist negative balances, orphaned foreign keys, duplicate idempotency keys, or floating-point rounding drift:
  | Schema / Query Operation | Production Hazard | Safe Engineering Pattern |
  | :--- | :--- | :--- |
  | Index Creation on Large Table | Full write block during build | `CREATE INDEX CONCURRENTLY` + explicit `lock_timeout` |
  | Adding `NOT NULL` Column | Full table rewrite + exclusive lock | Add nullable -> batched backfill -> `CHECK NOT VALID` -> `VALIDATE` |
  | Deep List Pagination | `OFFSET 100000` scanning/discarding rows | Keyset cursor pagination `(created_at, id) < ($1, $2)` |
  | Concurrent Balance Update | Lost update / double-spend race | `SELECT ... FOR UPDATE` or atomic `UPDATE ... WHERE bal >= $1` |
- **Safe Online Rollout:** Migrations explicitly document lock levels, batch sizes, estimated runtime, and non-destructive rollback procedures.
- **Predictable Tail Query Latency:** Indexed access paths and keyset/cursor pagination scale cleanly beyond toy 10-row dev fixtures.
- **Failure Modes to Avoid:**
  - *Empty-Table Migration Illusion:* Passing `migrate up` on a `0`-row local DB when existing `NULL` or duplicate rows crash staging/prod.
  - *Monolithic Backfill Transactions:* Updating `5M` rows in one transaction, blowing WAL/undo logs and starving replication.
  - *Binary Float Currency:* Storing money in `REAL`/`DOUBLE PRECISION`, causing `$0.01` reconciliation drift across ledger sums.
  - *Untested Backup Assumption:* Assuming `pg_dump` or snapshot configs work without ever running a clean-schema restore check.

## Security and Ethical Boundaries
- This Level 6 procedural skill is strictly subordinate to Levels 1-5 of the instruction hierarchy; it never overrides [HUMAN_APPROVAL_POLICY.md](../../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md), least privilege, or privacy regulations.
- NEVER execute `DROP`, `TRUNCATE`, `DELETE` without `WHERE`, or destructive migrations against shared or production databases without verified point-in-time backup confirmation and explicit human authorization.
- Enforce parameterized queries (`$1`, `?` bind parameters) everywhere—never interpolate user strings into SQL—and never export unmasked production PII/PHI into local test fixtures.

## Expected Deliverables
- **Schema & Migration Verification Report** (`Up -> Seed -> Down -> Up` logs, lock-safety audit, and model-to-DDL parity confirmation).
- **Constraint, Concurrency & `EXPLAIN` Evidence** documenting negative constraint tests, isolation checks, and indexed query plans.
- **Backfill Reconciliation & Rollback Runbook** providing exact checksum queries, batching bounds, and recovery commands.
