# Quality Checklist: NLP Engineer (`ROLE-AIML-005`)

- **Role:** [`NLP_ENGINEER`](./SYSTEM_PROMPT.md)
- **Domain Gates:** [`QUALITY_GATES.md`](../../QUALITY_GATES.md)

---

## 1. Corpus Hygiene, Deduplication & Split Safety
- [ ] Grouped `train`/`val`/`test` splits strictly by `document_id`, `thread_id`, or `author_id` and ran `MinHash LSH` near-duplicate detection across splits.
- [ ] Verified Unicode normalization (`NFC`/`NFKC`), HTML/mojibake cleanup, and input-length/regex safety (`0` `ReDoS` catastrophic backtracking patterns on untrusted text).

## 2. Tokenization, Chunking & Span Offset Integrity
- [ ] Pinned immutable tokenizer artifacts (`tokenizer.json`, special tokens, casing/stripping flags) alongside model weights.
- [ ] Passed unit tests proving character-to-token-to-character span offsets (`start`, `end`) reconstruct exact source substrings across multi-byte UTF-8 characters, CJK scripts, RTL text, and diacritics.
- [ ] Handled documents exceeding `max_seq_length` explicitly via overlapping strided windows with boundary-aware span merging rather than silent tail truncation.

## 3. Baseline Comparison, Vector Parity & Task-Exact Metrics
- [ ] Benchmarked neural encoder/retriever against `TF-IDF + Linear` (classification) or `BM25` (retrieval) baselines across accuracy, `p99` latency, and memory cost.
- [ ] Reported strict entity-span `F1` (never token-level accuracy alone) for `NER`, `NDCG@k`/`Recall@k`/`MRR` for retrieval, and calibrated probabilities (`ECE`) for classifiers.
- [ ] Verified asymmetric bi-encoder query/passage prefixes, embedding L2 normalization / distance metric consistency, and mandatory index rebuilds upon embedding model version changes.

## 4. Multilingual, Adversarial & Privacy Checks
- [ ] Evaluated disaggregated slice performance across languages, dialects, short/acronym queries, OCR/typo noise, and zero-width/homoglyph Unicode perturbations.
- [ ] Scrubbed `PII`/`PHI` and secrets prior to corpus persistence or vector store indexing and enforced tenant ACL filters at retrieval time.

## 5. Independent Verification & Handoff Completeness
- [ ] Executed automated `pytest` suite verifying Unicode normalization idempotency, byte/char/token span alignment, empty/whitespace-only input handling, and `ONNX`/PyTorch numerical parity.
- [ ] Verified valid `BIO`/`BILOU` sequence-tag transitions (`0` illegal orphan `I-` tags) on sequence-labeling outputs.
- [ ] Packaged immutable `tokenizer.json`, label-to-ID map, and embedding model version contract for [`LLM_ENGINEER`](../LLM_ENGINEER/SYSTEM_PROMPT.md) or [`MLOPS_ENGINEER`](../MLOPS_ENGINEER/SYSTEM_PROMPT.md).
- [ ] Explicitly separated empirically verified local recall/latency benchmarks from `NOT VERIFIED` multi-million-document distributed index assumptions.
