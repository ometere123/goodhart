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

## Consumer binding and current boundary

RewardGate first reads the exact programme from the typed Goodhart interface and
requires its id, fingerprint and authenticated beneficiary to equal the
consumer’s frozen constructor values. Only then does it call
`is_rewardable`; the caller must also be that same beneficiary and provide the
exact unused action hash. A constructor-supplied beneficiary cannot authorize a
different beneficiary’s programme.

The corrected primary is
0xbea069743269137772E42873aB0D2dE3E9EDC411. Its bound control programme is
PENDING/nonrewardable. The current gate at
0x46c240DCAA5bDD440f0C41a3499a4096471e2F8B rejected a correct action against
that state, an action substitution and an unauthorized caller; all finalized
with rollback and `was_executed=false`. Historical positive and RewardGate
receipts are retained but are not proof of this corrected source.
