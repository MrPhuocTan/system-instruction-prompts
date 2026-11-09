# Domain 03: AI & Machine Learning (`AI_MACHINE_LEARNING`)

- **Domain ID:** `DOM-03-AIML`
- **Precedence Layer:** Level 4 Domain Governance (subordinate to [`00_GLOBAL_CONSTITUTION`](../../00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md) and [`01_ORCHESTRATION`](../../01_ORCHESTRATION/ORCHESTRATION_SYSTEM_PROMPT.md))
- **Normative Policy:** [`DOMAIN_SYSTEM_PROMPT.md`](./DOMAIN_SYSTEM_PROMPT.md)
- **Verification Standard:** [`QUALITY_GATES.md`](./QUALITY_GATES.md)
- **Canonical Specialist Roles:** `10` (`ROLE-AIML-001` through `ROLE-AIML-010`)

---

## 1. Domain Scope & Engineering Charter

The `AI_MACHINE_LEARNING` domain governs end-to-end statistical modeling, representation learning, computer vision, natural language processing, large language model systems, distributed accelerator compute, production MLOps pipelines, and adversarial/out-of-distribution (`OOD`) model evaluation. Workstreams routed to this domain treat training loss convergence as necessary but insufficient: every model or AI subsystem must establish dataset provenance, zero train-test/temporal leakage, calibrated decision thresholds against non-trivial baselines, deterministic reproducibility, slice-level error attribution, and realistic serving latency/memory envelopes.

---

## 2. Canonical Role Inventory (`10` Roles)

| Role ID | Canonical Role Name | System Prompt | Quality Checklist | Primary Responsibility Boundary |
| :--- | :--- | :--- | :--- | :--- |
| `ROLE-AIML-001` | `AI_ARCHITECT` | [`SYSTEM_PROMPT.md`](./ROLES/AI_ARCHITECT/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/AI_ARCHITECT/QUALITY_CHECKLIST.md) | End-to-end AI system topology, build-vs-fine-tune-vs-RAG trade-offs, latency/cost budgets, fallback routing, and model governance contracts. |
| `ROLE-AIML-002` | `MACHINE_LEARNING_ENGINEER` | [`SYSTEM_PROMPT.md`](./ROLES/MACHINE_LEARNING_ENGINEER/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/MACHINE_LEARNING_ENGINEER/QUALITY_CHECKLIST.md) | Tabular/classical ML pipelines, feature engineering, online/offline parity, model serialization, and low-latency inference services. |
| `ROLE-AIML-003` | `DEEP_LEARNING_RESEARCHER` | [`SYSTEM_PROMPT.md`](./ROLES/DEEP_LEARNING_RESEARCHER/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/DEEP_LEARNING_RESEARCHER/QUALITY_CHECKLIST.md) | Neural architecture design, objective/loss formulation, optimizer dynamics, representation ablations, and convergence diagnostics. |
| `ROLE-AIML-004` | `COMPUTER_VISION_ENGINEER` | [`SYSTEM_PROMPT.md`](./ROLES/COMPUTER_VISION_ENGINEER/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/COMPUTER_VISION_ENGINEER/QUALITY_CHECKLIST.md) | Detection, segmentation, tracking, 3D/multi-view geometry, sensor/illumination robustness, and edge/stream vision inference. |
| `ROLE-AIML-005` | `NLP_ENGINEER` | [`SYSTEM_PROMPT.md`](./ROLES/NLP_ENGINEER/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/NLP_ENGINEER/QUALITY_CHECKLIST.md) | Tokenization, sequence labeling (`NER`), dense/lexical information retrieval, cross-encoders, multilingual normalization, and text classification. |
| `ROLE-AIML-006` | `LLM_ENGINEER` | [`SYSTEM_PROMPT.md`](./ROLES/LLM_ENGINEER/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/LLM_ENGINEER/QUALITY_CHECKLIST.md) | Prompt/context engineering, grounded `RAG`, structured tool-calling, `SFT`/`PEFT`/preference alignment (`DPO`), quantization, and prompt-injection defenses. |
| `ROLE-AIML-007` | `MLOPS_ENGINEER` | [`SYSTEM_PROMPT.md`](./ROLES/MLOPS_ENGINEER/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/MLOPS_ENGINEER/QUALITY_CHECKLIST.md) | Feature stores, training/CD DAGs, model registries, canary/shadow rollouts, data/concept drift telemetry, and automated rollback gates. |
| `ROLE-AIML-008` | `AI_EVALUATION_ENGINEER` | [`SYSTEM_PROMPT.md`](./ROLES/AI_EVALUATION_ENGINEER/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/AI_EVALUATION_ENGINEER/QUALITY_CHECKLIST.md) | Golden benchmark construction, slice/fairness audits, `LLM`-judge calibration against human raters, red-teaming, and `OOD` stress suites. |
| `ROLE-AIML-009` | `DATA_SCIENTIST` | [`SYSTEM_PROMPT.md`](./ROLES/DATA_SCIENTIST/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/DATA_SCIENTIST/QUALITY_CHECKLIST.md) | Exploratory data analysis (`EDA`), causal inference, A/B experimentation, uplift modeling, uncertainty quantification, and decision analytics. |
| `ROLE-AIML-010` | `GPU_HPC_ENGINEER` | [`SYSTEM_PROMPT.md`](./ROLES/GPU_HPC_ENGINEER/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/GPU_HPC_ENGINEER/QUALITY_CHECKLIST.md) | `CUDA`/`Triton` kernels, `DDP`/`FSDP`/tensor/pipeline parallelism, `KV`-cache/PagedAttention memory layout, roofline profiling, and thermal safety. |

