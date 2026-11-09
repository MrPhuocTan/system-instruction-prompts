---
name: performance-benchmarking
description: "Use this skill when measuring latency, throughput, memory footprint, CPU/GPU utilization, or algorithmic scalability, diagnosing bottlenecks via profiling, and proving optimizations empirically without thermal or host exhaustion."
---

# Performance Benchmarking

## Skill Metadata
- **Skill ID:** `SKL-SPEC-005`
- **Name:** `performance-benchmarking`
- **Domain:** `IT_SOFTWARE, AI_MACHINE_LEARNING, DATA_ANALYTICS`
- **Version:** `1.0.0`

## Purpose
Replace guesswork and premature micro-optimization with controlled, statistically reproducible empirical measurement and profiling. This skill establishes rigorous A/B baseline-vs-candidate benchmarking across tail latency (`p50/p95/p99/p99.9`), throughput (`RPS`, `tokens/s`, `rows/s`), memory/allocation pressure, I/O amplification, and GPU/CPU saturation while strictly protecting the host machine from disk, memory, or thermal exhaustion.

## Required Competencies
- Experimental benchmark design: workload representativeness, JIT/cache warm-up separation, steady-state windowing, multi-trial variance control, and coordinated-omission prevention.
- Bottleneck profiling across CPU flamegraphs, heap/GC allocation trackers, lock contention, syscall/I/O wait, SQL `EXPLAIN ANALYZE`, and GPU kernel/VRAM utilization.
- Queueing and scalability modeling: open-loop vs. closed-loop load generation, saturation knees, algorithmic complexity (`O(N)` vs. `O(N^2)` empirical scaling curves).
- Correctness-preserving optimization verification (ensuring faster code still produces bit-for-bit or contract-identical outputs).

## Prerequisites
- Target SLOs, resource budgets, and realistic input distributions (payload sizes, skew, concurrency) defined via [REQUIREMENTS_ANALYSIS](../../04_CROSS_DOMAIN_SKILLS/REQUIREMENTS_ANALYSIS/SKILL.md).
- Pre-flight host resource check (`df -h`, memory pressure, active CPU load) executed via `run_command` to guarantee safe execution headroom.
- Functional correctness test suite passing at baseline before any performance changes begin.

## Workflow
1. **Pin Workload, Hardware Context & SLO Targets:** Record exact CPU/GPU/RAM/OS specs, compiler/runtime flags, dataset shapes (small, nominal, skewed-large), and target metrics before touching code.
2. **Capture Reproducible Baseline & Profile First:** Run the unmodified baseline across warm-up + `N >= 5` measured trials; collect CPU/memory/I/O profiles to pinpoint the actual bottleneck rather than optimizing unprofiled hot-path guesses.
3. **Design Unbiased Benchmark Harness:** Separate warm-up iterations from timed windows, prevent dead-code elimination by consuming outputs, use open-loop arrival schedules when measuring queueing tail latency (avoiding coordinated omission), and test realistic cache-miss ratios rather than 1-key hot loops.
4. **Implement Targeted Structural Optimization:** Apply one isolated change at a time (algorithmic complexity reduction, batching, index addition, zero-copy streaming, bounded concurrency pool) so causal attribution is unambiguous.
5. **Re-Measure Candidate & Verify Correctness Parity:** Run the identical benchmark harness on the candidate under matching system load; verify output equivalence and full regression test pass alongside `p50`, `p95`, `p99`, max RSS memory, and throughput deltas.
6. **Check Scaling Curves & Host Resource Hygiene:** Test behavior across 1x, 10x, and 100x input scales (within safe host memory/thermal limits) to confirm asymptotic improvement, then clean up temporary benchmark datasets.

