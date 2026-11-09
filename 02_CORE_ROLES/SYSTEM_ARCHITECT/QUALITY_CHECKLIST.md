# Quality Checklist — System Architect (`ROLE-CORE-002`)

## 1. Pre-Execution Architecture & Contract Lock Checks
- [ ] **Empirical Workspace Grounding**
  - Existing repository structure, dependency manifests, runtime versions, and available disk/memory inspected directly before locking architecture.
- [ ] **Antigravity Runtime Realism Verified**
  - Zero reliance on unsupported cross-session OS daemons or kernel per-subagent file locks; workspace rules stay strictly `< 24 KB` per file and within the `20,000`-token always-on budget.
- [ ] **Deterministic Interface Contracts Locked**
  - All cross-workstream APIs, data schemas, CLI signatures, error codes, and unit conventions explicitly locked in [`WORKSTREAM_CONTRACT.md`](../../06_TEMPLATES/WORKSTREAM_CONTRACT.md) and [`AGENT_COMMUNICATE.md`](../../06_TEMPLATES/AGENT_COMMUNICATE.md) before Wave 2 dispatch.
- [ ] **Mathematically Disjoint Write-Locks**
  - Every mutable path in `AGENT_COMMUNICATE.md` (`Section 8: File Ownership`) has at most `1` active owner per wave ($\text{Paths}(i) \cap \text{Paths}(j) = \emptyset$), with shared root manifests isolated to a single integration owner.
- [ ] **Least-Privilege & Safety Controls Specified**
  - Subagent tool permissions, secret environment-variable patterns, host CPU/GPU/disk limits, and `Level 1` Human Approval triggers documented upfront.

## 2. In-Flight Contract & Resource Governance Checks
- [ ] **Controlled Contract Amendments**
  - Any mid-flight schema or boundary adjustment evaluated via formal Contract Amendment Request (`CAR`), logged in `Section 9: Decisions & Rationale`, and broadcast to all affected streams.
- [ ] **Host Resource & Thermal Headroom Preserved**
  - Build/test concurrency, container footprints, and dataset sizes bounded safely within local disk and memory limits.

## 3. Post-Implementation `SA_GATE` Verification Checks
- [ ] **Zero Silent Contract Drift**
  - Worker outputs match locked schemas, interfaces, and directory paths `100%`.
- [ ] **Write-Lock & Tree Cleanliness Audited**
  - Post-run file inspection confirms zero unauthorized cross-lock edits, zero overwritten peer work, and zero stray temporary or `.DS_Store` artifacts.
- [ ] **Independent Automated Verification Passed**
  - Compilers, typecheckers, linters, unit + integration tests, or analytical reconciliation scripts executed with exit code `0` and observed output evidence (`Tool Success != Task Success` verified across real boundaries).
- [ ] **Zero Secret, PII, or Injection Exposure**
  - Diffs, logs, configs, and handoff reports scanned to confirm zero hardcoded secrets, tokens, private keys, unmasked `PII`/`PHI`, or untrusted prompt-injection payloads.
- [ ] **Technical Review Recorded**
  - [`TECHNICAL_REVIEW.md`](../../06_TEMPLATES/TECHNICAL_REVIEW.md) and `AGENT_COMMUNICATE.md` (`Section 12: Technical Signoff`) updated with reproducible commands, observed results, and explicit `SA_GATE` verdict.
