# GOODHART verification plan

## Commands

```text
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
```

## Current results

- Offline/unit: 32 passed.
- Direct Mode: 16 passed, including native `run_validator()` re-observation.
- Combined pytest: 48 passed.
- Preflight: 18 assertions passed.
- Mutation checks: 4/4 critical weakened variants killed.
- GenVM lint and schema: both contracts passed with linter `0.11.0` and
  runner `v0.2.12`.
- `eth_chainId`: `0xf22f` / `61999`; local CLI: `0.39.1`.

Direct Mode uses a local simulated VM and mocked sources. It is not a finalized
StudioNet transaction or proof of publisher independence.

## Security coverage

The suites cover exact proxy schema and integer arithmetic, URL restrictions,
control characters, prompt injection, complete-source bounds, distant
counterevidence, unique witnesses, source mutation, digest mismatch, malformed
semantic responses, positive-witness veto, malicious leader proposals,
independent validator callbacks, owner authorization, stale fingerprints,
bounded retry, terminal states, cancellation and RewardGate replay/binding.

The true Keccak-256 test uses the standard empty-input vector
`c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470` and a
domain-separated programme hash. Python `hashlib.sha3_256` is not used as a
GenVM Keccak substitute.

## Live evidence levels

The corrected primary deployment is recorded in `DEPLOYMENT.md`. Its fresh
external XZ assessment finalized `MAJORITY_AGREE` and terminal
`INCONCLUSIVE`, with proxy `20 -> 80` and both outcomes `UNKNOWN`; this is a
successful fail-closed control. A separate controlled fixture finalized
`REWARDABLE` after one bounded retry, and the newly bound RewardGate authorized
action succeeded once and rejected an identical replay. These are finalized
corrected-primary receipts, not simulations or historical-primary
substitutions. The controlled fixture remains mechanics evidence rather than
authenticated real-world publisher or outcome proof.
