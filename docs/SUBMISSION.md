# GOODHART submission brief

## Title

GOODHART — Consensus-backed proxy–objective divergence gate

## Description

GOODHART is a consensus-backed proxy–objective divergence primitive that freezes an incentive programme’s real objective and measurable proxy, independently evaluates public evidence of underlying outcomes, and exposes an exact-hash reward permission only when proxy and objective improvements withstand validator scrutiny. The contract computes proxy thresholds deterministically, rejects incomplete or oversized evidence, and requires two independently re-observed outcome sources plus adversarial positive-witness checks. Immutable fingerprints, bounded retries, terminal receipts and RewardGate replay protection make the result composable without custody or payouts. Public evidence remains bounded: this does not prove identity, publisher independence, causation, payment, intentional metric gaming or legal liability.

**Description character count (including spaces): 828.**

## Links

- Repository: https://github.com/ometere123/goodhart
- Goodhart explorer: Not verified; `https://genlayer-explorer.vercel.app` returned HTTP 503 during closeout
- RewardGate explorer: Not verified; `https://genlayer-explorer.vercel.app` returned HTTP 503 during closeout

## GenLayer-native mechanism

Deterministic code can verify a proxy JSON schema and exact basis-point
movement, but it cannot safely reduce conflicting public outcome narratives to a
single objective verdict. The leader and validators independently fetch the
three frozen HTTPS sources and classify the underlying objective. Validators
recompute material labels and digests, reject malformed or substituted
observations, and adversarially challenge each leader witness before a positive
result is accepted. Only the deterministic post-consensus state transition can
create `REWARDABLE`; an LLM never selects a recipient or reward amount.

## Verification snapshot

- Offline/host tests: 31 passed.
- Native Direct Mode tests: 15 passed, including `direct_vm.run_validator()`.
- Combined pytest collection: 46 passed.
- Preflight: 18 assertions passed.
- GenVM linter/schema: both contracts pass with `genvm-linter==0.11.0` and
  `GENVM_VERSION=v0.2.12`.
- Final Goodhart deployment: `0x7F1eE6dA4ED706E363B54713B6dfc0dB2AA64234`,
  finalized deployment transaction `0x9453ddcc3f8bfa96e84f26227b5c8ffbc59478166d20e1f0ec022fc7997847d8`.
- Final RewardGate source deployment: `0x04f0e8C16256161ac674C0dE5305769bE1b895c9`,
  finalized deployment transaction `0x8524c59c01f181a2c2b903acf21739f31825de8a65e12957bd59183e25f75f30`.
- Final proof-bound RewardGate instance: `0xa718F7aff4a7fB57E3070100c27b90830b60A3Ae`,
  finalized deployment transaction `0xc4595146d2d667e2b52603cd6f2eac4c1f8638fa76d3e1559e2d4ee053b36f9c`.
- Fresh final Goodhart positive assessment:
  `0x51297a28d9f9cf30b7a4f519c72f2203d2befc7fa2d49bd60c2de508a1e37481`,
  finalized `MAJORITY_AGREE` with `REWARDABLE`, both outcomes `IMPROVED`, and
  `is_rewardable=true` for fingerprint
  `e01446f6d9b58e0913f780f0901d094dc4940ac0fc2d14fa35c00d4eec0917dd`.
- Authorized exact-action execution finalized in
  `0x926f8248e746667aaccbc0ea899b3a1c6318f51ecffdec66b71485b444a415f9`;
  identical replay finalized in
  `0xce7a86670ddf252cd317273d401058b8c7a32840de0c66a163e4dc991b18aea1` with
  `EXPECTED: replay`. Local Direct Mode is not live StudioNet evidence.

## Limitations

Three hostnames do not prove independent ownership or truthful reporting.
Public snapshots can be stale, selectively curated or changed after an
assessment. The protocol does not establish real-world identity, action
completion, causality, data completeness, intentional manipulation, payment or
legal liability. RewardGate demonstrates a conditional one-shot permission and
does not custody or transfer GEN. No frontend, backend or application wallet is
part of this submission.

## Readiness

Submission-ready for the documented protocol scope. The final byte-identical
Goodhart deployment has a fresh finalized `REWARDABLE` receipt and the exact
bound RewardGate has a finalized authorized execution plus replay rejection.
The live positive case uses controlled public fixtures; it does not establish
publisher identity, real-world action completion, causality, payment,
intentional metric gaming or legal liability.
