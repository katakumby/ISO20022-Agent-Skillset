---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "setr.009.001.05 participant and direction evidence"
domain: "securities"
message_id: "setr.009.001.05"
message_family: "setr.009"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.009.001.05"
source_ids: ["src-000096", "src-000145"]
message_sets: ["investment-funds"]
role_labels: ["an executing party", "authorised representative", "executing party", "instructing party", "investment manager", "the instructing party", "transfer agent"]
search_terms: ["an executing party", "authorised representative", "executing party", "instructing party", "investment manager", "the instructing party", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-authorised-representative", "participant-narrative-src-000096-investment-manager", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "49 setr.009.001.05 SubscriptionBulkOrderConfirmationV05", "file_pages": [2766, 3000]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# setr.009.001.05 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 5 uniquely resolved participant references.

## src-000096 — 49 setr.009.001.05 SubscriptionBulkOrderConfirmationV05

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); Functionality file pp2766, 2767; publication May 2026.

### Direction and initiation clauses

#### src-000096-setr.009.001.05-p2766-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p2766, scope.

- Sender: **an executing party, for example, a transfer agent**. [an executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).
- Receiver: **the instructing party, for example, an investment manager or its authorised representative**. [the instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md).

> The SubscriptionBulkOrderConfirmation message is sent by an executing party, for example, a transfer agent, to the instructing party, for example, an investment manager or its authorised representative, to confirm the details of the execution of a SubscriptionBulkOrder instruction.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-setr.009.001.05-p2766-c001 — file p2766, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md); [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000096-investment-manager.md); [authorised representative](../../../../../shared/reference/participants/participant-functionality-src-000096-authorised-representative.md).

Quoted above in src-000096-setr.009.001.05-p2766-c001-d1.

**src-000096-setr.009.001.05-p2766-c002 — file p2766, usage.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).

> If the executing party needs to confirm a SubscriptionOrder instruction, then the SubscriptionOrderConfirmation must be used.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p2766, usage.**

> The SubscriptionBulkOrderConfirmation message is used to confirm the execution of all individual orders.

**File p2766, usage.**

> There is usually one bulk confirmation message for one bulk order message.

**File p2766, usage.**

> Each individual order confirmation specified is identified in DealReference.

**File p2766, usage.**

> The reference of the original individual order is specified in OrderReference.

**File p2766, usage.**

> The message identification of the SubscriptionBulkOrder message in which the individual order was conveyed may also be quoted in RelatedReference.

**File p2766, usage.**

> A SubscriptionBulkOrder must in all cases be responded to by a SubscriptionBulkOrderConfirmation and in no circumstances by a SubscriptionOrderConfirmation.

**File p2766, usage.**

> When the message is used to convey a confirmation amendment/s, the AmendmentIndicator must be present with the value 'true' or '1'.

**File p2766, usage.**

> When this is the case, the message must only contain a confirmation amendment/s and not contain both a confirmation amendment/s and a 'new' confirmation/s.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
