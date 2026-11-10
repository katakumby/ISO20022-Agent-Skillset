---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "setr.051.001.03 participant and direction evidence"
domain: "securities"
message_id: "setr.051.001.03"
message_family: "setr.051"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.051.001.03"
source_ids: ["src-000096", "src-000157"]
message_sets: ["investment-funds"]
role_labels: ["an executing party", "authorised representative", "executing party", "instructing party", "investment manager", "the instructing party", "transfer agent"]
search_terms: ["an executing party", "authorised representative", "executing party", "instructing party", "investment manager", "the instructing party", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-authorised-representative", "participant-narrative-src-000096-investment-manager", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "61 setr.051.001.03 RedemptionOrderConfirmationCancellationInstructionV03", "file_pages": [4265, 4270]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# setr.051.001.03 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 5 uniquely resolved participant references.

## src-000096 — 61 setr.051.001.03 RedemptionOrderConfirmationCancellationInstructionV03

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); Functionality file pp4265, 4266; publication May 2026.

### Direction and initiation clauses

#### src-000096-setr.051.001.03-p4265-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p4265, scope.

- Sender: **an executing party, for example, a transfer agent**. [an executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).
- Receiver: **the instructing party, for example, an investment manager or its authorised representative**. [the instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md).

> The RedemptionOrderConfirmationCancellationInstruction message is sent by an executing party, for example, a transfer agent, to the instructing party, for example, an investment manager or its authorised representative, to cancel a previously sent RedemptionOrderConfirmation.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-setr.051.001.03-p4265-c001 — file p4265, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md); [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000096-investment-manager.md); [authorised representative](../../../../../shared/reference/participants/participant-functionality-src-000096-authorised-representative.md).

Quoted above in src-000096-setr.051.001.03-p4265-c001-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p4265, usage.**

> To request the cancellation of one or more individual order executions, the order reference and deal reference of each individual order execution in the original RedemptionOrderConfirmation are specified in the order reference and deal reference elements respectively.

**File p4265, usage.**

> The message identification of the RedemptionOrderConfirmation message in which the individual order execution was conveyed may also be quoted in PreviousReference but this is not recommended.

**File p4265, usage.**

> The AmendmentIndicator is used to specify whether the redemption order confirmation cancellation is to be followed by an amendment An amendment of a redemption order confirmation is carried out by sending a RedemptionOrderConfirmation message in which the AmendmentIndicator contains the value 'true'.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
