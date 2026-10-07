# Equivalence Principle

`gl.vm.run_nondet_unsafe(analyze, validator)` isolates retrieval and LLM execution.
The validator first independently retrieves all locked sources. It authenticates
the candidate's citation excerpts against its own verified documents, then runs
the full adjudication task independently. Storage writes happen only after consensus.

Agreement requires:

- Exact authentication reports: URLs, IDs, expected and observed hashes/lengths/status.
- Exact outcome and each locked criterion ID/status.
- Exact decisive cited-source IDs for each criterion: relevant primary/official/publication records take precedence; otherwise technical artifacts, otherwise remaining cited records. Irrelevant/missing records do not anchor a material finding.
- Exact IDs of every source classified REFUTE or CONFLICT, including uncited counter-evidence.
- Exact source class, role, independence, stale and circular flags for decisive and materially opposing records.
- All model scores remain bounded 0–100 diagnostics, with no economic or consensus authority. Incidental source labels and extra background quotations do not need exact agreement.

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

The initial hosted trial exposed valid independent verdicts that disagreed about the class of an immaterial archive and subjective independence scores. The refined rule compares critical evidence determinations while preserving strict authentication, criterion, outcome, opposing-record and decisive-quality agreement. Tests explicitly reject a changed decisive record, changed decisive independence, and added material conflict; they accept incidental label and score differences. No free-form prose chooses amounts or recipients.
