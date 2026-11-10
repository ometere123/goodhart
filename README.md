# GOODHART — make rewards depend on the objective, not the proxy

**Standalone GenLayer Intelligent Contract primitive. No frontend or product backend.**

GOODHART is a consensus-backed proxy–objective divergence primitive that freezes
an incentive programme’s real objective and measurable proxy, independently
evaluates public evidence of underlying outcomes, and exposes an exact-hash
reward permission only when proxy and objective improvements withstand validator
scrutiny.

This addresses a common Goodhart failure: a worker can increase a measurable
proxy—tickets closed, patches merged or inspections completed—while the actual
objective stays unchanged or deteriorates. GOODHART makes proxy progress
necessary but insufficient. It does not prove causality, intentional gaming,
publisher identity, data completeness, payment eligibility or legal liability.

## Lifecycle

```text
register one immutable programme
  owner + typed beneficiary + objective + indicator
  proxy schema + threshold + three frozen HTTPS URLs + fixed time window
                         |
                         v
assess (owner only, inside the window)
  deterministic proxy parsing and exact basis-point arithmetic
  independent leader/validator source retrieval and semantic classification
                         |
  proxy short of threshold  -> PROXY_NOT_IMPROVED
  both outcomes improved     -> REWARDABLE
  degraded or mixed outcome  -> DIVERGENT
  stable or unsupported      -> UNSUPPORTED
  unknown, missing or stale  -> INCONCLUSIVE / bounded RETRYABLE
                         |
                         v
immutable receipt -> is_rewardable(program_id, fingerprint)
                         |
                         v
RewardGate records one exact precommitted action
```

`gl.vm.run_nondet_unsafe` is used only for source observation and semantic
classification. The contract deterministically parses the exact four-field
proxy JSON, computes basis-point movement, validates schemas and digests,
maps statuses and commits the receipt. A model never chooses an amount,
recipient or state transition.

## Contracts

- [`contracts/goodhart.py`](contracts/goodhart.py) freezes the programme,
  re-fetches the proxy and both outcome URLs, performs independent validator
  recomputation, rejects incomplete/oversized evidence and exposes
  `is_rewardable(program_id, fingerprint)`.
- [`contracts/reward_gate.py`](contracts/reward_gate.py) is a minimal typed
  consumer. It checks the exact primary address, programme, fingerprint,
  beneficiary and action hash, then records a successful action once. It does
  not custody or transfer GEN.

The owner is authenticated at registration and the beneficiary binding is
immutable. GOODHART intentionally has no beneficiary-consent or publisher-
identity protocol; those are integration/governance assumptions.

## Evidence boundary

`_clean_page` accepts a complete normalized source only when it is below the
12,000-character and 48,000-byte bounds. Oversized, invalid, empty or
redirected evidence fails closed; it is never silently sliced. Validators
re-fetch the frozen URL and compare material labels, numeric values, source
digests and witness occurrence. Positive witnesses also undergo an independent
compatible-reading audit.

Three different HTTPS hostnames are a URL-separation constraint, not proof of
three independent publishers. The repository includes an external evidence
manifest for a CERT-EU / Debian XZ Utils case, but the fresh StudioNet
assessment correctly returned `INCONCLUSIVE` with both outcome labels
`UNKNOWN`. It is not presented as a reward proof. See
[`docs/EVIDENCE_MANIFEST.md`](docs/EVIDENCE_MANIFEST.md).

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

```bash
npm ci --ignore-scripts
python3 -m pip install -r requirements-dev.txt
npm run cli:version
npm run network:check
npm run preflight
npm run test:offline
python3 -m pytest -q tests/direct -s
npm run test:mutation
GENVM_VERSION=v0.2.12 genvm-lint check contracts/goodhart.py
GENVM_VERSION=v0.2.12 genvm-lint check contracts/reward_gate.py
```

The verified local suite currently has 32 offline tests, 16 Direct Mode tests,
48 combined pytest tests, 18 preflight assertions and 4 mutation checks.
Direct Mode is a simulated VM with mocked sources; it is not live StudioNet
evidence.

## Deployment status

The corrected primary source is deployed byte-for-byte on StudioNet:

- Goodhart: `0x9aAB4148ff9C939Be58C64dD5bfa0FCFecBDA881`
- Deployment transaction: `0xa400c4def28d7e74820252f6f7be13b7b4467712928202336aad3363b87fe638`
- Source SHA-256: `e516fb4a497bb2b8bad20cca5b141b3b033fc625a609201119c660d375d4d10b`
- Deployment: finalized `MAJORITY_AGREE`, execution `SUCCESS`

The code correction classifies permanent HTTP/redirect/source-identity
failures as terminal fail-closed evidence failures while retaining one bounded
retry for transient service failures. It also adds true Keccak-256 host tests;
Python SHA3-256 is not used as a Keccak substitute.

The corrected primary now has a fresh finalized positive mechanics proof. The
programme `fresh-positive-auth-beneficiary-20261110` was registered by
`0x0d5540e0aD4B92Aa0ad4e5F1b8cD645ee1E363E7` for the distinct beneficiary
`0x271FeAA6764865c2c8309e4C603D10650DbD0F95`. Assessment
`0xf20659666a3b89cee1e6bd0076d150e8ab2b4c5c16765f87863630c079c32fb2`
finalized `MAJORITY_AGREE` with successful execution, returned `REWARDABLE`,
and read back `is_rewardable=true` for the exact fingerprint. The bound
RewardGate is `0x83C553f6Ccd9d3Ea5f474f69F275b781F22F52F0`, deployed by
`0x58f6f86c3e2ba43d66351d006edee34463e39a4eec50f609130680b8f04f3200`.
The beneficiary’s exact action succeeded in
`0x8c838c497d329247147c52db4c317ccd5e0b262853c5aa5c0bcb48b3dce7c423`;
the identical replay finalized with `EXPECTED: replay` in
`0xb81743cea6d116f0472a036d3136bc364ae7ebfc0c5c512f50ed3f5db3c534d8`, and
`was_executed` remained `true`.

This positive case is a controlled public fixture proving protocol mechanics,
not proof of publisher identity, independent real-world measurement or a
beneficiary’s actual fleet outcome. The separate external XZ case on the
corrected primary finalized `MAJORITY_AGREE` and `INCONCLUSIVE`
(`0x68dd7b602f83193be6ed03a388fa7beefb26cbb633c72fd111d191d4e781edae`),
with proxy `20 -> 80` and both outcome labels `UNKNOWN`; it remains the
fail-closed external-evidence control.

All deployment receipts, source parity, historical evidence and blockers are
recorded in [`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md). Explorer links are not
claimed because the explorer endpoint returned HTTP 503 during closeout.

## Scope and limitations

GOODHART is a reusable protocol primitive, not a payment application. Public
source material does not independently prove real-world identity, publisher
ownership, action completion, subjective reliance, causality, hidden data or
legal liability. A digest attests only to the URL and normalized bytes observed
by the contract. A separate trusted publisher/attestor policy was not added:
the stable runtime has no enforceable authority registry that would make such a
claim truthful without changing the public protocol.

No frontend, backend, database, Docker deployment, custody, token transfer or
application wallet is included.
