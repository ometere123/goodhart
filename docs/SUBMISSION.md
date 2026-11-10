# GOODHART submission brief

## Title

GOODHART — Consensus-backed proxy–objective divergence gate

## Description

GOODHART is a consensus-backed proxy–objective divergence primitive that freezes an incentive programme’s real objective and measurable proxy, independently evaluates public evidence of underlying outcomes, and exposes an exact-hash reward permission only when proxy and objective improvements withstand validator scrutiny. The contract computes proxy thresholds deterministically, rejects incomplete or oversized evidence, and requires two independently re-observed outcome sources plus adversarial positive-witness checks. Immutable fingerprints, bounded retries, terminal receipts and RewardGate replay protection make the result composable without custody or payouts. Public evidence remains bounded: this does not prove identity, publisher independence, causation, payment, intentional metric gaming or legal liability.

**Description character count including spaces: 824.**

## Links

- Repository: https://github.com/ometere123/goodhart
- Corrected Goodhart: `0x9aAB4148ff9C939Be58C64dD5bfa0FCFecBDA881`
- Explorer: not verified; the configured explorer endpoint returned HTTP 503.

## GenLayer-native mechanism

Deterministic code can verify a proxy JSON schema and exact basis-point
movement, but it cannot safely reduce conflicting public outcome narratives to a
single objective verdict. The leader and validators independently fetch the
three frozen HTTPS sources and classify the underlying objective. Validators
recompute material labels and digests, reject malformed or substituted
observations and adversarially challenge positive witnesses before a result can
be `REWARDABLE`. An LLM never selects a recipient or reward amount.

## Verification snapshot

- Offline: 32 passed.
- Native Direct Mode: 16 passed.
- Combined pytest: 48 passed.
- Preflight: 18 assertions passed.
- Mutation checks: 4/4 killed.
- GenVM lint/schema: both contracts passed with linter `0.11.0`, runner
  `v0.2.12`.
- Corrected primary deployment: `0xa400c4def28d7e74820252f6f7be13b7b4467712928202336aad3363b87fe638`,
  finalized `MAJORITY_AGREE`, execution `SUCCESS`.
- Fresh external assessment: `0x68dd7b602f83193be6ed03a388fa7beefb26cbb633c72fd111d191d4e781edae`,
  finalized `MAJORITY_AGREE`, execution `SUCCESS`, terminal `INCONCLUSIVE`,
  both outcomes `UNKNOWN`.

The earlier positive and RewardGate receipts are explicitly historical for the
previous primary. No fresh `REWARDABLE` plus authorized consumer/replay proof
has been established on the corrected primary.

## Limitations and readiness

Three hostnames do not prove independent ownership or truthful reporting.
Public snapshots can be stale, selectively curated or changed after an
assessment. The protocol does not establish real-world identity, action
completion, causality, data completeness, intentional manipulation, payment or
legal liability. RewardGate proves a conditional one-shot permission and does
not custody or transfer GEN. No frontend, backend or application wallet is
included.

**Submission readiness: blocked.** The exact remaining gate is a fresh
finalized `REWARDABLE` assessment on the corrected primary, followed by a newly
bound RewardGate action that succeeds once and rejects replay. The repository
does not claim that outcome without actual finalized evidence.
