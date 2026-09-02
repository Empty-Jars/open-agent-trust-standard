# Issue Lifecycle and Review Guidance

## Lifecycle and labels

1. **Submit:** Use the proposal or general-report template. Provide a bounded problem, scope, exclusions, acceptance criteria or expected result, evidence, risk implications, and AI-agent involvement. New work uses `status: needs-triage`.
2. **Triage:** A maintainer checks duplication, repository scope, sensitive content, applicable license, change class, dependencies, conflicts, and required expertise. Use `status: needs-information` when the reporter must clarify; use `status: blocked` for a known prerequisite.
3. **Accept or decline:** `status: accepted` means the problem is in scope and worth stewarding; it does not promise assignment, merge, payment, conformance, or authority. Declined work is closed with a reason.
4. **Steward:** A named maintainer or working-group steward records scope, owner/steward, acceptance criteria, change class, required RFC/ADR path, and reviewers. Stewardship does not grant unilateral approval.
5. **Ready:** `status: ready` means the issue has independently reviewable deliverables, non-goals, dependencies, verification evidence, human checkpoints, and a confirmed review path.
6. **In progress:** A contributor comments before starting, is assigned or acknowledged by the steward, and links a draft pull request. Use `status: in-progress`; parallel work is coordinated openly.
7. **Review:** Use `status: needs-review` when a linked contribution is ready. Reviewers assess scope, evidence, licensing, security/privacy/safeguarding, interoperability, authority, documentation, compatibility/migration, conflicts, and unresolved objections.
8. **Decision:** Close as completed, declined, duplicate, invalid, superseded, or no longer planned, with a concise reason and links. A blocked issue stays open unless the dependency has no credible path.

Only maintainers assign or confirm stewardship. Assignment permits work within the issue; it is not approval of the eventual change.

## Bounded contributor issue standard

A `contributors-welcome` issue should include:

- one primary deliverable that can be reviewed independently;
- explicit non-goals;
- expected artifact paths or output format;
- acceptance criteria and verification evidence;
- dependencies and relevant prior decisions;
- a named interim steward and required reviewers;
- change class and RFC/ADR applicability;
- AI-agent suitability and required human review;
- warnings against posting confidential or personal data.

## Review expectations

Review the change, not the contributor. Distinguish blocking requirements from suggestions and cite evidence or policy for material objections. Do not approve work you authored, generated, control through an undisclosed relationship, or are otherwise materially conflicted about.

Pull requests identify their issue/RFC/ADR, normative effect, compatibility/migration impact, conflicts and recusals, required reviewers, unresolved objections, security/privacy/safeguarding/IPR review, verification, and AI assistance. Automated review may summarize or identify defects, but accountable humans make approvals and high-impact decisions.

GitHub branch protection requires pull requests, CODEOWNERS approval, successful `Foundation validation` and `DCO sign-off`, current-head approval, resolved conversations, and linear history. High-impact approval thresholds in [RFC-PROCESS.md](../RFC-PROCESS.md) and [MAINTAINER-LIFECYCLE.md](../MAINTAINER-LIFECYCLE.md) are additional procedural requirements; the current platform rule does not technically distinguish change classes.

## Inactivity and reopening

After approximately thirty days without needed activity, a maintainer may request status and allow at least thirty further days for response before closing without prejudice. Accepted RFCs, active appeals, security/conduct/safeguarding matters, governance records, and issues marked `status: blocked` are exempt from automatic inactivity closure.

A contributor may request reopening with new evidence, resolved dependencies, or a concrete next step. Security-sensitive content may be removed or transferred immediately under [INCIDENT-RESPONSE.md](../INCIDENT-RESPONSE.md).

Response targets are in [SUPPORT.md](../SUPPORT.md); appeals follow [CONFLICTS-AND-APPEALS.md](../CONFLICTS-AND-APPEALS.md).
