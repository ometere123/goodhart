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

- Offline unittest suite: 33 passed.
- Direct Mode: 25 passed, including native validator re-observation.
- Combined pytest: 58 passed.
- Preflight: 20 assertions passed.
- Mutation checks: 5/5 weakened variants killed.
- Python compilation: passed.
- GenVM lint/schema: both contracts passed with linter 0.11.0 and runner v0.2.12.
- Stable RPC guard: eth_chainId=0xf22f / 61999.
- Local repository CLI: 0.39.1.

Coverage includes beneficiary authentication, exact fingerprint acceptance, duplicate/late acceptance, post-acceptance cancellation, owner or beneficiary assessment rights, source bounds, distant counterevidence, prompt injection, strict proxy arithmetic, source mutation, digest mismatch, malicious leader proposals, independent validator callbacks, bounded retry, terminal state and RewardGate replay/binding. True Keccak-256 tests use the standard empty-input vector; hashlib.sha3_256 is not used as a Keccak substitute.

Direct Mode uses controlled pages and mocked model responses where indicated. It is not a live StudioNet transaction or proof of publisher independence.

## Live evidence level

The new consented primary has finalized acceptance, unauthorized acceptance rejection, post-acceptance owner-cancellation rejection and a beneficiary-triggered fail-closed INCONCLUSIVE assessment. A fresh positive assessment was not finalized as a reward permission: one attempt was MAJORITY_DISAGREE, one was a stale/out-of-window rollback, and committed-fixture attempts were fail-closed or acceptance-incomplete. The historical positive RewardGate proof is not current-primary coverage.
