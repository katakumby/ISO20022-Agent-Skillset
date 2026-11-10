---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "setr.058.001.03 participant and direction evidence"
domain: "securities"
message_id: "setr.058.001.03"
message_family: "setr.058"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.058.001.03"
source_ids: ["src-000096", "src-000161"]
message_sets: ["investment-funds"]
role_labels: ["authorised representative", "executing party", "instructing party", "investment manager", "transfer agent"]
search_terms: ["authorised representative", "executing party", "instructing party", "investment manager", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-authorised-representative", "participant-narrative-src-000096-investment-manager", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "65 setr.058.001.03 RequestForOrderConfirmationStatusReportV03", "file_pages": [4303, 4322]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# setr.058.001.03 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 5 uniquely resolved participant references.

## src-000096 — 65 setr.058.001.03 RequestForOrderConfirmationStatusReportV03

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); Functionality file pp4303; publication May 2026.

### Direction and initiation clauses

#### src-000096-setr.058.001.03-p4303-c001-d1

Kind: sender-to-receiver; message applicability: **current-message-qualified-source-wording**; src-000096 file p4303, scope.

- Sender: **executing party**. [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).
- Receiver: **instructing party**. [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md).

> The RequestForOrderConfirmationStatusReport message is ent by an executing party, for example, a transfer agent, to the instructing party, for example, an investment manager or its authorised representative, to request the status of one or more order confirmations.

Original PDF p4303 visibly reads “is ent by”, missing the s of the expected sending verb. The explicit by/to role expressions are preserved as qualified direction evidence; the source quote is not corrected. Transfer agent/manager/representative are examples.

#### src-000096-setr.058.001.03-p4303-c002-d1

Kind: sender-to-receiver; message applicability: **related-response-message**; src-000096 file p4303, usage.

- Sender: **instructing party**. [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md).
- Receiver: **executing party**. [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).

> When the RequestForOrderConfirmationStatusReport message is used to request the status of several individual order confirmations or one or more order confirmation messages, the executing party may receive several OrderConfirmationStatusReport messages from the instructing party.

Several responses may result from a request covering several confirmations; the direction belongs to responses, not the indexed request.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-setr.058.001.03-p4303-c001 — file p4303, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md); [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000096-investment-manager.md); [authorised representative](../../../../../shared/reference/participants/participant-functionality-src-000096-authorised-representative.md).

Reviewed clause disposition: **source-explicit-role-assertion**. Exact source Functionality was read. The retained role kind distinguishes creation/distribution/action from wire-message direction.

Quoted above in src-000096-setr.058.001.03-p4303-c001-d1.

**src-000096-setr.058.001.03-p4303-c002 — file p4303, usage.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md); [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md).

Literal actions: executing party receive.

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000096-setr.058.001.03-p4303-c002-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p4303, usage.**

> The RequestForOrderConfirmationStatusReport message is used to request the status of either:

**File p4303, usage.**

> one or several individual order confirmations, or,

**File p4303, usage.**

> one or several order confirmation messages.

**File p4303, usage.**

> The response to a RequestForOrderConfirmationStatusReport message is the OrderConfirmationStatusReport message.

**File p4303, usage.**

> When the RequestForOrderConfirmationStatusReport is used to request the status of one or more individual order confirmations, each individual order confirmation is identified with its order reference.

**File p4303, usage.**

> The message identification of the message in which the individual order confirmation was conveyed may also be quoted in PreviousReference.

**File p4303, usage.**

> When the RequestForOrderConfirmationStatusReport is used to request the status of an order confirmation message, then the message identification of the order confirmation message is identified in PreviousReference.

Functionality role scope was directly reviewed on 2026-11-09. No unstated sender/receiver is manufactured. Header composition, creation/distribution, source wording defects and action-only evidence remain distinct; curated Part1 flow evidence may supply broader context.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
