# GOODHART submission brief

## Title

GOODHART — Consensus-backed proxy–objective divergence gate

## Description

GOODHART is a consensus-backed proxy–objective divergence primitive that freezes an incentive programme’s real objective and measurable proxy, independently evaluates public evidence of underlying outcomes, and exposes an exact-hash reward permission only when proxy and objective improvements withstand validator scrutiny. The contract computes proxy thresholds deterministically, rejects incomplete or oversized evidence, and requires two independently re-observed outcome sources plus adversarial positive-witness checks. Immutable fingerprints, bounded retries, terminal receipts and RewardGate replay protection make the result composable without custody or payouts. Public evidence remains bounded: this does not prove identity, publisher independence, causation, payment, intentional metric gaming or legal liability.

**Description character count (including spaces): 828.**

## Links

- Repository: https://github.com/ometere123/goodhart
- Goodhart explorer: Pending finalized deployment
- RewardGate explorer: Pending finalized deployment

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
- CI and finalized live proofs: update from the actual final run; local Direct
  Mode is not live StudioNet evidence.

## Limitations

Three hostnames do not prove independent ownership or truthful reporting.
Public snapshots can be stale, selectively curated or changed after an
assessment. The protocol does not establish real-world identity, action
completion, causality, data completeness, intentional manipulation, payment or
legal liability. RewardGate demonstrates a conditional one-shot permission and
does not custody or transfer GEN. No frontend, backend or application wallet is
part of this submission.
