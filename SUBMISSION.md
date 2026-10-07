# ClaimBond submission package

## Project

**ClaimBond** — a bonded, bounded public-evidence dispute Intelligent Contract for GenLayer.

ClaimBond locks a proposition, support and refutation standards, materiality, scope, time scope, source policy, evidence fingerprints, deadlines and a claimant bond. One challenger can accept those exact terms with an equal bond. GenLayer validators independently retrieve and authenticate commit-pinned public evidence, assess the locked criteria and source quality, and agree on a structured outcome. Deterministic contract code controls lifecycle, settlement, credits, withdrawals, deadlines and accounting.

Outcomes are `SUPPORTED`, `REFUTED`, `CONFLICTED` and `INSUFFICIENT`. Unchallenged and unadjudicated expiry paths refund escrow without pretending that expiry is an AI judgment.

## Links

- Repository: https://github.com/ANZA24k/ClaimBond
- Contract source: [contracts/claimbond.py](contracts/claimbond.py)
- Fixture inputs: [fixtures/live_claim/inputs.json](fixtures/live_claim/inputs.json)
- Deployment instructions: [DEPLOYMENT.md](DEPLOYMENT.md)
- Verification record: [docs/LIVE_VERIFICATION.md](docs/LIVE_VERIFICATION.md)

## Recommended tags

AI & Agents; Verifiable Inference; Developer Tools.

## Current source binding

- Deployment candidate commit: `701a37d48e26987d66cf1ddd51677d31eb22d979`
- Canonical source: `contracts/claimbond.py`
- Source SHA-256: `66889798a1864b37661e9b46e6736f8f5193cfdd22da6ab1675ab7818ed9a27f`
- Source length: 23,963 bytes
- Current source status: GitHub-published and locally verified; a hosted redeployment of this exact commit is still required before a current contract address can be submitted.

## Verification

- Direct Mode: 68 passed.
- GLSim integration: 1 passed with five mocked validators agreeing on `SUPPORTED`.
- GenVM lint check and validation: passed.
- Pyright/typecheck: passed.
- ABI schema extraction: passed.
- CI: [run 37671259064](https://github.com/ANZA24k/ClaimBond/actions/runs/37671259064), successful on the current source commit.

These local and CI results do not claim hosted GenVM execution or hosted Full Consensus.

## Historical hosted attempt

An earlier candidate at commit `44c921e2d259da89be40c3d9a2f28dc5389fd0fe` was deployed on stable Studionet (chain 61999) at:

`0x50ceAE711B4a1c04a720101B382AfC55DB4E89B3`

The earlier candidate reached a Full Consensus `SUPPORTED` result. Its exact lifecycle transaction receipts were not retained in the repository. This address is historical and must not be used as proof for the current `701a37d` source.

## Scope

This is intentionally contract-focused. It has no wallet-connect UI, authentication system, backend, database or unnecessary frontend. Studio-provided accounts and simulated Studionet GEN are sufficient for deployment and testing.

## Copy-ready description

ClaimBond is a GenLayer Intelligent Contract for bonded public-evidence disputes. A claimant locks a precise proposition, resolution standard, bounded commit-pinned evidence package, deadlines and a GEN bond. One challenger accepts the same terms with an equal bond. Validators independently retrieve and authenticate both evidence packages, interpret the locked criteria, classify source quality and reach an equivalent structured outcome: SUPPORTED, REFUTED, CONFLICTED or INSUFFICIENT. Deterministic rules enforce authorization, immutable terms, replay protection, expiry, settlement, withdrawal credits and accounting. The repository contains the canonical contract, fixtures, Direct Mode tests, GLSim integration, ABI and CI checks. No external wallet, website, backend or database is required.
