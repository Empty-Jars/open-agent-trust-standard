# RFC Process

RFCs are recorded proposals for material, cross-cutting, difficult-to-reverse, or normative changes. They make alternatives, risks, evidence, and accountable decisions reviewable.

## When an RFC is required

Use an RFC for:

- new or changed normative requirements, profiles, conformance levels, or compatibility rules;
- identity, authority, permission, privacy, safeguarding, security, revocation, or evidence models;
- specification versioning or breaking schema and validator behavior;
- governance, licensing/IPR, certification, or major interoperability policy;
- decisions that materially bind multiple implementations or adopter groups.

Routine corrections, clearly bounded implementation work, and reversible maintenance may use an issue and pull request. Security-sensitive proposals begin privately under [SECURITY.md](SECURITY.md) and become public only when coordinated disclosure is safe.

## Lifecycle

1. **Discuss:** Open a proposal issue describing the problem, scope, exclusions, evidence, risks, stakeholders, and accountable steward.
2. **Draft:** Copy `docs/RFCS/0000-template.md` to `docs/RFCS/NNNN-short-title.md`. A maintainer assigns the number. Open a DCO-signed pull request linked to the issue.
3. **Review:** The steward records affected groups, specialist reviewers, substantive objections, alternatives, and revisions. Review normally remains open for at least seven calendar days after the draft is ready; an urgent exception requires a recorded rationale and must not bypass required review or licensing terms.
4. **Decision:** The responsible Primary Maintainer records consensus or a reasoned decision after required specialist and CODEOWNERS review. Silence is not consent. Authors and conflicted participants do not approve their own proposal.
5. **Implement:** Acceptance authorizes only the recorded direction. Normative text, schemas, tests, migration material, and release decisions require their own reviewed pull requests.
6. **Maintain:** Set the RFC status to Accepted, Rejected, Withdrawn, or Superseded and link later decisions.

## Decision standard

Foundation-stage decisions seek documented rough consensus: major concerns are answered with evidence or explicitly accepted as residual risk. If consensus is not available, a Primary Maintainer may defer or reject the proposal, or record a narrow reversible decision. There is no pay-to-vote mechanism and contribution volume does not create decision authority.

An accepted RFC does not certify an agent, authorize a deployment, represent an institution, or guarantee implementation funding.

## Licensing

RFC records under `docs/RFCS/` are process and design documentation licensed under Apache-2.0. Any accepted normative specification or profile text must be contributed under `specification/**` or `profiles/**`, where Community-Spec-1.0 applies. Authors must satisfy the DCO and the path-based terms in [LICENSE.md](LICENSE.md).

## Appeals and changes

Use [CONFLICTS-AND-APPEALS.md](CONFLICTS-AND-APPEALS.md) to challenge process, conflicts, or a decision. Material changes to an accepted RFC require a new RFC that supersedes it; minor clarifications may use a pull request if they do not alter the decision.
