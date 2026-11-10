---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "sese.006.001.09 participant and direction evidence"
domain: "securities"
message_id: "sese.006.001.09"
message_family: "sese.006"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.006.001.09"
source_ids: ["src-000096", "src-000125"]
message_sets: ["investment-funds"]
role_labels: ["an instructing party", "authorised representative", "executing party", "instructing party", "investment manager", "the executing party", "transfer agent"]
search_terms: ["an instructing party", "authorised representative", "executing party", "instructing party", "investment manager", "the executing party", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-authorised-representative", "participant-narrative-src-000096-investment-manager", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "29 sese.006.001.09 TransferInCancellationRequestV09", "file_pages": [689, 694]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# sese.006.001.09 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 5 uniquely resolved participant references.

## src-000096 — 29 sese.006.001.09 TransferInCancellationRequestV09

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); Functionality file pp689, 690; publication May 2026.

### Direction and initiation clauses

#### src-000096-sese.006.001.09-p689-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p689, scope.

- Sender: **an instructing party, for example, an investment manager or its authorised representative**. [an instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md).
- Receiver: **the executing party, for example, a transfer agent**. [the executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).

> The TransferInCancellationRequest message is sent by an instructing party, for example, an investment manager or its authorised representative, to the executing party, for example, a transfer agent, to request the cancellation of a previously sent transfer in instruction.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-sese.006.001.09-p689-c001 — file p689, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md); [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000096-investment-manager.md); [authorised representative](../../../../../shared/reference/participants/participant-functionality-src-000096-authorised-representative.md); [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md).

Quoted above in src-000096-sese.006.001.09-p689-c001-d1.

**src-000096-sese.006.001.09-p689-c002 — file p689, usage.**

> The TransferInCancellationRequest message is used to request the cancellation of one or more transfer in instructions.

**src-000096-sese.006.001.09-p689-c003 — file p689, usage.**

> There is no amendment, but a cancellation and re-instruct policy.

**src-000096-sese.006.001.09-p689-c004 — file p689, usage.**

> To request the cancellation of one or more transfer in instructions, the transfer reference of the transfer, as specified in the original TransferInInstruction message, is specified in the transfer reference element.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p689, usage.**

> The message identification of the original TransferOutInstruction message may also be quoted in PreviousReference but this is not recommended.

**File p689, usage.**

> The deadline and acceptance of a cancellation request is subject to a service level agreement (SLA).

**File p689, usage.**

> This cancellation message is a cancellation request.

**File p689, usage.**

> There is no automatic acceptance of the cancellation.

**File p689, usage.**

> The rejection or acceptance of a TransferInCancellationRequest is made using a TransferCancellationStatusReport message.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
