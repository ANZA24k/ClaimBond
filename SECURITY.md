# Security model

This is an experimental Studionet contract, not an audited production escrow.

| Risk | Mitigation and residual limitation |
| --- | --- |
| Prompt injection and malicious documents | Contract policy separates locked user terms and evidence as JSON data. Output shape/quotes are validated; independent models reanalyze. Model susceptibility remains. |
| Biased evidence and malicious claims | Bounded categories, scope, criteria and locked source policy; only committed documents considered. Omitted facts and deceptive standards remain possible. Avoid private allegations. |
| False provenance, prestige and secondary evidence | Validators classify sources and compare logical relevance; fingerprints prove bytes, not author identity. Derivative/circular sources do not become independent evidence. |
| Mutable or stale sources | Only commit-pinned raw paths with mandatory hash and length accepted. Validators compare build/time scope. Repository disappearance remains possible. |
| Conflicting/inaccessible sources | Separate CONFLICTED and INSUFFICIENT outcomes, both refund each party; timeout is separately unadjudicated. |
| Parser attacks and SSRF | Single strict ASCII URL grammar; no userinfo, IPs, ports, encodings, queries/fragments, dot segments or mutable branches. DNS/transport redirect controls belong to GenVM host; they are not enforceable with this SDK's request parameters. |
| Oversized responses | Manifest byte bounds and response admission caps before decode/prompt. No streaming predownload limit in v0.2.16 SDK. |
| Substitution, replay and duplicate packages | Exact fingerprint checks; terms/manifests immutable; canonical package hash registry; cross-side URLs/content rejected. Registry scope is one deployment. |
| Challenge front-running | First valid challenger wins. Front-running an observed challenge remains possible. Exact equal bond and immutable terms prevent terms manipulation, not mempool ordering. |
| Deadline attacks | Half-open transaction timestamp windows, fixed deadlines, permissionless expiry and settlement. Network delay can exclude otherwise timely submissions; model load can force neutral expiry. |
| Bond accounting/double settlement | Integer u256 ledgers, bounded positive symmetric bonds, exact value, terminal-state guards and deposit invariant. No fee deduction or AI-chosen payment amounts. |
| Consensus disagreement | Independently rerun analysis; strict material facts/source findings, bounded score tolerance. Expiry provides own-bond refunds if a new transaction can be processed. |
| Transfer/message failure | Pull credits, checks-before-emission, finalization-only external transfers, direct participant sender/origin restriction. Emission is recorded separately from delivery. Never retry a transfer blindly or refund an already-emitted amount. SDK exposes no safe arbitrary transfer acknowledgment/recovery primitive. |
| Contract/delegated recipients | V1 intended for ordinary Studio EOAs. Sender==origin rejects forwarded calls but is not a general no-code proof on all EVM networks. Code-bearing/delegated EOAs and production chain behavior require additional reviewed integration before production use. |
| Network finality and liveness | Accepted is not necessarily successful or finalized. Consumers verify execution success, finality, messages and balances. No application can promise recovery during a permanent chain outage. |

There is no privileged upgrade, adjudicator override, fee recipient, arbitrary transfer
destination, or contract-owner withdrawal. Do not publish keys or secrets in evidence.
Report defects through the repository's private security reporting where enabled.
