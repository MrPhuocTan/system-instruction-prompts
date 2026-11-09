# File Ownership & Exclusive Write-Lock Protocol

## 1. Runtime Reality & Why Explicit Locking Is Mandatory
In the Antigravity runtime, `write_file`, `edit_file`, and `run_command` execute under the host user's operating-system permissions without kernel-enforced per-subagent ACL locks ([`TOOL_USAGE_AND_LIMITATIONS.md`](../00_GLOBAL_CONSTITUTION/TOOL_USAGE_AND_LIMITATIONS.md)).
Without deterministic architectural file ownership, two parallel subagents editing the same file or directory will overwrite each other's diffs, corrupt schemas, or create race-condition build failures.

## 2. The Single-Writer Exclusive Write-Lock Invariant
On every `Level 2` through `Level 4` project with `>= 2` active agents:
1. **At Most One Active Writer**
   - Every mutable file path or directory glob (e.g., `src/billing/**`, `03_DOMAINS/IT_SOFTWARE/**`, `docs/api_spec.yaml`) has **at most `1` active write-lock holder** within an execution wave (`0` concurrent writers on any overlapping path).
2. **Zero Unilateral Edits to Shared Governance or Index Files**
   - Worker subagents never unilaterally edit `PROJECT_MANIFEST.md`, `PROJECT_STATE.md`, `AGENT_COMMUNICATE.md`, `LIBRARY_INDEX.md`, or `CHANGELOG.md` unless explicitly designated as the single owner for that integration batch ([`AUTONOMOUS_ORCHESTRATION.md`](./AUTONOMOUS_ORCHESTRATION.md)).
3. **Unrestricted Scoped Read Access**
   - Any authorized agent may inspect (`read_file`) files outside its write-lock (such as locked `SA` schemas, shared utilities, or upstream interfaces) subject to [`SECURITY_AND_PRIVACY.md`](../00_GLOBAL_CONSTITUTION/SECURITY_AND_PRIVACY.md).
4. **Zero Lock Overhead on Single-Agent Work**
   - `Level 0`, single-agent `Level 1`, and sequential fallback batches execute with `1` writer and require zero lock-table ceremony.

## 3. Lock Granularity & Shared-File Partitioning Patterns
`SA` assigns write-locks in `Section 8: File Ownership` of [`AGENT_COMMUNICATE.md`](../06_TEMPLATES/AGENT_COMMUNICATE.md) before Wave 1 or Wave 2 begins:

| File / Artifact Category | Collision Risk | Mandatory `SA` Ownership Pattern |
| :--- | :--- | :--- |
| **Feature / Domain Subtrees** (`src/orders/**`, `03_DOMAINS/FINANCE/**`) | Low when directory-partitioned | Assign disjoint directory globs (`dir_a/**`, `dir_b/**`) to parallel Wave 2 workers. |
| **Shared Schemas, Types & Protobufs** (`src/types/**`, `prisma/schema.prisma`) | Very High | Lock exclusively to `SA` or a single Wave 1 foundation worker; freeze read-only during Wave 2. |
| **Root Manifests & Dependency Locks** (`package.json`, `pyproject.toml`, `Cargo.toml`, `skills.json`) | Very High | Assign exclusively to `1` designated platform/integration owner; workers request dependency additions via `send_message` rather than editing manifests directly. |
| **Barrel Exports, Routers & Master Catalogs** (`src/index.ts`, `LIBRARY_INDEX.md`, `README.md`) | High | Defer aggregation writes to a dedicated Wave 3 integration batch after Wave 2 workers complete. |
| **Coordination & Handoff Logs** (`AGENT_COMMUNICATE.md`, `configs/handoffs/<stream>.md`) | High if shared | Coordinator owns `AGENT_COMMUNICATE.md`; each worker owns strictly its own `configs/handoffs/<stream>.md` ([`AGENT_COMMUNICATION.md`](./AGENT_COMMUNICATION.md)). |

## 4. Formal Lock Lifecycle & Sequential Wave Transfer Protocol
1. **Pre-Wave Mathematical Disjointness Check**
   - `SA` populates `File Ownership` in `AGENT_COMMUNICATE.md` (`Path/Glob | Owner Agent ID | Wave | Lock Status = LOCKED_ACTIVE`).
   - `SA` verifies that for all active locks $i \neq j$, $\text{Paths}(i) \cap \text{Paths}(j) = \emptyset$.
2. **Subagent Prompt Enforcement**
   - Field 12 (`File Ownership`) of [`SUBAGENT_CREATION_PROMPT.md`](../07_SUBAGENT_PROMPTS/SUBAGENT_CREATION_PROMPT.md) lists exact permitted write paths.
   - Workers must halt immediately and escalate via `send_message` if their task appears to require out-of-lock edits.
3. **Sequential Lock Transfer Across Waves**
   - Wave $N$ owner submits [`HANDOFF_REPORT.md`](../06_TEMPLATES/HANDOFF_REPORT.md) and ceases all writes (`Lock Status -> RELEASED`).
   - Coordinator/`SA` verifies modified files match the Wave $N$ lock before assigning `LOCKED_ACTIVE` to any Wave $N+1$ owner.

## 5. Post-Execution Write-Lock Audit & Violation Containment
Before granting `SA_GATE` signoff ([`REVIEW_AND_SIGNOFF.md`](./REVIEW_AND_SIGNOFF.md)), `SA` or the orchestrator executes an empirical filesystem check (`git status --short`, `git diff --name-only`, or directory validator):
- Confirm every created or modified file maps to an authorized write-lock entry.
- Confirm zero stray scratch files, `.DS_Store` artifacts, or out-of-scope shell mutations exist.
- If an unauthorized cross-lock write occurred:
  1. Immediately mark the offending handoff `FAILED`.
  2. Inspect diffs for collateral overwrite damage and restore overwritten peer work cleanly.
  3. Re-run verification across both affected streams before proceeding.

## 6. Common File-Locking Anti-Patterns to Prevent
- Allowing two feature subagents to append routes to a shared `router.ts` or exports to `index.ts` in the same parallel wave.
- Running repo-wide auto-formatters (`prettier --write .`, `ruff format .`) inside a scoped worker instead of formatting strictly owned paths (`ruff format src/billing/`).
- Letting workers append directly to `AGENT_COMMUNICATE.md` or `LIBRARY_INDEX.md` concurrently instead of writing to isolated per-stream handoff files (`configs/handoffs/<stream>.md`).
