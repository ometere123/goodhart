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

The final proof-bound RewardGate deployment is
`0xa718F7aff4a7fB57E3070100c27b90830b60A3Ae`. It is bound to the final
Goodhart address, program `fixture-rewardable-final-20261110`, fingerprint
`e01446f6d9b58e0913f780f0901d094dc4940ac0fc2d14fa35c00d4eec0917dd`, the
beneficiary address and action hash
`5d16f2b1ddada8ea1963aa89645b1b12426a830e8793c80914163fbd5cd8713b`.
After the primary assessment finalized `REWARDABLE`, the authorized beneficiary
executed successfully in
`0x926f8248e746667aaccbc0ea899b3a1c6318f51ecffdec66b71485b444a415f9` and
`was_executed` read back `true`. A second identical call finalized with
`EXPECTED: replay` in
`0xce7a86670ddf252cd317273d401058b8c7a32840de0c66a163e4dc991b18aea1`, while
the execution record remained true. Stale, substituted and unauthorized calls
remain separately recorded as failed closed controls.

The positive live case uses controlled public fixtures. It proves exact
cross-contract permission and replay behavior, not publisher identity,
real-world action completion, causality or payment.

