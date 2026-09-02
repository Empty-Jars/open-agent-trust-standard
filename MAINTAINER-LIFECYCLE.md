# Maintainer Lifecycle and Access Governance

This procedure governs repository maintainers, code owners, administrators, and organization-owner access used for this project. Roles are repository-governance responsibilities only; they do not confer certification, ecclesiastical, institutional, employment, or legal authority.

## Eligibility and nomination

A nominee should demonstrate sustained constructive participation, sound judgment, respect for confidentiality and safeguarding, licensing/IPR awareness, ability to review within the proposed scope, and willingness to follow conflict and accountability rules.

A nomination uses a public `type: decision` issue containing:

- the proposed role, scope, term, and permissions;
- evidence of relevant public contributions or experience;
- nominee consent and public attribution preference;
- material conflicts that can safely be disclosed;
- required specialist or institutional authorization, if representation is claimed;
- a transition and review plan.

Private due-diligence or conflict details go through an appropriate confidential route and are summarized publicly only when safe. No one may nominate an AI agent for unsupervised maintainer, moderation, release, access-administration, or final governance authority.

## Appointment

Appointment requires:

1. scope and least-privilege access defined before approval;
2. nominee acceptance of the charter, DCO, Code of Conduct, security, incident, moderation, and conflict procedures;
3. at least two unconflicted human maintainer approvals, including a Primary Maintainer;
4. no self-approval by the nominee or sponsor;
5. an accepted ADR recording role, term, decision participants, recusals, permissions, review date, and succession coverage.

Where required specialist expertise is not formally appointed, the decision pauses or records independent advice; absence of a specialist must not be presented as specialist approval.

## Terms and review

New appointments are interim for no more than twelve months and may be renewed through recorded review. Maintainers listed when this procedure is adopted receive their first role-and-access review within six months and at least annually thereafter.

Review covers participation, conduct, conflicts, security practices, review quality, response capacity, role necessity, least privilege, succession, and whether public responsibilities match actual platform access. Contribution volume alone does not justify renewal or greater authority.

## Activity and voluntary departure

A maintainer may step down at any time. When expected participation lapses, another maintainer should request status after approximately thirty days, review stewardship and access after sixty days, and propose role change or removal after ninety days unless leave or a different plan is recorded. Security risk may require immediate action rather than these intervals.

Departing maintainers identify owned issues and responsibilities for reassignment. Access is revoked or reduced promptly when the role ends; shared credentials are prohibited and must never be transferred as a substitute for proper access grants.

## Suspension and removal

An administrator may temporarily suspend access when there is credible risk involving account compromise, retaliation, confidentiality, safeguarding, serious conduct, or repository integrity. A second unconflicted maintainer reviews the suspension as soon as practical and normally within 72 hours.

Non-emergency removal requires notice of the concern where safe, a reasonable opportunity to respond, documented evidence and conflicts, proportionality, and at least two unconflicted human reviewers. At least one reviewer is a current maintainer and, when available, a Primary Maintainer; a qualified independent external reviewer may fill the second seat. The person concerned does not vote or count toward the threshold. Possible outcomes include restoration, narrower scope, conditions, suspension, non-renewal, or removal.

If no current maintainer can participate without conflict, an unconflicted organization owner who will not decide the merits appoints two qualified independent external reviewers and executes their recorded outcome. If safe appointment is also impossible, protective limits may continue and final removal is deferred rather than decided by conflicted people. Appeals follow [CONFLICTS-AND-APPEALS.md](CONFLICTS-AND-APPEALS.md).

## Access security and periodic review

Privileged maintainers must use two-factor authentication, protect recovery methods, avoid shared accounts, use least-privilege credentials, and report suspected compromise promptly. Organization administrators verify privileged membership, outside collaborators, teams, Apps, repository roles, deploy keys, hooks, secrets metadata, and recovery coverage at least quarterly and after every role change or incident.

The organization-level two-factor-authentication requirement must be enabled before broader promotion and remain enabled. Administrators first verify that enabling it will not unexpectedly remove a member or collaborator. Any exception is time-bounded, documented, and cannot permit privileged repository access.

Access changes are recorded separately from role titles. Working-group membership or CODEOWNERS listing does not automatically grant organization ownership, repository administration, secret access, release authority, or deployment authority.

## Succession and continuity

Maintain at least two active human administrators able to recover repository governance without shared credentials. Primary Maintainers document responsibility transfer, current critical controls, and recovery contacts in restricted operational records. A single person or agent must not be the only holder of organization recovery, repository administration, security-triage, or release authority.

Organization-owner access retained for continuity remains subject to the same review, recusal, incident, and least-privilege requirements. Emergency succession grants only the minimum access needed and receives retrospective review.

## Records and transparency

Public records identify appointments, terms, scopes, decisions, recusals where safe, review dates, and departures. Private records contain only necessary security, personal, safeguarding, or conflict evidence with access and retention controls under [INCIDENT-RESPONSE.md](INCIDENT-RESPONSE.md).
