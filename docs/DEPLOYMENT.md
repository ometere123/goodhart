# GOODHART deployment and verification ledger

This ledger separates current final-source facts, failed or fail-closed attempts,
and historical receipts. No historical receipt is promoted to proof of a changed
build.

## Locked target

- Network: studionet
- Chain ID: 61999 (0xf22f)
- RPC: https://studio.genlayer.com/api
- Repository-local CLI: genlayer@0.39.1
- GenVM runner: v0.2.12
- GenVM linter: 0.11.0
- Direct Mode: genlayer-test==0.29.2
- Global CLI 0.40.0rc2: not used
- Chain 61997 and preview networks: not used

The RPC guard queried the exact RPC and returned eth_chainId 0xf22f. The local
binary returned 0.39.1.

## Baseline and local verification

The pre-change baseline for this final binding closeout was
4c972d47dfb381d56618a4ac6cd7089187b2b406. The binding corrections were
committed as 22e1e067f34971ddba85162a5ed2299baa196780. The earlier
beneficiary-consent implementation was committed as
07abd66cf7c6b1170115d9fdcc83cadf3e25accc; fixture additions followed in
fa5d0617a3689cbebacfdd47153b04b06e57f4b3 and
7113208ce3ed0e1a1b1cc027d80f5db9585ef8f7.

Latest executed results:

- unittest offline: 34 passed
- Direct Mode: 26 passed
- combined pytest: 60 passed
- preflight: 20 assertions passed
- mutation checks: 6 weakened variants killed
- compileall: passed
- GenVM lint/schema: both contracts passed with linter 0.11.0 and runner v0.2.12
- production npm audit: no high-severity production vulnerability was reported
- network guard: passed for studionet / 61999

## Current corrected primary

| Field | Verified value |
|---|---|
| Goodhart | 0xbea069743269137772E42873aB0D2dE3E9EDC411 |
| Deployment transaction | 0xcd47489c9e46e18b595b086a9cee71f3d9330070bab1e88977caceba321a7841 |
| Finality/result | finalized MAJORITY_AGREE, execution SUCCESS |
| Source SHA-256 | 10414807d2545f999915e62300d8b385c2888ae36b6faaf55176be5163fa6bab |
| Source bytes | 30,279; exact byte equality through gen_getContractCode |
| Deployment signer | 0x271FeAA6764865c2c8309e4C603D10650DbD0F95 |

## Current-primary control and RewardGate

The control programme `binding-control-20261111` was registered in
`0x5a4979e38fdedc34614e7d0a972062d92493934609acb3725cdb94bc23d864f7` with
owner `0x271FeAA6764865c2c8309e4C603D10650DbD0F95`, beneficiary
`0x0d5540e0aD4B92Aa0ad4e5F1b8cD645ee1E363E7`, and fingerprint
`5a6a6dacbd577d77d19bf0f07af4cd655260309c5654a2ea18b7c111a908d750`.
The finalized readback is `accepted=0`, `PENDING`; no reward permission exists.
An acceptance attempt with an incorrect fingerprint rolled back in
`0x1be8967057e71f7d50425b93b49bfe84a547ed6e2ceef686b6d270e09920aa6a`.

The corrected RewardGate is bound to this primary at
`0x46c240DCAA5bDD440f0C41a3499a4096471e2F8B`, deployed in
`0xcfc3d88f13f89a63989f309e0605e562df885be8bd2c71813b3a4f2941efa95d`.
The gate deployment finalized with `MAJORITY_AGREE` and execution `SUCCESS`.
Its source is 3,159 bytes with SHA-256
`612cc909263f8d1bff3d7ec4d9ceeab0f0f31ee2252bb39f79c7443305eda20b`, exactly
matching the local file.

Current-primary gate controls were all finalized consensus with execution
rollback and left `was_executed(expected_action_hash)=false`:

- correct action: `0x978d3ada3f03f9dbfe758d6a8166128f5a0c9e67ca32c82ac2d17669e8dbc0de`,
  `underlying objective not certified`;
- substituted action: `0x86176c54f009f00d052f766324d2239fc34c5f449bd36d8371765771a1ea1bee`,
  `action substitution`;
- unauthorized caller: `0xd14b8e4be53e2a6fc50874fea2a1e32f676792071a41949fd99e14b9d4443cb8`,
  `only beneficiary`.

## Final bounded positive attempt on the corrected primary

This was the single fresh positive attempt requested for the current primary.
The controlled fixture commit was
`cee6f2c18598ee116d360d5d3ab0420f7de335cf`; all URLs were anchored to that
immutable revision and preflighted with HTTPS, no redirect, HTTP 200 and full
bodies below the 12,000-character limit:

