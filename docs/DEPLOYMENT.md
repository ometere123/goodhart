# GOODHART deployment and verification ledger

This ledger separates finalized evidence for the corrected source from the
earlier deployment. No historical receipt is promoted to proof of a changed
build.

## Locked target

- Network: `studionet`
- Chain ID: `61999` (`0xf22f`)
- RPC: `https://studio.genlayer.com/api`
- Repository-local CLI: `genlayer@0.39.1`
- GenVM runner: `v0.2.12`
- GenVM linter: `0.11.0`
- Direct Mode: `genlayer-test==0.29.2`

`node scripts/assert_studionet.mjs` queried the locked RPC and confirmed
`eth_chainId = 0xf22f`; the local CLI printed `0.39.1`. The global CLI was not
used. No chain 61997 or preview network was used.

## Baseline and local verification

Baseline HEAD before hardening was `3f4285ff8916fb9456363939fb24b22a96060828`
with a clean worktree. Baseline source hashes were Goodhart
`d027cb8009a16197448efbfd2055c54c76c86d0586a51d11058d2f8d281e9a3a` and
RewardGate `29e1254de00c6f61963ea65c63929ceaf0663c790c9feae1ec2133c634a7bd22`.

The corrected local verification was rerun after the code change:

- Offline/host: 32 passed.
- Direct Mode: 16 passed, including native validator re-observation.
- Combined pytest collection: 48 passed.
- Preflight: 18 assertions passed.
- Mutation checks: 4 weakened variants killed.
- Python compileall: passed.
- GenVM lint/schema: both contracts passed with `genvm-lint 0.11.0` and
  `GENVM_VERSION=v0.2.12`.
- Production npm audit: no high-severity production vulnerabilities.
- RPC guard and local CLI check: passed.

Direct Mode and controlled fixtures are simulated/test evidence, not publisher
authentication or live-world truth.

## Corrected primary deployment

The `_fetch` correction changed contract bytes, so a new primary was deployed.

| Field | Verified value |
|---|---|
| Goodhart address | `0x9aAB4148ff9C939Be58C64dD5bfa0FCFecBDA881` |
| Deployment transaction | `0xa400c4def28d7e74820252f6f7be13b7b4467712928202336aad3363b87fe638` |
| Finality/result | `FINALIZED`, `MAJORITY_AGREE`, execution `SUCCESS` |
| Final local source SHA-256 | `e516fb4a497bb2b8bad20cca5b141b3b033fc625a609201119c660d375d4d10b` |
| Read-back deployed SHA-256 | `e516fb4a497bb2b8bad20cca5b141b3b033fc625a609201119c660d375d4d10b` |
| Read-back source bytes | 28,052 bytes; exact byte equality |

The deployed source was read through `gen_getContractCode`, decoded and hashed
locally. The final Git blob has the same bytes and hash.

## Fresh corrected-primary live attempts

The owner was `0x0d5540e0aD4B92Aa0ad4e5F1b8cD645ee1E363E7` and the distinct
beneficiary was `0xaC3508205964f73AcFc1F2cb33Ad529dBed8Cda1`. The CLI used the
typed address form `addr#` followed by the 40 hexadecimal characters; the
first attempted `addr#0x...` form was rejected by the contract and was not
counted as a successful registration.

### External XZ evidence candidate

| Action | Finalized evidence |
|---|---|
| Registration | `0x05a914e1a7a07efe2d7997daab2c88c85c716414a53aa67da0bdba71d2f7f4b5`; execution `SUCCESS` |
| Programme/fingerprint | `xz-security-remediation-20261110` / `92a217eaf7de6ad96a26a19c64e4ec442f755badd6c6d97b90e49cd19d694709` |
| Assessment | `0x68dd7b602f83193be6ed03a388fa7beefb26cbb633c72fd111d191d4e781edae`; `FINALIZED`, `MAJORITY_AGREE`, execution `SUCCESS` |
| Read-back | proxy `20 -> 80`; outcome A `UNKNOWN`; outcome B `UNKNOWN`; status `INCONCLUSIVE`; `is_rewardable=false` |

The external sources were CERT-EU and the Debian Security Tracker. Their URLs,
raw hashes, normalized lengths and limitations are in
[`EVIDENCE_MANIFEST.md`](EVIDENCE_MANIFEST.md). This result is the desired
fail-closed behavior when public material does not establish a comparable
positive outcome; it is not a reward proof.

### Controlled fixture attempts on the corrected primary

