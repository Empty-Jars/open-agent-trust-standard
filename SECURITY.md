# Security Policy

This repository is in foundation stage and has no production deployment.

## Reporting

Do not open public issues for vulnerabilities, exposed secrets, private data, identity bypasses, certification/conformance bypasses, unsafe assessment methods, or exploitable agent behavior.

Report security concerns confidentially to [security@emptyjars.net](mailto:security@emptyjars.net). Use a subject such as `Security report: open-agent-trust-standard — brief summary`.

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

## Handling

The confidential address forwards reports to responsible Empty Jars recipients; it does not provide anonymity from everyone on that forwarding path. Maintainers aim to acknowledge a report within three business days, but this is a foundation-stage target rather than a guaranteed response time. If a report concerns a likely recipient or maintainer, send only the minimum conflict notice needed to request reassignment and avoid including details that would be unsafe for that recipient to see. An unconflicted reviewer must establish an alternate safe route before substantive evidence is shared.

Recipients limit disclosure to people needed for triage, safeguarding, remediation, or required escalation; preserve only evidence necessary for an auditable response; and avoid placing sensitive details in public records. Acknowledgement should establish a safe contact route, an initial severity and scope, immediate containment needs, the responsible coordinator, and the next update. Public disclosure, if any, is coordinated around affected versions, remediation, and risk to users.

## Scope

Security review includes source code, dependencies, workflows, smart contracts, identity and delegation, private-project access, AI-agent permissions, financial controls, provenance, and contributor infrastructure.

No contributor may test against systems, wallets, accounts, data, or people without explicit authorization.
