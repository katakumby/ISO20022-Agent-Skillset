---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "sese.003.001.10 participant and direction evidence"
domain: "securities"
message_id: "sese.003.001.10"
message_family: "sese.003"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.003.001.10"
source_ids: ["src-000096", "src-000122"]
message_sets: ["investment-funds"]
role_labels: ["an executing party", "authorised representative", "executing party", "instructing party", "investment manager", "the instructing party", "third party", "transfer agent"]
search_terms: ["an executing party", "authorised representative", "executing party", "instructing party", "investment manager", "the instructing party", "third party", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-authorised-representative", "participant-narrative-src-000096-investment-manager", "participant-narrative-src-000096-third-party", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "26 sese.003.001.10 TransferOutConfirmationV10", "file_pages": [519, 601]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# sese.003.001.10 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 6 uniquely resolved participant references.

## src-000096 — 26 sese.003.001.10 TransferOutConfirmationV10

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); Functionality file pp519, 520; publication May 2026.

### Direction and initiation clauses

#### src-000096-sese.003.001.10-p519-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p519, scope.

- Sender: **an executing party, for example, a transfer agent**. [an executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).
- Receiver: **the instructing party, for example, an investment manager or its authorised representative**. [the instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md).

> The TransferOutConfirmation message is sent by an executing party, for example, a transfer agent, to the instructing party, for example, an investment manager or its authorised representative, to confirm the delivery of a financial instrument, free of payment, on a given date, to a specified party.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-sese.003.001.10-p519-c001 — file p519, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md); [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000096-investment-manager.md); [authorised representative](../../../../../shared/reference/participants/participant-functionality-src-000096-authorised-representative.md).

Quoted above in src-000096-sese.003.001.10-p519-c001-d1.

**src-000096-sese.003.001.10-p519-c002 — file p519, scope.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-narrative-src-000096-third-party.md).

> This message may also be used to confirm the delivery of a financial instrument, free of payment, to another of the instructing parties own accounts or to a third party.

**src-000096-sese.003.001.10-p519-c003 — file p519, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-narrative-src-000096-third-party.md).

> The TransferOutConfirmation message is used to confirm the withdrawal of a financial instrument from the owner's account and its delivery to another own account, or to a third party, has taken place.

**src-000096-sese.003.001.10-p519-c004 — file p519, usage.**

> The reference of the original transfer instruction is specified in TransferReference.

**src-000096-sese.003.001.10-p519-c005 — file p519, usage.**

> The message identification of the TransferOutInstruction message in which the transfer instruction was conveyed may also be quoted in RelatedReference but this is not recommended.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p519, usage.**

> The reference of the transfer confirmation is identified in TransferConfirmationReference.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
