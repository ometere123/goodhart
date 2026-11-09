# GOODHART — make rewards depend on the objective, not the proxy

**Standalone GenLayer Intelligent Contract primitive. No frontend or product backend.**

When an autonomous worker is paid for a proxy (tickets closed, patches merged,
items inspected), the proxy can improve while the actual goal deteriorates.
GOODHART creates a version-frozen, consensus-backed **proxy–objective divergence
gate**. A consumer can execute its precommitted reward action only after two
public, separately hosted outcome surfaces support improvement in the underlying
objective. Numerical proxy changes and all transition decisions are deterministic.

**This is not a general-purpose “AI decides whether to pay” oracle.** The model
cannot write or change the contract's objective, calculate a reward, choose a
recipient, or bypass a gate. A safe verdict is narrowly scoped to the
predeclared public evidence surface; it does not prove genuine causal impact,
the independence of publishers or that unpublished failures do not exist.

## The mechanism

```text
Create one frozen programme
  owner + beneficiary + objective + observable outcome indicator
  exact proxy baseline/unit/direction/minimum basis-point improvement
  public proxy JSON endpoint + 2 outcome endpoints on different HTTPS hosts
  earliest assessment time + deadline
               |
               v
Assess (owner only, within the fixed window)
  validators independently fetch and parse proxy JSON (no model arithmetic)
               |
               +-- proxy short of threshold --> PROXY_NOT_IMPROVED
               |
               +-- proxy improved -----------> classify both outcome sources
                                                + positive-claim adversarial audit
                                                + independent validator re-fetch
                                                + independent substantive re-read
               |
               +-- BOTH improved ------------> REWARDABLE
               +-- either degraded/mixed ----> DIVERGENT
               +-- no affirmative improvement > UNSUPPORTED
               +-- ambiguous / missing -----> INCONCLUSIVE (fail closed)
               |
               v
Receipt binds objective, sources, claimed numeric result and programme hash
               |
               v
Another IC: is_rewardable(program_id, fingerprint) → exact one-shot gate
```

## Why GenLayer is necessary

Counting closed tickets is deterministic. Establishing whether actual customer
issues became less harmful, despite selective reporting, reopened tickets and
contradictory language, is not. GOODHART puts only the latter operation in
GenLayer's nondeterministic consensus block. Leader and validators separately
fetch every public source, classify the **underlying objective** rather than
the proxy, and scrutinize favourable findings for material qualifications.
This is a custom `gl.vm.run_nondet_unsafe` comparator, not JSON-format voting.
State writes, exact basis-point arithmetic and reward gating occur after
consensus in deterministic code.

## Contracts

- [`contracts/goodhart.py`](contracts/goodhart.py): persistent programme registry,
  frozen fingerprint, source-backed assessments, bounded retry, immutable
  terminal receipts, `is_rewardable(program_id, fingerprint)`.
- [`contracts/reward_gate.py`](contracts/reward_gate.py): minimal typed IC consumer.
  It verifies the exact registry/programme fingerprint and allows a specified
  beneficiary to record one precommitted action once. **It intentionally does
  not custody or transfer GEN**; a wallet/escrow/treasury can instead consume
  the same exact view method during its own deterministic transfer logic.

Both contracts are standalone Python Intelligent Contracts, not an app.

### Primary interface

| Method | Effect |
|---|---|
| `register_program(...)` | Freezes objective, proxy parameters, 3 source URLs, beneficiary and time window; returns fingerprint |
| `assess(program_id, expected_fingerprint)` | Bounded owner-only consensus observation; terminal verdict or one retry |
| `cancel(program_id)` | Owner may stop an unassessed programme; irreversible |
| `is_rewardable(program_id, fingerprint)` | True only on matching, finalized `REWARDABLE` state |
| `get_program(program_id)` | Exact terms, fingerprint and phase |
| `get_receipt(program_id)` | Decision, numerical metric, quotes and source digests |

### Example

