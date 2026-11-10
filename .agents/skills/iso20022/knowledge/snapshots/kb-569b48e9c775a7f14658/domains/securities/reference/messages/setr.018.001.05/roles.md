---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "setr.018.001.05 participant and direction evidence"
domain: "securities"
message_id: "setr.018.001.05"
message_family: "setr.018"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.018.001.05"
source_ids: ["src-000096", "src-000154"]
message_sets: ["investment-funds"]
role_labels: ["an instructing party", "authorised representative", "executing party", "instructing party", "investment manager", "the executing party", "transfer agent"]
search_terms: ["an instructing party", "authorised representative", "executing party", "instructing party", "investment manager", "the executing party", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-authorised-representative", "participant-narrative-src-000096-investment-manager", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "58 setr.018.001.05 RequestForOrderStatusReportV05", "file_pages": [4232, 4252]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# setr.018.001.05 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 3 direction/initiator/exchange clauses; 5 uniquely resolved participant references.

## src-000096 — 58 setr.018.001.05 RequestForOrderStatusReportV05

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); Functionality file pp4232, 4233; publication May 2026.

### Direction and initiation clauses

#### src-000096-setr.018.001.05-p4232-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p4232, scope.

- Sender: **an instructing party, for example, an investment manager or its authorised representative**. [an instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md).
- Receiver: **the executing party, for example, a transfer agent**. [the executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).

> The RequestForOrderStatusReport message is sent by an instructing party, for example, an investment manager or its authorised representative, to the executing party, for example, a transfer agent, to request the status of one or more order instructions or order cancellation requests.

#### src-000096-setr.018.001.05-p4232-c003-d1

Kind: sender-to-receiver; message applicability: **related-response-message**; src-000096 file p4232, usage.

- Sender: **executing party**. [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).
- Receiver: **instructing party**. [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md).

> If the RequestForOrderStatusReport message is used to request the status of several individual order instructions or one or more order instruction messages, then the instructing party may receive several OrderInstructionStatusReport messages from the executing party.

The request for several items may yield several responses. Direction belongs to the named response message, not the indexed request.

#### src-000096-setr.018.001.05-p4232-c004-d1

Kind: sender-to-receiver; message applicability: **related-response-message**; src-000096 file p4232, usage.

- Sender: **executing party**. [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).
- Receiver: **instructing party**. [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md).

> If the RequestForOrderStatusReport message is used to request the status of several individual order cancellation requests or one or more order cancellation messages, then the instructing party may receive several OrderCancellationStatusReport messages from the executing party.

The request for several items may yield several responses. Direction belongs to the named response message, not the indexed request.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-setr.018.001.05-p4232-c001 — file p4232, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md); [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000096-investment-manager.md); [authorised representative](../../../../../shared/reference/participants/participant-functionality-src-000096-authorised-representative.md); [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md).

Quoted above in src-000096-setr.018.001.05-p4232-c001-d1.

**src-000096-setr.018.001.05-p4232-c002 — file p4232, usage.**

> one or several individual order instructions, or,

**src-000096-setr.018.001.05-p4232-c003 — file p4232, usage.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md); [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).

Literal actions: instructing party receive.

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000096-setr.018.001.05-p4232-c003-d1.

**src-000096-setr.018.001.05-p4232-c004 — file p4232, usage.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md); [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).

Literal actions: instructing party receive.

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000096-setr.018.001.05-p4232-c004-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p4232, usage.**

> The RequestForOrderStatusReport message is used to request the status of:

**File p4232, usage.**

> one or several order messages, or

**File p4232, usage.**

> one or several individual order cancellation requests, or,

**File p4232, usage.**

> one or several order cancellation request messages.

**File p4232, usage.**

> The response to a RequestForOrderStatusReport message is the OrderInstructionStatusReport message or OrderCancellationStatusReport message.

**File p4232, usage.**

> When the RequestForOrderStatusReport is used to request the status of one or more individual orders or order cancellations, each individual order is identified with its order reference.

**File p4232, usage.**

> The investment account and/or financial instrument related to the order can also be identified.

**File p4232, usage.**

> The message identification of the message in which the individual order was conveyed may also be quoted in PreviousReference.

**File p4232, usage.**

> When the RequestForOrderStatusReport is used to request the status of an order message or an order cancellations request message, then the message identification of the order or cancellation message is identified in PreviousReference.

**File p4232, usage.**

> The RequestForOrderStatusReport message may not be used to request the status of an investment account, a transfer or the status of a financial instrument.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