- proxy: `https://raw.githubusercontent.com/ometere123/goodhart/cee6f2c18598ee116d360d5d3ab0420f7de335cf/fixtures/live/proxy_positive_final_20261111.json`, 84 normalized characters;
- outcome A: `https://cdn.jsdelivr.net/gh/ometere123/goodhart@cee6f2c18598ee116d360d5d3ab0420f7de335cf/fixtures/live/outcome_reward_permission_a.md`, 584 normalized characters;
- outcome B: `https://raw.githack.com/ometere123/goodhart/cee6f2c18598ee116d360d5d3ab0420f7de335cf/fixtures/live/outcome_reward_permission_b.md`, 556 normalized characters.

| Field | Finalized/read-back value |
|---|---|
| Programme | `positive-final-20261111` |
| Owner | `0x0d5540e0aD4B92Aa0ad4e5F1b8cD645ee1E363E7` |
| Beneficiary | `0x271FeAA6764865c2c8309e4C603D10650DbD0F95` |
| Fingerprint | `76f9f685830c7c76731b357a821901b531598e3bc5118f62bbe3a51af6ef8dd6` |
| Registration | `0x8e8134f30b1353c9dce32a92a9fd36cb2d0ea28922f98d512899ebed6afc7c15`; finalized `MAJORITY_AGREE`, execution `SUCCESS` |
| Earliest/deadline | `1794389422` / `1794992422` |
| Acceptance | `0xf78e7e983d5488faa7bddb16e8f037ce2755a7d16323d9cfb4254db975461058`; finalized `MAJORITY_AGREE`, execution `SUCCESS`; `accepted=1` |
| Assessment | `0xc79c00d72d8be00e79030032fc60ea86e956ae86c9777c44b1ce5f1df0afe12c`; finalized `MAJORITY_AGREE`, execution `SUCCESS` |
| Assessment result | terminal `INCONCLUSIVE`; attempts `1`; proxy `20 -> 80`; outcomes `UNKNOWN` / `UNKNOWN`; `is_rewardable=false` |
| Proxy digest | `d6e17f4d700ec75783dbbcd36fe01e3ad33a43fd65da8821e9615e4c5b0c0bfa` |
| Outcome A digest | `92afacefbe8e4925583944f5a75f1a8bf75b3839c90de29b986c88e0a9aa7453` |
| Outcome B digest | `5295b192952ab486a308c52db3e4dd2d731ae318aa6864e4934c6367c8a59bd9` |

The source preflight succeeded, but the finalized semantic observation carried
no quote witnesses and both labels were `UNKNOWN`. The available transaction
trace method `gen_dbg_traceTransaction` returned RPC `Method not found`, so no
stronger substep-level cause is claimed. The confirmed contract-level cause is
fail-closed semantic uncertainty, not source substitution or oversized input.
Because the programme is terminal `INCONCLUSIVE`, no bounded retry was
available and no new RewardGate was deployed for it.

## Historical consent and fail-closed proofs on the superseded primary

The following receipts were finalized against the prior primary
`0xc6f159b8A0475D32c39033131D5b4E496581f38a`. They remain useful historical
evidence of the consent lifecycle but are not proof of the corrected primary
`0xbea069743269137772E42873aB0D2dE3E9EDC411`.

### consent-live-20261111

- Registration: 0xb3a659aa40da24cb99b1d6102dd5e9d18eb2f250e4c04ba34612f82f02829620; execution SUCCESS.
- Fingerprint: 09cb4951795059ff70c91ea2467eb2c0faa41a92d50d2176acc0680122f0a2cf.
- Unauthorized owner acceptance: 0x3dea3a13aa16982b8786020491f7158e8917d42d815af705717ac17a950847f3; finalized expected rollback only beneficiary may accept.
- Beneficiary acceptance: 0x5aafe84d15b2d72125327371bd542b77ec0947b3ddc9294c4d124086ac604511; execution SUCCESS.
- Beneficiary assessment: 0x339d9a253852b49287f4e7607d4e6bee17056a001a10f73051f41a1e8ab32731; finalized MAJORITY_AGREE, execution SUCCESS, returned INCONCLUSIVE; outcomes UNKNOWN / UNKNOWN and is_rewardable=false.

### consent-positive-20261111

