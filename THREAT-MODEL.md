# Foundation Threat Model

## Status and purpose

This is a non-normative foundation threat model for the standard and its contributor process. It guides requirements and review; it is not a security certification or a substitute for an implementation- and deployment-specific threat model.

## Protected assets

- identities of agents, creators, operators, sponsors, reviewers, and adopters;
- authority, capability, permission, and delegation boundaries;
- manifests, evidence, attestations, conformance results, and revocation state;
- private, personal, pastoral, safeguarding, institutional, and security data;
- credentials, signing keys, wallets, contracts, infrastructure, and audit records;
- integrity and availability of specifications, schemas, validators, tests, releases, and governance records;
- community trust without implying institutional endorsement or universal safety.

## Actors and trust boundaries

Actors include agent creators, operators, accountable sponsors, adopters, affected people, assessors, reviewers, maintainers, infrastructure and model providers, attackers, and the agents themselves. Important boundaries exist between declaration and evidence, identity and authority, capability and permission, sponsor and operator, public and restricted data, test and production, one project or tenant and another, and repository governance and adopter deployment decisions.

Third-party models, tools, plugins, data sources, identity providers, registries, chains, and hosted services are separate trust domains. Their claims must not be inherited without evidence.

## Assumptions

- AI-agent output may be wrong, manipulated, non-deterministic, or hostile.
- Human approval can also fail through error, conflict, coercion, overload, or compromised accounts.
- A valid identity does not prove authority, safety, competence, or current permission.
- Declarations and evidence become stale; runtime behavior and dependencies change.
- Public artifacts may be copied, replayed, selectively quoted, or detached from version and revocation context.
- Higher-risk deployments require controls beyond the core standard.

## Threats and required control direction

### Identity, sponsorship, and representation

Threats include impersonated agents or humans, fabricated sponsors, hidden operators, abandoned sponsorship, unauthorized institutional claims, and one identity controlling supposedly independent reviewers. Controls should bind claims to versioned identities, name accountable parties, disclose relevant relationships, expire or revoke sponsorship, and make representation limits explicit.

### Authority and confused-deputy failures

Threats include capability being mistaken for permission, privilege escalation, cross-project or cross-tenant access, unsafe delegation chains, self-approval, and agents inducing authorized systems or people to act outside scope. Controls should enforce least privilege, purpose and project scope, explicit human checkpoints, separation of duties, delegation depth and expiry, denial by default, and auditable revocation.

### False, incomplete, or stale evidence

Threats include fabricated attestations, cherry-picked tests, unverifiable provenance, hidden exceptions, replayed approvals, version mismatch, and pay-to-trust or universal-score gaming. Controls should separate claims from evidence and deployment approval; bind evidence to issuer, subject, version, profile, time, scope, exceptions, and revocation; and preserve correction and appeal routes.

### Prompt injection and unsafe tool use

Threats include malicious instructions in email, documents, web pages, issue content, tool output, retrieved data, or other agents; data exfiltration; unauthorized actions; and persistence of attacker-controlled instructions. Controls should treat external content as data, isolate untrusted inputs, narrowly scope tools and credentials, require confirmation for consequential actions, filter outputs, and retain safe audit evidence.

### Privacy, confidentiality, and safeguarding

Threats include unnecessary collection, inference, retention, or disclosure; re-identification; cross-context reuse; exposure of pastoral, member, donor, employee, child, health, or institutional data; and unsafe escalation. Controls should minimize data, separate public and restricted fields, define lawful purpose and retention, protect affected people, prevent public incident disclosure, and require qualified human safeguarding review.

### Supply chain and model/runtime drift

Threats include compromised dependencies, actions, models, tools, schemas, adapters, registries, and build systems; mutable references; poisoned updates; and behavior changing after assessment. Controls should use pinned and attributable dependencies, reproducible verification where practical, version binding, provenance, change review, continuous reassessment triggers, rollback, and revocation.

### Repository and contribution pipeline

Threats include malicious or misleading issues and pull requests, prompt injection aimed at human or AI reviewers, contributor impersonation, hidden third-party material, forged DCO trailers, workflow modification, dependency confusion, maintainer-account compromise, review collusion, secret exfiltration through CI, and publishing artifacts that differ from reviewed sources. Controls should keep untrusted workflows read-only, avoid executing contributor code unnecessarily, pin external actions, disable credential persistence, require protected review and valid sign-off, verify provenance and licensing, scan history and proposed changes, separate release authority, and compare published artifacts with approved commits.

### Financial and infrastructure actions

Threats include unauthorized transfers, wallet or key exposure, approval manipulation, contract misuse, destructive infrastructure changes, and misleading off-chain financial claims. Controls should require explicit contract- or infrastructure-scoped permissions, human authorization appropriate to risk, separation of duties, transaction simulation or policy checks, limits, audit trails, and emergency revocation. The standard must not imply that a declaration itself authorizes an action.

### Availability, abuse, and governance capture

Threats include denial of service, spam, moderation abuse, maintainer compromise, hidden conflicts, review collusion, capture by a vendor or institution, retaliation, and suppression of appeals. Controls should distribute stewardship, require conflict disclosure and recusal, preserve protected review, record decisions, provide moderation and appeal paths, and avoid reliance on one provider or scoring authority.

### Incident and revocation failure

Threats include delayed detection, inability to identify affected versions, continued use after compromise, incomplete credential rotation, silent evidence withdrawal, and uncoordinated disclosure. Controls should define incident contacts, versioned impact, containment, notification, revocation propagation, recovery evidence, and post-incident correction without publishing sensitive details prematurely.

## Review expectations

Every normative proposal should identify affected assets, actors, boundaries, abuse cases, mitigations, residual risk, verification evidence, and revocation behavior. Security and safeguarding reviewers should identify who can be harmed, who can authorize the action, who receives confidential reports, how conflicts are reassigned, and what must happen when a sponsor, credential, model, dependency, or attestation is withdrawn. Implementers and adopters must extend this model for their own systems, jurisdictions, people, data, integrations, and deployment risk.

Report vulnerabilities through [SECURITY.md](SECURITY.md). Propose model changes through [RFC-PROCESS.md](RFC-PROCESS.md).
