# GOODHART — make rewards depend on the objective, not the proxy

GOODHART is a consensus-backed proxy–objective divergence primitive that freezes
an incentive programme’s real objective and measurable proxy, independently
evaluates public evidence of underlying outcomes, and exposes an exact-hash
reward permission only when proxy and objective improvements withstand validator
scrutiny.

It addresses a common Goodhart failure: a worker can increase a measurable
proxy—tickets closed, patches merged or inspections completed—while the actual
objective stays unchanged or deteriorates. Proxy progress is necessary but not
sufficient. GOODHART does not prove causality, intentional gaming, publisher
identity, data completeness, payment eligibility or legal liability.

## Consent-bound lifecycle

```text
owner registers immutable programme and typed beneficiary
                         |
                         v
OFFERED -- beneficiary accepts exact fingerprint --> ACTIVE
                         |
                         v
owner or accepted beneficiary assesses inside frozen window
  deterministic proxy arithmetic + independent source consensus
                         |
  proxy short of threshold -> PROXY_NOT_IMPROVED
  both outcomes improved   -> REWARDABLE
  degraded or mixed        -> DIVERGENT
  stable/unsupported       -> UNSUPPORTED
  unknown/missing/stale    -> INCONCLUSIVE / bounded RETRYABLE
                         |
                         v
immutable receipt -> is_rewardable(program_id, fingerprint)
                         |
                         v
RewardGate records one exact precommitted action
```

The beneficiary must authenticate acceptance with the exact fingerprint before
the assessment window opens. The owner may withdraw only an unaccepted offer;
an accepted programme cannot be cancelled unilaterally. After acceptance, the
owner or the authenticated beneficiary may initiate assessment, so the owner
cannot withhold the only assessment transaction.

## Consensus boundary

Deterministic code validates the exact four-field proxy JSON, computes integer
basis-point movement, validates schemas and digests, enforces actors and time
windows, and commits the final status. The leader and validators independently
fetch the frozen proxy and outcome URLs. Validators recompute the proxy and
semantic outcome labels, compare material digests, verify unique quotes and
perform adversarial compatible-reading checks before a positive result can be
accepted. A model never selects a reward amount, recipient or state transition.

`_clean_page` rejects invalid, empty, redirected or oversized sources; it never
slices a page to hide later counterevidence. Three HTTPS hostnames are a source
binding constraint, not authenticated publisher independence.

## Contracts

- [`contracts/goodhart.py`](contracts/goodhart.py) freezes the programme,
  beneficiary acceptance, proxy schema, three source URLs and time window;
  it exposes `accept_program`, `assess`, `cancel`, `get_program`,
  `get_receipt` and `is_rewardable`.
- [`contracts/reward_gate.py`](contracts/reward_gate.py) is a minimal typed
  consumer. It checks the exact primary address, programme, fingerprint,
  beneficiary and action hash, then records a successful action once. It does
  not custody or transfer GEN.

## Locked environment

| Setting | Required value |
|---|---|
| Network | `studionet` |
| Chain ID | `61999` (`0xf22f`) |
| RPC | `https://studio.genlayer.com/api` |
| Local CLI | `genlayer@0.39.1` |
| Direct Mode | `genlayer-test==0.29.2` |
| GenVM runner | `v0.2.12` |
| GenVM linter | `0.11.0` |

Never use `studionet-dev`, chain `61997` or global CLI `0.40.0rc2`.

```text
npm ci --ignore-scripts
py -3.12 -m pip install -r requirements-dev.txt
node scripts/assert_studionet.mjs
py -3.12 scripts/preflight.py
py -3.12 -m unittest discover -s tests -p 'test_*.py' -v
py -3.12 -m pytest -q tests/direct -s
py -3.12 -m pytest -q tests
py -3.12 scripts/mutation_check.py
py -3.12 -m compileall -q contracts scripts tests
```

Direct Mode is a simulated VM with controlled sources; it is not live
StudioNet evidence.

## Current corrected deployment

