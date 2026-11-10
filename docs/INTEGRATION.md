# GOODHART integration

`RewardGate` is a minimal Intelligent Contract consumer. Its constructor
freezes a typed Goodhart registry address, programme ID, programme fingerprint,
beneficiary address and 64-character action hash. `execute_once(action_hash)`
requires the frozen beneficiary, exact action hash, an unused action and a
successful cross-contract `IGoodhart.View.is_rewardable(program_id,
fingerprint)` call. `was_executed` exposes deterministic replay state.

The gate does not custody GEN, transfer funds, accept a caller-supplied verdict
or interpret a receipt. A pending, reverted, non-`REWARDABLE` or mismatched
Goodhart state cannot authorize the action. A different programme, fingerprint,
beneficiary or action is not interchangeable.

## Testing level

Direct Mode exercises Goodhart’s contract class and native
`direct_vm.run_validator()` re-observation. The pinned Direct Mode runner does
not provide production cross-contract finality, so local consumer tests are
not live StudioNet proof.

## Current deployment status

The corrected primary is
`0x9aAB4148ff9C939Be58C64dD5bfa0FCFecBDA881`, with source hash
`e516fb4a497bb2b8bad20cca5b141b3b033fc625a609201119c660d375d4d10b`.

No RewardGate has been deployed against a fresh `REWARDABLE` programme on that
corrected primary. The exact live external assessment
`0x68dd7b602f83193be6ed03a388fa7beefb26cbb633c72fd111d191d4e781edae`
finalized `INCONCLUSIVE`, so an authorized new-build action would correctly be
blocked. The required fresh positive authorization and replay receipts remain
unverified rather than being inferred from a different deployment.

## Historical interoperability proof

The prior Goodhart deployment had a proof-bound gate at
`0xa718F7aff4a7fB57E3070100c27b90830b60A3Ae`, bound to the prior primary
`0x7F1eE6dA4ED706E363B54713B6dfc0dB2AA64234`. Its authorized action finalized
successfully in
`0x926f8248e746667aaccbc0ea899b3a1c6318f51ecffdec66b71485b444a415f9`,
and the identical replay finalized with the expected rollback in
`0xce7a86670ddf252cd317273d401058b8c7a32840de0c66a163e4dc991b18aea1`.
Those receipts prove the consumer design and replay protection on the prior
source only; they are historical and are not new-primary proof.
