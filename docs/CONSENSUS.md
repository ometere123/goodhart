# GOODHART consensus boundary

GOODHART uses GenLayer consensus only for the part of the decision that a
deterministic contract cannot safely infer: whether two frozen public outcome
surfaces affirmatively support improvement of the predeclared underlying
objective.

## Deterministic boundary

`Goodhart.register_program` freezes the owner, typed beneficiary, objective,
indicator, proxy schema, source URLs, time bounds and a domain-separated
fingerprint. `_improved` performs exact integer basis-point arithmetic. The
contract owns all status mapping in `_decision`, the bounded retry counter and
the terminal `Receipt`. `is_rewardable` is a deterministic conjunction of the
matching fingerprint, terminal receipt and `REWARDABLE` status.

## Leader path

`Goodhart.assess` authenticates the owner, expected fingerprint, pending state
and time window, then calls `_consensus`. The leader callback calls
`_observe`, which independently fetches the proxy and both outcome URLs using
`_fetch`. `_clean_page` either accepts the complete normalized source under the
12,000-character/48,000-byte bound or returns an empty fail-closed result; it
never slices a page. `_proxy_json` parses the exact four-field proxy schema.
`_outcome` asks the model to classify the underlying objective, requires a
unique verbatim witness, and runs `_audit_prompt` for every `IMPROVED` result.

## Validator path

The validator receives a typed `gl.vm.Return` and first checks the exact
observation schema in `_valid_observation`. It then calls `_observe` again,
which refetches and reinterprets the frozen URLs rather than trusting the
leader’s page, quote or classification. Material status, proxy value, proxy
digest, outcome labels and outcome digests must agree. For conclusive results,
the validator fetches each source again, verifies the leader witness occurs
exactly once in the same complete snapshot, recomputes the source digest, and
`_audit_witness` independently challenges each leader witness before a
`REWARDABLE` proposal can pass.

This is substantive recomputation, not JSON-shape voting. Different model
reason wording is not stored or compared; a material verdict, source digest,
numeric value, or witness mismatch is rejected. Extra fields, malformed JSON,
UNKNOWN results carrying quotes, oversized sources, redirects and unavailable
sources fail closed. The model never selects a reward amount or changes state.

On the final byte-identical StudioNet deployment, the fresh controlled fixture
registered as `fixture-rewardable-final-20261110` was independently fetched and
its proxy passed (`80` from baseline `20`). Assessment
`0x51297a28d9f9cf30b7a4f519c72f2203d2befc7fa2d49bd60c2de508a1e37481`
finalized `MAJORITY_AGREE` with successful execution, `REWARDABLE`, and both
outcome labels `IMPROVED`. The deterministic read-back
`is_rewardable(program_id, fingerprint)` returned `true` only for the exact
registered fingerprint. The proof-bound RewardGate then accepted the exact
action once and rejected the identical replay; those receipts are recorded in
`docs/DEPLOYMENT.md`.

Earlier controlled attempts finalized `INCONCLUSIVE`/`UNKNOWN` and remain
fail-closed historical controls. The successful positive case uses bounded
repository fixtures, so it demonstrates consensus and binding mechanics rather
than publisher identity, causal impact or real-world data truth.

## Evidence limits

The source digest binds the URL and normalized bytes observed during this
assessment. It does not authenticate publisher identity, prove ownership of a
hostname, establish causal impact, prove data completeness, or show that an
actor performed a real-world action. Distinct hostnames are a separation
constraint, not proof of independent ownership. Redirect and DNS properties
that the stable GenVM response does not expose remain residual risks and are
documented in the threat model.

