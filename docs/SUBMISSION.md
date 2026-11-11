# GOODHART submission brief

## Title

GOODHART — Consensus-backed proxy–objective divergence gate

## Description

GOODHART is a consensus-backed proxy–objective divergence primitive that freezes an incentive programme’s real objective and measurable proxy, independently evaluates public evidence of underlying outcomes, and exposes an exact-hash reward permission only when proxy and objective improvements withstand validator scrutiny. The contract computes proxy thresholds deterministically, rejects incomplete or oversized evidence, and requires two independently re-observed outcome sources plus adversarial positive-witness checks. Immutable fingerprints, beneficiary acceptance, bounded retries, terminal receipts and RewardGate replay protection make the result composable without custody or payouts. Public evidence remains bounded: this does not prove identity, publisher independence, causation, payment, intentional metric gaming or legal liability.

Description character count including spaces: 848.

## Links

- Repository: https://github.com/ometere123/goodhart
- Current Goodhart: 0xc6f159b8A0475D32c39033131D5b4E496581f38a
- Current explorer: not verified; the configured explorer endpoint returned HTTP 503.
- Current RewardGate: not deployed; no fresh REWARDABLE receipt exists on the current primary.
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

- Offline unittest: 33 passed.
- Direct Mode: 25 passed.
- Combined pytest: 58 passed.
- Preflight: 20 assertions passed.
- Mutation checks: 5/5 killed.
- GenVM lint/schema: both contracts passed with linter 0.11.0 and runner v0.2.12.
- Current primary deployment: 0x7cb4e4544e03257b6fcbbce512977f288d9ec5af3b93acb2c8a4b33bb7b5cc58, finalized MAJORITY_AGREE and execution SUCCESS.
- Current beneficiary assessment: 0x339d9a253852b49287f4e7607d4e6bee17056a001a10f73051f41a1e8ab32731, finalized MAJORITY_AGREE and execution SUCCESS, INCONCLUSIVE, is_rewardable=false.

## Limitations and readiness

Three hostnames do not prove independent ownership or truthful reporting. Public
snapshots can be stale or selectively curated. The protocol does not establish
real-world identity, action completion, causality, data completeness,
intentional manipulation, payment or legal liability. RewardGate proves a
conditional one-shot permission and does not custody or transfer GEN.

Submission readiness: NOT READY — a fresh finalized REWARDABLE receipt on the
current primary and a new-primary RewardGate authorized/replay proof remain
unverified.
