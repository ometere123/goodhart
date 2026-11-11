# GOODHART consensus boundary

GOODHART uses GenLayer consensus only for whether complete, frozen public outcome sources affirm the predeclared objective. It never asks a model to calculate a reward, choose a recipient or mutate programme state.

## Deterministic state and consent

Goodhart.register_program authenticates the owner, stores the typed beneficiary, freezes the objective, indicator, proxy schema, three URLs and time window, and computes a domain-separated fingerprint. accept_program requires the actual beneficiary sender and exact fingerprint before earliest_at; it records accepted and accepted_at permanently. cancel is owner-only and rejects accepted programmes. assess requires PENDING, acceptance, the current fingerprint, the frozen window, and an owner or beneficiary sender. _improved performs exact integer basis-point arithmetic. _decision maps semantic outcomes to stable statuses. is_rewardable is a deterministic conjunction of the registered fingerprint, receipt fingerprint and REWARDABLE states.

## Leader and validator paths

assess calls _consensus. The leader calls _observe, which fetches the proxy and both frozen outcome URLs. _clean_page accepts only a complete normalized body under the 12,000-character / 48,000-byte bound; it never truncates. _proxy_json parses the exact schema and the contract computes numeric thresholds. _outcome classifies the underlying objective, requires a unique verbatim quote for conclusive labels, and runs the positive compatible-reading audit.

The validator receives only the typed proposal, checks its exact schema, then calls _observe independently. It re-fetches and reinterprets all frozen sources, recomputes numeric values and material labels, compares digests, verifies cross-field status rules, checks quotes against the complete snapshot and repeats the adversarial witness audit. This is substantive recomputation, not JSON-shape voting.

HTTP errors, redirects, final-URL changes, permanent failures, empty or oversized bodies fail closed. Timeouts, rate limits and 5xx responses are bounded retry cases; unresolved recovery cannot create a reward.

## Evidence trust model

Three hostnames are not three authenticated publishers. The stable runtime can bind URLs, bytes, digests and transaction actors, but cannot prove real-world ownership or independent measurement. No decorative attestation contract was added because no trusted authority root exists.

## Current boundary

The consented primary is 0xc6f159b8A0475D32c39033131D5b4E496581f38a. Its beneficiary assessment 0x339d9a253852b49287f4e7607d4e6bee17056a001a10f73051f41a1e8ab32731 finalized successfully but returned INCONCLUSIVE with UNKNOWN / UNKNOWN. A fresh positive assessment finalized MAJORITY_DISAGREE and left its programme pending. Historical positive and RewardGate receipts are retained but are not proof of this source.
