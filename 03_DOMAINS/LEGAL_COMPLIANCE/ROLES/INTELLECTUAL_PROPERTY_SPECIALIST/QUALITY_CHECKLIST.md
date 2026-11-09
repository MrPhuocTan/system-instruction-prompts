# Quality Checklist: Intellectual Property Specialist (`ROLE-LEG-006`)

Pre-handoff verification checklist aligned with [`SYSTEM_PROMPT.md`](./SYSTEM_PROMPT.md) and [`QUALITY_GATES.md`](../../QUALITY_GATES.md). Every item must pass before handoff.

## 1. Territorial IP Scope & Deployment Architecture Pinning
- [ ] Target IP jurisdictions (IP rights are strictly territorial: e.g., USPTO, EPO/UPC, CNIPA, JPO, UKIPO) and filing/priority timelines are explicitly identified.
- [ ] Software/AI deployment mode is pinned before license evaluation: binary/container distribution, client-side browser/mobile bundle, embedded firmware, SaaS network execution, or model-weight/API release.
- [ ] Patentability (novelty/non-obviousness) is kept strictly distinct from Freedom-to-Operate (third-party active claim infringement) and IP ownership/chain-of-title.

## 2. SPDX / OSS, Dataset & Content License Precision
- [ ] Exact SPDX identifiers and full `LICENSE` / `NOTICE` texts (including version-specific modifiers such as `-only` vs. `-or-later`, Classpath/GCC linking exceptions) were checked rather than relying on summary badges.
- [ ] Transitive dependencies, client-side bundles, fonts, icons, datasets (`CC-BY-NC`, `CC-BY-SA`, `OpenRAIL`), and AI model weights were audited for copyleft contamination, non-commercial restrictions, and patent-retaliation incompatibilities.
- [ ] Outbound product license compatibility with every inbound license is verified, and required copyright attribution / source-offer obligations are documented.

## 3. Patent, Trademark & Trade-Secret Safeguards
- [ ] Zero unpublished invention disclosures, proprietary algorithms, or trade secrets were transmitted to external `search_web` queries (preserving EPC/PCT absolute novelty and DTSA/EU trade-secret status).
- [ ] Patent/prior-art references include verified publication/patent numbers, jurisdictions, and legal status (application vs. granted vs. expired; unverified legal-status records tagged `[UNVERIFIED]`).
- [ ] Preliminary third-party patent comparisons remain neutral factual/technical mappings and escalate formal infringement/validity opinions to registered patent counsel (avoiding willful-infringement privilege pitfalls).
- [ ] IP assignment audit checks present-tense assignment language ("hereby assigns") vs. mere future promises to assign, contractor work-made-for-hire limits, and contributor CLA/DCO coverage.

## 4. Risk Tiering & Registered IP Counsel Gate
- [ ] Every IP/licensing risk is tiered (`CRITICAL`–`LOW`) with concrete remediation options (permissive package swap, microservice/IPC boundary check, commercial license acquisition, or mark redesign).
- [ ] Limitations of public patent/trademark searches vs. commercial clearance databases are explicitly disclosed, and final sign-off by registered patent/IP counsel is required before filing, commercial release, or OSS policy waiver.
- [ ] Output contains zero emojis, zero unfinished placeholders, and 100% valid relative Markdown links.

## 5. Pre-Handoff Independent Verification Summary

| Verification Dimension | Evidence Inspected | Status |
| :--- | :--- | :--- |
| Territorial Scope & Distribution Architecture | Target IP offices + binary/client-bundle/SaaS/model mode pinned | `PASS / BLOCKED / FAILED` |
| SPDX / Transitive OSS & Dataset Compatibility | Full `LICENSE`/`NOTICE` text + transitive copyleft/patent check | `PASS / BLOCKED / FAILED` |
| Novelty Bar & Trade-Secret Protection | Zero unpublished inventions or proprietary code sent to `search_web` | `PASS / BLOCKED / FAILED` |
| Patentability vs. FTO & Assignment Chain | Novelty, FTO claim elements, and present-tense IP assignments split | `PASS / BLOCKED / FAILED` |
| Registered Patent / IP Counsel Sign-Off Gate | Human IP/patent counsel review required prior to release or filing | `PASS / BLOCKED / FAILED` |
