# Architecture

`contracts/claimbond.py` is a single deployable source. Storage uses `TreeMap[u256,str]`
for canonical JSON records, `TreeMap[Address,u256]` for credits, a package-replay map,
and `DynArray[str]` for append-only hashed transitions. Normal Python dictionaries
and lists exist only in memory; no storage object is captured by nondet closures.

The exact source runner is pinned in the dependency header. All identifiers,
authorization, deadlines, paid value checks, uniqueness, terms/manifest hashing,
state transitions, allocations and ledger updates run deterministically.

Create assigns increasing IDs and locks terms immediately. Challenge fills the only
challenger slot atomically. No public method alters either evidence package. Lock
is an explicit auditable transition; it can happen immediately after challenge
because both manifests are already final. Adjudicate can run once before expiry.
Settle moves escrow to credits once; withdrawal consumes each credit before emitting.
A refund path exists from each unresolved state once its committed deadline arrives.
An already-adjudicated decision remains settleable even after that deadline.

## Hashes

Canonical JSON uses sorted keys, ASCII escaping, no whitespace, and integer values.
Manifests sort by canonical URL; duplicate JSON keys are rejected. Terms hash binds
protocol, claimant address, claimant bond and every term. Decision hash binds protocol,
claim ID, both participants, terms hash, both manifest hashes, authenticated structured
verdict and settlement allocation. Source SHA-256 is over raw file bytes without any
normalization. Each history entry hashes its exact post-transition claim record.

## Limits

Eight criterion IDs; four sources per side; 16,384 bytes per source; 512-character
URLs; 1,000-character interpretation/reasoning; eight 300-character items per prose
list; bounded exact quotations; 16,000-character total verdict. Challenge windows
are at most 30 days and adjudication windows at most seven additional days. Bonds
are equal, positive and individually less than 2^128; aggregates use u256.
