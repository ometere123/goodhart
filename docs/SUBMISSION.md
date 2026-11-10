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
- Fresh corrected-primary controlled positive: `0xf20659666a3b89cee1e6bd0076d150e8ab2b4c5c16765f87863630c079c32fb2`,
  finalized `MAJORITY_AGREE`, execution `SUCCESS`, `REWARDABLE`, proxy `20 -> 80`,
  outcomes `IMPROVED` / `IMPROVED`, and `is_rewardable=true`.
- Fresh bound RewardGate: `0x83C553f6Ccd9d3Ea5f474f69F275b781F22F52F0`, deployment
  `0x58f6f86c3e2ba43d66351d006edee34463e39a4eec50f609130680b8f04f3200`.
- Authorized exact action: `0x8c838c497d329247147c52db4c317ccd5e0b262853c5aa5c0bcb48b3dce7c423`;
  replay rollback: `0xb81743cea6d116f0472a036d3136bc364ae7ebfc0c5c512f50ed3f5db3c534d8`.

The fresh positive and consumer receipts are controlled fixture mechanics
evidence. They do not establish publisher identity, independent measurement,
causality, payment or a real beneficiary production outcome.

## Limitations and readiness

Three hostnames do not prove independent ownership or truthful reporting.
Public snapshots can be stale, selectively curated or changed after an
assessment. The protocol does not establish real-world identity, action
completion, causality, data completeness, intentional manipulation, payment or
legal liability. RewardGate proves a conditional one-shot permission and does
not custody or transfer GEN. No frontend, backend or application wallet is
included.

**Submission readiness: corrected-primary mechanics gate complete, with
evidence limitations disclosed.** The fresh finalized `REWARDABLE` assessment,
exact bound consumer action, successful authorization and replay rejection are
now independently recorded. The external XZ case remains fail-closed and the
repository does not claim authenticated publisher independence or real-world
causality from the controlled positive fixture.
