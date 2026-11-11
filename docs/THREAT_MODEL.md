# GOODHART threat model

## Roles and assets

- Owner: registers the incentive terms and may assess. The owner is not the beneficiary and cannot impersonate that address.
- Beneficiary: a typed address that must explicitly accept the exact fingerprint before the assessment window. This authenticates a protocol actor, not a human identity or independent economic interest.
- Metric reporter: supplies the frozen proxy JSON endpoint.
- Outcome publishers: supply public narrative evidence. Host separation is not authenticated publisher identity or measurement independence.
- RewardGate: checks the exact primary view and records one action; it does not transfer GEN.

## Threats and mitigations

- Owner withdrawal or assessment veto: beneficiary acceptance is required; accepted programmes cannot be cancelled by the owner, and either owner or beneficiary can initiate assessment.
- Self-beneficiary and consent collapse: registration rejects an owner address
  equal to the beneficiary, so the owner cannot satisfy the distinct-party
  consent model by accepting its own programme.
- Unauthorized acceptance or substitution: the actual sender must equal the typed beneficiary and the supplied fingerprint must equal the frozen value. Duplicate and late acceptance revert.
- Metric gaming: proxy movement is necessary but never sufficient; both outcome sources must survive independent semantic review.
- Malicious leader: validators independently fetch, parse, classify, compare digests and audit positive witnesses. Leader excerpts do not become authoritative evidence.
- Hostile evidence: prompt injection, repeated quotes, changed denominators, different populations and distant counterevidence are treated as data. The complete bounded source is retained; it is never truncated.
- Redirect/source substitution: redirects, final-URL changes, permanent HTTP failures, empty bodies and source identity failures fail closed.
- Malformed model output: exact schemas, enum checks, quote bounds, digest widths and cross-field rules reject incomplete results.
- Retry griefing: only the owner or accepted beneficiary can assess; retries are bounded and unresolved recovery cannot grant clearance.
- Replay/misbinding: RewardGate checks primary address, programme, fingerprint,
  and the beneficiary read back from that exact Goodhart programme—not only
  the constructor beneficiary—then checks the caller and exact action before
  recording a one-shot execution.

## Invariants

1. is_rewardable implies a matching registered fingerprint, terminal receipt, proxy improvement and two affirmative underlying-objective labels.
2. Oversized, malformed, empty, redirected or unavailable evidence cannot grant reward permission.
3. Numeric thresholds and state transitions are deterministic and outside nondeterministic callbacks.
4. Unknown, mixed, stable, pending, reverted, stale and ambiguous outcomes fail closed.
5. Acceptance and terminal receipts are historical facts; they cannot be overwritten by owner mutation.

## Residual risks

The owner still chooses URLs and can propose controlled or colluding publishers. The beneficiary can refuse an offer but cannot prove publisher independence through acceptance alone. Different domains may share an operator. A content digest attests only to observed bytes; it does not prove publisher ownership, truth, causality, hidden populations, data completeness, worker identity or action completion. The stable runtime has no trusted publisher-authority registry. Models can miss meaning or disagree conservatively.

No critical or high-severity contract bypass was identified in the local audit. Release evidence remains incomplete because a fresh finalized REWARDABLE result and new-primary RewardGate execution were not obtained; this is an evidence/release blocker, not a reason to weaken fail-closed rules.
