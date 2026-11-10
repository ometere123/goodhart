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

## Live deployment ledger

No live deployment is recorded until a finalized transaction, readback and
source-parity check are captured from the corrected source. Do not replace the
pending fields with a submission or accepted transaction status.

| Evidence | Value |
|---|---|
| Goodhart address | Pending finalized deployment |
| Goodhart deployment transaction | Pending |
| Goodhart final status | Pending |
| RewardGate address/transaction | Pending finalized deployment |
| Positive programme/fingerprint/receipt | Pending |
| Divergent programme/receipt | Pending |
| RewardGate blocked/success/replay proofs | Pending |
| Source SHA-256 | Record from final committed bytes |
| Deployed-source parity | Pending; never infer from local hash alone |

## Live proof standard

The final ledger must retain the exact transaction hash, final status, signer
address where appropriate, explorer URL, programme fingerprint, public source
URLs and post-finality readbacks for registration, assessment and consumer
calls. A public page is not proof of publisher identity, real-world action,
causality or payment. Controlled fixtures must be labelled as fixtures. Direct
Mode output must never be substituted for finalized consensus.
