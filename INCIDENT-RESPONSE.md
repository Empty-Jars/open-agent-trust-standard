# Incident Response and Sensitive-Content Handling

This procedure covers repository vulnerabilities, exposed secrets, privacy incidents, safeguarding or conduct reports, compromised accounts, malicious contributions, release or provenance failures, and sensitive material submitted to public project channels. It does not provide emergency, pastoral, legal, or production-agent response services.

## Safe intake

- **Security vulnerabilities, exposed credentials, or repository compromise:** use [GitHub private vulnerability reporting](https://github.com/Empty-Jars/open-agent-trust-standard/security/advisories/new) or `security@emptyjars.net`.
- **Conduct, retaliation, doxxing, privacy, or safeguarding concerns:** email `empty-jars-manager@agentmail.to` with subject `Confidential conduct report — open-agent-trust-standard`.
- **Conflict with the manager mailbox only:** send only a minimum conflict notice to `security@emptyjars.net` and request an alternate unconflicted route before sharing details.
- **Conflict with a security-address recipient only:** send only a minimum conflict notice to `empty-jars-manager@agentmail.to` and request reassignment.
- **Conflict affecting both routes:** do not contact either route. Privately contact an unconflicted organization owner identified in [MAINTAINERS.md](MAINTAINERS.md), using independently verified contact information and initially disclosing only that a dual-route conflict exists. The owner must appoint qualified external reviewers under [CONFLICTS-AND-APPEALS.md](CONFLICTS-AND-APPEALS.md) without receiving substantive evidence. If no owner is unconflicted or safely reachable, use GitHub Support for GitHub-platform abuse/security, or an appropriate independent safeguarding, legal, regulatory, or emergency authority for matters within its remit; retain the minimum evidence offline until a safe route exists.

The two named routes are operationally separate but do not guarantee organizational independence and are not anonymous. Ordinary email may expose routing metadata and should not carry passwords, private keys, recovery phrases, pastoral records, identifying safeguarding evidence, or active exploit packages. Begin with a minimal description and request a safer exchange method if sensitive evidence is necessary. The absence of a permanent independent ombuds service is a disclosed foundation-stage residual risk; reports must pause rather than circulate through a conflicted route.

For immediate danger, contact appropriate local emergency or safeguarding services. Repository maintainers cannot provide emergency response.

## Severity and ownership

An unconflicted Primary Maintainer appoints an incident coordinator and, for material incidents, a second unconflicted reviewer. If every Primary Maintainer is conflicted, compromised, or unavailable, an unconflicted organization owner who will not decide the merits appoints the coordinator and review team. If every owner is affected, a qualified independent external reviewer reached through the dual-conflict procedure may establish the review team; affected administrators may execute only narrowly specified containment directed by that team. If no independent reviewer is available, protective action may continue but final disposition is deferred or outside advice is documented.

- **Critical:** active credential/key exposure, unauthorized privileged access, credible immediate harm, public safeguarding evidence, malicious release, or exploitation in progress.
- **High:** material vulnerability, significant personal/confidential data exposure, maintainer-account compromise, coercion/retaliation, or integrity loss without confirmed active exploitation.
- **Moderate:** bounded security/privacy weakness, policy bypass, harassment pattern, or provenance concern with limited exposure.
- **Low:** hardening opportunity, minor process failure, or non-sensitive policy violation.

Severity may change as evidence develops. Classification is not a certification or legal conclusion.

## Response lifecycle

1. **Acknowledge and protect:** aim to acknowledge security reports within two business days and conduct/safeguarding reports within three business days. These are targets, not guarantees. Take narrowly scoped immediate protective action where delay could increase harm.
2. **Triage:** identify category, severity, affected people/assets/versions, conflicts, evidence sensitivity, current exposure, coordinator, required specialists, and next-update target.
3. **Contain:** hide or remove sensitive public content, lock discussion if needed, suspend affected automation/access, rotate or revoke exposed credentials, and stop unsafe publication or release activity.
4. **Investigate:** preserve only necessary evidence in restricted storage, establish a timeline, validate provenance, avoid contacting affected or reported people in ways that increase risk, and distinguish verified facts from claims.
5. **Remediate:** correct artifacts and controls, invalidate affected claims, releases, tags, credentials, or attestations when applicable, and test the correction without exposing protected data.
6. **Notify:** contact affected people or maintainers on a need-to-know basis. Coordinate public disclosure for vulnerabilities. Public records use safe identifiers and omit personal, pastoral, safeguarding, exploit, credential, and private-conflict details.
7. **Close and review:** record the disposition, residual risk, appeals route, follow-up owners, retention review date, and any public summary safe to publish. Material incidents receive a post-incident review of control failures and preventive actions.

## Public sensitive-content takedown

When a public issue, pull request, comment, commit, attachment, workflow log, or release exposes sensitive content:

1. Do not quote, download, mirror, or redistribute it unnecessarily.
2. Capture the minimum metadata needed to identify and handle the exposure.
3. Hide, delete, lock, or unpublish through the least-destructive effective platform action.
4. Revoke or rotate affected credentials and invalidate exposed artifacts before treating deletion as containment.
5. If Git history contains the material, an administrator may coordinate a history rewrite and force-update only with explicit incident authorization, a verified clean replacement, notification to affected maintainers, and documented recovery guidance for clones and forks.
6. Contact GitHub Support or affected cache/index operators when platform copies cannot be removed by maintainers.
7. Record a redacted rationale and verification result outside the rewritten public history.

Deletion does not guarantee removal from forks, caches, notifications, or third-party archives. Reporters must not attempt broad cleanup themselves.

## Evidence, privacy, and retention

Case access is need-to-know. The coordinator records the collection purpose, access, storage location, disclosure limits, and a review/deletion date. Keep no more evidence than is necessary for safety, remediation, accountability, appeal, or applicable obligations. Do not place sensitive case files in normal repository history or public project boards.

DCO names/emails and public contribution history normally remain public. Incident handling may remove unnecessarily exposed personal data, but it cannot promise erasure from distributed Git history.

## Emergency changes and review

A qualified administrator may make a temporary emergency restriction or correction before normal review when delay creates material risk. The action must be narrow, logged, reviewed by a second unconflicted maintainer as soon as practical and normally within 72 hours, and either ratified through the ordinary issue/RFC/ADR path or reversed. Emergency handling does not waive licensing, DCO, evidence-minimization, or conflict requirements.

Appeals follow [CONFLICTS-AND-APPEALS.md](CONFLICTS-AND-APPEALS.md). Moderation actions also follow [MODERATION.md](MODERATION.md).
