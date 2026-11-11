# GOODHART submission brief

## Title

GOODHART — Consensus-backed proxy–objective divergence gate

## Description

GOODHART is a consensus-backed proxy–objective divergence primitive that freezes an incentive programme’s real objective and measurable proxy, independently evaluates public evidence of underlying outcomes, and exposes an exact-hash reward permission only when proxy and objective improvements withstand validator scrutiny. The contract computes proxy thresholds deterministically, rejects incomplete or oversized evidence, and requires two independently re-observed outcome sources plus adversarial positive-witness checks. Immutable fingerprints, beneficiary acceptance, bounded retries, terminal receipts and RewardGate replay protection make the result composable without custody or payouts. Public evidence remains bounded: this does not prove identity, publisher independence, causation, payment, intentional metric gaming or legal liability.

Description character count including spaces: 848.

## Links

- Repository: https://github.com/ometere123/goodhart
- Current Goodhart: 0xbea069743269137772E42873aB0D2dE3E9EDC411
- Current explorer: not verified; the configured explorer endpoint returned HTTP 503.
- Current RewardGate: 0x46c240DCAA5bDD440f0C41a3499a4096471e2F8B, bound to the
  current primary and a nonrewardable control programme.
- Historical RewardGate: 0x83C553f6Ccd9d3Ea5f474f69F275b781F22F52F0, bound to the previous primary only.

## GenLayer-native mechanism

Deterministic code verifies the proxy schema and integer threshold, while the
leader and validators independently fetch and interpret frozen public outcome
sources. Validators recompute material labels, digests, quotes and adversarial
compatible readings before a positive status can be committed. The beneficiary
also authenticates acceptance of the exact frozen programme, and either owner
or beneficiary can initiate assessment after the window opens. An LLM never
selects a recipient or reward amount.

## Verification snapshot

- Offline unittest: 34 passed.
- Direct Mode: 26 passed.
- Combined pytest: 60 passed.
- Preflight: 20 assertions passed.
- Mutation checks: 6/6 killed.
- GenVM lint/schema: both contracts passed with linter 0.11.0 and runner v0.2.12.
- Current primary deployment: 0xcd47489c9e46e18b595b086a9cee71f3d9330070bab1e88977caceba321a7841, finalized MAJORITY_AGREE and execution SUCCESS.
- Current RewardGate deployment: 0xcfc3d88f13f89a63989f309e0605e562df885be8bd2c71813b3a4f2941efa95d, finalized MAJORITY_AGREE and execution SUCCESS.
- Current control programme readback: `binding-control-20261111`, accepted=0,
  PENDING, fingerprint `5a6a6dacbd577d77d19bf0f07af4cd655260309c5654a2ea18b7c111a908d750`.
- Current gate controls: nonrewardable action, substituted action and
  unauthorized caller all finalized with rollback; `was_executed=false`.

## Limitations and readiness

Three hostnames do not prove independent ownership or truthful reporting. Public
snapshots can be stale or selectively curated. The protocol does not establish
real-world identity, action completion, causality, data completeness,
intentional manipulation, payment or legal liability. RewardGate proves a
conditional one-shot permission and does not custody or transfer GEN.

Submission recommendation: CONDITIONAL — the two scoped binding corrections
are implemented, tested, deployed and source-parity verified. Current-primary
fail-closed consumer controls are live. A fresh current-primary REWARDABLE
assessment followed by successful authorized RewardGate execution and replay
remains unverified; the historical positive proof is not promoted to current
build evidence. Do not claim complete end-to-end current-build integration
unless that receipt is required and later obtained.