- Registration: 0x338889a34bb003e53fe54fe04a106753658534573d6c1b6bdb3c1e405dd6b236.
- Fingerprint: b2c652daec97457402317975817d459eab616e52dc77127d10d9b04255722e79.
- Beneficiary acceptance: 0x66226835222c50f0e59914315e78d4f411465cb7238ed13960698caada4f5e62; execution SUCCESS.
- Owner cancellation after acceptance: 0xc805ff4c3147415a1443a5793bd22013c68ff3e92a49b342a87a9dd34c23a66d; finalized expected rollback accepted program cannot be cancelled.
- Duplicate acceptance: 0xa3954b037be034275aa8aa05aa7842d2987785fcbc3cd127f8b051236b93b08d; finalized expected rollback already accepted.
- Beneficiary assessment: 0x4c2c619a8aea75c5407132bbbef923b44d8bff7d95098afea0e7a463afbdf0b8; execution SUCCESS, fail-closed INCONCLUSIVE.

## Historical positive attempts on the superseded primary

The exact controlled outcome fixture pair was used only as mechanics evidence. It
does not prove publisher independence or a real-world beneficiary outcome.

- fixture-rewardable-20261110: beneficiary acceptance
  0xbe0e4c8d29d978a3dbdc6d06f88b6f447619bb3b4450120e3267525a42edff6a.
  Assessment 0x08a77973f7c1fabe1e8a1ab2d2f429a7631393bb96507a61ec2a40fd8333d805
  finalized MAJORITY_DISAGREE; validators disagreed with the full proposed
  nondeterministic result and the programme remained PENDING. A later bounded
  retry 0x7bc69ae7fe6d188787e806fe0fd17ce7d2dd3e431afd88d755fc5848339408bf
  finalized consensus but rolled back outside assessment window.
- final-primary-rewardable-20261111: registration
  0xcde687a692d14e904f8be16a0f91acd0ca8b2fc9eba006b41609535aa7f79171 and
  acceptance 0x82e8c3840e3e52d8c01e70018c503dd759576f1986ec9b20940a038f83addf7.
  The assessment 0x7c817f88c2c30bc5872dc6b5ebcc7593fc1755b476a97da630adf215f976a67c
  finalized successfully but returned INCONCLUSIVE because the proxy URL
  pointed at an uncommitted fixture revision; proxy_after was 0.
- final-primary-rewardable-20261111b: registration
  0xe5cb65b17c4f031087794faa905386b1901e2b27f23dddbd61fac9376b4d56a5.
  The acceptance transaction 0xd77f426c33b10cd5c67ebc33cd8465f871924dc16ca54d3cb667f3975bd4b1ae
  did not record acceptance before its window; get_program read accepted=0.
  Assessment 0x6c5a6e976fdf5553ee18e06e04b52738754f6148c27db2fb06bc1a370af326e3
  finalized with an expected stale-program rollback.

No `REWARDABLE` receipt was obtained on the superseded primary. The current-primary
RewardGate is deployed and its fail-closed, substitution and unauthorized-call
controls were exercised, but no successful current-primary action or replay
receipt can be claimed because the bound programme is not rewardable.

## Historical proof, retained but not promoted

The prior corrected primary was
0x9aAB4148ff9C939Be58C64dD5bfa0FCFecBDA881 with source SHA-256
e516fb4a497bb2b8bad20cca5b141b3b033fc625a609201119c660d375d4d10b. Its
controlled positive assessment
0xf20659666a3b89cee1e6bd0076d150e8ab2b4c5c16765f87863630c079c32fb2 returned
REWARDABLE. The bound historical RewardGate was
0x83C553f6Ccd9d3Ea5f474f69F275b781F22F52F0; its successful action was
0x8c838c497d329247147c52db4c317ccd5e0b262853c5aa5c0bcb48b3dce7c423 and its
replay rollback was
0xb81743cea6d116f0472a036d3136bc364ae7ebfc0c5c512f50ed3f5db3c534d8.

Those receipts prove the previous primary only and are not new-primary proof.

## Source integrity and release status

- Current Goodhart local SHA-256:
  10414807d2545f999915e62300d8b385c2888ae36b6faaf55176be5163fa6bab.
- Current RewardGate local SHA-256:
  612cc909263f8d1bff3d7ec4d9ceeab0f0f31ee2252bb39f79c7443305eda20b.
- Current Goodhart deployed bytes match the final local contract bytes exactly.
- The RewardGate deployed bytes match the final local contract bytes exactly.
- No explorer URL is claimed because the configured explorer endpoint returned
  HTTP 503 during prior closeout.
- No secrets, frontend, backend, database, Docker or wallet UI are committed.

Release recommendation: CONDITIONAL. The two scoped binding defects are fixed,
tested, deployed and source-parity verified, and current-primary fail-closed
consumer controls are live. A fresh current-primary `REWARDABLE` assessment,
successful authorized RewardGate action and replay receipt remain unverified;
the historical positive proof belongs to an earlier primary. Hold a claim of
complete end-to-end current-build integration if that receipt is mandatory for
the reviewer, but do not weaken consensus or turn the controlled fixture into
false positive evidence.
