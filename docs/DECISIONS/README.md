# Architecture Decision Records

Architecture Decision Records document significant implementation, repository, and supporting-system decisions that do not require a cross-cutting RFC.

## Use an ADR when

- a choice affects schemas, validators, tests, reference implementations, tooling, or repository architecture;
- alternatives and consequences should remain discoverable;
- the decision is difficult or costly to reverse but does not itself establish normative standard requirements.

Use an RFC instead when [RFC-PROCESS.md](../../RFC-PROCESS.md) requires one. Security-sensitive decisions begin privately under [SECURITY.md](../../SECURITY.md).

## Procedure

1. Discuss the decision in an issue.
2. Copy `0000-template.md` to `NNNN-short-title.md`; a maintainer assigns the next number.
3. Open a DCO-signed pull request and identify the accountable steward and required reviewers.
4. Record status as Proposed, Accepted, Rejected, or Superseded.
5. Preserve accepted and rejected records. A later ADR supersedes rather than silently rewrites a material decision.

ADRs are supporting documentation licensed under Apache-2.0.
