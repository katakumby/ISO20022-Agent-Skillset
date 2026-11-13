---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.009.001.08 participant and direction evidence"
domain: "payments"
message_id: "camt.009.001.08"
message_family: "camt.009"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08"
source_ids: ["src-000015", "src-000023"]
message_sets: ["cash-management"]
role_labels: ["member", "transaction administrator"]
search_terms: ["member", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator"]
role_extraction_status: "narrative-only-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "8 camt.009.001.08 GetLimitV08", "file_pages": [364, 390]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.009.001.08 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **narrative-only-needs-review**. 0 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000015 — 8 camt.009.001.08 GetLimitV08

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); Functionality file pp364; publication February 2025.

### Direction and initiation clauses

No complete sender/receiver pattern was resolved here. This does not establish that the message has no participants. Consult the remaining narrative evidence and original.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.009.001.08-p364-c001 — file p364, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator managed; member sets limits; transaction administrator manages limits.

Reviewed clause disposition: **source-explicit-role-action**. Exact source Functionality was read. The retained role kind distinguishes creation/distribution/action from wire-message direction.

> The GetLimit message is used to request information on the details of one or more limits set by the member (or on behalf of the member) and managed by the transaction administrator.

### Unresolved extraction and interpretation

- source-does-not-state-complete-direction: Functionality was directly reviewed; it supplies content, actions, participant or header context without a complete named sender/receiver direction. Broader curated business/flow evidence remains available.

Functionality role scope was directly reviewed on 2026-11-09. No unstated sender/receiver is manufactured. Header composition, creation/distribution, source wording defects and action-only evidence remain distinct; curated Part1 flow evidence may supply broader context.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
