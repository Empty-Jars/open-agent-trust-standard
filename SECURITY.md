# Security Policy

This repository is in foundation stage and has no production deployment.

## Reporting

Do not open public issues for vulnerabilities, exposed secrets, private data, identity bypasses, certification/conformance bypasses, unsafe assessment methods, or exploitable agent behavior.

Use [GitHub private vulnerability reporting](https://github.com/Empty-Jars/open-agent-trust-standard/security/advisories/new) or report security concerns to [security@emptyjars.net](mailto:security@emptyjars.net). Use a subject such as `Security report: open-agent-trust-standard — brief summary`.

Include, when safe and applicable:

- affected specification/profile version, schema, test, example, or process;
- impact on agents, operators, assessors, adopters, or affected people;
- reproduction steps or proof of concept;
- relevant evidence with secrets and personal information removed;
- possible certification, attestation, registry, permission, or revocation implications;
- suggested remediation or coordination needs;
- whether the issue is already public or actively exploited;
- a secure contact route for follow-up.

Do not send active credentials, private keys, wallet recovery material, unredacted personal data, safeguarding records, or unnecessary confidential evidence by ordinary email. Revoke or rotate exposed credentials immediately and describe them only by safe identifiers.

Please allow coordinated investigation and remediation before public disclosure. Reporting does not authorize testing against agents, systems, accounts, data, institutions, or people you do not own or have explicit permission to test.

## Handling and alternate routes

The confidential address forwards reports to responsible Empty Jars recipients; it does not provide anonymity from everyone on that forwarding path. Maintainers aim to acknowledge a report within two business days, but this is a foundation-stage target rather than a guaranteed response time. If a report concerns a likely security-address recipient, send only a minimum conflict notice to `empty-jars-manager@agentmail.to` and request an alternate unconflicted route before sharing substantive evidence.

Recipients limit disclosure to people needed for triage, safeguarding, remediation, or required escalation; preserve only evidence necessary for an auditable response; and avoid placing sensitive details in public records. Acknowledgement should establish a safe contact route, an initial severity and scope, immediate containment needs, the responsible coordinator, and the next update. Public disclosure, if any, is coordinated around affected versions, remediation, and risk to users.

The full severity, containment, takedown/history-rewrite, evidence, notification, retention, emergency-change, and post-incident lifecycle is in [INCIDENT-RESPONSE.md](INCIDENT-RESPONSE.md). Conduct and safeguarding reports use the distinct route in [MODERATION.md](MODERATION.md).

## Scope

Security review includes source code, dependencies, workflows, smart contracts, identity and delegation, private-project access, AI-agent permissions, financial controls, provenance, and contributor infrastructure.

No contributor may test against systems, wallets, accounts, data, or people without explicit authorization.
