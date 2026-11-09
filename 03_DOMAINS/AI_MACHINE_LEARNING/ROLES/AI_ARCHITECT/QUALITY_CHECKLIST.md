# Quality Checklist: AI Architect (`ROLE-AIML-001`)

- **Role:** [`AI_ARCHITECT`](./SYSTEM_PROMPT.md)
- **Domain Gates:** [`QUALITY_GATES.md`](../../QUALITY_GATES.md)

---

## 1. Architectural Justification & Paradigm Fit
- [ ] Confirmed simpler alternatives (deterministic rules, SQL/heuristics, classical ML, lexical search) were benchmarked or analytically ruled out before introducing deep learning, `PEFT`/`SFT`, or multi-step `LLM` agents.
- [ ] Documented explicit error cost asymmetry (`FP` vs. `FN`, hallucination impact) and mapped it to calibrated decision and abstention thresholds.
- [ ] Verified model, checkpoint, tokenizer, and dataset licenses (`Apache-2.0`, `MIT`, `Llama` community terms, commercial API ToS) permit target commercial deployment and redistribution.

## 2. Latency, Capacity & Economics Verification
- [ ] Verified end-to-end `p50`/`p95`/`p99` latency budget sums across preprocessing, feature/vector retrieval, model `TTFT`/`TPOT`, reranking, and guardrail stages with `>= 20%` safety headroom.
- [ ] Calculated `VRAM` and host memory footprint (weights + activations + `KV`-cache at peak concurrency and max context length) against target accelerator limits.
- [ ] Quantified unit economics (cost per `1,000` inferences, indexing/retraining cost, observability storage) with explicit rate limits, token caps, and retry circuit breakers.

## 3. Data Parity, Reliability & Fallback Contracts
- [ ] Locked typed input/output payload schemas, model version headers, and point-in-time feature freshness contracts to eliminate training-serving skew.
- [ ] Defined deterministic degraded-mode or fail-closed paths when model confidence falls below threshold, context grounding fails, or inference dependencies time out.
- [ ] Accounted for feedback-loop bias (censored labels, counterfactual exploration logging, delayed ground truth) in telemetry architecture.

## 4. Security, Privacy & Governance Readiness
- [ ] Enforced structural isolation between trusted system prompts, user inputs, and untrusted retrieved corpora (`OWASP LLM01` prompt injection defense).
- [ ] Confirmed `PII`/`PHI` scrubbing, tenant-level retrieval ACL enforcement, secret redaction, and safe serialization (`safetensors` / `ONNX`) across the artifact supply chain.
- [ ] Verified human-in-the-loop (`HITL`) override and kill-switch gates exist for consequential downstream actions (`NIST AI RMF` / `EU AI Act` alignment).

## 5. Independent Verification & Handoff Completeness
- [ ] Executed analytical capacity/cost scripts (`python3`) confirming `VRAM`, token budget, and latency numbers compute cleanly without arithmetic contradictions.
- [ ] Locked explicit evaluation acceptance gates for [`AI_EVALUATION_ENGINEER`](../AI_EVALUATION_ENGINEER/SYSTEM_PROMPT.md) and [`SYSTEM_ARCHITECT`](../../../../02_CORE_ROLES/SYSTEM_ARCHITECT/SYSTEM_PROMPT.md).
- [ ] Clearly separated empirically verified local contracts from `NOT VERIFIED` live production cluster or third-party API assumptions.
