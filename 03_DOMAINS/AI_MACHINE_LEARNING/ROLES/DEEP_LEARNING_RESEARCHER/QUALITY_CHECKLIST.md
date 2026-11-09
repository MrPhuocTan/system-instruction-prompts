# Quality Checklist: Deep Learning Researcher (`ROLE-AIML-003`)

- **Role:** [`DEEP_LEARNING_RESEARCHER`](./SYSTEM_PROMPT.md)
- **Domain Gates:** [`QUALITY_GATES.md`](../../QUALITY_GATES.md)

---

## 1. Tensor, Mask & Loss Mathematical Correctness
- [ ] Verified initial untrained loss matches theoretical random-chance expectation (e.g., `ln(V)` for vocabulary size `V`) without `NaN`/`Inf` instability.
- [ ] Passed automated mask-invariance unit tests confirming future tokens (`t' > t`) and `<PAD>` positions exert zero influence (`grad == 0.0`) on causal or masked representations.
- [ ] Audited all tensor reductions and broadcasting operations with explicit shape assertions; verified padding tokens are excluded from loss denominators (`ignore_index`) and `log_softmax`/`cross_entropy` run in numerically stable `FP32` accumulation.

## 2. Optimization & Numerical Health
- [ ] Passed deterministic single-batch overfit sanity check reaching near-zero training loss prior to launching full-scale sweeps.
- [ ] Verified weight decay excludes biases, `1D` `LayerNorm`/`RMSNorm` parameters, and embeddings where appropriate; confirmed mixed-precision (`BF16`/`FP16`) gradient health and clipping norms.
- [ ] Confirmed strict `model.train()` / `model.eval()` and `torch.inference_mode()` state transitions, batch-size invariance, and exact token/sample-weighted metric reduction across distributed shards.

## 3. Compute-Matched Baselines & Controlled Ablations
- [ ] Benchmarked proposed architecture/objective against a tuned baseline matched on `FLOPs`, parameter count, data splits, and training tokens.
- [ ] Isolated each novel architectural or loss term in a controlled single-factor ablation table reporting mean and variance across multiple `PRNG` seeds (or explicitly flagged single-seed runs if compute-constrained).

## 4. Reproducibility, Serialization Safety & Resource Discipline
- [ ] Locked `PRNG` seeds, dependency versions, declarative configs, and `safetensors` checkpoint serialization (`weights_only=True` on any legacy `PyTorch` loads).
- [ ] Verified checkpoint reload round-trip reproduces identical forward logits (`torch.testing.assert_close`) in `eval()` mode.
- [ ] Bounded host memory/`VRAM` usage and disk checkpoint counts (`save_total_limit`) to prevent host resource exhaustion.

## 5. Independent Verification & Handoff Completeness
- [ ] Executed automated `pytest` suite covering tensor shape contracts, causal/padding mask invariance, autograd flow (`0` dead/disconnected parameters), and single-batch memorization.
- [ ] Documented architectural hyperparameters, parameter/FLOP counts, and failure modes for [`GPU_HPC_ENGINEER`](../GPU_HPC_ENGINEER/SYSTEM_PROMPT.md) and [`AI_EVALUATION_ENGINEER`](../AI_EVALUATION_ENGINEER/SYSTEM_PROMPT.md).
- [ ] Explicitly separated empirically executed ablation results from `NOT VERIFIED` full-scale cluster scaling projections.
