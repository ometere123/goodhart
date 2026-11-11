# GOODHART verification plan

## Commands actually run

    npm ci --ignore-scripts
    py -3.12 -m pip install -r requirements-dev.txt
    node scripts/assert_studionet.mjs
    py -3.12 scripts/preflight.py
    py -3.12 -m unittest discover -s tests -p 'test_*.py' -v
    py -3.12 -m pytest -q tests/direct -s
    py -3.12 -m pytest -q tests
    py -3.12 -m compileall -q contracts scripts tests
    py -3.12 scripts/mutation_check.py
    GENVM_VERSION=v0.2.12 genvm-lint check contracts/goodhart.py
    GENVM_VERSION=v0.2.12 genvm-lint check contracts/reward_gate.py
    GENVM_VERSION=v0.2.12 genvm-lint schema contracts/goodhart.py --json
    GENVM_VERSION=v0.2.12 genvm-lint schema contracts/reward_gate.py --json

## Latest local results

- Offline unittest suite: 34 passed.
- Direct Mode: 26 passed, including native validator re-observation.
- Combined pytest: 60 passed.
- Preflight: 20 assertions passed.
- Mutation checks: 6/6 weakened variants killed.
- Python compilation: passed.
- GenVM lint/schema: both contracts passed with linter 0.11.0 and runner v0.2.12.
- Stable RPC guard: eth_chainId=0xf22f / 61999.
- Local repository CLI: 0.39.1.

Coverage includes beneficiary authentication, exact fingerprint acceptance, duplicate/late acceptance, post-acceptance cancellation, owner or beneficiary assessment rights, source bounds, distant counterevidence, prompt injection, strict proxy arithmetic, source mutation, digest mismatch, malicious leader proposals, independent validator callbacks, bounded retry, terminal state and RewardGate replay/binding. True Keccak-256 tests use the standard empty-input vector; hashlib.sha3_256 is not used as a Keccak substitute.

Direct Mode uses controlled pages and mocked model responses where indicated. It is not a live StudioNet transaction or proof of publisher independence.

## Live evidence level

The corrected primary `0xbea069743269137772E42873aB0D2dE3E9EDC411` and bound
RewardGate `0x46c240DCAA5bDD440f0C41a3499a4096471e2F8B` have finalized
deployment parity. The bound control programme is PENDING/nonrewardable. Its
correct action, substituted action and unauthorized caller all finalized with
rollback and left `was_executed=false`. A fresh current-primary positive
assessment attempt `0xc79c00d72d8be00e79030032fc60ea86e956ae86c9777c44b1ce5f1df0afe12c`
finalized execution SUCCESS but terminal `INCONCLUSIVE` with proxy `20 -> 80`
and `UNKNOWN / UNKNOWN` outcomes. A successful current-primary consumer action
was not obtained; the historical positive RewardGate proof is not current-primary
coverage.
