# Equivalence Principle

`gl.vm.run_nondet_unsafe(analyze, validator)` isolates retrieval and LLM execution.
The validator first independently retrieves all locked sources. It authenticates
the candidate's citation excerpts against its own verified documents, then runs
the full adjudication task independently. Storage writes happen only after consensus.

Agreement requires:

- Exact authentication reports: URLs, IDs, expected and observed hashes/lengths/status.
- Exact outcome and each locked criterion ID/status.
- Exact set of cited source IDs for each criterion (different valid excerpts allowed).
- Exact source classifications, material roles, independence, stale and circular flags.
- Every 0–100 score within 15 points of the independently produced score.

These are decision-critical structured fields, rather than exact LLM prose. Criterion
IDs anchor stable material facts and material conflicts to the committed task.
Independent material conflict classifications must match, not merely a count of
conflicts. Prose fact lists are explanatory; economic decisions follow the structured
outcome. Leader output schema and quotations must validate on each validator.

Authentication comparison is strict equality inside the custom equivalence rule,
not strict equality over arbitrary LLM responses. Failed leader results are rejected;
validator errors return disagreement. There is no nested nondet execution or a model
prompt asking whether the leader 'sounds reasonable.' Timeout refunds preserve the
absence of a judgment rather than relabeling disagreement as factual insufficiency.
