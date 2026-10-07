# Deployment

Target stable hosted **Studionet**, documented chain ID 61999 and RPC
`https://studio.genlayer.com/api`. Studio-dev 61997 is a separate release candidate;
do not substitute it silently. Current Studio sample confirms ABI v0.2.16 and pinned
runner `1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6`.

Use Studio-generated accounts/faucet, official CLI or genlayer-py. No external wallet
is needed. Before deployment, verify chain/RPC live, clean tree, passing tests,
check/validate/typecheck/schema, remote candidate commit and raw source SHA-256.
Deploy precisely that source and retain source readback. Inspect finalized lifecycle
AND GenVM success, not merely transaction submission/acceptance. A candidate source
change invalidates a previous deployment verification and requires redeployment.

Live sequence: funded create → challenge from another account → lock → Full Consensus
adjudicate → settle → inspect credits → participant withdraw → verify delivered
balances after finalization. Use long enough committed deadlines for queue latency.
Read claim, accounting, histories, authentication and decision hash. Verify explorer
links from actual UI/receipts; never synthesize transaction IDs or contract addresses.

Read docs/LIVE_VERIFICATION.md for facts observed in this execution. An integration
test/readback does not imply deployment if its contract address was never obtained.
