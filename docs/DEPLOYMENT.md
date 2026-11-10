# Deployment and proof ledger

## Locked target

- Network: `studionet`
- Chain ID: `61999` (`0xf22f`)
- RPC: `https://studio.genlayer.com/api`
- Repository-local CLI: `genlayer@0.39.1`
- GenVM runner: `v0.2.12`
- GenVM linter: `0.11.0`

`node scripts/assert_studionet.mjs` verifies both the RPC result and the
repository-local CLI immediately before any deployment. No global CLI,
development network or chain 61997 is an accepted fallback.

## Baseline and local verification

The starting repository was `03c3e1e84560decde9815cf9a419eb68252589e9`.
Before hardening, the unchanged host suite passed 23 tests and preflight passed
12 assertions. The pinned Direct Mode suite initially could not start on this
Windows host because `genlayer-test==0.29.2` attempted to unlink an open stdin
temporary file. The repository now contains a Windows-only test shim that
defers that cleanup until VM teardown; the native contract runner itself is
unchanged.

Current local verification after hardening:

- Offline/host tests: 31 passed.
- Direct Mode: 15 passed, including native `direct_vm.run_validator()`.
- Combined pytest collection: 46 passed.
- Preflight: 18 assertions passed.
- Python compileall: passed.
- `genvm-lint 0.11.0`, `GENVM_VERSION=v0.2.12`: lint and semantic validation
  passed for both contracts; JSON schema extraction passed for both.
- RPC guard: confirmed `eth_chainId = 0xf22f`.

These are local or simulated checks, not StudioNet transaction evidence.

## Final deployed-source ledger

The final byte-normalized deployment was made after correcting a Windows
working-tree line-ending mismatch. Both deployed source blobs were read back
through `gen_getContractCode`; the returned bytes match the final Git blobs
exactly.

| Evidence | Final verified value |
|---|---|
| Goodhart address | `0x7F1eE6dA4ED706E363B54713B6dfc0dB2AA64234` |
| Goodhart deployment transaction | `0x9453ddcc3f8bfa96e84f26227b5c8ffbc59478166d20e1f0ec022fc7997847d8` |
| Goodhart deployment finality | `FINALIZED`, `MAJORITY_AGREE`, execution `SUCCESS` |
| Goodhart source SHA-256 | `d027cb8009a16197448efbfd2055c54c76c86d0586a51d11058d2f8d281e9a3a` (27,297 bytes) |
| Original final-source RewardGate address | `0x04f0e8C16256161ac674C0dE5305769bE1b895c9` |
| Original final-source RewardGate deployment transaction | `0x8524c59c01f181a2c2b903acf21739f31825de8a65e12957bd59183e25f75f30` |
| Original RewardGate deployment finality | `FINALIZED`, `MAJORITY_AGREE`, execution `SUCCESS` |
| Final proof-bound RewardGate address | `0xa718F7aff4a7fB57E3070100c27b90830b60A3Ae` |
| Final proof-bound RewardGate deployment transaction | `0xc4595146d2d667e2b52603cd6f2eac4c1f8638fa76d3e1559e2d4ee053b36f9c` |
| Final proof-bound RewardGate deployment finality | `FINALIZED`, `MAJORITY_AGREE`, execution `SUCCESS` |
| RewardGate source SHA-256 | `29e1254de00c6f61963ea65c63929ceaf0663c790c9feae1ec2133c634a7bd22` (2,436 bytes) |
| Deployed-source parity | Exact byte equality for Goodhart and both RewardGate instances: verified `True` through `gen_getContractCode` |
| Explorer | Not recorded as verified: explorer endpoint returned HTTP 503 during closeout |

The final Goodhart and RewardGate source files were unchanged in content from
the hardened contract commit; only the working-tree encoding was normalized so
the committed and deployed bytes are identical. The earlier CRLF deployment
(`0xcC51c9935E77d3a25ecCcCB6Fc19e9B8685f7cc9`) and its receipts are historical
only and are not used as final-release source evidence.

## Finalized live lifecycle ledger

The live fixtures below are controlled public mechanics fixtures. They are
retrievable HTTPS documents, not independent proof of publisher identity,
real-world action, causality, payment eligibility or data truth.

