# Quality Checklist: LLM Engineer (`ROLE-AIML-006`)

- **Role:** [`LLM_ENGINEER`](./SYSTEM_PROMPT.md)
- **Domain Gates:** [`QUALITY_GATES.md`](../../QUALITY_GATES.md)

---

## 1. Prompt, Context & Structured Output Rigor
- [ ] Versioned all system/user prompt templates outside business logic with explicit input/output token caps, deterministic context truncation, and prefix-cache-friendly static prefix ordering.
- [ ] Enforced grammar/schema-constrained structured outputs (`JSON Schema` / `Pydantic`) with deterministic validation, bounded retries, and safe fallback on parse failure.
- [ ] Verified explicit abstention and span-level citation contracts so missing or conflicting context produces `"insufficient evidence"` rather than ungrounded fabrication.

## 2. `RAG`, Tenant Isolation & Post-Training Integrity
- [ ] Enforced document-level ACL and tenant metadata filtering AT retrieval query time (never post-retrieval filtering) and evaluated retrieval (`Recall@k`, `MRR`) separately from generation faithfulness.
- [ ] If `SFT`/`PEFT`/`DPO` was performed: passed unit tests verifying exact chat-template parity (`BOS`/`EOS`/turn tokens), assistant-only completion loss masking, packed-sequence cross-document attention isolation, and benchmark decontamination.
- [ ] If quantized (`AWQ`/`GPTQ`/`FP8`/`GGUF`): benchmarked task accuracy, calibration-corpus domain match, and schema adherence degradation against `BF16`/`FP16`.

## 3. Agentic Safety, Prompt Injection Defense & Cost Controls
- [ ] Enforced hard `max_steps`, `max_tokens`, request timeouts, per-request cost caps, and idempotency keys on all multi-turn or tool-calling workflows.
- [ ] Tested direct and indirect prompt-injection payloads embedded inside retrieved chunks and tool outputs (`OWASP LLM01`, `LLM02`, `LLM07`), gating state-mutating tools behind strict allowlists + human approval where required.

## 4. Latency, Privacy & Observability
- [ ] Measured or analytically bounded `TTFT`, `TPOT`, `p95`/`p99` end-to-end latency, `KV`-cache footprint, and dollar cost per `1,000` requests.
- [ ] Redacted `PII`, API keys, and customer secrets from all prompt/completion trace logs and fine-tuning datasets.
- [ ] Verified stop-token / `EOS` configuration prevents runaway generation loops across serving engines (`vLLM`, `SGLang`, `TensorRT-LLM`, API gateways).

## 5. Independent Verification & Handoff Completeness
- [ ] Executed automated `pytest` suite covering prompt rendering, JSON schema enforcement, citation substring grounding, abstention triggers, and tool-argument validation.
- [ ] Delivered versioned prompt/RAG/adapter package and failure taxonomy to [`AI_EVALUATION_ENGINEER`](../AI_EVALUATION_ENGINEER/SYSTEM_PROMPT.md) for independent red-team and benchmark sign-off.
- [ ] Explicitly separated empirically verified local tests from `NOT VERIFIED` live provider API or GPU cluster metrics.
