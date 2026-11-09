# Pre-Execution Contracts & Worker Handoff Validation

## 1. Contract-First Engineering Principle
Parallel multi-agent execution succeeds only when cross-workstream boundaries are specified deterministically **before** implementation begins (`Design Principle 4` in [`GLOBAL_SYSTEM_PROMPT.md`](../00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md)).
Implicit interface assumptions between concurrent Backend, Frontend, Data, AI/ML, Finance, or Documentation workers guarantee integration rework and subtle runtime defects.

## 2. Pre-Execution Workstream & Interface Contract (`SA + PM` Lock)
Before dispatching any `Level 2`–`Level 4` workstream, `PM` and `SA` lock a formal contract using [`WORKSTREAM_CONTRACT.md`](../06_TEMPLATES/WORKSTREAM_CONTRACT.md) and record its reference in [`AGENT_COMMUNICATE.md`](../06_TEMPLATES/AGENT_COMMUNICATE.md).
Every locked contract defines nine binding elements:

1. **Workstream ID & Accountable Owner**
   - Unique stream identifier, execution wave, assigned runtime agent, and logical role(s).
2. **Objective & User-Value Context**
   - Concrete business, research, analytical, or system capability delivered by this stream.
3. **Exact Scope Boundaries**
   - Explicit `In-Scope` deliverables and `Out-of-Scope` exclusions so adjacent streams neither duplicate nor omit boundary logic.
4. **Exclusive Owned File/Module Paths**
   - Exact write-locked files and globs ([`FILE_OWNERSHIP_AND_LOCKING.md`](./FILE_OWNERSHIP_AND_LOCKING.md)).
5. **Locked Input/Output Interfaces**
   - *Software, API & Data:* Exact HTTP methods, paths, status codes, JSON/Protobuf/SQL schemas, nullability, pagination, idempotency keys, CLI flags, and exit codes.
   - *AI/ML & Analytics:* Tensor shapes, feature column names/dtypes, split boundaries, evaluation metric formulas, and artifact serialization formats.
   - *Finance, Science & Multi-Domain:* Currency/unit conventions (`USD $M`, SI units), time-horizon dates, citation formats, and shared assumption tables.
6. **Domain, Security, Regulatory & Resource Constraints**
   - Applicable `03_DOMAINS/<DOMAIN>/QUALITY_GATES.md` invariants, `RoE` bounds, secret handling, license constraints, and disk/CPU/GPU memory limits.
7. **Upstream Dependencies & Downstream Consumers**
   - Exact input paths consumed and downstream workstreams awaiting outputs ([`WORKSTREAM_MANAGEMENT.md`](./WORKSTREAM_MANAGEMENT.md)).
8. **Required Verification Commands & Evidence**
   - Deterministic commands, test suites, or reconciliation scripts the worker must run prior to handoff.
9. **Explicit `PM + SA` Acceptance Criteria**
   - Objective pass/fail conditions governing gate approval.

## 3. Zero Silent Drift & Contract Amendment Protocol
A worker subagent **never** unilaterally renames a shared endpoint, alters a database column type, changes financial unit scaling, or modifies a schema required by peer streams:
1. If implementation uncovers a flaw or edge case in a locked contract, the worker halts boundary changes and submits a concise **Contract Amendment Request (`CAR`)** via `send_message` stating:
   - Current locked specification clause.
   - Empirical defect or constraint discovered.
   - Proposed minimal interface update.
   - Impacted peer workstreams.
2. `SA` evaluates cross-stream impact, `PM` confirms scope alignment, `AGENT_COMMUNICATE.md` (`Section 9: Decisions & Rationale`) is updated with the revised contract version, and all impacted workers receive an explicit update message.

## 4. Structured Eight-Item Worker Handoff Validation
Upon completing assigned work, every worker produces a structured handoff following [`HANDOFF_REPORT.md`](../06_TEMPLATES/HANDOFF_REPORT.md) ([`AGENT_COMMUNICATION.md`](./AGENT_COMMUNICATION.md)) containing all **8 mandatory verification elements**:
1. **Workstream ID & Canonical Status:** `PASS`, `PARTIAL`, `BLOCKED`, `FAILED`, or `NOT VERIFIED`.
2. **Summary of Changes & Engineering Rationale:** Key design choices and trade-offs resolved.
3. **Exact Files Created / Modified:** Complete path list verified on disk (`read_file` / directory check).
4. **Contract & Write-Lock Compliance Confirmation:** Explicit attestation that `100%` of locked interfaces were honored and `0` out-of-lock paths were touched.
5. **Executed Verification Commands & Observed Results:** Exact CLI commands run, exit codes, pass/fail counts, or analytical tie-out numbers ([`INDEPENDENT_VERIFICATION.md`](../00_GLOBAL_CONSTITUTION/INDEPENDENT_VERIFICATION.md)).
6. **Known Limitations, Assumptions & `NOT VERIFIED` Items:** Honest disclosure of any check blocked by environment limits.
7. **Follow-Up Actions & Cross-Stream Impacts:** Integration notes for Wave 3 consumers or reviewers.
8. **Verification Evidence & Log Paths:** Paths to test outputs, screenshots, benchmark artifacts, or handoff summaries.

Handoffs omitting empirical command evidence or claiming `PASS` without verification are rejected back to the worker prior to `SA_GATE`.
