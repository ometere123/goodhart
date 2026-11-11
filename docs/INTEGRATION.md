# GOODHART integration

RewardGate is a minimal Intelligent Contract consumer. Its constructor freezes a typed Goodhart registry address, programme ID, programme fingerprint, beneficiary address and 64-character action hash. execute_once(action_hash) requires the frozen beneficiary, exact action hash, an unused action and a successful cross-contract IGoodhart.View.is_rewardable(program_id, fingerprint) call. was_executed exposes deterministic replay state.

The gate does not custody GEN, transfer funds, accept a caller-supplied verdict or interpret a receipt. Pending, reverted, non-REWARDABLE or mismatched Goodhart state cannot authorize an action.

## Testing level

Direct Mode exercises Goodhart and native direct_vm.run_validator() source re-observation. The pinned runner does not provide live StudioNet cross-contract finality; local consumer tests are not on-chain proof.

## Deployment status

The corrected Goodhart primary is
0xbea069743269137772E42873aB0D2dE3E9EDC411 with source SHA-256
10414807d2545f999915e62300d8b385c2888ae36b6faaf55176be5163fa6bab.

RewardGate is deployed against this exact address at
0x46c240DCAA5bDD440f0C41a3499a4096471e2F8B with source SHA-256
612cc909263f8d1bff3d7ec4d9ceeab0f0f31ee2252bb39f79c7443305eda20b. Its
constructor beneficiary is additionally checked against the primary programme
readback before the primary `is_rewardable` predicate is called.

The bound control programme is PENDING/nonrewardable. The current gate’s
correct-action, substituted-action and unauthorized-caller transactions all
finalized with rollback, and `was_executed` remained false. A successful current
primary action and replay proof therefore remain unverified. The historical gate
0x83C553f6Ccd9d3Ea5f474f69F275b781F22F52F0 is bound to the previous primary
0x9aAB4148ff9C939Be58C64dD5bfa0FCFecBDA881; its successful action and replay
rollback remain historical evidence only.
