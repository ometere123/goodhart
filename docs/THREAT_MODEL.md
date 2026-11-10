# GOODHART threat model

## Assets and roles

- The owner controls registration and assessment but cannot rewrite a frozen
  programme or create a reward after a terminal decision.
- The beneficiary is an immutable typed address and is not automatically a
  consenting human or independent economic party.
- The metric reporter supplies the frozen proxy endpoint.
- Outcome publishers supply public narrative evidence. URL host separation is
  not authenticated publisher identity or measurement independence.
- RewardGate protects one exact downstream action and does not transfer GEN.

## Adversaries and mitigations

- **Metric manipulator:** increases the proxy without improving the objective.
  Proxy movement is necessary but never sufficient; both outcome sources must
  survive independent semantic review.
- **Malicious leader:** fabricates a quote, source digest, number, scope or
  classification. Validators independently fetch all frozen sources, parse the
  proxy, recompute material labels, compare digests and audit positive witnesses.
- **Hostile evidence:** embeds prompt injection, a repeated quote, a changed
  denominator, a different population or distant counterevidence. Evidence is
  hostile data; `_clean_page` accepts a complete bounded body and never slices
  away later text. Exact quotes must occur once, and positive claims receive a
  compatible-reading audit.
- **Redirect/source substitution:** redirects, final-URL changes, permanent
  HTTP failures and source-identity changes fail closed. The GenVM response does
  not expose enough trusted DNS/publisher metadata to prove ownership.
- **Malformed model output:** exact response schemas, enum checks, quote bounds,
  digest widths and cross-field status rules reject malformed or incomplete
  results.
- **Owner/beneficiary rewrite:** programme terms, URLs, fingerprint and
  beneficiary are immutable; owner-only assessment/cancellation and terminal
  receipts prevent post-result changes.
- **Retry griefing:** only the owner can assess; transient errors have one
  bounded retry and unresolved recovery becomes terminal `INCONCLUSIVE`.
- **Replay/misbinding:** RewardGate checks the primary address, programme,
  fingerprint, beneficiary and exact action, and records a one-shot execution.

## Protocol invariants

1. `is_rewardable` implies a matching registered fingerprint, a terminal
   receipt, proxy improvement and two affirmative underlying-objective labels.
2. Oversized, malformed, empty, redirected or unavailable evidence cannot grant
   reward permission.
3. Numeric thresholds and all status transitions are deterministic and outside
   nondeterministic callbacks.
4. Unknown, mixed, stable, unsupported, pending, reverted and stale outcomes
   fail closed.
5. The accepted programme cannot be reopened or silently refreshed.

## Residual risks and assumptions

The owner chooses URLs and can choose controlled or colluding publishers.
Different domains may share an operator. A content digest attests only to the
observed URL/normalized bytes; it does not prove publisher ownership, truth,
causality, hidden populations, data completeness, worker identity or real-world
action completion. The stable runtime does not supply a trusted publisher
authority registry, so GOODHART deliberately does not claim one. A model can
still miss meaning inside an accepted source, and heterogeneous models can
produce disagreement or a conservative `INCONCLUSIVE` result.

The corrected primary was live-tested with an external CERT-EU/Debian source
pair; it finalized `INCONCLUSIVE` with both outcomes `UNKNOWN`. Earlier
positive and consumer receipts belong to the previous deployment and are
retained as historical evidence only. A fresh rewardable proof for the
corrected deployment remains an explicit release blocker.

GOODHART is not a substitute for independent measurement, fraud investigation,
privacy controls, publisher authentication or high-value financial custody.