```text
Registered objective: actually reduce unresolved support incidents and repeats.
Proxy: tickets marked closed, baseline=20, direction=UP, minimum +30%.

Case A: proxy=80. Two public outcome sources establish fewer repeats.
  => REWARDABLE; consumer may record its one precommitted reward action.

Case B: proxy=80. Independent customer report says repeats worsened.
  => DIVERGENT; consumer refuses execution.

Case C: proxy=21 (+5%). Even if outcome pages praise the agent:
  => PROXY_NOT_IMPROVED. The expensive LLM audit is not needed.

Case D: proxy=80; one outcome source unavailable or ambiguous:
  => RETRYABLE or INCONCLUSIVE; no reward.
```

## Locked network — do not substitute

| Setting | Required value |
|---|---|
| Network | **`studionet`** |
| Chain ID | **`61999`** (`0xf22f`) |
| RPC | `https://studio.genlayer.com/api` |
| CLI | Repository-local **`genlayer@0.39.1`** |
| Direct Mode SDK | `v0.2.12` |
| GenVM contract runner pin | `py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6` |

Do not use network `studionet-dev`, chain `61997`, or global
`genlayer@0.40.0rc2` for this release. CLI invocations go through `npm run`
or `./node_modules/.bin/genlayer` only.

## Install and verify

```bash
npm ci --ignore-scripts
python3 -m pip install -r requirements-dev.txt
npm run cli:version           # must print 0.39.1
npm run network:check        # must print studionet / 61999
npm run preflight
npm run test:offline
python3 -m pytest -q tests/direct
GENVM_VERSION=v0.2.12 genvm-lint check contracts/goodhart.py
GENVM_VERSION=v0.2.12 genvm-lint check contracts/reward_gate.py
```

Native Direct Mode uses a local simulated VM and does **not** contact the
`localnet` RPC displayed by the test plugin. Never mistake Direct Mode for a
finalized on-chain StudioNet execution.

## Live deployment handoff

Deployment requires a locally configured, funded GenLayer CLI account. This
repository never includes or asks you to commit a private key.

```bash
npm ci --ignore-scripts
npm run network:check
./node_modules/.bin/genlayer account list
npm run deploy:studionet
```

After deploying, **wait for finalization**, inspect transaction receipt and
code/schema, exercise both a favourable and a divergent programme against
real public HTTPS evidence (not just mocks), and document links in
[`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md). Use the same explicit chain/RPC for
the separately deployed `RewardGate`. Never represent an `Accepted` transaction
or a Direct Mode test as a finalized StudioNet proof.

## Verification and scope

- Host-side tests: exact integer arithmetic, disagreement handling, parser
  hardening, witness integrity, URL filtering, prompt boundaries and state
  immutability checks.
- GenVM Direct Mode tests: live contract-class execution, independently
  re-run validator, forged result/source mutation, owner-only assessment,
  bounded retry and terminal-state behaviour.
- Static GenVM lint: both contracts must pass with the pinned runner.
- [Threat model](docs/THREAT_MODEL.md) describes critical trust boundaries.
- [Deployment status](docs/DEPLOYMENT.md) separates proof from work remaining.
- [Submission brief](docs/SUBMISSION.md) gives a reviewer-focused summary.

## Limitations, deliberately visible

1. Three different hostnames do **not** prove independent ownership, truthful
   reporting, or immunity to collusion. Real integrations should use established
   external publishers and verify their authority separately.
2. A public snapshot can be stale, selectively curated or subsequently edited;
   the receipt proves only what the consensus-examined surface supported during
   assessment. No unstated time-series completeness guarantee exists.
3. No arbitrary subjective or probabilistic confidence score authorizes value.
   Mixed, contradictory, ambiguous or unavailable material fails closed.
4. GOODHART assesses alignment, not causation or intentional manipulation. It
   cannot prove that the evaluated agent caused the outcome, or infer fraud.
5. The `RewardGate` shows composability but makes no financial transfer. Native
   GEN custody is intentionally outside this primitive's trust boundary.

MIT licensed. Source and tests are intended to be read, adapted and extended.