All of the following used the same distinct beneficiary and repository-hosted
or repository-derived bounded fixtures. They are mechanics tests, not
independent publisher evidence.

| Programme | Registration | Assessment | Final read-back |
|---|---|---|---|
| `fixture-rewardable-final-20261110` | `0x8543b7b2d5df8808e7817ed5b0796fcd046cf874d87c2057bd9a352f131ab6a0` | `0x9cec76401776524b3bc6a8c8b951e59b7b6bd2768427834f19ac665dc73a3002` | `INCONCLUSIVE`, proxy `20 -> 80`, A/B `UNKNOWN` |
| `fixture-positive-20261110` | `0xf5fb7494451fbfb2e34fa47f590ccce2e3e74f01cbeb1b262c412facff18a8e4` | `0x23551006dd9c9cc227cfd43f0a5cafb575d16c42b5a46175ade64ced0622b32e` | `INCONCLUSIVE`, proxy `20 -> 80`, A/B `UNKNOWN` |
| `fixture-consensus-positive-20261110` | `0x637a97e7c9a92dc2ab347294849039691fceb6d901db531675d54ed9e1eccc55` | `0x3784eba481d4ab244cce1a7b81b3fb48a75b2f8c9124cfb4faf35dfa9f353dd9` | First assessment submission was not returned by the RPC; the later finalized call rolled back `EXPECTED: stale program or already terminal`; no receipt and no reward clearance |
| `reward-permission-positive-20261110` | `0x5ca7be79e50a7f4448788cb0f0b41a1ec88a9bb46783b667c2c3cdfeeab52772` | `0x20f94ec1580007b41f2c291982f26fc5ba769dfbdebda7efeb73531334a3eea8` | Finalized rollback `EXPECTED: stale program or already terminal`; programme remained `PENDING`; no reward clearance |

No fresh corrected-primary assessment returned `REWARDABLE`. No new
RewardGate was deployed against a rewardable programme on this primary, and no
new-build authorized consumer execution or replay can honestly be recorded.

## Historical proof, retained but not promoted

The previous byte-identical deployment was Goodhart
`0x7F1eE6dA4ED706E363B54713B6dfc0dB2AA64234`, source hash
`d027cb8009a16197448efbfd2055c54c76c86d0586a51d11058d2f8d281e9a3a`.
Its controlled positive cycle and proof-bound RewardGate remain useful
historical evidence:

- Goodhart deployment: `0x9453ddcc3f8bfa96e84f26227b5c8ffbc59478166d20e1f0ec022fc7997847d8`.
- Positive assessment: `0x51297a28d9f9cf30b7a4f519c72f2203d2befc7fa2d49bd60c2de508a1e37481`,
  finalized `MAJORITY_AGREE`, execution `SUCCESS`, read-back `REWARDABLE`.
- Historical proof-bound RewardGate: `0xa718F7aff4a7fB57E3070100c27b90830b60A3Ae`,
  deployment `0xc4595146d2d667e2b52603cd6f2eac4c1f8638fa76d3e1559e2d4ee053b36f9c`.
- Historical authorized action: `0x926f8248e746667aaccbc0ea899b3a1c6318f51ecffdec66b71485b444a415f9`.
- Historical replay rollback: `0xce7a86670ddf252cd317273d401058b8c7a32840de0c66a163e4dc991b18aea1`.

These receipts prove the previous deployment only. They are not proof of the
corrected primary source.

## Source integrity and scope

- Corrected `contracts/goodhart.py`: SHA-256
  `e516fb4a497bb2b8bad20cca5b141b3b033fc625a609201119c660d375d4d10b`.
- `contracts/reward_gate.py`: SHA-256
  `29e1254de00c6f61963ea65c63929ceaf0663c790c9feae1ec2133c634a7bd22`.
- Goodhart deployed bytes match the final committed Goodhart file exactly.
- RewardGate source is unchanged from its historical deployment, but no new
  gate is claimed for the corrected primary.
- No explorer URL is claimed; the explorer endpoint returned HTTP 503.
- No secrets, private keys, frontend, backend, database, Docker or wallet UI
  are part of the repository.

## Release blocker

The corrected primary is deployed and locally verified, but the release is not
submission-ready for the requested end-to-end proof. The exact blocker is a
fresh finalized `REWARDABLE` assessment on the corrected primary, followed by
a RewardGate bound to that fingerprint and successful authorized execution plus
replay rejection. The live source/model path returned conservative
`INCONCLUSIVE`/`UNKNOWN` results, and no transaction was reinterpreted or
reused to manufacture clearance.
