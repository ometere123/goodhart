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

On the new primary 0xc6f159b8A0475D32c39033131D5b4E496581f38a, beneficiary assessment 0x339d9a253852b49287f4e7607d4e6bee17056a001a10f73051f41a1e8ab32731 finalized MAJORITY_AGREE and execution SUCCESS, but returned INCONCLUSIVE with UNKNOWN / UNKNOWN; is_rewardable returned false.

The best fresh positive attempt, programme fixture-rewardable-20261110, finalized assessment 0x08a77973f7c1fabe1e8a1ab2d2f429a7631393bb96507a61ec2a40fd8333d805 as MAJORITY_DISAGREE, leaving the programme pending. A later retry 0x7bc69ae7fe6d188787e806fe0fd17ce7d2dd3e431afd88d755fc5848339408bf finalized consensus but rolled back outside assessment window. No fresh REWARDABLE state or new-primary RewardGate execution is claimed.

## Trust boundary

Digests attest only to observed bounded bytes and their declared URL. They do not prove publisher ownership, source truth, unchanged future content, beneficiary identity, causal impact or payment. An attestation registry was not added because the stable runtime does not provide a trusted authority root that could make publisher authentication enforceable without inventing a guarantee.
