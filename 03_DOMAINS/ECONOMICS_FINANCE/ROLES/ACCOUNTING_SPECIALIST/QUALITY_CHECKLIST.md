# Quality Checklist: Accounting Specialist (`ACCOUNTING_SPECIALIST` — `ROLE-FIN-009`)

- **Role ID:** `ROLE-FIN-009`
- **Canonical Role:** `ACCOUNTING_SPECIALIST`
- **Parent Domain:** `ECONOMICS_FINANCE` ([DOMAIN_INDEX.md](../../DOMAIN_INDEX.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md))
- **Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)

> Pre-handoff verification checklist aligned with [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md). Verify cent-exact accounting identities programmatically before `PASS`.

## 1. Authoritative Standard Accuracy & Contract Mapping
- [ ] Reporting framework (US GAAP, IFRS, or dual comparison) and fiscal period are explicitly specified (`FIN-QG-01`).
- [ ] Cited standards are current and accurate (e.g., ASC 606 / IFRS 15 for revenue, ASC 842 / IFRS 16 for leases, ASC 805 / IFRS 3 for business combinations, ASC 326 / IFRS 9 for credit losses — never superseded ASC 605/840 as active rules).
- [ ] Every contractual term driving accounting judgment (termination clauses, variable rebates, acceptance milestones, renewal options, principal/agent control) is documented in the Assumption & Judgment Ledger (`FIN-QG-02`).

## 2. Double-Entry, Roll-Forward & Tax Consistency
- [ ] Every journal entry and pro-forma adjustment lists explicit Debit and Credit accounts, statement classification (IS/BS/CFS), and satisfies `Sum(Debits) == Sum(Credits)` to exact `Decimal('0.00')` (`FIN-QG-03`).
- [ ] Opening-to-ending Balance Sheet, Retained Earnings, Deferred Revenue, ROU Asset / Lease Liability, and Intercompany Elimination schedules reconcile completely with zero plug accounts (`FIN-QG-04`).
- [ ] Book-tax temporary differences and corresponding Deferred Tax Assets/Liabilities (ASC 740 / IAS 12) are reflected consistently on adjustments.

## 3. Quality of Earnings (QoE), Sensitivity & Risk Judgments
- [ ] QoE EBITDA bridges evaluate both upward add-backs and downward deductions symmetrically, separating non-recurring items from recurring operational costs (`SBC`, ongoing restructuring, capitalized software).
- [ ] Key accounting judgments (SSP ranges, variable consideration constraints, incremental borrowing rates, useful lives, NWC peg windows, debt-like items) include sensitivity impact tables (`FIN-QG-05`, `FIN-QG-06`, `FIN-QG-07`).

## 4. Audit Trail, Uncertainty & Non-Attestation Disclosure
- [ ] Uninspected contracts, missing sub-ledger support, or ambiguous interpretive areas requiring external auditor consultation are flagged (`FIN-QG-08`).
- [ ] Output contains zero emojis/placeholders and states clearly (`FIN-QG-09`) that it is technical accounting analysis — not a statutory CPA audit opinion, PCAOB/AICPA attestation, or licensed tax opinion.

## 5. Handoff & Governance Readiness
- [ ] Exclusive Write-Lock boundaries were strictly honored (`0` files modified outside assigned workstream paths).
- [ ] Deterministic `run_command` verification commands, script exit codes, and observed numerical outputs are recorded.
- [ ] Verified empirical facts, explicit model assumptions, and any `PARTIAL` or `NOT VERIFIED` items are cleanly separated.
- [ ] Internal relative Markdown links resolve cleanly on disk with zero `TODO`/`TBD` tokens or decorative prose.
- [ ] Structured 8-item Worker Handoff Report is complete and ready for `SA_GATE` and `PM_GATE` signoff.
