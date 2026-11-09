# End-to-End Walkthrough: Level 0 Instant Interaction (`SIMPLE_TASK.md`)

> **Walkthrough Governance:** Demonstrates proportional zero-overhead execution for **Complexity Level 0** per [TASK_COMPLEXITY_ROUTER.md](../00_GLOBAL_CONSTITUTION/TASK_COMPLEXITY_ROUTER.md), [COGNITIVE_EXECUTION.md](../00_GLOBAL_CONSTITUTION/COGNITIVE_EXECUTION.md), and [INDEPENDENT_VERIFICATION.md](../00_GLOBAL_CONSTITUTION/INDEPENDENT_VERIFICATION.md).

---

## 1. Realistic User Scenario
**User Prompt:**
> "In our repo's `config/cdn_headers.json`, what does `Cache-Control: public, s-maxage=900, max-age=60, stale-while-revalidate=120` actually do for browsers vs. CloudFront edge caches, and how many requests hit origin per hour for a single edge POP under steady 50 RPS traffic?"

---

## 2. Complexity Classification (`Level 0 — Direct Factual / Trivial Lookup`)
Before acting, the main agent evaluates the request against [TASK_COMPLEXITY_ROUTER.md](../00_GLOBAL_CONSTITUTION/TASK_COMPLEXITY_ROUTER.md):
- **File Mutation Scope:** `0` files created, edited, or deleted (strictly read-only inspection of `config/cdn_headers.json`).
- **Architectural / Security / Regulatory Risk:** None (`0` credentials, `0` external network mutations, `0` destructive commands).
- **Subagent & Artifact Footprint:**
  - **Spawned Subagents:** `0` (`PM` and `SA` subagents are **NOT** instantiated).
  - **Templates Instantiated:** `0` (**NEVER** create or update `PROJECT_MANIFEST.md`, `PROJECT_STATE.md`, or `AGENT_COMMUNICATE.md` on `Level 0` interactions).
  - **Escalation Check:** Confirmed `config/cdn_headers.json` contains no misconfigured auth-cookie caching rule that would trigger escalation to `Level 1`/`Level 2`.

---

## 3. Inline Cognitive Execution & Read-Only Verification
Even at `Level 0`, the main agent applies lightweight cognitive discipline (`Understand -> Inspect -> Compute -> Verify`):

1. **Read-Only File Verification (`read_file`):**
   - Reads target workspace file `config/cdn_headers.json` to confirm whether `Vary: Authorization` or private session routes share that policy before answering.
   - Observed contents of `config/cdn_headers.json`:
     ```json
     {
       "staticCatalogRoute": "/api/v1/public/catalog",
       "cacheControl": "public, s-maxage=900, max-age=60, stale-while-revalidate=120"
     }
     ```
2. **Standards & Arithmetic Verification (RFC 9111 + RFC 5861):**
   - **Browser Behavior (`max-age=60`):** Shared-cache directive `s-maxage` is ignored by private browser caches. A browser treats the response as fresh for `60s`; between `60s` and `180s` (`60 + 120`), the browser may serve the cached response immediately while issuing an asynchronous background revalidation request.
   - **CDN Edge POP Behavior (`s-maxage=900`):** Shared edge cache overrides `max-age=60` with `s-maxage=900` (`15 minutes`). Between `900s` and `1,020s` (`900 + 120`), under steady `50 RPS`, the first request arriving after `t = 900s` triggers a single asynchronous origin revalidation (`If-None-Match` / `If-Modified-Since`) while concurrent edge requests continue receiving cached responses without origin stampede.
   - **Origin Request Rate Calculation:**
     - Cycle period under continuous `50 RPS` (`1` request every `20 ms`): revalidation triggers virtually immediately at `t = 900.02s`.
     - Origin requests per `3,600s` hour from `1` single-key edge POP (assuming `100%` cache residency, single URL/cache key, no evictions or invalidations):
       $$\frac{3600\text{ seconds}}{900\text{ seconds/refresh}} = 4\text{ origin revalidation requests/hour}$$

---

## 4. Direct User Response Delivered (`Zero "AI Sign"` Overhead)
The main agent responds directly without governance ceremony, decorative emojis, or filler:

> **`config/cdn_headers.json` Policy Breakdown (`/api/v1/public/catalog`):**
>
> 1. **Browser Cache (`private` client):** Honors `max-age=60` (ignores `s-maxage`). Responses are fresh for **60s**. If a user triggers another request between **60s and 180s** (`60s + 120s`), the browser serves the cached payload immediately and revalidates asynchronously in the background; after **180s**, the browser blocks on a synchronous network fetch.
> 2. **CloudFront Edge POP (`shared` cache):** Overrides `max-age` with `s-maxage=900` (**15 minutes**). Under steady **50 RPS**, when TTL expires at **900s**, `stale-while-revalidate=120` allows the POP to keep serving cached responses with zero latency spike while sending a single background conditional revalidation request to origin.
> 3. **Origin Load per Edge POP (50 RPS):**
>    - **Verified Formula:** `3,600s / 900s = 4 origin requests/hour` per unique cache key per POP.
>    - **Key Assumptions:** Single normalized URL/query cache key, steady traffic (`>= 1` request within the `120s` SWR window), no LRU cache eviction before `900s`, and origin responds within `120s`. Multiply by `(distinct cache keys x active POPs / origin shield factor)` for fleet-wide origin RPS.

---

## 5. Escalation Triggers Audited & Confirmed Absent
Per [TASK_COMPLEXITY_ROUTER.md](../00_GLOBAL_CONSTITUTION/TASK_COMPLEXITY_ROUTER.md), the main agent verified none of the following escalation conditions applied before answering at `Level 0`:
- User did **not** ask to modify `config/cdn_headers.json` or Terraform CloudFront behaviors (which would escalate to `Level 1`).
- Route `/api/v1/public/catalog` does **not** serve authenticated user PII or `Set-Cookie` headers under `Cache-Control: public` (which would escalate to a security defect advisory).
- Calculation required deterministic RFC arithmetic with zero external ambiguity.

---

## 6. Governance & Verification Summary
| Check | Target Rule | Outcome |
| :--- | :--- | :--- |
| **Proportionality** | `0` subagents spawned, `0` templates or state files created | `PASS` |
| **Factual Grounding** | Inspected `config/cdn_headers.json` directly + verified RFC 9111 / RFC 5861 semantics | `PASS` |
| **Epistemic Clarity** | Explicitly separated verified `4 req/hr` formula from cache-key, eviction, and Origin Shield assumptions | `PASS` |
| **Zero `"AI Sign"` Prose** | Concise direct engineering answer with zero decorative emojis or governance boilerplate | `PASS` |
