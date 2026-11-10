# GOODHART evidence manifest

This manifest separates source-backed observations from protocol guarantees.
GOODHART can freeze URLs, re-fetch bounded bodies, bind normalized bytes to
Keccak-256 digests, and obtain independent GenLayer classifications. It cannot
authenticate that a URL is controlled by the named organization, prove that two
organizations measured the same private population, or establish causality,
identity, payment or legal liability.

## Role model

The intended security-patching programme is:

- **Programme owner:** an incentive operator funding a maintainer or security
  worker to remediate a declared vulnerable package.
- **Worker / beneficiary:** the maintainer whose patching throughput is the
  gameable proxy target.
- **Metric reporter:** the frozen JSON source reporting patch actions. In the
  reproducible test path this is a controlled repository fixture, so it is not
  an independent measurement of a real fleet.
- **Outcome publishers:** CERT-EU and the Debian Security Tracker, separate
  public organizations and services that published bounded reports about
  CVE-2024-3094 and affected/fixed XZ Utils versions.
- **Consumer:** `RewardGate`, which receives only the exact deterministic
  `is_rewardable(program_id, fingerprint)` predicate and precommitted action.

The proxy is “patched packages” or merged remediation work. The underlying
objective is reduction of exposure to compromised XZ Utils versions, not the
number of patches or tickets closed. A worker could improve the proxy while
leaving vulnerable installations, a changed population, or a non-comparable
distribution unresolved.

## External source access checks

These are real, dated public sources—not GOODHART-controlled mirrors. Checks
were performed on 2026-11-10 from the release workstation with HTTPS, no
redirect, UTF-8 decoding and complete normalized bodies below GOODHART's
12,000-character / 48,000-byte cap.

| Publisher | Frozen URL | Published material | Raw SHA-256 | Normalized chars | GOODHART source digest |
|---|---|---|---|---:|---|
| CERT-EU, Cybersecurity Service for EU institutions | `https://cert.europa.eu/publications/security-advisories/2024-032/markdown` | Advisory 2024-032, dated 2024-04-02; identifies compromised XZ versions and recommends an unaffected downgrade | `774644a3b4a4f4703bc7cfc813f168638c3f6ec94703efb5d4cca4c5139769f6` | 4,553 | `cd790e11b3ce7a51cffa3220f25d8d9362f643c2be27f439ada33cbbfa4e836e` |
| Debian Security Tracker | `https://security-tracker.debian.org/tracker/CVE-2024-3094` | CVE record and fixed/not-affected XZ Utils package versions by Debian release | `c7ae75352eba37d5ba9fb782695f6c3ae9f0e318dadf5b9737b296749f6fbfd6` | 5,763 | `ba1c400219aa330f300edf09cc5e05ce9e8df89bfd0a57ecbe23068556747f2d` |

Representative source text includes CERT-EU’s statement that XZ was
compromised starting with version 5.6.0 and that 5.4.6 was understood to be
unaffected. The Debian tracker lists fixed package versions for its releases.
Those facts are relevant to the declared objective, but they do not prove that
the GOODHART beneficiary changed any particular fleet.

## On-chain demonstration status

The repository’s finalized positive cycle uses controlled fixtures because the
protocol’s exact four-field proxy schema requires a source whose `program_id`
is bound to the registered programme. The external XZ pair is retained as an
independently hosted, bounded evidence candidate and adversarial review case;
it is not presented as proof of a real beneficiary’s remediation or as a
publisher-authenticated reward clearance.

Three hostnames are therefore not promoted to “three independent publishers.”
Publisher organization, authority, measurement independence and source
ownership remain human/governance assumptions outside stable GenVM. An
attestor/signature policy was not added because the current contract has no
trusted authority registry or stable-runtime publisher identity primitive that
could make such a policy truthful without changing the protocol’s public model.