## Tools and Techniques
- **Language/Runtime Profilers & Harnesses:** `pytest-benchmark` / `py-spy` / `cProfile` / `tracemalloc` (Python), `go test -bench -benchmem` / `pprof` (Go), `Criterion` (Rust), `Clinic.js` / `autocannon` / `k6` (Node/HTTP), `EXPLAIN (ANALYZE, BUFFERS)` (SQL).
- **Full Quantile & Variance Reporting:** Report `median (p50)`, `IQR/std`, `p95`, `p99`, peak RSS, and allocation counts—never report single best-run cherry-picked numbers or arithmetic means alone.
- **Amdahl's Law Sanity Check:** Calculate the maximum theoretical speedup given the profiled fraction of runtime spent in the target routine before investing engineering effort.
- **Bounded Resource Envelopes:** Cap benchmark worker threads, dataset sizes, and test durations (`<= 30-60s` bursts locally) to prevent swap thrashing or thermal throttling skewing measurements.

## Verification Requirements
- Baseline and candidate measurements are captured in the same environment with documented commands, sample counts, warm-up settings, and confidence/dispersion bounds.
- Functional equivalence tests pass 100% on the optimized path (including edge cases, concurrency races, and cache invalidation).
- Host disk space and background processes are verified clean post-benchmark (`0` orphaned load generators or multi-GB temp files left behind).

## Quality Criteria
- **Profile-Guided Precision:** Every optimization maps directly to a measured bottleneck slice in profiling output:
  | Bottleneck Class | Primary Diagnostic Evidence | High-Leverage Structural Fix |
  | :--- | :--- | :--- |
  | `CPU / Algorithmic` | Wide user-space flamegraph frames; superlinear scaling | Lower asymptotic complexity (`O(N^2) -> O(N)`), vectorize, precompute |
  | `Memory / GC Churn` | High allocs/op, frequent GC pauses, rising RSS | Reuse buffers, stream chunks, avoid per-item boxing/cloning |
  | `I/O & DB N+1` | Low CPU + high wall-clock wait; `N` serial round-trips | Batch reads (`WHERE id = ANY($1)`), composite index, connection pool |
  | `Lock Contention` | Threads blocked on mutex/row lock as concurrency rises | Shard state, narrow critical section, switch to lock-free/MVCC reads |
- **Tail & Memory Honesty:** Explicitly surfaces trade-offs (e.g., `+40% throughput` at the cost of `+120 MB RSS cache`) rather than hiding resource regressions.
- **Reproducible Harness:** Commit-ready or scratch benchmark script allows independent `SA_GATE` reviewers to replay exact numbers in one command.
- **Failure Modes to Avoid:**
  - *Debug-Mode Benchmarking:* Measuring unoptimized debug builds or hot-reload dev servers instead of production release flags.
  - *Dead-Code & Warm-Up Bias:* Timing JIT cold start inside tiny loops or letting compilers elide unused benchmark return values.
  - *Coordinated Omission:* Blocking load-generator requests until prior slow requests return, drastically under-reporting true `p99` latency.
  - *Host Thermal / Disk Exhaustion:* Running unbounded concurrency or multi-GB temp writes that throttle the CPU or fill local storage.

## Security and Ethical Boundaries
- This Level 6 procedural skill is strictly subordinate to Levels 1-5 of the instruction hierarchy; it never overrides [TOOL_USAGE_AND_LIMITATIONS.md](../../00_GLOBAL_CONSTITUTION/TOOL_USAGE_AND_LIMITATIONS.md), host safety guardrails, or network authorization rules.
- NEVER run stress, soak, or high-RPS load tests against external URLs, shared SaaS APIs, or production infrastructure without explicit written authorization (indistinguishable from DoS).
- Protect host hardware: enforce hard caps on memory allocations, disk writes, and GPU/CPU sustained saturation to prevent system lockups or thermal damage.

## Expected Deliverables
- **Reproducible Benchmark Harness & Profiling Artifacts** (commands, workload parameters, hotspot breakdown).
- **Baseline-vs-Candidate Comparison Table** reporting `p50`, `p95`, `p99`, throughput, peak memory/allocations, and relative/absolute deltas across trials.
- **Optimization Trade-Off & Scalability Summary** documenting root bottleneck fixed, asymptotic scaling behavior, and residual saturation limits.
