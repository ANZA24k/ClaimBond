# Evidence format and fixture

Submit a JSON object with a `sources` array. Each source contains exactly `url`,
`sha256` (64 lowercase hex characters), `bytes` (positive integer), and `media_type`
(`text/plain`, `text/markdown`, or `application/json`). All fingerprints are mandatory.

Supported canonical URLs match HTTPS `raw.githubusercontent.com/OWNER/REPO/40-HEX-COMMIT/PATH`.
No query, fragment, userinfo, port, percent escapes, Unicode authority, branch name,
empty segment, dot segment, or nonallowlisted host is accepted. Literal IPs, localhost,
private hosts and alternate authorities are consequently rejected before a fetch.

SDK v0.2.16 returns `Response.status`, not `status_code` shown in parts of the general
web guide. The exact SDK was inspected and typechecked. The SDK does not expose a
per-request streaming byte cap, timeout, or redirect-limit parameter. The contract
checks response length before hashing/decoding and admitting evidence. This is an
application-level cap, not a predownload cap. Host-enforced transport/redirect policies
remain necessary; do not claim the allowlist alone controls DNS or hidden redirects.
Unsuccessful, oversized, hash-mismatched, length-mismatched or non-UTF-8 data cannot
be cited. HTTP errors and fetch exceptions are recorded as unavailable.

Fixture commit: `9e9ecbc5572f5d6746f07a0a6ae8792303fec176`.
The policy requires mandatory checks C1–C3 for R-17, tolerates optional benchmark
failure and excludes R-16 records. The primary report passes mandatory R-17 checks,
the secondary digest is derivative, and the challenger discusses the old build and
optional benchmark. Expected interpretive outcome: SUPPORTED, not a live result.
`scripts/build_fixture.py` emits exact manifests and input terms for Studio.
