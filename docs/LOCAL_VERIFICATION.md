# Local verification

2026-10-07 UTC. Canonical raw source SHA-256: `66889798a1864b37661e9b46e6736f8f5193cfdd22da6ab1675ab7818ed9a27f`.

- Official genlayer-test 0.29.2 Direct Mode: 68 passed.
- Official GLSim integration: 1 passed; five mocked validators agreed on SUPPORTED; settlement credits were 20/0 units.
- genvm-linter 0.11.0 check and validate: passed.
- Pyright via genvm-lint typecheck: no errors.
- ABI schema extraction: passed; 11 public methods (4 view, 7 write).
- Cloudpickle closure roundtrip and JSON/storage readback: passed.

These are local native execution and SDK/schema checks, not proof of hosted GenVM execution or hosted Full Consensus. Withdrawal test verifies emission/accounting, not external delivery.

Official references consulted:

- https://docs.genlayer.com/full-documentation.txt
- https://docs.genlayer.com/developers/intelligent-contracts/features/non-determinism
- https://docs.genlayer.com/developers/intelligent-contracts/features/storage
- https://docs.genlayer.com/developers/intelligent-contracts/features/web-access
- https://docs.genlayer.com/developers/intelligent-contracts/features/transaction-context
- https://docs.genlayer.com/developers/intelligent-contracts/features/value-transfers
- https://docs.genlayer.com/api-references/genlayer-test/direct
- https://docs.genlayer.com/api-references/genlayer-linter
- https://docs.genlayer.com/developers/intelligent-contracts/deploying/network-configuration

The Studio sample's v0.2.16 pin was also observed directly. General docs occasionally use Response.status_code; the pinned SDK declares Response.status, which this contract uses. A newer runner advertised by the linter is not substituted into the stable Studio target.
