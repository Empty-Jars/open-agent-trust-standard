# ADR 0003: Adopt specification, software, and contribution licenses

- Status: Accepted

## Decision

Use the Community Specification License 1.0 for normative specifications and profiles developed by the Open Agent Trust Standard Working Group. Use Apache License 2.0 for schemas, validators, test suites, examples, adapters, reference implementations, scripts, and general repository documentation.

Require Developer Certificate of Origin 1.1 sign-off on every commit. Contributors retain copyright and grant rights under the applicable license without assigning copyright to Empty Jars.

An accountable individual or organization must sign off agent-generated or agent-assisted work and remains responsible for provenance, rights, confidentiality, review, patent commitments where applicable, and license compatibility.

## Rationale

The Community Specification License was designed for collaborative specifications and includes implementation-oriented necessary-patent terms. Apache-2.0 is appropriate for executable and supporting material and includes an express contributor patent grant. DCO 1.1 records the contributor's right to submit without requiring centralized copyright assignment.

## Consequences

- `LICENSE.md` is the authoritative path-to-license mapping.
- Normative contributions must comply with Community-Spec-1.0 contribution terms.
- Contributions without valid DCO sign-off cannot be merged.
- Incompatible third-party material cannot be accepted.
- The protected default branch requires the `DCO sign-off` status check; contributions without a valid trailer cannot merge.
