# GOODHART verification plan

All commands use the repository-local CLI and Python 3.12 environment:

```text
npm ci --ignore-scripts
py -3.12 -m pip install -r requirements-dev.txt
node scripts/assert_studionet.mjs
py -3.12 scripts/preflight.py
py -3.12 -m unittest discover -s tests -p 'test_*.py' -v
py -3.12 -m pytest -q tests/direct -s
py -3.12 -m compileall -q contracts scripts tests
GENVM_VERSION=v0.2.12 genvm-lint check contracts/goodhart.py
GENVM_VERSION=v0.2.12 genvm-lint check contracts/reward_gate.py
GENVM_VERSION=v0.2.12 genvm-lint schema contracts/goodhart.py --json
GENVM_VERSION=v0.2.12 genvm-lint schema contracts/reward_gate.py --json
```

The host suite covers exact proxy parsing and arithmetic, URL restrictions,
prompt-injection boundaries, exact model schemas, source normalization,
oversized evidence, distant counterevidence, witness provenance and immutable
public write surface. The Direct Mode suite covers live contract-class
execution, the native `run_validator()` callback, positive and divergent
outcomes, proxy failure, ambiguity, source mutation, forged observations,
owner-only assessment, terminal state and oversized-source fail-closed
behavior.

The current verified local counts are 31 host/offline tests and 15 Direct Mode
tests, 46 when collected together by pytest. The 12 original preflight checks
were expanded to 18 assertions. Direct Mode uses the local simulated VM and
mocked sources; it is not a StudioNet transaction or proof of publisher
independence. Live evidence, finality, cross-contract execution and deployed
source parity are recorded separately in `docs/DEPLOYMENT.md`.

CI repeats offline tests, compilation, preflight, pinned GenVM lint/schema,
Direct Mode, the explicit StudioNet RPC guard and a production-dependency npm
audit. The locked GenLayer package currently has development-tool advisories;
the CI audit intentionally excludes dev-only tooling, while the exact graph
remains pinned for reproducibility.

## Finalized StudioNet evidence

The final byte-identical deployments are recorded in `docs/DEPLOYMENT.md`.
Finalized live controls include `PROXY_NOT_IMPROVED`, `UNSUPPORTED`, bounded
`RETRYABLE` then terminal `INCONCLUSIVE`, cancellation, stale fingerprint,
stale consumer binding, action substitution and unauthorized executor rejection.
The final byte-identical deployment was also exercised with a fresh bounded
positive fixture. Registration finalized in
`0xb1a9f01bd91b8a9c741fe8c9c44b5fc89f1c643ec58b142e1fc0c4d50a3ae0a4` and the
assessment finalized in
`0x51297a28d9f9cf30b7a4f519c72f2203d2befc7fa2d49bd60c2de508a1e37481` as
`REWARDABLE`, with proxy `20 -> 80`, both outcome labels `IMPROVED`, and
`is_rewardable=true`. The exact-bound RewardGate authorized execution and
replay rejection are recorded in `docs/DEPLOYMENT.md`. Controlled fixtures
demonstrate protocol mechanics and are not claims of publisher identity,
causality or real-world outcome truth. Earlier `INCONCLUSIVE` attempts remain
historical fail-closed controls.

