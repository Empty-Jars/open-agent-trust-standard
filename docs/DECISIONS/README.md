# Architecture Decision Records

Architecture Decision Records document significant implementation, repository, governance, or supporting-system decisions. High-impact accepted RFCs require a linked ADR; bounded decisions that do not need an RFC may use an ADR directly.

## Use an ADR for

- repository architecture or tooling that is difficult to reverse;
- security, privacy, or operational control choices;
- adoption of a proposal or RFC;
- a decision whose rationale future contributors will need;
- retrospective review of an emergency action.

Routine edits and temporary work do not need ADRs.

## Required record

Copy `0000-template.md` to the next sequential `NNNN-short-title.md`. Record status, date, owner, linked issue/RFC/PR, participants, approvers, recusals/conflicts, context, decision, alternatives, rationale, consequences, security/privacy/safeguarding/IPR effects, objections/residual risk, implementation/verification, and supersession.

The decision owner keeps the record current while **Proposed**. An **Accepted**, **Rejected**, or **Superseded** ADR is an immutable historical record: do not silently rewrite its substance. A factual or typographical correction must be dated and identified without altering the decision. A changed decision receives a new ADR with reciprocal supersession links.

## Lifecycle

1. Create the ADR as **Proposed** in the decision pull request.
2. Obtain the review and approval required by [GOVERNANCE.md](../../GOVERNANCE.md), [RFC-PROCESS.md](../../RFC-PROCESS.md), and [CONFLICTS-AND-APPEALS.md](../../CONFLICTS-AND-APPEALS.md).
3. Set it to **Accepted** or **Rejected** when the decision is recorded.
4. Mark implementation evidence without rewriting the original rationale.
5. Set it to **Superseded** only through a later accepted ADR.

ADR status does not grant certification, deployment approval, institutional authority, or exception from repository protections.

See [0000-template.md](0000-template.md).
