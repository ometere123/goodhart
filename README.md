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

## Current final-source deployment

The beneficiary-consented source is deployed byte-for-byte at
`0xc6f159b8A0475D32c39033131D5b4E496581f38a`.

- Deployment transaction:
  `0x7cb4e4544e03257b6fcbbce512977f288d9ec5af3b93acb2c8a4b33bb7b5cc58`
- Finality/result: finalized `MAJORITY_AGREE`, execution `SUCCESS`
- `contracts/goodhart.py` SHA-256:
  `7d2dae0e1c8c5e3b7ecf26c79fc3534beb8909f2394ef157baeb814f3f138106`
- Deployed source: 30,156 bytes, exact byte equality with the local file
- Owner signer: `0x0d5540e0aD4B92Aa0ad4e5F1b8cD645ee1E363E7`
- Beneficiary signer: `0x271FeAA6764865c2c8309e4c603D10650DbD0F95`

The new primary has finalized consent and authorization proofs:

- Unauthorized owner acceptance on `consent-live-20261111`:
  `0x3dea3a13aa16982b8786020491f7158e8917d42d815af705717ac17a950847f3`,
  expected rollback `only beneficiary may accept`.
- Beneficiary acceptance:
  `0x5aafe84d15b2d72125327371bd542b77ec0947b3ddc9294c4d124086ac604511`,
  successful.
- Beneficiary assessment:
  `0x339d9a253852b49287f4e7607d4e6bee17056a001a10f73051f41a1e8ab32731`,
  finalized `MAJORITY_AGREE`, execution `SUCCESS`, returned `INCONCLUSIVE`,
  outcomes `UNKNOWN` / `UNKNOWN`, and `is_rewardable=false`.
- Owner cancellation after acceptance on `consent-positive-20261111`:
  `0xc805ff4c3147415a1443a5793bd22013c68ff3e92a49b342a87a9dd34c23a66d`,
  expected rollback `accepted program cannot be cancelled`.

## Release status

The new primary’s consent hardening, independent validator tests, fail-closed
external controls and source parity are verified. A fresh finalized
`REWARDABLE` receipt on this new primary has not been obtained: the best-bound
positive attempt finalized `MAJORITY_DISAGREE` and remained pending; its later
retry rolled back outside the assessment window. A separate attempted positive
fixture was correctly `INCONCLUSIVE` when its proxy file was not yet present at
the frozen GitHub commit. A subsequent committed-fixture attempt did not
record acceptance before its window and its assessment rolled back as stale.

Therefore a new RewardGate bound to the final primary has not been deployed or
claimed. The earlier positive RewardGate proof remains historical evidence for
the previous primary only and is not proof of this consented deployment.

## Tests and source-trust limits

The latest local run recorded 33 unittest/offline tests, 25 Direct Mode tests,
58 combined pytest tests, 20 preflight assertions and 5 mutation variants
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
