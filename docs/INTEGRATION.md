# GOODHART integration

RewardGate is a minimal Intelligent Contract consumer. Its constructor freezes a typed Goodhart registry address, programme ID, programme fingerprint, beneficiary address and 64-character action hash. execute_once(action_hash) requires the frozen beneficiary, exact action hash, an unused action and a successful cross-contract IGoodhart.View.is_rewardable(program_id, fingerprint) call. was_executed exposes deterministic replay state.

The gate does not custody GEN, transfer funds, accept a caller-supplied verdict or interpret a receipt. Pending, reverted, non-REWARDABLE or mismatched Goodhart state cannot authorize an action.

## Testing level

Direct Mode exercises Goodhart and native direct_vm.run_validator() source re-observation. The pinned runner does not provide live StudioNet cross-contract finality; local consumer tests are not on-chain proof.

## Deployment status

The final consented Goodhart primary is 0xc6f159b8A0475D32c39033131D5b4E496581f38a with source SHA-256 7d2dae0e1c8c5e3b7ecf26c79fc3534beb8909f2394ef157baeb814f3f138106.

No RewardGate has been deployed against this address because no fresh REWARDABLE receipt was finalized on it. The historical gate 0x83C553f6Ccd9d3Ea5f474f69F275b781F22F52F0 is bound to the previous primary 0x9aAB4148ff9C939Be58C64dD5bfa0FCFecBDA881; its successful action and replay rollback remain historical evidence only.

The final-primary beneficiary assessment finalized INCONCLUSIVE and is_rewardable=false. A new gate should be deployed only after a fresh finalized reward receipt is independently read back.
