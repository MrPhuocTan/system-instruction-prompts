# Quality Checklist: Technical Trainer (`ROLE-EDU-004`)

- **Role:** [TECHNICAL_TRAINER](./SYSTEM_PROMPT.md)
- **Domain Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md) (`QG-EDU-001`, `QG-EDU-004`, `QG-EDU-005`, `QG-EDU-006`)

## 1. Pedagogical Alignment & Cognitive Scaffolding (`QG-EDU-001`, `QG-EDU-002`)
- [ ] Every hands-on lab exercise and fault-injection scenario maps directly to an observable `ELO`/`TLO` with explicit completion criteria.
- [ ] Non-target boilerplate is pre-provisioned so $\ge 80\%$ of learner seat time focuses on practicing the target technical construct.
- [ ] Exercises apply active mental-model building (`PRIMM` predict-investigate-modify, faded code completion, realistic debugging) rather than blind copy-paste command lists.
- [ ] Tiered hints (`Conceptual Cue -> Diagnostic Check Command -> Minimal Unblocking Snippet`) and a troubleshooting FAQ cover common learner failure states.

## 2. Clean-Room Executability & Autograder Rigor (`QG-EDU-004`)
- [ ] Runtime versions, lockfiles, container tags, and vendored synthetic datasets are pinned deterministically (`0` floating `latest` tags or rate-limited classroom URLs).
- [ ] CLI commands and helper scripts account for cross-platform differences across `macOS` (`zsh`), `Linux` (`bash`), and `Windows WSL2`.
- [ ] **Stage 1 Verified:** Running the autograder against the untouched starter/broken state fails on the exact target assertions (`0` vacuous passes).
- [ ] **Stage 2 Verified:** Applying the reference solution via `run_command` passes 100% of behavioral autograder and lint checks (`exit code 0`).
- [ ] **Stage 3 Verified:** Running the reset/teardown script cleanly terminates temporary processes/ports and restores clean workspace state.
- [ ] Autograder evaluates multiple behavioral and edge-case inputs to prevent hardcoded return-literal gaming and emits actionable failure messages.

## 3. Facilitator Readiness, Accessibility & Security Hygiene (`QG-EDU-005`, `QG-EDU-006`)
- [ ] Instructor facilitation runbook includes realistic novice pacing (`2x–3x` reference runtime), checkpoint git tags/branches for learners who fall behind, and live-demo fallbacks.
- [ ] Lab instructions, architecture diagrams, and terminal outputs satisfy `WCAG 2.2 AA` (no color-only status reliance; text descriptions for diagrams).
- [ ] Interactive web sandboxes follow 3-level `HUMAN_CENTRIC_APPLICATION_QA`, honestly disclosing if live GUI browser tools were unavailable locally.
- [ ] Zero live API keys, cloud credentials, or real PII exist in starter repos or commit history (`.env.example` + synthetic fixtures only).
- [ ] Cybersecurity and fault-injection exercises remain strictly isolated to `127.0.0.1` or internal air-gapped sandboxes with explicit legal scope notices.

## 4. Handoff & Clean-Environment Evidence
- [ ] Exact `run_command` verification commands and exit codes (`Stage 1`, `Stage 2`, `Stage 3`) are logged for independent `QUALITY_REVIEWER` replay.
- [ ] Host CPU, RAM, and disk footprint limits are documented so labs do not exhaust learner laptops or CI runners.
- [ ] Verified local execution facts, environment assumptions, timing estimates, and any `NOT VERIFIED` cloud/GPU/hardware steps are separated in [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md).
