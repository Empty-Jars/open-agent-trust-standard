# Conflicts of Interest and Appeals

## Material conflicts

A material conflict is an interest or relationship that a reasonable participant could expect to affect independent judgment. Examples include:

- creating, operating, sponsoring, selling, assessing, or competing with an affected agent or service;
- employment, governance, funding, family, personal, contractual, litigation, or close organizational relationships;
- access to non-public information or a direct financial or reputational outcome;
- authorship, moderation involvement, or active dispute that would make a person reviewer and approver of the same matter.

Ordinary technical preferences are not automatically conflicts, but relevant affiliations and incentives should be disclosed.

## Disclosure and recusal

Participants disclose material conflicts as early as practical in the issue, RFC, ADR, pull request, or confidential report. An unconflicted Primary Maintainer records whether recusal, an alternate reviewer, additional review, narrower scope, or another safeguard is required.

A recused person does not review, approve, decide, moderate, hear an appeal, or count toward any threshold. They may provide requested facts or technical input when safe. Agent creators, operators, sponsors, and assessors cannot grant final conformance or deployment approval to their own systems. Repository or organization ownership is not a bypass.

Sensitive details use the routes in [INCIDENT-RESPONSE.md](INCIDENT-RESPONSE.md); the public record may state that a conflict was reviewed without exposing protected information. If too few qualified and unconflicted reviewers remain, pause or defer the decision rather than waive independence.

## Appeals

A contributor or affected participant may appeal:

- a scope, review, RFC, ADR, moderation, access, or governance decision;
- failure to disclose or manage a material conflict;
- a material procedural error, disproportionate response, inconsistent application, or significant new evidence.

Open a `type: decision` issue within fourteen calendar days of the decision when the matter is safe for public handling. Link the decision and identify the requested remedy, basis, conflicts, and publishable facts. For sensitive conduct, security, privacy, safeguarding, retaliation, or maintainer-conflict concerns, use the appropriate confidential route in [INCIDENT-RESPONSE.md](INCIDENT-RESPONSE.md). Late appeals may be accepted when safety, access, delayed discovery, or other reasonable circumstances prevented timely filing.

Disagreement alone does not invalidate a decision.

## Appeal review

A different qualified and unconflicted maintainer acknowledges an appeal within five business days where practical and identifies the review path. A material governance, access, moderation, conformance, maintainer, or security appeal requires at least two unconflicted human reviewers: at least one current maintainer and, when available, a Primary Maintainer; a qualified independent external reviewer may fill the second seat. The original decision participants do not count.

The target disposition is thirty calendar days, but safety, specialist advice, or evidence may require more time; status is updated when safe. If no current maintainer can participate without conflict, an unconflicted organization owner who will not decide the merits appoints two qualified independent external reviewers under confidentiality and conflict safeguards and executes their recorded outcome. If even safe appointment or necessary expertise is unavailable, the appeal remains pending rather than being denied for lack of quorum. Temporary protective restrictions may remain only when lifting them could increase harm, exposure, or repository risk, with reasons and review dates recorded. Independence must not be fabricated.

The outcome records whether the decision is affirmed, modified, remanded, or withdrawn, with reasons, conditions, and any dissent safe to publish. Urgent protective measures may remain in effect. Retaliation for a good-faith disclosure or appeal is prohibited. The appeal outcome is final at repository level unless material new evidence or process failure is later identified.
