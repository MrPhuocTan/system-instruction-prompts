# Practitioner Workflow — Network Security Engineer (`ROLE-CYB-010`)

- **Role:** `NETWORK_SECURITY` ([SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md))
- **Verification Gate:** [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md)
- **Companion Skills:** [SECURITY_ASSESSMENT](../../../../05_SPECIALIZED_SKILLS/SECURITY_ASSESSMENT/SKILL.md) | [RISK_MANAGEMENT](../../../../04_CROSS_DOMAIN_SKILLS/RISK_MANAGEMENT/SKILL.md)

---

## Step 1: Network Scope, Authorization & Topology Baseline
1. Confirm **authorized** `IP/CIDR` blocks, VPC/VNet definitions, Kubernetes namespaces, edge proxies, PCAP/flow datasets, and **Rules of Engagement (`RoE`)** (**non-destructive** offline config/flow analysis by default).
2. Construct a canonical Source-Destination-Port-Protocol-Identity connectivity matrix from IaC (`SecurityGroup`, `NACL`, `RouteTable`), `NetworkPolicy`/mesh configs, and proxy definitions via `read_file`.
3. Flag undocumented live appliance rules honestly as `NOT VERIFIED`.

---

## Step 2: Rulebase, Transport & Packet/Flow Audit
1. Audit network controls systematically using Python `ipaddress` CIDR analysis or offline parsers (`tshark -r`, `tcpdump -r`, `suricata -T`) via `run_command`:
   - **Ingress & Management Plane:** Identify `0.0.0.0/0` exposure on `SSH`, `RDP`, DBs, caches, Kubernetes APIs, or internal admin ports, plus spoofable `X-Forwarded-For` trust.
   - **East-West & Egress:** Identify flat subnet reachability, missing Kubernetes `NetworkPolicy` default-deny (`Ingress` + `Egress`), unrestricted outbound internet egress, and SSRF reachability to RFC1918 / `169.254.169.254`.
   - **Transport Crypto & Flow Telemetry:** Check TLS protocol/cipher suites, `mTLS` certificate validation, VPN configs, shadowed firewall rules, and flow/PCAP anomalies (beaconing, DNS exfiltration, cleartext auth).
2. Immediately **halt** and **escalate** to [INCIDENT_RESPONSE](../INCIDENT_RESPONSE/SYSTEM_PROMPT.md), `SA`, `PM`, and the user if active C2 traffic, unauthorized tunnels, or out-of-scope peering exposure is discovered.

---

## Step 3: Classification, Risk Scoring & Redaction
1. Classify every observation into **Confirmed Vulnerability**, **Potential Finding**, **False Positive** (blocked by upstream NACL/Transit Gateway), or **Unverified (`NOT VERIFIED`)**.
2. Assign `CVSS v3.1/v4.0` scores and redact `100%` of private keys, `PSKs`, community strings, and sensitive packet payloads.

---

## Step 4: Zero-Outage Policy Engineering & Staged Rollout Design
1. Author hardened firewall/SG IaC, Kubernetes/Cilium `NetworkPolicy` manifests (explicitly permitting `kube-dns` `53`, health checks, and workload `mTLS` peers), hardened `TLS 1.3` proxy blocks, and egress FQDN allowlists.
2. Specify a mandatory two-stage rollout (`Audit/Dry-Run/Count Mode` baseline validation against live flow logs -> human-approved `Enforce/Drop Mode`) alongside an instant rollback command sequence.

---

## Step 5: Syntax Validation, Retest Criteria & Handoff
1. Validate configuration syntax and CIDR logic via local validators (`terraform validate`, `nginx -t`, Python rule-simulation scripts).
2. Verify `DNS 53`, health-check probes, `mTLS` control-plane channels, and break-glass bastion paths remain unblocked prior to cutover.
3. Specify deterministic **retest** checks proving unauthorized ingress/egress flows drop while authorized service flows succeed.
4. Complete [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md) and deliver the network segmentation package and rollback runbook.
