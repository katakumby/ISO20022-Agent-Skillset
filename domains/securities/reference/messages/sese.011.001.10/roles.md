---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "sese.011.001.10 participant and direction evidence"
domain: "securities"
message_id: "sese.011.001.10"
message_family: "sese.011"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.011.001.10"
source_ids: ["src-000096", "src-000130"]
message_sets: ["investment-funds"]
role_labels: ["an executing party", "another party in the transfer transaction chain", "any party in the transfer transaction", "authorised representatives", "executing party", "instructing party", "investment manager", "the instructing party", "transfer agent"]
search_terms: ["an executing party", "another party in the transfer transaction chain", "any party in the transfer transaction", "authorised representatives", "executing party", "instructing party", "investment manager", "the instructing party", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-authorised-representative", "participant-functionality-src-000096-transfer-transaction-party", "participant-narrative-src-000096-investment-manager", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "34 sese.011.001.10 TransferInstructionStatusReportV10", "file_pages": [816, 942]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# sese.011.001.10 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 6 uniquely resolved participant references.

## src-000096 — 34 sese.011.001.10 TransferInstructionStatusReportV10

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); Functionality file pp816; publication May 2026.

### Direction and initiation clauses

#### src-000096-sese.011.001.10-p816-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p816, scope.

- Sender: **an executing party, for example, a transfer agent**. [an executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).
- Receiver: **the instructing party, for example, an investment manager or one of its authorised representatives**. [the instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md).

> The TransferInstructionStatusReport message is sent by an executing party, for example, a transfer agent, to the instructing party, for example, an investment manager or one of its authorised representatives to provide the status of a previously received request for holdings information, portfolio transfer or transfer instruction.

#### src-000096-sese.011.001.10-p816-c002-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p816, scope.

- Sender: **any party in the transfer transaction**. [any party in the transfer transaction](../../../../../shared/reference/participants/participant-functionality-src-000096-transfer-transaction-party.md).
- Receiver: **another party in the transfer transaction chain**. [another party in the transfer transaction chain](../../../../../shared/reference/participants/participant-functionality-src-000096-transfer-transaction-party.md).

> The TransferInstructionStatusReport message may also be sent by any party in the transfer transaction to another party in the transfer transaction chain to provide information relevant for the settlement of a transfer transaction.

The source deliberately uses generic contextual roles. No particular institution or named functional role is substituted.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-sese.011.001.10-p816-c001 — file p816, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md); [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000096-investment-manager.md); [authorised representatives](../../../../../shared/reference/participants/participant-functionality-src-000096-authorised-representative.md).

Quoted above in src-000096-sese.011.001.10-p816-c001-d1.

**src-000096-sese.011.001.10-p816-c002 — file p816, scope.**

Mentioned roles: [any party in the transfer transaction](../../../../../shared/reference/participants/participant-functionality-src-000096-transfer-transaction-party.md); [another party in the transfer transaction chain](../../../../../shared/reference/participants/participant-functionality-src-000096-transfer-transaction-party.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000096-sese.011.001.10-p816-c002-d1.

**src-000096-sese.011.001.10-p816-c003 — file p816, usage.**

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> The TransferInstructionStatusReport message is used to provide the status of a previously received request for holdings information, portfolio transfer or transfer instruction, or in response to a RequestForTransferStatus message.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p816, scope.**

> It may also be used to report the status of an event related to the asset being transferred or provide additional information.

**File p816, usage.**

> It may also be used to report the status of an event related to the asset being transferred or provide additional information.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
