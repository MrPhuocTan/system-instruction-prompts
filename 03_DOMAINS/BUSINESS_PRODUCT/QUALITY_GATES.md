# Domain 05: Business & Product — Mandatory Quality Gates

- **Domain ID:** `DOM-05-BUSINESS-PRODUCT`
- **Enforcement:** Mandatory pre-handoff verification for all `BUSINESS_PRODUCT` roles and pre-signoff audit for [DOMAIN_LEAD](../../02_CORE_ROLES/DOMAIN_LEAD/SYSTEM_PROMPT.md), [QUALITY_REVIEWER](../../02_CORE_ROLES/QUALITY_REVIEWER/SYSTEM_PROMPT.md), `SA_GATE`, and `PM_GATE` per [REVIEW_AND_SIGNOFF.md](../../01_ORCHESTRATION/REVIEW_AND_SIGNOFF.md) and [INDEPENDENT_VERIFICATION.md](../../00_GLOBAL_CONSTITUTION/INDEPENDENT_VERIFICATION.md).

---

## Mandatory 6-Gate Pass/Fail Matrix

Every `BUSINESS_PRODUCT` deliverable MUST satisfy all applicable domain quality gates below before status can be marked `PASS`:

| Gate ID | Gate Name | Objective Pass Criteria | Automatic `FAIL` / `BLOCKED` Trigger |
| :--- | :--- | :--- | :--- |
| **BIZ-QG-01** | **User/Customer Problem Validation** | Clearly defines target ICP/segment, specific job-to-be-done or pain point, current baseline workaround cost/friction, and evidence tier (distinguishing verified behavioral/interview data from untested hypotheses with a concrete validation plan). | Solution-first feature list with no articulated customer pain, fabricated interview quotes/survey stats, or generic "everyone is the target user" framing. |
| **BIZ-QG-02** | **Measurable Outcome Metrics & Unit Economics** | Specifies baseline $\rightarrow$ target North Star / primary KPIs, anti-gaming guardrail metrics, telemetry event definitions, and gross-margin-adjusted unit economics (`Contribution Margin`, `CAC Payback`, `LTV:CAC`, `NDR`, or `Cost-to-Serve`) verified via script math. | Relying solely on vanity metrics (pageviews, raw signups), computing LTV on gross revenue instead of gross profit, or omitting cannibalization and variable fulfillment/compute costs. |
| **BIZ-QG-03** | **Scope & Trade-off Clarity** | Explicitly documents `In-Scope` requirements, `Out-of-Scope / Non-Goals`, prioritization rationale (opportunity cost of deprioritized options), falsifiable acceptance criteria (including empty, loading, error, permission, and edge states), and pre-committed pivot/kill thresholds. | Open-ended scope creep, vague non-testable adjectives (`"intuitive"`, `"scalable"` without bounds), or pretending strategic choices carry zero trade-offs. |
| **BIZ-QG-04** | **Operational Feasibility** | Validates end-to-end delivery capacity across engineering, support, fulfillment, legal/compliance, and ops: queueing/throughput bottlenecks, SLAs/SLOs, SOP exception paths, staffing/training load, and rollback/incident recovery plans are quantified. | Launching products, promotions, or schedules that exceed operational/support throughput, omit failure/refund handling, or assume zero onboarding/change-management friction. |
| **BIZ-QG-05** | **Experiment Rigor** | Every growth, pricing, or product experiment specifies a falsifiable hypothesis, randomization unit (avoiding network/cluster spillover), baseline rate, Minimum Detectable Effect (MDE), statistical power ($1 - \beta \ge 0.80$), significance ($\alpha \le 0.05$), runtime duration, SRM check, and invariant guardrails. | Unpowered "ship and see" tests, p-hacking via unadjusted mid-test peeking, survivorship/selection bias in pre-post comparisons, or dark-pattern manipulation. |
| **BIZ-QG-06** | **Stakeholder Alignment** | Includes an explicit RACI / decision-rights matrix (`Responsible`, `Accountable`, `Consulted`, `Informed`), cross-functional dependency contracts (Engineering, Design, Finance, Legal/Security, Sales/Support), risk/RAID mitigations, and clear executive decision options. | Unowned cross-team dependencies, ambiguous single-threaded accountability (multiple `A` owners on one deliverable), or unescalated legal/security/financial blockers. |

---

## Independent Verification Protocol

1. **Quantitative Sanity & Funnel Verification:**
   - Recompute all prioritization scores (RICE/WSJF), funnel conversion cascades, cohort retention curves, A/B sample-size/MDE formulas, critical-path floats, and Little's Law capacity calculations via deterministic Python scripts (`run_command`).
   - Verify unit economics (`Contribution Margin`, `LTV:CAC`, `Payback Months`) incorporate variable compute/API, payment, support, and fulfillment costs.
2. **Traceability & Edge-Case Audit:**
   - Verify 100% bidirectional traceability from validated user problem $\rightarrow$ business objective $\rightarrow$ functional/non-functional requirement $\rightarrow$ edge/error state $\rightarrow$ acceptance test & telemetry event (`BIZ-QG-01` through `BIZ-QG-06`).
   - Confirm MECE completeness on business-rule decision tables and acyclic graph validity (`0` circular loops) on project schedules.
3. **Human-Centric & Ethical Check:**
   - When validating live product implementations, pair with [HUMAN_CENTRIC_APPLICATION_QA](../../05_SPECIALIZED_SKILLS/HUMAN_CENTRIC_APPLICATION_QA/SKILL.md) to verify clean utilitarian UX, zero decorative "AI Sign" clutter, and zero deceptive dark patterns.

---

## Mandatory Evidence Artifacts Per Complexity Level

| Task Complexity | Minimum Required Verification Evidence | Sign-Off Authority |
| :--- | :--- | :--- |
| **Level 1 (Scoped Spec / Funnel Check)** | Problem statement + explicit acceptance criteria / metric math (`run_command`) + non-goals list. | Executing Specialist + Lightweight Main/SA Check |
| **Level 2 (Single-Domain PRD / Plan)** | Graded evidence table + unit-economics / capacity / experiment math + complete edge-state & RACI matrices. | Specialist + `SA_GATE` + `PM_GATE` |
| **Level 3 (Cross-Domain Product Delivery)** | All Level 2 artifacts + locked Engineering/Design/Finance handoff contracts + Level 1–3 QA verification. | Independent QA/Reviewer + `SA_GATE` + `PM_GATE` |
| **Level 4 (Regulated / Enterprise Rollout)** | All Level 3 artifacts + `DOMAIN_LEAD` audit + cutover/rollback rehearsal criteria + human approval gate. | `DOMAIN_LEAD` + `SA_GATE` + `PM_GATE` + Human Gate |

---

## Gate Escalation & Rejection Rules

- Any deliverable failing **`BIZ-QG-01`** (fabricated customer/survey evidence), **`BIZ-QG-02`** (negative unflagged contribution margin or broken funnel math), or **`BIZ-QG-05`** (p-hacked / SRM-invalidated experiment readout or dark pattern) is marked **`FAILED`**.
- Unresolved cross-functional legal, privacy, security, or architectural dependencies under **`BIZ-QG-06`** must be marked **`BLOCKED`** and escalated to Core `PM` + `SA`.