| Proof | Finalized transaction/readback |
|---|---|
| Final fresh positive registration on byte-identical Goodhart | `0xb1a9f01bd91b8a9c741fe8c9c44b5fc89f1c643ec58b142e1fc0c4d50a3ae0a4`; program `fixture-rewardable-final-20261110`; fingerprint `e01446f6d9b58e0913f780f0901d094dc4940ac0fc2d14fa35c00d4eec0917dd`; `FINALIZED`, `MAJORITY_AGREE`, execution `SUCCESS` |
| Final fresh positive assessment | `0x51297a28d9f9cf30b7a4f519c72f2203d2befc7fa2d49bd60c2de508a1e37481`; `FINALIZED`, `MAJORITY_AGREE`, execution `SUCCESS`; read-back `REWARDABLE`, proxy `20 -> 80`, outcome A/B `IMPROVED`, `is_rewardable=true` |
| Proof-bound RewardGate deployment | `0xc4595146d2d667e2b52603cd6f2eac4c1f8638fa76d3e1559e2d4ee053b36f9c`; address `0xa718F7aff4a7fB57E3070100c27b90830b60A3Ae`; `FINALIZED`, `MAJORITY_AGREE`, execution `SUCCESS` |
| Authorized exact-action execution | `0x926f8248e746667aaccbc0ea899b3a1c6318f51ecffdec66b71485b444a415f9`; action hash `5d16f2b1ddada8ea1963aa89645b1b12426a830e8793c80914163fbd5cd8713b`; `FINALIZED`, `MAJORITY_AGREE`, execution `SUCCESS`; `was_executed=true` |
| Exact-action replay attempt | `0xce7a86670ddf252cd317273d401058b8c7a32840de0c66a163e4dc991b18aea1`; `FINALIZED`, `MAJORITY_AGREE`, execution rollback `EXPECTED: replay`; `was_executed=true` unchanged |
| Earlier positive registration attempt | `0x6a27ff9d360681dce82279e375b610b2df01b33e93700cdab22020691edc5e47`; fingerprint `fcb053bcd2b9fb19089f40ea099468a961524d81f2f449d57308bb23c37037e3` |
| Positive assessment attempt on final Goodhart | `0x9ba2bdfdf8d3e5e5a1651a2f343a4e7ab97573f7cd07b2b5d1c3f81bdf5a21aa`; `FINALIZED`, `MAJORITY_AGREE`, terminal `INCONCLUSIVE`, proxy `80`, both outcomes `UNKNOWN`, `is_rewardable=false` |
| Second positive fixture registration | `0x26df1667d119b23d6d553e0d9df09e19f6d700ae815f15da6cb26a6e7e3dc29e`; fingerprint `1f640a20d548f6bd843c1279cc22dfdcbde105a9097c566166b1a29f50bab0fd` |
| Second positive fixture assessment | `0xa3d1c8f0f1e06760e0fec5447b654c5031d7646fd4e64c3cac5947edd6f8ed56`; `FINALIZED`, `MAJORITY_AGREE`, terminal `INCONCLUSIVE`, `is_rewardable=false` |
| Stale/fingerprint-bound RewardGate call | `0xfa0edf7dc933059f560b76920ad7b7a5c57d712fcdb089a04175f66ab6559113`; `FINALIZED` rollback `EXPECTED: underlying objective not certified` |
| Final RewardGate payload substitution | `0xd703f4f55f6723122bb00771dbf570a95fa6d17d57409ac33acef0a33e5f21e8`; `FINALIZED` rollback `EXPECTED: action substitution` |
| Final RewardGate unauthorized executor | `0x6fa5ad37af91fc0e573e753f0991b9b0b40e9866ffd803085c717f08404d02b1`; `FINALIZED` rollback `EXPECTED: only beneficiary`; `was_executed=false` |

The final positive fixture uses controlled public HTTPS documents committed as
repository fixtures. They demonstrate the protocol and validator source
bindings, not publisher identity, real-world action completion, causality,
payment eligibility or data truth. Earlier `INCONCLUSIVE` attempts were
preserved as fail-closed historical controls; no failed semantic decision was
reinterpreted as reward clearance. The final proof-bound RewardGate instance
uses the exact finalized programme fingerprint and action hash above.

## Live proof standard

The final ledger must retain the exact transaction hash, final status, signer
address where appropriate, explorer URL, programme fingerprint, public source
URLs and post-finality readbacks for registration, assessment and consumer
calls. A public page is not proof of publisher identity, real-world action,
causality or payment. Controlled fixtures must be labelled as fixtures. Direct
Mode output must never be substituted for finalized consensus.
