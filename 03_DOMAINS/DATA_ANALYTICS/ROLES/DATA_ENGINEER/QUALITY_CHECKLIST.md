# Quality Checklist: Data Engineer (`ROLE-DATA-002`)

- **Role:** [`DATA_ENGINEER`](./SYSTEM_PROMPT.md)
- **Domain Gates:** [`QUALITY_GATES.md`](../../QUALITY_GATES.md)

---

## 1. Idempotency, Replayability & `CDC` Correctness
- [ ] Parameterized pipeline windows strictly by logical interval (`[window_start, window_end)`) with zero `datetime.now()` / `CURRENT_TIMESTAMP` coupling inside transformation logic.
- [ ] Passed automated `2x`-replay verification proving duplicate runs, out-of-order updates, and late-arriving records within lookback watermarks produce identical target row counts and control sums (`0` duplicates).
- [ ] Handled `CDC` sequence numbers (`LSN`/version) and hard-delete tombstones (`op = 'd'`) accurately; used cursor/keyset pagination instead of `OFFSET` on mutable sources.

## 2. Schema Evolution, `DLQ` & Fault Tolerance
- [ ] Enforced explicit input/output schema contracts (`PyArrow`/`Pydantic`/DDL) and routed corrupt/malformed records to an auditable Dead-Letter Queue (`DLQ`) without silent drops or batch crashes.
- [ ] Configured bounded retries with exponential backoff + jitter on transient network/rate-limit (`HTTP 429`/`5xx`) responses and enforced `Write-Audit-Publish` staging isolation before promotion.

## 3. Compute, Memory & Storage Hygiene
- [ ] Eliminated driver and host `OOM` hazards (zero unbounded `.collect()`/`.toPandas()` or full-payload RAM buffering; verified chunked/streaming execution).
- [ ] Verified predicate/projection pushdown, partition pruning, key-skew mitigation, and healthy output columnar file sizes (`Parquet`/`Iceberg`).

## 4. Security, SQL Safety & Host Protection
- [ ] Confirmed `100%` parameterized SQL/connector bindings (`0` SQL injection vectors) and zero hardcoded or logged credentials/`PII` in code, exceptions, or `DLQ` payloads.
- [ ] Verified upstream `GDPR`/`CCPA` deletion events propagate deterministically to target tables.
- [ ] Bounded local disk and RAM usage during test runs and gated any live production mutation behind explicit human approval.

## 5. Independent Verification & Handoff Completeness
- [ ] Executed automated `pytest` suite covering `2x` idempotent replay, out-of-order `CDC` `LSN` ordering, tombstone deletion, and poison-record `DLQ` quarantine.
- [ ] Verified failed mid-batch writes roll back or remain isolated in staging without exposing partial partitions to readers.
- [ ] Reconciled output staging row counts and control totals (`0` unexplained variance) for downstream [`ANALYTICS_ENGINEER`](../ANALYTICS_ENGINEER/SYSTEM_PROMPT.md) and [`DATA_QUALITY_ENGINEER`](../DATA_QUALITY_ENGINEER/SYSTEM_PROMPT.md) handoff.
- [ ] Explicitly separated empirically verified local pipeline runs from `NOT VERIFIED` live `Kafka`/`Spark` cluster throughput metrics.
