---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "setr.057.001.03 participant and direction evidence"
domain: "securities"
message_id: "setr.057.001.03"
message_family: "setr.057"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.057.001.03"
source_ids: ["src-000096", "src-000160"]
message_sets: ["investment-funds"]
role_labels: ["an instructing party", "authorised representative", "executing party", "instructing party", "intermediary", "investment manager", "next party", "order executing party", "order instructing party", "the executing party", "transfer agent"]
search_terms: ["an instructing party", "authorised representative", "executing party", "instructing party", "intermediary", "investment manager", "next party", "order executing party", "order instructing party", "the executing party", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-authorised-representative", "participant-functionality-src-000096-next-party", "participant-functionality-src-000096-order-executing-party", "participant-functionality-src-000096-order-instructing-party", "participant-narrative-src-000096-investment-manager", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-intermediary", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "64 setr.057.001.03 OrderConfirmationStatusReportV03", "file_pages": [4283, 4302]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# setr.057.001.03 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 3 direction/initiator/exchange clauses; 9 uniquely resolved participant references.

## src-000096 — 64 setr.057.001.03 OrderConfirmationStatusReportV03

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); Functionality file pp4283, 4284; publication May 2026.

### Direction and initiation clauses

#### src-000096-setr.057.001.03-p4283-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p4283, scope.

- Sender: **an instructing party, for example, an investment manager or its authorised representative**. [an instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md).
- Receiver: **the executing party, for example, a transfer agent**. [the executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).

> The OrderConfirmationStatusReport message is sent by an instructing party, for example, an investment manager or its authorised representative, to the executing party, for example, a transfer agent, to report the status of an order confirmation or an order confirmation amendment.

#### src-000096-setr.057.001.03-p4283-c005-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p4283, usage.

- Sender: **order instructing party**. [order instructing party](../../../../../shared/reference/participants/participant-functionality-src-000096-order-instructing-party.md).
- Receiver: **order executing party**. [order executing party](../../../../../shared/reference/participants/participant-functionality-src-000096-order-executing-party.md).

> It is likely that the OrderConfirmationStatusReport is only sent by the order instructing party to the order executing party to reject an order confirmation or to reject an order confirmation amendment, although if an intermediary party is used, the statuses sent to next party and communication problem with next party are also likely be used.

Source says “It is likely” and qualifies rejection use and intermediary statuses. This is not upgraded to a mandatory exclusive rule.

#### src-000096-setr.057.001.03-p4283-c006-d1

Kind: sender-only; message applicability: **related-request-message**; src-000096 file p4283, usage.

- Sender: **order executing party**. [order executing party](../../../../../shared/reference/participants/participant-functionality-src-000096-order-executing-party.md).

> The statuses confirmation accepted and confirmation received would only be used in the event the order executing party sends a RequestForOrderConfirmationStatusReport message and one of the other statuses does not apply.

This request is a condition for using confirmation accepted/received statuses; another status must not apply.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-setr.057.001.03-p4283-c001 — file p4283, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md); [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000096-investment-manager.md); [authorised representative](../../../../../shared/reference/participants/participant-functionality-src-000096-authorised-representative.md); [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md).

Quoted above in src-000096-setr.057.001.03-p4283-c001-d1.

**src-000096-setr.057.001.03-p4283-c002 — file p4283, usage.**

Mentioned roles: [next party](../../../../../shared/reference/participants/participant-functionality-src-000096-next-party.md).

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> sent to next party, or,

**src-000096-setr.057.001.03-p4283-c003 — file p4283, usage.**

Mentioned roles: [next party](../../../../../shared/reference/participants/participant-functionality-src-000096-next-party.md).

> communication problem with next party, or,

**src-000096-setr.057.001.03-p4283-c004 — file p4283, usage.**

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> confirmation received.

**src-000096-setr.057.001.03-p4283-c005 — file p4283, usage.**

Mentioned roles: [order instructing party](../../../../../shared/reference/participants/participant-functionality-src-000096-order-instructing-party.md); [order executing party](../../../../../shared/reference/participants/participant-functionality-src-000096-order-executing-party.md); [intermediary](../../../../../shared/reference/participants/participant-src-000095-intermediary.md); [next party](../../../../../shared/reference/participants/participant-functionality-src-000096-next-party.md); [next party](../../../../../shared/reference/participants/participant-functionality-src-000096-next-party.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000096-setr.057.001.03-p4283-c005-d1.

**src-000096-setr.057.001.03-p4283-c006 — file p4283, usage.**

Mentioned roles: [order executing party](../../../../../shared/reference/participants/participant-functionality-src-000096-order-executing-party.md).

Literal actions: order executing party sends.

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000096-setr.057.001.03-p4283-c006-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p4283, usage.**

> The OrderConfirmationStatusReport message is used to report on the status of one or more individual:

**File p4283, usage.**

> subscription confirmations,

**File p4283, usage.**

> subscription confirmation amendments,

**File p4283, usage.**

> redemption confirmations,

**File p4283, usage.**

> redemption confirmation amendments,

**File p4283, usage.**

> switch order confirmations,

**File p4283, usage.**

> switch order confirmation amendments.

**File p4283, usage.**

> One of the following statuses can be reported:

**File p4283, usage.**

> confirmation rejected, or,

**File p4283, usage.**

> amendment rejected, or,

**File p4283, usage.**

> confirmation accepted, or,

**File p4283, usage.**

> If the status being reported is either confirmation rejected or amendment rejected, then a reason for the rejection must be given.

**File p4283, usage.**

> The individual order confirmation or confirmation amendment for which the status is given is identified with its order reference.

**File p4283, 4284, usage.**

> The message identification of the message in which the individual order Approved by the Securities SEG on 27 January 2026 setr.057.001.03 OrderConfirmationStatusReportV03 Investment Funds - Maintenance 2025 - 2026 4283 May 2026 confirmation or confirmation amendment was conveyed may also be quoted in RelatedReference, but this is not recommended.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
