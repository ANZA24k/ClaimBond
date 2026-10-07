# ClaimBond verification record

## Current status

The current deployment candidate is commit `701a37d48e26987d66cf1ddd51677d31eb22d979`.
It is published on `main`, locally verified and covered by the successful GitHub Actions
run [37671259064](https://github.com/ANZA24k/ClaimBond/actions/runs/37671259064).

A hosted Studionet deployment of this exact current commit is **not yet confirmed**.
There is intentionally no current contract address, deployment transaction, lifecycle
receipt, Full Consensus receipt or current decision hash in this record.

## Current source identity

- Canonical source: `contracts/claimbond.py`
- SHA-256: `66889798a1864b37661e9b46e6736f8f5193cfdd22da6ab1675ab7818ed9a27f`
- Length: 23,963 bytes
- Fixture commit: `9e9ecbc5572f5d6746f07a0a6ae8792303fec176`
- Network target: stable Studionet, chain 61999
- RPC: `https://studio.genlayer.com/api`

## Local and CI verification

The official Direct Mode suite reports 68 passed. The official GLSim integration reports
one passed run with five mocked validators agreeing on `SUPPORTED`. GenVM lint check,
semantic validation, Pyright/typecheck and ABI schema extraction passed. These tests use
native or mocked execution and do not establish hosted GenVM execution or hosted Full
Consensus.

The CI workflow runs:

- `genvm-lint check contracts/claimbond.py`
- `genvm-lint validate contracts/claimbond.py`
- `genvm-lint typecheck contracts/claimbond.py`
- ABI schema extraction
- `pytest tests/direct -q`
- `pytest tests/integration -q`

## Historical hosted attempt

An earlier candidate at commit
`44c921e2d259da89be40c3d9a2f28dc5389fd0fe` was deployed on stable Studionet at:

`0x50ceAE711B4a1c04a720101B382AfC55DB4E89B3`

The earlier candidate reached a Full Consensus `SUPPORTED` result after validator
rotations. The exact deployment, create, challenge, lock, adjudication, settlement and
withdrawal transaction hashes were not retained in the repository. This address and
result are historical only; they do not verify the current `701a37d` source.

## Required current hosted proof

After deploying the exact current source bytes, record only finalized observations:

1. deployment address and finalized deployment transaction;
2. Explorer source readback matching the current commit and SHA-256;
3. create claim from the claimant account with the committed bond;
4. challenge from a separate funded account with the equal bond;
5. evidence lock and Full Consensus adjudication;
6. settled claim, outcome, decision hash and accounting;
7. finalized withdrawals and post-withdrawal credits/balances.

Do not copy the historical address into the current submission fields.