---

## 3. Role Selection & Multi-Domain Routing Matrix

| Problem Pattern | Primary Role(s) | Mandatory Supporting / Review Role(s) | Cross-Domain Touchpoints |
| :--- | :--- | :--- | :--- |
| Enterprise `RAG` or agentic `LLM` product | `AI_ARCHITECT`, `LLM_ENGINEER` | `AI_EVALUATION_ENGINEER` (independent eval gate) | `DATA_ENGINEER` ([`DATA_ANALYTICS`](../DATA_ANALYTICS/DOMAIN_INDEX.md)), `APPLICATION_SECURITY` (`CYBERSECURITY`) |
| Tabular risk, churn, or ranking pipeline | `DATA_SCIENTIST`, `MACHINE_LEARNING_ENGINEER` | `MLOPS_ENGINEER`, `AI_EVALUATION_ENGINEER` | `ANALYTICS_ENGINEER`, `DATA_QUALITY_ENGINEER` ([`DATA_ANALYTICS`](../DATA_ANALYTICS/DOMAIN_INDEX.md)) |
| Custom backbone, multimodal loss, or `SFT` recipe | `DEEP_LEARNING_RESEARCHER` | `GPU_HPC_ENGINEER`, `AI_EVALUATION_ENGINEER` | `RESEARCH_METHODOLOGIST` (`RESEARCH_SCIENCE`) |
| Real-time video/camera inspection or `OCR` | `COMPUTER_VISION_ENGINEER` | `MLOPS_ENGINEER`, `GPU_HPC_ENGINEER` | `ROBOTICS_SYSTEMS_ARCHITECT` (`ROBOTICS_AUTOMATION`) |
| High-throughput serving or distributed training | `GPU_HPC_ENGINEER`, `MLOPS_ENGINEER` | `AI_ARCHITECT` | `PLATFORM_ENGINEER`, `SITE_RELIABILITY_ENGINEER` (`IT_SOFTWARE`) |

---

## 4. Recommended Reusable Skills

- **Cross-Domain Skills (`04_CROSS_DOMAIN_SKILLS`):**
  - [`COGNITIVE_EXECUTION`](../../04_CROSS_DOMAIN_SKILLS/COGNITIVE_EXECUTION/SKILL.md) — Hypothesis ledgering and explicit separation of empirical metrics from architectural assumptions.
  - [`DATA_INTERPRETATION`](../../04_CROSS_DOMAIN_SKILLS/DATA_INTERPRETATION/SKILL.md) — Confounder analysis, Simpson's paradox checks, and sample-size power discipline.
  - [`RISK_MANAGEMENT`](../../04_CROSS_DOMAIN_SKILLS/RISK_MANAGEMENT/SKILL.md) — Hallucination, bias, adversarial input, and silent model degradation mitigation.
- **Specialized Skills (`05_SPECIALIZED_SKILLS`):**
  - [`MODEL_EVALUATION`](../../05_SPECIALIZED_SKILLS/MODEL_EVALUATION/SKILL.md) — Leakage-free split validation, calibration (`ECE`/Brier), slice metrics, and significance testing.
  - [`SCIENTIFIC_REPRODUCIBILITY`](../../05_SPECIALIZED_SKILLS/SCIENTIFIC_REPRODUCIBILITY/SKILL.md) — Deterministic seed locking, dataset hash pinning, and ablation traceability.
  - [`PERFORMANCE_BENCHMARKING`](../../05_SPECIALIZED_SKILLS/PERFORMANCE_BENCHMARKING/SKILL.md) — `TTFT`, `TPOT`, `p50`/`p95`/`p99` tail latency, throughput, and accelerator memory profiling.
