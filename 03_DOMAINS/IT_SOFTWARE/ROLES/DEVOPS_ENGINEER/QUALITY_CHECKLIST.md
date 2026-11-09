# DevOps Engineer Quality Checklist (`DEVOPS_ENGINEER`)

- **Role ID:** `ROLE-IT-005`
- **Prompt Reference:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)
- **Domain Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md)

---

## 1. Pre-Handoff Verification Checklist

### 1.1 Supply-Chain, Container & Secret Hardening
- [ ] **Pinned Immutable Dependencies:** Base container images, OS packages, IaC provider versions, and third-party CI actions are pinned to explicit versions/SHA digests (`0` floating `:latest` or `@main` references).
- [ ] **Hardened Container Specification:** `Dockerfile` uses multi-stage builds, `.dockerignore` excludes secrets/VCS/build caches, runtime runs as non-root UID, and `SIGTERM` propagates cleanly to PID 1.
- [ ] **Zero Secret Exposure in Artifacts/State:** Secrets are never passed via `Dockerfile` `ARG`/`ENV`, committed in `.tfstate`/manifests, or echoed in CI debug steps; OIDC federation is preferred over static CI keys.

### 1.2 Pipeline Determinism, IaC & Rollback Readiness
- [ ] **Build-Once Promote-Digest Pipeline:** CI workflow compiles and tests once, gates deployment on `100%` passing automated checks, and promotes the verified artifact digest across environments.
- [ ] **Resource Quotas & Health Probes:** Orchestration manifests define CPU/memory requests and limits, `PodDisruptionBudget` / anti-affinity where multi-replica, and separate liveness/readiness probes.
- [ ] **IaC Validation & Idempotency:** Terraform/OpenTofu/Helm/Kustomize templates render and validate cleanly via `run_command` (or structural parser fallback when CLIs are absent) with strict input variable constraints.
- [ ] **Documented Rollback & Migration Ordering:** Deployment runbook specifies exact automated/manual rollback commands and enforces expand-contract migration safety prior to traffic cutover.

### 1.3 Operational Safety & Write-Lock Compliance
- [ ] **Human Approval Guardrails:** Production apply/deploy jobs and destructive operations are gated behind explicit human approval environments/steps and were never executed unilaterally.
- [ ] **Host Disk & Process Safety:** Local build verification bounded CPU/disk consumption and cleaned temporary build artifacts or background daemons.
- [ ] **Exclusive Write-Lock Compliance:** All modified pipeline, container, and IaC files reside strictly inside assigned write-lock paths.

---

## 2. Required Handoff Evidence & Gate Classification

1. Exact validation/render/build commands run (`terraform validate`, `helm template`, `docker build`, YAML schema checks) and exit codes (`PASS` / `FAILED`).
2. Summary of artifact hardening (base image, runtime UID, exposed ports, health endpoints) and rollback procedure.
3. Explicit `PARTIAL` or `NOT VERIFIED` disclosure for any cloud/cluster/daemon check unavailable in the local runtime.