The final corrected primary, including the distinct-owner/beneficiary guard,
is deployed byte-for-byte at
`0xbea069743269137772E42873aB0D2dE3E9EDC411`.

- Deployment transaction:
  `0xcd47489c9e46e18b595b086a9cee71f3d9330070bab1e88977caceba321a7841`
- Finality/result: finalized `MAJORITY_AGREE`, execution `SUCCESS`
- `contracts/goodhart.py` SHA-256:
  `10414807d2545f999915e62300d8b385c2888ae36b6faaf55176be5163fa6bab`
- Deployed source: 30,279 bytes, exact byte equality with the local file
- Deployment signer: `0x271FeAA6764865c2c8309e4C603D10650DbD0F95`

The current-primary control programme `binding-control-20261111` was registered
with owner `0x271FeAA6764865c2c8309e4C603D10650DbD0F95`, beneficiary
`0x0d5540e0aD4B92Aa0ad4e5F1b8cD645ee1E363E7`, and fingerprint
`5a6a6dacbd577d77d19bf0f07af4cd655260309c5654a2ea18b7c111a908d750`.
Registration finalized successfully in
`0x5a4979e38fdedc34614e7d0a972062d92493934609acb3725cdb94bc23d864f7` and
the readback remains `accepted=0`, `PENDING`. An attempted acceptance with an
incorrect fingerprint rolled back in
`0x1be8967057e71f7d50425b93b49bfe84a547ed6e2ceef686b6d270e09920aa6a`.

The corrected RewardGate is deployed against this exact primary at
`0x46c240DCAA5bDD440f0C41a3499a4096471e2F8B`:

- Deployment transaction:
  `0xcfc3d88f13f89a63989f309e0605e562df885be8bd2c71813b3a4f2941efa95d`
- Finality/result: finalized `MAJORITY_AGREE`, execution `SUCCESS`
- `contracts/reward_gate.py` SHA-256:
  `612cc909263f8d1bff3d7ec4d9ceeab0f0f31ee2252bb39f79c7443305eda20b`
- Deployed source: 3,159 bytes, exact byte equality with the local file

The current gate verifies the beneficiary returned by the primary programme,
not only its constructor argument. A correct-action call rolled back with
`underlying objective not certified` in
`0x978d3ada3f03f9dbfe758d6a8166128f5a0c9e67ca32c82ac2d17669e8dbc0de`; an
action substitution rolled back in
`0x86176c54f009f00d052f766324d2239fc34c5f449bd36d8371765771a1ea1bee`; and
an unauthorized caller rolled back with `only beneficiary` in
`0xd14b8e4be53e2a6fc50874fea2a1e32f676792071a41949fd99e14b9d4443cb8`.
`was_executed` remains `false` after these failures.

## Release status

The corrected primary’s distinct-address guard, independent validator tests,
fail-closed controls and deployed-source parity are verified. A fresh finalized
`REWARDABLE` receipt on this primary was not obtained, so the current gate has
only been proven to reject nonrewardable, substituted and unauthorized actions;
it has not been proven to execute successfully or replay successfully on this
build. The earlier positive RewardGate proof remains historical evidence for a
previous primary only and is not proof of this deployment.

## Tests and source-trust limits

The latest local run recorded 34 unittest/offline tests, 26 Direct Mode tests,
60 combined pytest tests, 20 preflight assertions and 6 mutation variants
killed. Both contracts pass the compatible GenVM lint/schema checks described in
the deployment ledger. Direct Mode includes native validator re-observation,
but controlled semantic inputs are not a live-world publisher proof.

GOODHART cannot authenticate real-world publisher ownership, prove that two
domains are independently controlled, establish a worker’s identity or action,
prove causality or data completeness, or transfer a reward. Content digests
attest only to the bounded bytes observed at assessment. No trusted publisher
attestation registry was added because the stable runtime provides no authority
root that would make such a claim truthful.

No frontend, backend, database, Docker deployment, custody, token transfer or
application wallet is included. See [`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md)
for the complete ledger and explicit blockers.
