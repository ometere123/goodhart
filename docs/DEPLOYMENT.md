# Deployment and proof ledger

**Target (locked):** `studionet` / **61999** / `https://studio.genlayer.com/api`.
**CLI (locked):** repository-local `genlayer@0.39.1`.

## What has been verified in this workspace

- `npm run cli:version`: `0.39.1`.
- `npm run network:check`: JSON-RPC `eth_chainId` returned `0xf22f` (61999).
- Local Python contract source compiled, GenVM linter accepted both contracts.
- Offline and Direct Mode suites run with the pinned `v0.2.12` SDK.

## Live deployment status

**Not deployed.** The connected workspace has no configured GenLayer CLI
account (`genlayer account list` returned no accounts). No private keys were
imported, no transaction submitted and no StudioNet deployment address exists
from this build. Do not claim finalized live consensus from local tests.

## On a funded machine

1. `npm ci --ignore-scripts` then `npm run network:check`.
2. `./node_modules/.bin/genlayer account list` and select a funded wallet using
   the CLI's normal authenticated account workflow. Never paste a private key
   into this repo or a GitHub issue.
3. `npm run deploy:studionet` (Goodhart main contract).
4. After finalized status, save the transaction and deployed address below.
5. Deploy `contracts/reward_gate.py` separately, using the **actual** registry
   address, registered programme ID, returned fingerprint, beneficiary and
   64-character exact action commitment as constructor args.
6. Run live favourable/divergent/ambiguous programme cases with actual public
   sources. Avoid claiming controlled test fixtures are independent external
   publishers. Verify `is_rewardable` both before and after finalization.
7. Populate receipts and source hashes, verify explorer visibility and commit
   the evidence links. Do not edit historical receipts.

| Evidence | Value |
|---|---|
| Goodhart address | Pending |
| Goodhart deployment transaction | Pending |
| Finalized status | Pending |
| RewardGate address/transaction | Pending |
| Favourable programme ID/receipt | Pending |
| Divergent programme ID/receipt | Pending |
| Consumer gating proof | Pending |

### Reviewer proof standard

Keep raw transaction hashes, explorer URLs, contract code hashes, programme
fingerprints, the public source URLs and the verbatim observed receipts.
Distinguish a submitted/accepted transaction from an executed/finalized one.
