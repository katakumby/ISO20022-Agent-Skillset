---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "sese.010.001.07 participant and direction evidence"
domain: "securities"
message_id: "sese.010.001.07"
message_family: "sese.010"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.010.001.07"
source_ids: ["src-000096", "src-000129"]
message_sets: ["investment-funds"]
role_labels: ["an executing party", "authorised representatives", "executing party", "instructing party", "investment manager", "next party", "the instructing party", "transfer agent"]
search_terms: ["an executing party", "authorised representatives", "executing party", "instructing party", "investment manager", "next party", "the instructing party", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-authorised-representative", "participant-functionality-src-000096-next-party", "participant-narrative-src-000096-investment-manager", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "33 sese.010.001.07 TransferCancellationStatusReportV07", "file_pages": [809, 815]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# sese.010.001.07 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 6 uniquely resolved participant references.

## src-000096 — 33 sese.010.001.07 TransferCancellationStatusReportV07

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); Functionality file pp809, 810; publication May 2026.

### Direction and initiation clauses

#### src-000096-sese.010.001.07-p809-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p809, scope.

- Sender: **an executing party, for example, a transfer agent**. [an executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).
- Receiver: **the instructing party, for example, an investment manager or one of its authorised representatives**. [the instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md).

> The TransferCancellationStatusReport message is sent by an executing party, for example, a transfer agent, to the instructing party, for example, an investment manager or one of its authorised representatives to provide the status of a previously received transfer cancellation instruction.

#### src-000096-sese.010.001.07-p809-c005-d1

Kind: receiver-only; message applicability: **related-transfer-cancellation-status**; src-000096 file p809, usage.

- Receiver: **next party**. [next party](../../../../../shared/reference/participants/participant-functionality-src-000096-next-party.md).

> the transfer cancellation has been sent to the next party, or,

This is the meaning of a status option, not the receiver of the indexed TransferInstructionStatusReport.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-sese.010.001.07-p809-c001 — file p809, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md); [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000096-investment-manager.md); [authorised representatives](../../../../../shared/reference/participants/participant-functionality-src-000096-authorised-representative.md).

Quoted above in src-000096-sese.010.001.07-p809-c001-d1.

**src-000096-sese.010.001.07-p809-c002 — file p809, usage.**

> The reference of the transfer instruction for which the cancellation status is reported is identified in TransferReference.

**src-000096-sese.010.001.07-p809-c003 — file p809, usage.**

> The message identification of the transfer cancellation request message in which the transfer instruction was conveyed may also be quoted in RelatedReference.

**src-000096-sese.010.001.07-p809-c004 — file p809, usage.**

> The message identification of the transfer instruction request message in which the transfer instruction was conveyed may also be quoted in RelatedReference.

**src-000096-sese.010.001.07-p809-c005 — file p809, usage.**

Mentioned roles: [next party](../../../../../shared/reference/participants/participant-functionality-src-000096-next-party.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000096-sese.010.001.07-p809-c005-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p809, usage.**

> The TransferCancellationStatusReport message is used to report on the status of a transfer in or transfer out cancellation request.

**File p809, usage.**

> One of the following statuses can be reported:

**File p809, usage.**

> the transfer cancellation is accepted, or,

**File p809, usage.**

> the transfer cancellation is complete and the reason for the status,

**File p809, usage.**

> the transfer cancellation pending and the reason for the status,

**File p809, usage.**

> the transfer cancellation is rejected and the reason for the status.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
