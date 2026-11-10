# GOODHART threat model

## Adversaries

- **Metric manipulator** increases the reported number of completed work units
  without improving the underlying objective. Mitigation: proxy improvement is
  necessary but never sufficient.
- **Malicious consensus leader** inserts a fabricated favourable outcome,
  changes a quote, changes proxy numbers or substitutes a source snapshot.
  Mitigation: validators independently re-fetch the exact frozen URLs, parse
  numeric fields, repeat semantic outcome classification, compare source hashes,
  challenge positive findings and check the proposed quote in source material.
- **Hostile public web page** contains instructions to the model. Mitigation:
  separate untrusted tagged data and context-escape all embedded text; do not
  follow page instructions; independently re-evaluate.
- **Evidence truncation or normalization attack** places a favourable witness
  before a later contradiction, or uses control/encoding edge cases to make
  leader and validator see different material. Mitigation: `_clean_page`
  rejects oversized, invalid UTF-8 and disallowed-control input rather than
  slicing it; both sides normalize under the same bound, hash the complete
  normalized snapshot, and the validator rechecks the leader witness and
  digest.
- **Malformed semantic response** adds fields, attaches a quote to `UNKNOWN`,
  or claims a positive result with an unsupported witness. Mitigation:
  `_classify`, `_audit_value` and `_valid_observation` enforce exact schemas;
  invalid results become nonrewardable and validator checks are fail closed.
- **Owner/beneficiary** attempts to change criterion, source, baseline, deadline,
  or beneficiary after observing results. Mitigation: immutable programme hash,
  no update method, exact-hash consumer and terminal once-only assessment.
- **Third party** tries to burn recovery attempts during source outages.
  Mitigation: owner-only assessment and bounded two attempts.
- **Replay caller** attempts to consume the same conditional permission twice.
  Mitigation: consumer binds programme fingerprint, exact action hash,
  beneficiary and one-shot execution record.

## Protocol invariants

1. `is_rewardable` implies exact registered fingerprint, existing immutable
   terminal receipt, proxy improvement meeting the threshold, and two
   affirmative underlying-objective assessments.
2. A quote is at least twelve characters and occurs exactly once in a complete,
   bounded, normalized source. Oversized or malformed evidence is rejected,
   never truncated. The source digest is tied to its URL.
3. No deterministic economic or programme state is modified in a nondet block.
4. An observation without affirmative, sufficiently grounded evidence cannot
   set `REWARDABLE`.
5. Unavailable/malformed proxy sources and ambiguous objective evidence fail
   closed; transient failures get at most one additional owner-only attempt.
6. The accepted programme definition cannot be silently rewritten, refreshed
   after the fact, or reopened after a terminal status.

## Residual risks

The owner chooses publisher URLs and the publisher controls what it publishes.
Different domains may share one underlying operator. Website redirects/DNS
resolution may not be independently authenticated by the GenVM web response.
Web observations do not establish ground truth, hidden populations, data
completeness, causal attribution, service identity, or motivation to game a
metric. The bounded complete-source rule rejects material pages that exceed
the cap, but a model can still miss a contradiction within an accepted source,
and heterogeneous model outputs can prevent consensus. No encryption/privacy
guarantee exists for public source content. The contract must not process
private customer records.

Do not use this release as a substitute for verified independent outcome
measurement, fraud investigation or high-value financial custody safeguards.
