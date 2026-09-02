# RFC Process

RFCs are recorded proposals for material, cross-cutting, difficult-to-reverse, or normative changes. They make alternatives, risks, evidence, objections, and accountable decisions reviewable.

## Change classification

- **Routine and reversible:** corrections or bounded maintenance may use an approved issue and pull request.
- **Substantive implementation:** behavior, schema, validator, test, or interoperability changes require a proposal issue and may require an RFC when cross-cutting or difficult to reverse.
- **High impact:** normative specification, governance, licensing/IPR, conformance, identity, authority, security, privacy, safeguarding, certification, publication, or breaking compatibility changes require an RFC and an ADR recording acceptance.
- **Emergency security:** temporary containment may precede public process under [INCIDENT-RESPONSE.md](INCIDENT-RESPONSE.md), followed by retrospective review and an ADR.

A maintainer records the classification during triage. Disagreement about classification is a governance question and may be appealed.

## Lifecycle

1. **Discuss:** Open a proposal issue describing the problem, sponsor/steward, scope, non-goals, evidence, affected groups, risks, conflicts, dependencies, and desired outcome.
2. **Draft:** Copy `docs/RFCS/0000-template.md` to `docs/RFCS/NNNN-short-title.md`. A maintainer assigns the number. Open a DCO-signed pull request linked to the issue.
3. **Discussion:** Reviewers record alternatives, compatibility/migration, security/privacy/safeguarding, institutional-representation and IPR effects, specialist input, implementation/verification plans, unresolved questions, and substantive objections.
4. **Final Comment Period:** When the draft is decision-ready, a maintainer announces an FCP. It lasts at least fourteen calendar days for high-impact RFCs and seven calendar days for other RFCs. A material revision restarts or extends FCP; the steward records why. Silence is not consent.
5. **Decision:** Required reviewers record approval, rejection, or deferral. Accepted high-impact RFCs require at least two unconflicted human maintainer approvals, including a Primary Maintainer, plus formally appointed specialist review where applicable. The author, sponsor, and recused participants do not count toward the threshold.
6. **ADR:** Acceptance is recorded in a linked ADR with participants, recusals, decision, rationale, alternatives, consequences, residual objections, and implementation conditions.
7. **Implement:** Acceptance authorizes only the recorded direction. Normative text, schemas, tests, migration material, publication, and release decisions require their own reviewed pull requests.
8. **Maintain:** Set status to Implemented when the accepted work is complete. Later material changes use a superseding RFC and ADR.

RFC states are **Draft**, **Discussion**, **Final Comment Period**, **Accepted**, **Rejected**, **Withdrawn**, **Implemented**, and **Superseded**.

## Decision standard and deadlock

Foundation-stage decisions seek documented rough consensus: major concerns are answered with evidence or explicitly accepted as residual risk. Contribution volume, payment, repository ownership, or silence does not create decision authority.

If the approval threshold, required expertise, or unconflicted review cannot be obtained, the RFC is deferred. A Primary Maintainer may narrow a proposal to a reversible experiment, but may not waive high-impact independence, licensing, or safety requirements. Deadlock and any unresolved objection are recorded; appeal follows [CONFLICTS-AND-APPEALS.md](CONFLICTS-AND-APPEALS.md).

An accepted RFC does not certify an agent, authorize a deployment, represent an institution, or guarantee implementation funding.

## Emergency exception

A qualified administrator may authorize a temporary, narrow, reversible security or safeguarding action when normal timing would create material risk. The action must not introduce normative requirements or external authority. A second unconflicted maintainer reviews it as soon as practical and normally within 72 hours. A retrospective issue and ADR record the facts safe to publish, authority used, duration, outcome, and whether the action is ratified, superseded, or reversed.

## Licensing

RFC records under `docs/RFCS/` are process and design documentation licensed under Apache-2.0. Accepted normative specification or profile text must be contributed separately under `specification/**` or `profiles/**`, where Community-Spec-1.0 applies. Authors must satisfy the DCO and path-based terms in [LICENSE.md](LICENSE.md).

## Record integrity

Accepted and rejected RFCs are historical decision records. Do not silently rewrite their substance. Correct factual or typographical errors with an explicit dated correction that does not alter the decision; use a superseding RFC and ADR for changed direction.
