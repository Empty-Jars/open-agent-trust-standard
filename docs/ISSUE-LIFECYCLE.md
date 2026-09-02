# Issue Lifecycle and Review Guidance

## Lifecycle

1. **Submit:** Use the proposal template and provide a bounded problem, scope, exclusions, acceptance criteria, evidence, risk implications, and AI-agent suitability.
2. **Triage:** A maintainer checks duplication, repository scope, sensitive content, applicable license, dependencies, and required expertise. `status: needs-triage` remains until this is complete.
3. **Steward:** A named maintainer or working-group steward is recorded in the issue body or comment. Stewardship coordinates the issue; it does not grant unilateral approval.
4. **Ready:** The steward confirms deliverables, non-goals, dependencies, acceptance evidence, human checkpoints, and whether an RFC or ADR is required. Only then should substantial implementation begin.
5. **In progress:** A contributor comments before starting and links a draft pull request. Parallel work must be coordinated openly.
6. **Review:** Reviewers assess scope, evidence, licensing, security/privacy/safeguarding, interoperability, authority, documentation, and migration effects. Authors resolve or explicitly record substantive comments.
7. **Decision:** Close as completed, declined, duplicate, superseded, or blocked, with a concise reason and links to resulting artifacts.

## Bounded starter issue standard

A `contributors-welcome` issue should include:

- one primary deliverable that can be reviewed independently;
- explicit non-goals;
- expected artifact paths or output format;
- acceptance criteria and verification evidence;
- dependencies and relevant prior decisions;
- a named interim steward;
- AI-agent suitability and required human review;
- warnings against posting confidential or personal data.

An issue is not a promise of assignment, acceptance, compensation, conformance, or authority.

## Review expectations

Review the change, not the contributor. Distinguish blocking requirements from suggestions. Cite evidence or project policy for material objections. Do not approve work you authored, generated, control through an undisclosed relationship, or are otherwise materially conflicted about.

AI-assisted review may summarize or identify possible defects, but an accountable human reviewer remains responsible for approval. Security, safeguarding, legal/IPR, institutional-representation, conformance, and other high-impact decisions require the qualified human checkpoints identified by governance.

## Inactivity and closure

Maintainers may close an issue that is out of scope, unsafe for public handling, superseded, or inactive after a status request and normally at least thirty days without a response. Closure does not prevent a later, better-scoped proposal. Security-sensitive material may be removed or transferred to a private process immediately.

Response targets are documented in [SUPPORT.md](../SUPPORT.md). Decision appeals follow [CONFLICTS-AND-APPEALS.md](../CONFLICTS-AND-APPEALS.md).
