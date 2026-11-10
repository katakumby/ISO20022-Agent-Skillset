---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "sese.014.001.09 participant and direction evidence"
domain: "securities"
message_id: "sese.014.001.09"
message_family: "sese.014"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09"
source_ids: ["src-000096", "src-000133"]
message_sets: ["investment-funds"]
role_labels: ["authorised representative", "executing party", "investment manager", "its authorised representative", "transfer agent"]
search_terms: ["authorised representative", "executing party", "investment manager", "its authorised representative", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-authorised-representative", "participant-narrative-src-000096-investment-manager", "participant-src-000095-executing-party", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "file_pages": [1302, 1307]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# sese.014.001.09 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 4 uniquely resolved participant references.

## src-000096 — 37 sese.014.001.09 PortfolioTransferCancellationRequestV09

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); Functionality file pp1302, 1303; publication May 2026.

### Direction and initiation clauses

#### src-000096-sese.014.001.09-p1302-c001-d1

Kind: sender-to-receiver; message applicability: **current-message-source-examples**; src-000096 file p1302, scope.

- Sender: **investment manager or its authorised representative**. [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000096-investment-manager.md); [its authorised representative](../../../../../shared/reference/participants/participant-functionality-src-000096-authorised-representative.md).
- Receiver: **executing party**. [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).

> The PortfolioTransferCancellationRequest message is sent by, for example, an investment manager or its authorised representative, to the executing party, for example, a transfer agent, to request the cancellation of a previously sent PortfolioTransferInstruction message.

Sender names are explicitly introduced as examples in the source; they are not an exhaustive sender definition. Transfer agent is an executing-party example.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-sese.014.001.09-p1302-c001 — file p1302, scope.**

Mentioned roles: [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000096-investment-manager.md); [authorised representative](../../../../../shared/reference/participants/participant-functionality-src-000096-authorised-representative.md); [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000096-sese.014.001.09-p1302-c001-d1.

**src-000096-sese.014.001.09-p1302-c002 — file p1302, usage.**

> The PortfolioTransferCancellationRequest message is used to request the cancellation of a portfolio transfer instruction.

**src-000096-sese.014.001.09-p1302-c003 — file p1302, usage.**

> There is no amendment, but a cancellation and re-instruct policy.

**src-000096-sese.014.001.09-p1302-c004 — file p1302, usage.**

> To request the cancellation of a portfolio transfer instruction, the transfer reference of the portfolio transfer, as specified in the original PortfolioTransferInstruction message, is specified in the transfer reference element.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p1302, usage.**

> The message identification of the original PortfolioTransferInstruction message may also be quoted in PreviousReference but this is not recommended.

**File p1302, usage.**

> The deadline and acceptance of a cancellation request is subject to a service level agreement (SLA).

**File p1302, usage.**

> This cancellation message is a cancellation request.

**File p1302, usage.**

> There is no automatic acceptance of the cancellation.

**File p1302, usage.**

> The rejection or acceptance of a PortfolioTransferCancellationRequest is made using an TransferCancellationStatusReport message.

Functionality role scope was directly reviewed on 2026-11-09. No unstated sender/receiver is manufactured. Header composition, creation/distribution, source wording defects and action-only evidence remain distinct; curated Part1 flow evidence may supply broader context.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
