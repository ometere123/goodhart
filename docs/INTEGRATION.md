# GOODHART integration

`RewardGate` is a minimal Intelligent Contract consumer. Its constructor
freezes a typed Goodhart registry address, program ID, program fingerprint,
beneficiary address and 64-character action hash. `execute_once(action_hash)`
requires the frozen beneficiary, exact action hash, an unused action and a
successful cross-contract `IGoodhart.View.is_rewardable(program_id,
fingerprint)` call. The execution receipt stores the same bindings and
`was_executed` exposes deterministic replay state.

The gate does not hold GEN, transfer funds, accept a caller-supplied verdict or
interpret a receipt. A reverted, pending or non-`REWARDABLE` Goodhart state
therefore cannot authorize the action. A different program, fingerprint,
beneficiary or action is not interchangeable.

Direct Mode exercises Goodhart’s contract class and native
`direct_vm.run_validator()` re-observation. The pinned Direct Mode runner does
not provide a production cross-contract chain, so RewardGate’s final
interoperability proof must come from a finalized StudioNet call. Local
simulation is never reported as live consensus.

