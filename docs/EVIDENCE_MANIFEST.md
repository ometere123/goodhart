# GOODHART evidence manifest

This manifest separates protocol guarantees from public-source observations. GOODHART freezes URLs, re-fetches bounded bodies, binds normalized bytes to Keccak-256 digests and obtains independent GenLayer classifications. It cannot authenticate that a URL is controlled by a named organization, prove that two organizations measured the same private population, or establish causality, identity, payment or legal liability.

## Role model

The intended application is a security-maintenance incentive:

- The programme owner offers a reward for remediation work.
- The worker/beneficiary accepts the complete frozen programme and may initiate assessment after the window opens.
- The metric reporter supplies the exact proxy JSON.
- Two outcome publishers should report the underlying objective, but GOODHART cannot authenticate their ownership or independence from URLs alone.
- RewardGate receives only the exact deterministic predicate.

The proxy may be tickets closed or patches merged. The underlying objective is reduced unresolved defects and repeat support failures. A proxy increase alone is therefore insufficient.

## External evidence candidate

An earlier manifest used CERT-EU and the Debian Security Tracker for the XZ Utils incident:

- CERT-EU: https://cert.europa.eu/publications/security-advisories/2024-032/markdown
- Debian Security Tracker: https://security-tracker.debian.org/tracker/CVE-2024-3094

These are distinct named public organizations and relevant public reports, but they do not prove that the beneficiary changed a particular fleet. On the previous corrected primary, the assessment finalized successfully with INCONCLUSIVE and both outcome labels UNKNOWN. That is a historical fail-closed control, not a reward proof for the new primary.

## Controlled fixture evidence

The repository contains bounded fixtures under fixtures/live/ with explicit same-period, same-population text. They are useful for deterministic mechanics and adversarial tests, but are controlled by the repository owner and are not independent real-world measurements. CDN hostnames and raw GitHub URLs are not promoted to independent publishers.

## Current live status

The corrected primary is
0xbea069743269137772E42873aB0D2dE3E9EDC411, deployed from the binding-fix
source. The control programme `binding-control-20261111` has distinct owner and
beneficiary addresses, but its finalized readback is `accepted=0`, `PENDING`,
so it has no reward permission. The current bound RewardGate is
0x46c240DCAA5bDD440f0C41a3499a4096471e2F8B.

Its correct-action call
0x978d3ada3f03f9dbfe758d6a8166128f5a0c9e67ca32c82ac2d17669e8dbc0de rolled
back at the primary predicate (`underlying objective not certified`). A
substituted action rolled back in
0x86176c54f009f00d052f766324d2239fc34c5f449bd36d8371765771a1ea1bee, and an
unauthorized caller rolled back in
0xd14b8e4be53e2a6fc50874fea2a1e32f676792071a41949fd99e14b9d4443cb8.
`was_executed` remained false. These are current-source fail-closed proofs;
they are not a successful reward execution.

The earlier assessment
0x339d9a253852b49287f4e7607d4e6bee17056a001a10f73051f41a1e8ab32731 belongs to
the superseded primary 0xc6f159b8A0475D32c39033131D5b4E496581f38a. It finalized
MAJORITY_AGREE and execution SUCCESS but returned INCONCLUSIVE with UNKNOWN /
UNKNOWN; is_rewardable returned false.

The best earlier positive attempt, programme fixture-rewardable-20261110, finalized assessment 0x08a77973f7c1fabe1e8a1ab2d2f429a7631393bb96507a61ec2a40fd8333d805 as MAJORITY_DISAGREE, leaving the superseded programme pending. A later retry 0x7bc69ae7fe6d188787e806fe0fd17ce7d2dd3e431afd88d755fc5848339408bf finalized consensus but rolled back outside the assessment window. No current-primary REWARDABLE state or successful current-primary RewardGate action is claimed.

## Trust boundary

Digests attest only to observed bounded bytes and their declared URL. They do not prove publisher ownership, source truth, unchanged future content, beneficiary identity, causal impact or payment. An attestation registry was not added because the stable runtime does not provide a trusted authority root that could make publisher authentication enforceable without inventing a guarantee.
