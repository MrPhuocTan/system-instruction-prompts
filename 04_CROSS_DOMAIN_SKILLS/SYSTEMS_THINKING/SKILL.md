---
name: systems-thinking
description: "Use this skill when designing architectures, diagnosing cascading failures, modeling socio-technical workflows, or evaluating cross-module changes with feedback loops, bottlenecks, and second-order effects."
---

# Systems Thinking

## Skill Metadata
- **Skill ID:** `SKL-CORE-003`
- **Name:** `systems-thinking`
- **Domain:** `CROSS_DOMAIN`
- **Version:** `1.0.0`

## Purpose
Analyze software platforms, industrial processes, financial markets, supply chains, and multi-agent workflows as interconnected dynamic systems rather than isolated components. This skill surfaces stocks and flows, reinforcing and balancing feedback loops, time delays, non-linear saturation points, tight coupling hazards, and unintended second- and third-order consequences before local optimizations degrade whole-system resilience.

## Required Competencies
- System boundary definition, interface contract mapping, and dependency graph topology analysis.
- Feedback loop modeling (reinforcing loops, balancing loops, retry storms, cache stampedes, bullwhip effects).
- Queueing, throughput, backpressure, and bottleneck theory (Little's Law, Amdahl's Law, Theory of Constraints).
- Socio-technical incentive alignment (Goodhart's Law, Conway's Law, alert fatigue, operational handoff friction).

## Prerequisites
- Architectural diagrams, repository module dependency trees, process maps, or operational telemetry inspected via `read_file` or `run_command`.
- Clear definition of system-wide invariants (SLOs, safety margins, financial solvency bounds, data consistency guarantees).
- Alignment with `SA` architectural boundaries when operating on Level 2-4 multi-workstream projects.

## Workflow
1. **Define System Boundaries & Environment:** Identify inside-the-system components, external upstream/downstream actors, trust boundaries, shared mutable state, and environmental stressors.
2. **Map Stocks, Flows, and Coupling:** Trace resource stocks (queues, connection pools, memory buffers, inventory, capital) and flow rates (ingest, processing, eviction, depletion), flagging synchronous tight coupling and single points of failure.
3. **Trace Feedback Loops & Time Delays:** Identify reinforcing loops (e.g., timeout -> retry -> higher load -> cascading timeout) and balancing loops (autoscaling, rate limiting, circuit breaking), explicitly quantifying observation-to-actuation lag.
4. **Locate Active & Latent Bottlenecks:** Find the current throughput constraint and calculate which downstream resource saturates next once the primary bottleneck is widened.
5. **Project Second- & Third-Order Effects:** Evaluate how a proposed local change alters upstream demand, downstream pressure, operational toil, security attack surface, and human incentives (`Goodhart's Law`).
6. **Design Structural Leverage & Circuit Breakers:** Introduce bounded queues, idempotency, load shedding, bulkheads, decoupled contracts, or incentive corrections at high-leverage control points.

## Tools and Techniques
- **Causal Loop & Stock-Flow Mapping:** Represent reinforcing (`R`) and balancing (`B`) loops with explicit polarity and delay annotations in Mermaid `flowchart` or `stateDiagram-v2` diagrams.
- **Little's Law & Saturation Check (`L = lambda * W`):** Verify concurrency, queue depth, and latency relationships under peak burst arrival rates rather than mean load.
- **Blast-Radius & Failure-Propagation Matrix:** Trace how partial degradation (slow dependency, split-brain network, stale cache, corrupted batch) propagates across module boundaries.
- **Dependency Graph Extraction:** Use `run_command` static importers, build graphs, or schema lineage queries to verify actual coupling vs. outdated architecture diagrams.

## Verification Requirements
- Dependency and data-flow claims are cross-checked against actual code imports, infrastructure configs, or process definitions rather than assumed architecture.
- Every proposed optimization explicitly verifies that shifting load does not breach downstream capacity, safety, or consistency invariants.
- Degraded-mode and backpressure behaviors (timeouts, retries, dead-letter handling, graceful fallback) are validated empirically or modeled with bounded worst-case parameters.

## Quality Criteria
- **Whole-System Optimization:** Local efficiency gains never compromise global reliability, safety margins, or data integrity.
- **Explicit Delay & Contention Accounting:** Scaling, caching, and control-loop designs account for cold-start latency, coordination overhead, and lock contention:
  | Systemic Dynamic | Observable Warning Signal | Structural Countermeasure |
  | :--- | :--- | :--- |
  | Reinforcing Retry Storm | Rising `429/503` rate + exponential traffic spike | Jittered exponential backoff + retry budgets + circuit breaker |
  | Cache Stampede (`Thundering Herd`) | Hot-key TTL expiry causing DB CPU saturation | Request coalescing (`singleflight`) + staggered probabilistic TTLs |
  | Unbounded Queue Growth | Monotonic memory RSS climb + tail latency explosion | Bounded queue capacity + explicit load shedding / backpressure |
  | Downstream Bottleneck Shift | Optimized service overwhelms legacy DB/partner API | Per-dependency concurrency bulkheads + token-bucket rate limits |
- **Clear Interface Isolation:** Cross-component interactions occur through versioned, contract-governed boundaries without hidden shared state.
- **Failure Modes to Avoid:**
  - *Local Sub-Optimization:* Speeding up an upstream producer only to crash an unbuffered downstream datastore.
  - *Synchronous Chain Coupling:* Chaining 5+ blocking RPCs where aggregate availability degrades multiplicatively (`0.99^5 = 95.1%`).
  - *Silent Feedback Delays:* Auto-scaling on lagging averages that oscillate wildly under bursty traffic.
  - *Incentive Distortion:* Optimizing narrow component KPIs that degrade end-to-end user reliability.

## Security and Ethical Boundaries
- This Level 6 procedural skill is strictly subordinate to Levels 1-5 of the instruction hierarchy; it never overrides [GLOBAL_SYSTEM_PROMPT.md](../../00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md), least-privilege isolation, or human approval gates.
- Never collapse security trust boundaries, audit logging, or separation-of-duties controls merely to reduce local latency or coordination steps.
- Escalate cross-workstream interface or write-lock impacts immediately to `SA` and `PM` via [AGENT_COMMUNICATE.md](../../06_TEMPLATES/AGENT_COMMUNICATE.md).

## Expected Deliverables
- **System Topology & Feedback Analysis** (component boundaries, stocks/flows, reinforcing/balancing loops, and time delays).
- **Bottleneck & Blast-Radius Assessment** identifying primary constraints, next-in-line saturation risks, and cascading failure paths.
- **Structural Mitigation & Control Specification** (bulkheads, backpressure rules, interface invariants, and monitoring signals).
