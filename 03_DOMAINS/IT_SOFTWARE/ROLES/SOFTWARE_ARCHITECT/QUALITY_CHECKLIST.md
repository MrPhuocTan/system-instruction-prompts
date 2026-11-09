# Software Architect Quality Checklist (`SOFTWARE_ARCHITECT`)

- **Role ID:** `ROLE-IT-001`
- **Prompt Reference:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)
- **Domain Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md)

---

## 1. Pre-Handoff Verification Checklist

### 1.1 Boundaries, Coupling & Interface Contracts
- [ ] **Bounded Context & Ownership Clarity:** Every module, service, database table, and message topic has a single authoritative owner with zero shared mutable persistence across service boundaries.
- [ ] **Acyclic Dependency Direction:** Module dependency rules enforce unidirectional inward flow (`transport -> application -> domain <- adapters`); programmatic import checks confirm zero dependency cycles.
- [ ] **Machine-Validated Interface Contracts:** OpenAPI 3.1, Protobuf, GraphQL, or JSON Schema specifications parse cleanly via `run_command` without syntax errors or unresolved `$ref` pointers.
- [ ] **ADR Trade-Off Completeness:** At least two viable architectural alternatives were compared with explicit pros, cons, operational cost, and rejected-option rationale.

### 1.2 Resilience, Capacity & Evolution Safety
- [ ] **Error, Timeout & Retry Semantics:** Every cross-process boundary defines explicit connection/read timeouts, bounded retry policies with jitter, dead-letter or fallback behavior, and deterministic error payloads (RFC 9457 or equivalent).
- [ ] **Idempotency & Concurrency Guarantees:** Mutating operations specify idempotency keys, optimistic concurrency version tokens (`ETag` / row version), or transactional outbox semantics preventing duplicate side effects.
- [ ] **Quantitative NFR Budgeting:** ADR documents explicit estimates for peak RPS, payload size ceilings, composite p95/p99 latency budgets, and storage growth rather than qualitative claims.
- [ ] **Backward Compatibility & Rollback Plan:** Schema and API changes follow additive expand-contract phasing so code rollback never orphans unreadable production state.

### 1.3 Security & Governance Hygiene
- [ ] **Security & Tenant Isolation:** Authentication, object-level authorization, secret injection, and tenant boundary enforcement are specified at architectural ingress and service-to-service boundaries.
- [ ] **Exclusive Write-Lock & Diagram Hygiene:** All modified files reside strictly inside the SA-assigned write-lock paths, Mermaid diagrams use supported syntax with quoted special-character labels, and zero unfinished placeholders remain.

---

## 2. Required Handoff Evidence & Gate Classification

1. Exact paths to created/updated ADRs and machine-readable contract schemas.
2. Command output confirming schema/linter validation exit code `0` (`PASS`), or explicit `PARTIAL` / `NOT VERIFIED` disclosure when external schema validators are absent locally.
3. Summary of locked upstream/downstream assumptions and open risks escalated to `SA` + `PM`.
