# Quality Checklist: GPU & HPC Engineer (`ROLE-AIML-010`)

- **Role:** [`GPU_HPC_ENGINEER`](./SYSTEM_PROMPT.md)
- **Domain Gates:** [`QUALITY_GATES.md`](../../QUALITY_GATES.md)

---

## 1. Analytical Roofline & Memory Accounting
- [ ] Computed explicit `VRAM` breakdown (parameters, gradients, optimizer states, activations, `KV`-cache, `NCCL` communication buffers) and arithmetic intensity (`FLOPs/byte`) prior to optimization.
- [ ] Classified primary bottleneck (HBM bandwidth, Tensor Core compute, `NCCL`/`PCIe` interconnect, or CPU host launch/dataloader overhead) with profiler trace or analytical evidence.
- [ ] Eliminated accidental host-device synchronizations (`.item()`, `.cpu()`, dynamic shape graph breaks) inside inner training/inference loops.

## 2. Numerical Equivalence & Boundary Memory Safety
- [ ] Verified custom kernels and quantized operators match `FP32`/`FP64` reference forward AND backward gradients within documented `atol`/`rtol` tolerances.
- [ ] Tested prime/non-power-of-two sequence lengths, batch size `1`, zero-element empty tensors, non-contiguous tensor strides (`.transpose()`), and 64-bit pointer offset arithmetic (`int64` indexing for tensors `> 2^31` elements).
- [ ] Confirmed reused `VRAM` workspaces and `PagedAttention` `KV`-cache blocks are zeroed or strictly isolated across multi-tenant requests.

## 3. Distributed Correctness & Benchmark Honesty
- [ ] Verified rank-symmetric collective ordering (`DDP`/`FSDP`/`TP`/`PP`), exact gradient/loss normalization across uneven ranks, and finite `NCCL` watchdog timeouts.
- [ ] Executed benchmarks on realistic production batch/sequence shapes with proper warmup iterations and hardware event synchronization (or marked `CUDA`/multi-node timings `NOT VERIFIED` if target GPUs were absent locally).

## 4. Host Thermal, Security & Resource Protection
- [ ] Capped local benchmark durations, memory allocation, and CPU worker threads to safeguard host thermal limits, RAM, and disk space.
- [ ] Audited native/custom kernel indexing expressions against out-of-bounds read/write hazards on ragged and unaligned tile tails.
- [ ] Verified shared-memory (`SRAM`) bank-conflict freedom and coalesced global memory access patterns where custom tiles were written.
- [ ] Confirmed explicit human approval gates before altering cluster drivers, scheduler quotas, or shared serving infrastructure.

## 5. Independent Verification & Handoff Completeness
- [ ] Executed automated `pytest` parity tests verifying forward outputs and backward gradients match `FP32`/`FP64` reference implementations across edge shapes and non-contiguous strides.
- [ ] Delivered analytical roofline breakdown (`FLOPs/byte`, achieved `%` of peak HBM bandwidth and Tensor Core `TFLOPS`, peak `VRAM`) to [`AI_ARCHITECT`](../AI_ARCHITECT/SYSTEM_PROMPT.md) and [`MLOPS_ENGINEER`](../MLOPS_ENGINEER/SYSTEM_PROMPT.md).
- [ ] Explicitly separated empirically measured local timings from `NOT VERIFIED` target `CUDA`/multi-node cluster projections.
