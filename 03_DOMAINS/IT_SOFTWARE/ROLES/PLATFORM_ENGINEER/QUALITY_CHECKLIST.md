# Platform Engineer Quality Checklist (`PLATFORM_ENGINEER`)

- **Role ID:** `ROLE-IT-006`
- **Prompt Reference:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)
- **Domain Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md)

---

## 1. Pre-Handoff Verification Checklist

### 1.1 SDK Modularity, CLI Ergonomics & Secure Defaults
- [ ] **Narrow Public Surface & SemVer Stability:** Shared SDKs/modules expose minimal, typed public APIs with minimal transitive dependencies and preserve backward compatibility for existing consumers.
- [ ] **Secure-by-Default Golden Paths:** Generated service/module templates include structured logging, trace propagation, secret redaction, health endpoints, and non-root container defaults out of the box.
- [ ] **CLI Ergonomics & Determinism:** Internal CLIs/scripts support `--help` and `--dry-run` (where mutating), separate structured `--json` or data on `stdout` from diagnostics on `stderr`, and return accurate non-zero POSIX exit codes on failure.

### 1.2 Idempotency, Policy Testing & Consumer Parity
- [ ] **Idempotent Scaffolding & Task Graphs:** Running generators, formatters, or monorepo task pipelines twice consecutively produces identical outputs without dirty workspace drift or cache poisoning.
- [ ] **Policy-as-Code Fixture Coverage:** Admission/lint/governance rules include automated test cases verifying both compliant (`ALLOW`) and non-compliant (`DENY` with actionable remediation message) inputs.
- [ ] **Local-to-CI Parity:** Every platform guardrail enforced in CI can be executed locally by developers with a single documented command via `run_command`.
- [ ] **Sample Consumer End-to-End Verification:** At least one representative consumer package or fixture was built, typechecked, and tested against the new platform artifact (`0` regressions).

### 1.3 Documentation, Registry Safety & Write-Locks
- [ ] **Escape-Hatch Documentation:** Concise engineering docs explain default behavior, supported configuration overrides, and migration steps free of marketing filler.
- [ ] **Registry & Cluster Safety:** Zero unapproved package publications to external registries or live cluster CRD/admission mutations occurred.
- [ ] **Exclusive Write-Lock Compliance:** Edits are strictly confined to owned platform/tooling directories without silently mutating sibling feature streams.

---

## 2. Required Handoff Evidence & Gate Classification

1. Command outputs from SDK/CLI unit suites, policy fixture tests, idempotency re-runs, and sample consumer builds (`PASS` / `FAILED`).
2. Public interface summary (exported functions/types, CLI flags, exit codes) locked for downstream workstreams.
3. Explicit `PARTIAL` or `NOT VERIFIED` disclosure of any cluster-level CRD/operator runtime checks unavailable locally.
