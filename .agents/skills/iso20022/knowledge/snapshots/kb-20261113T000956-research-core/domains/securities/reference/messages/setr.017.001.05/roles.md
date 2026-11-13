---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "setr.017.001.05 participant and direction evidence"
domain: "securities"
message_id: "setr.017.001.05"
message_family: "setr.017"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.017.001.05"
source_ids: ["src-000096", "src-000153"]
message_sets: ["investment-funds"]
role_labels: ["an executing party", "authorised representative", "executing party", "instructing party", "investment manager", "the instructing party", "transfer agent"]
search_terms: ["an executing party", "authorised representative", "executing party", "instructing party", "investment manager", "the instructing party", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-authorised-representative", "participant-narrative-src-000096-investment-manager", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "57 setr.017.001.05 OrderCancellationStatusReportV05", "file_pages": [4205, 4231]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# setr.017.001.05 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 5 uniquely resolved participant references.

## src-000096 — 57 setr.017.001.05 OrderCancellationStatusReportV05

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); Functionality file pp4205, 4206; publication May 2026.

### Direction and initiation clauses

#### src-000096-setr.017.001.05-p4205-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p4205, scope.

- Sender: **an executing party, for example, a transfer agent**. [an executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).
- Receiver: **the instructing party, for example, an investment manager or its authorised representative**. [the instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md).

> The OrderCancellationStatusReport message is sent by an executing party, for example, a transfer agent, to the instructing party, for example, an investment manager or its authorised representative, to report the status of an order cancellation request that was previously received.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-setr.017.001.05-p4205-c001 — file p4205, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md); [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000096-investment-manager.md); [authorised representative](../../../../../shared/reference/participants/participant-functionality-src-000096-authorised-representative.md).

Quoted above in src-000096-setr.017.001.05-p4205-c001-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p4205, usage.**

> The OrderCancellationStatusReport message is used to provide the status of:

**File p4205, usage.**

> one or more individual order cancellation requests by using IndividualCancellationStatusReport, or,

**File p4205, usage.**

> an order cancellation request message by using CancellationStatusReport.

**File p4205, usage.**

> If the OrderCancellationStatusReport message is used to report the status of an individual order cancellation request, then the repetitive IndividualCancellationStatusReport sequence is used and the order reference of the individual order is quoted in OrderReference.

**File p4205, usage.**

> The message identification of the message in which the individual order was conveyed may also be quoted in RelatedReference but this is not recommended.

**File p4205, usage.**

> If the OrderCancellationStatusReport message is used to report the status of an entire order cancellation request message, for example, the SubscriptionBulkOrderCancellationRequest, or a SubscriptionOrderCancellationRequest containing several orders, then the CancellationStatusReport sequence is used.

**File p4205, usage.**

> The message identification of the order cancellation request message may also be quoted in RelatedReference but this is not recommended.

**File p4205, usage.**

> All the order cancellation requests within the message must have the same status.

**File p4205, usage.**

> One of the following statuses can be reported:

**File p4205, usage.**

> the order cancellation is pending, or,

**File p4205, usage.**

> the order cancellation request is rejected, or,

**File p4205, usage.**

> the order is cancelled.

**File p4205, usage.**

> When the cancellation is rejected, the reason for the rejection must be specified.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
