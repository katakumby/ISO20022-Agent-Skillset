---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "setr.016.001.05 participant and direction evidence"
domain: "securities"
message_id: "setr.016.001.05"
message_family: "setr.016"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.016.001.05"
source_ids: ["src-000096", "src-000152"]
message_sets: ["investment-funds"]
role_labels: ["an executing party", "authorised representative", "executing party", "instructing party", "investment manager", "next party", "the instructing party", "transfer agent"]
search_terms: ["an executing party", "authorised representative", "executing party", "instructing party", "investment manager", "next party", "the instructing party", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-authorised-representative", "participant-functionality-src-000096-next-party", "participant-narrative-src-000096-investment-manager", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "56 setr.016.001.05 OrderInstructionStatusReportV05", "file_pages": [4109, 4204]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# setr.016.001.05 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 6 uniquely resolved participant references.

## src-000096 — 56 setr.016.001.05 OrderInstructionStatusReportV05

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); Functionality file pp4109, 4110; publication May 2026.

### Direction and initiation clauses

#### src-000096-setr.016.001.05-p4109-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p4109, scope.

- Sender: **an executing party, for example, a transfer agent**. [an executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).
- Receiver: **the instructing party, for example, an investment manager or its authorised representative**. [the instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md).

> The OrderInstructionStatusReport message is sent by an executing party, for example, a transfer agent, to the instructing party, for example, an investment manager or its authorised representative, to report the status of an order from the time the executing party receives the order until the time the order is executed.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-setr.016.001.05-p4109-c001 — file p4109, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md); [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000096-investment-manager.md); [authorised representative](../../../../../shared/reference/participants/participant-functionality-src-000096-authorised-representative.md); [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).

Literal actions: executing party receives.

Quoted above in src-000096-setr.016.001.05-p4109-c001-d1.

**src-000096-setr.016.001.05-p4109-c002 — file p4109, usage.**

> one or more individual order instructions by using IndividualOrderDetailsReport, or

**src-000096-setr.016.001.05-p4109-c003 — file p4109, usage.**

Mentioned roles: [next party](../../../../../shared/reference/participants/participant-functionality-src-000096-next-party.md).

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> a sent to next party status, or,

**src-000096-setr.016.001.05-p4109-c004 — file p4109, usage.**

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> a received status, or,

**src-000096-setr.016.001.05-p4109-c005 — file p4109, usage.**

Mentioned roles: [next party](../../../../../shared/reference/participants/participant-functionality-src-000096-next-party.md).

> a communication problem with next party status, or, Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05 Investment Funds - Maintenance 2025 - 2026 4109 May 2026

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p4109, usage.**

> The OrderInstructionStatusReport message is used to report on the status of a subscription, redemption or a switch order.

**File p4109, usage.**

> The OrderInstructionStatusReport message may be used to give the status of:

**File p4109, usage.**

> one order message by using OrderDetailsReport or,

**File p4109, usage.**

> one or more switch orders by using SwitchOrderDetailsReport.

**File p4109, usage.**

> If the OrderInstructionStatusReport message is used to report the status of an individual order, then IndividualOrderDetailsReport is used and the order reference of the individual order is quoted in OrderReference.

**File p4109, usage.**

> The message identification of the message in which the individual order was conveyed may also be quoted in RelatedReference but this is not recommended.

**File p4109, usage.**

> If the OrderInstructionStatusReport message is used to report the status of a switch order, then SwitchOrderDetailsReport is used and the order reference of the switch order is quoted in OrderReference.

**File p4109, usage.**

> The message identification of the message in which the switch order was conveyed may also be quoted in RelatedReference but this is not recommended.

**File p4109, usage.**

> If the OrderInstructionStatusReport message is used to report the status of an entire order message, for example, the SubscriptionBulkOrder, or a SubscriptionOrder containing several orders, then OrderDetailsReport is used and the message identification of the order message is quoted in RelatedReference.

**File p4109, usage.**

> All the orders within the message must have the same status.

**File p4109, usage.**

> One of the following statuses can be reported:

**File p4109, usage.**

> an accepted status, or,

**File p4109, usage.**

> an already executed status, or,

**File p4109, usage.**

> a settled status, or,

**File p4110, usage.**

> a confirmation amendment status, or,

**File p4110, usage.**

> a done for the day status, or,

**File p4110, usage.**

> a partially done status, or,

**File p4110, usage.**

> an open status, or,

**File p4110, usage.**

> a cancelled status, or

**File p4110, usage.**

> a conditionally accepted status, or,

**File p4110, usage.**

> a rejected status, or,

**File p4110, usage.**

> a suspended status, or,

**File p4110, usage.**

> a partially settled status, or,

**File p4110, usage.**

> an in-repair status (only for an individual or switch order).

**File p4110, usage.**

> For a switch order, the OrderInstructionStatusReport message provides the status of the whole switch order, that is, it is not possible to accept one leg and to reject the other leg: the entire switch order has to be rejected.

**File p4110, usage.**

> In order to identify the legs within the switch that are causing the problem, the leg is identified in either the RedemptionLegIdentification or SubscriptionLegIdentification elements.

**File p4110, usage.**

> When the OrderInstructionStatusReport is used to give the status of an individual or a switch order, the following can be specified:

**File p4110, usage.**

> repaired conditions (for a switch, this is at the level of a leg),

**File p4110, usage.**

> information related to the order, for example, settlement amount, number of units, expected trade date.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
