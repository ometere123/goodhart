# GOODHART consensus boundary

GOODHART uses GenLayer consensus only for the part a deterministic contract
cannot safely infer: whether complete, frozen public outcome sources affirm the
predeclared underlying objective. It never asks a model to calculate a reward,
choose a recipient or mutate programme state.

## Deterministic boundary

`Goodhart.register_program` authenticates the owner, stores the typed
beneficiary, freezes the objective, indicator, proxy schema, three URLs and
time window, and computes a domain-separated fingerprint. `_improved` performs
exact integer basis-point arithmetic. `_decision` maps the two semantic
outcomes to stable statuses. `assess` validates the current fingerprint,
owner, window and bounded attempts before committing a terminal `Receipt`.
`is_rewardable` is a deterministic conjunction of the registered fingerprint,
receipt fingerprint and `REWARDABLE` states.

## Leader path

The `assess` method calls `_consensus`. The leader callback calls `_observe`,
which invokes `_fetch` for the proxy and both frozen outcome URLs. `_clean_page`
accepts only a complete normalized body under the 12,000-character / 48,000-byte
bound; it never truncates. `_proxy_json` parses the exact four-field schema and
the contract computes the numeric threshold. `_outcome` asks `_prompt` to
classify the underlying objective, requires a unique verbatim quote for a
conclusive label, and runs `_audit_prompt` for every `IMPROVED` result.

HTTP 4xx, redirects, final-URL changes, empty/oversized bodies and source
identity failures are non-transient and fail closed. Timeouts, rate limits and
5xx responses are the only bounded retry class. A second unresolved transient
result becomes terminal `INCONCLUSIVE`.

## Validator path

The validator receives only the typed `gl.vm.Return` proposal. It first checks
the exact schema in `_valid_observation`, then calls `_observe` independently:
the validator fetches and interprets the frozen proxy and both outcome sources
again. It compares status, numeric proxy value, proxy digest, outcome labels and
outcome digests. For conclusive proposals it fetches each source again, checks
that the leader’s quote occurs exactly once in the complete independently
retrieved snapshot, recomputes the URL-bound digest and runs
`_audit_witness` before accepting `REWARDABLE`.

This is substantive recomputation, not JSON-shape voting. A leader cannot
authorize a cached excerpt, substitute a source or turn `UNKNOWN`, `MIXED`,
missing, malformed, oversized or stale evidence into a positive state. A source
digest binds the URL and normalized bytes observed at assessment; it does not
authenticate publisher ownership, truth, causality or future freshness.

## Evidence trust model

Three different hostnames are not three authenticated publishers. The stable
runtime can bind URLs, bytes, digests and transaction actors; it cannot prove
that a real-world organization owns a hostname or that two reports measured
independent populations. An attestor/signature registry was deliberately not
added because no trusted authority root is present in this protocol. Those
properties remain human/governance assumptions and are disclosed in
[`EVIDENCE_MANIFEST.md`](EVIDENCE_MANIFEST.md).

## Current live result

The corrected primary at
`0x9aAB4148ff9C939Be58C64dD5bfa0FCFecBDA881` has both a fail-closed external
control and a finalized controlled positive mechanics proof. The CERT-EU /
Debian XZ transaction
`0x68dd7b602f83193be6ed03a388fa7beefb26cbb633c72fd111d191d4e781edae`
returned `INCONCLUSIVE`, with proxy `20 -> 80` and both outcomes `UNKNOWN`.
The controlled programme assessment
`0xf20659666a3b89cee1e6bd0076d150e8ab2b4c5c16765f87863630c079c32fb2`
finalized `REWARDABLE` after a single bounded retry. Its exact RewardGate
action succeeded and the identical replay was rejected; details are in
`DEPLOYMENT.md`. The positive fixture demonstrates consensus and consumer
binding mechanics, not publisher authentication or real-world causality.
