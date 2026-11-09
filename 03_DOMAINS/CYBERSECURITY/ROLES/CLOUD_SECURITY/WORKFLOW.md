# Practitioner Workflow — Cloud Security Engineer (`ROLE-CYB-009`)

- **Role:** `CLOUD_SECURITY` ([SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md))
- **Verification Gate:** [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md)
- **Companion Skills:** [SECURITY_ASSESSMENT](../../../../05_SPECIALIZED_SKILLS/SECURITY_ASSESSMENT/SKILL.md) | [RISK_MANAGEMENT](../../../../04_CROSS_DOMAIN_SKILLS/RISK_MANAGEMENT/SKILL.md)

---

## Step 1: Scope, Authorization & Cloud Topology Inventory
1. Confirm **authorized** IaC repositories, cloud accounts/subscriptions/projects, Kubernetes clusters, and **Rules of Engagement (`RoE`)** (**non-destructive** static/read-only inspection by default).
2. Map cloud account hierarchy (`Organizations`/`Folders`), state backends, compute (`EC2`/`EKS`/`GKE`/`AKS`/`Lambda`/Cloud Run), storage/DB tiers, KMS hierarchies, VPC egress paths, and CI/CD deployment identities via `read_file`.
3. Record uninspected live console drift honestly as `NOT VERIFIED`.

---

## Step 2: IaC, Container & Control-Plane Posture Audit
1. Run available local static IaC/container scanners (`trivy config`, `checkov`, `opa`, `hadolint`) via `run_command` and perform deep manual review against `CIS Benchmarks`:
   - **Identity & Metadata:** Hunt static cloud keys, wildcard `*` IAM policies, unconditioned `iam:PassRole` / `sts:AssumeRole`, cross-account trust confusion (`sts:ExternalId` absence), and `IMDSv1` exposure.
   - **Data & Storage:** Verify S3/GCS/Blob public-access blocks, `KMS` encryption at rest, snapshot sharing settings, and TLS-only bucket/DB transport policies.
   - **Kubernetes & Containers:** Audit `Dockerfile` base images, `USER` UIDs, `Pod` securityContexts (`privileged`, `hostNetwork`, `hostPath`, capabilities), `RBAC` `ClusterAdmin`/secret-list bindings, and `NetworkPolicy` isolation.
2. Immediately **halt** and **escalate** to `SA`, `PM`, and the user if publicly readable sensitive storage, leaked live cloud keys, or unauthorized control-plane principals are found.

---

## Step 3: Triage, Blast-Radius Scoring & State-Safety Check
1. Filter out false positives where upstream `SCPs`, GCP Org Policies, or private subnet isolation already block exposure; classify items into **Confirmed Vulnerability**, **Potential Finding**, **False Positive**, or **Unverified (`NOT VERIFIED`)** with `CVSS` vectors and `100%` secret redaction.
2. Audit every proposed IaC change for stateful resource replacement (`forces replacement`) and KMS/SCP admin self-lockout risks before authoring patches.

---

## Step 4: Hardening Implementation & Policy-as-Code Authoring
1. Patch `Terraform`/`Helm`/`Kubernetes`/`Dockerfile` manifests (`edit_file`) with least-privilege OIDC workload roles, `IMDSv2`, `restricted` pod security contexts, and KMS policies containing explicit break-glass/admin conditions.
2. Author `OPA/Rego` or `Kyverno` admission rules enforcing those invariants continuously in CI/CD and cluster admission.

---

## Step 5: Deterministic Retest, Rollback Plan & Handoff
1. Re-run IaC validators, policy unit tests (`opa test`), and static scanners via `run_command` to prove **retest** closure on hardened manifests and rejection of insecure fixtures.
2. Verify `terraform plan` / diff simulations introduce zero destructive replacements on stateful resources and preserve break-glass emergency administrative access.
3. Attach safe staged rollout and instant rollback commands for human operators.
4. Complete [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md) and deliver the redacted Cloud Security package.
