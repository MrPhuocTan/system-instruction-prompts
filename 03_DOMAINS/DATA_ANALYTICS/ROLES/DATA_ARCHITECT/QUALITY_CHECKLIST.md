# Quality Checklist: Data Architect (`ROLE-DATA-001`)

- **Role:** [`DATA_ARCHITECT`](./SYSTEM_PROMPT.md)
- **Domain Gates:** [`QUALITY_GATES.md`](../../QUALITY_GATES.md)

---

## 1. Grain, Dimensional Modeling & Bitemporal Soundness
- [ ] Declared explicit atomic grain, immutable surrogate/natural keys, and nullability rules for every table across `Bronze`/`Silver`/`Gold` (`Staging`/`Core`/`Mart`) layers.
- [ ] Separated `UTC` event timestamp (`occurred_at`), business validity interval (`valid_from`, `valid_to`), and system ingestion timestamp (`ingested_at`) to guarantee point-in-time historical queries and leak-free ML feature generation.
- [ ] Verified all monetary and accounting fields use exact `DECIMAL(p, s)` or integer minor units (`0` `FLOAT`/`DOUBLE` currency columns).
- [ ] Mapped conformed dimensions in an Enterprise Bus Matrix to prevent siloed duplicate dimension definitions.

## 2. Physical Layout, Partitioning & FinOps Cost Control
- [ ] Sized partition granularity to maintain healthy columnar file sizes (`~128 MB`–`512 MB`) and prevented high-cardinality partition explosion.
- [ ] Aligned sort/clustering/`Z-order` keys with dominant `WHERE` and `JOIN` predicates (`sargable` partition pruning verified via `EXPLAIN` or predicate analysis).
- [ ] Modeled compute pool isolation, auto-suspend timeouts, compaction cadence, snapshot expiration, and storage/egress FinOps guardrails.

## 3. Evolvability, Replayability & Producer Contracts
- [ ] Preserved immutable append-only raw (`Bronze`) payloads enabling full deterministic replay without re-extracting upstream operational systems.
- [ ] Defined backward/forward schema evolution contracts (additive nullable fields vs. versioned breaking migrations) and `Write-Audit-Publish` staging isolation.

## 4. Privacy, Residency & Governance By Design
- [ ] Isolated `PII`/`PHI` for dynamic column masking, row-level security (`RLS`), regional data residency, and cost-efficient `GDPR`/`CCPA` erasure (`crypto-shredding` or isolated `PII` vaults).
- [ ] Confirmed zero credentials, tokens, or live connection secrets appear in DDL files or catalog definitions.

## 5. Independent Verification & Handoff Completeness
- [ ] Parsed and executed DDL contracts locally (`DuckDB`/`sqlglot`) verifying syntax validity, `DECIMAL` monetary types, `UTC` timestamps, and acyclic layer dependencies.
- [ ] Verified analytical storage, compaction, and query-scan FinOps estimates compute cleanly without arithmetic errors.
- [ ] Delivered locked grain, Bus Matrix, and `WAP` contracts to [`DATA_ENGINEER`](../DATA_ENGINEER/SYSTEM_PROMPT.md), [`ANALYTICS_ENGINEER`](../ANALYTICS_ENGINEER/SYSTEM_PROMPT.md), and [`DATA_GOVERNANCE_SPECIALIST`](../DATA_GOVERNANCE_SPECIALIST/SYSTEM_PROMPT.md).
- [ ] Explicitly separated empirically validated local schemas from `NOT VERIFIED` live cloud-warehouse cluster benchmarks.
