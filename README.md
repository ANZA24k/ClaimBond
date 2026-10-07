# ClaimBond

**A reusable GenLayer Intelligent Contract for bonded, bounded public-evidence disputes.**

A claimant commits a precise proposition, support and refutation standards, materiality,
scope, time scope, source policy, evidence fingerprints, deadlines, and a GEN bond.
The first valid challenger accepts those exact terms and stakes an equal bond behind
counter-evidence. Independent GenLayer validators retrieve the locked documents,
authenticate their bytes, interpret the standards, assess relevance and provenance,
and agree on a structured outcome. Deterministic code allocates the bonds.

Contribution type: **Intelligent Contracts**. There is no frontend, wallet-connect,
authentication, centralized backend, or database.

## Why GenLayer

The difficult step is interpreting evidence against a committed standard: a failed
optional benchmark is different from a failed mandatory check, and a record for an
older build may be irrelevant. A byte comparison cannot resolve that dispute.
Each validator repeats retrieval and analysis; it does not simply endorse a leader's
reasoning. GenLayer's equivalence rule checks the outcome, material criterion
statuses and cited source IDs, source-quality classifications, independence/staleness/
circularity flags, and bounded score differences. Fingerprint results must match exactly.
Free-form reasoning and quotations need not match word for word, but every quotation
must occur in a document that the validating node independently authenticated.

## Deliberately bounded v1

Evidence adapters currently support **commit-pinned GitHub raw UTF-8 text only**.
Every source requires SHA-256, byte length, and an allowed text media type. Four
sources per side and 16 KiB per document are hard maxima. Other immutable repositories
can be added as reviewed adapters in future protocol versions; arbitrary HTTPS is
not accepted. Fingerprints authenticate bytes, not the truth, authorship, or official
status of a document. Sources are assessed from their content, with claimed provenance
remaining a limitation. A repository owned by a party is not independent merely
because its files have different names.

Terms and manifests lock on submission; there are no editing methods. Duplicate
URLs or fingerprints within and across sides are rejected. Canonically serialized
manifest packages cannot be replayed across claims in one contract instance. This
conservative rule can also prevent legitimate reuse; deploy a separate instance for
an independent dispute using exactly the same package.

Every fetched document and all user-authored terms are untrusted prompt data.
Contract policy defines the task and output fields. Documents cannot provide payment
instructions, new evidence URLs, or a replacement resolution policy. Model output is
bounded and checked for enum, numeric, criterion, source, and citation validity.
This boundary reduces injection risk; it cannot mathematically guarantee model safety.

## Lifecycle

`OPEN → CHALLENGED → EVIDENCE_LOCKED → ADJUDICATED → SETTLED`

Anyone can lock evidence after challenge, adjudicate before the adjudication deadline,
and settle a terminal result. No participant can withdraw a bond after challenge.
There is no administrator who can override a verdict or take escrow.

If no challenge arrives, anyone can expire the claim at the challenge deadline and
settle the claimant refund: `UNCHALLENGED` means **not adjudicated**, never true.
If challenged evidence cannot reach adjudication before its deadline, anyone can
expire and settle symmetric refunds under `EXPIRED_UNADJUDICATED`. This is distinct
from an AI `INSUFFICIENT` outcome and provides a recovery path for model errors,
network outages, and consensus disagreement. The transaction timestamp determines
eligibility, rather than a validator's wall clock. At the exact boundary, challenge
or adjudication is closed and the applicable expiry is available.

## Economic model

All values use integer GEN wei. Bonds are equal and positive; challenge must send
exactly the committed amount.

| Outcome | Claimant credit | Challenger credit |
| --- | --- | --- |
| SUPPORTED | Both bonds | 0 |
| REFUTED | 0 | Both bonds |
| CONFLICTED | Own bond | Own bond |
| INSUFFICIENT | Own bond | Own bond |
| Unchallenged | Own bond | No challenger |
| Unadjudicated expiry | Own bond | Own bond |

`settle` creates withdrawal credits once. A participant calls `withdraw` to emit an
external EOA transfer on finalization. Forwarded/internal participant calls are
excluded by sender/origin equality. This is a direct-account restriction, not a
universal EVM proof that an address has no code (see SECURITY.md). Settlement,
withdrawal emission, and recipient balance delivery are separate events. The ledger
invariant is `deposits = escrow + credits + emitted`. An emitted amount is **not**
a claim of verified delivery. Onchain consumers must verify protocol finality and
actual recipient balances. Studio uses simulated GEN, not mainnet money.

## Run locally

Python 3.12+ and Node for Pyright:

```sh
pip install -r requirements.txt
pytest tests/direct -q
genvm-lint check contracts/claimbond.py
genvm-lint validate contracts/claimbond.py
genvm-lint typecheck contracts/claimbond.py
genvm-lint schema contracts/claimbond.py --output docs/abi.json
```

Official `genlayer-test` Direct Mode tests cover lifecycle, authorization, immutable
terms, bonds, URLs, counts/sizes, duplicates/replay, all outcomes, independently
replayed validator agreement/disagreement, malformed outputs, quote authentication,
source-quality disagreement, hash/length failures, expiry, canonical decision hashes,
append-only events, and withdrawal emission. A separate official GLSim integration runs five mocked validators through the full contract lifecycle. Mocks do not establish hosted consensus
or real delivery. See [verification record](docs/LIVE_VERIFICATION.md) for observed
local and hosted facts, [deployment](DEPLOYMENT.md), and [consensus](docs/CONSENSUS.md).

## Reuse and limitations

Builders can consume `get_claim`, the criterion-level result, authentication records,
`decision_hash`, and withdrawal credits without implementing an adjudicator themselves.
Useful domains include release acceptance, dataset properties, public report findings,
and documented milestones. Private information, allegations about people, opinions,
predictions, medical decisions, and legal judgments are outside this v1's purpose.

A policy can be biased; committed sources can omit decisive public facts. No validator
is allowed to silently broaden the evidence universe. `CONFLICTED` distinguishes
opposing credible records from `INSUFFICIENT` evidence. Exact fingerprints may make
unavailable sources unusable. Conservative agreement can fail even on a sensible
leader result. Expiry needs a submitted transaction and network liveness. No audited
production-security or perpetual fund-delivery guarantee is claimed.
