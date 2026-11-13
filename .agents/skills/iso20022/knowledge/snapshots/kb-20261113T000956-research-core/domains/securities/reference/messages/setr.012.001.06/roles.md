---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "setr.012.001.06 participant and direction evidence"
domain: "securities"
message_id: "setr.012.001.06"
message_family: "setr.012"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.012.001.06"
source_ids: ["src-000096", "src-000148"]
message_sets: ["investment-funds"]
role_labels: ["an executing party", "authorised representative", "executing party", "instructing party", "investment manager", "the instructing party", "transfer agent"]
search_terms: ["an executing party", "authorised representative", "executing party", "instructing party", "investment manager", "the instructing party", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-authorised-representative", "participant-narrative-src-000096-investment-manager", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "52 setr.012.001.06 SubscriptionOrderConfirmationV06", "file_pages": [3248, 3486]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# setr.012.001.06 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 5 uniquely resolved participant references.

## src-000096 — 52 setr.012.001.06 SubscriptionOrderConfirmationV06

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); Functionality file pp3248, 3249; publication May 2026.

### Direction and initiation clauses

#### src-000096-setr.012.001.06-p3248-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p3248, scope.

- Sender: **an executing party, for example, a transfer agent**. [an executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).
- Receiver: **the instructing party, for example, an investment manager or its authorised representative**. [the instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md).

> The SubscriptionOrderConfirmation message is sent by an executing party, for example, a transfer agent, to the instructing party, for example, an investment manager or its authorised representative, to confirm the details of the execution of a SubscriptionOrder instruction.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-setr.012.001.06-p3248-c001 — file p3248, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md); [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000096-investment-manager.md); [authorised representative](../../../../../shared/reference/participants/participant-functionality-src-000096-authorised-representative.md).

Quoted above in src-000096-setr.012.001.06-p3248-c001-d1.

**src-000096-setr.012.001.06-p3248-c002 — file p3248, usage.**

> When a SubscriptionOrderConfirmation message contains fewer confirmations that originally instructed in the original SubscriptionOrder message, there is no specification indication in the confirmation for this.

**src-000096-setr.012.001.06-p3248-c003 — file p3248, usage.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).

> If the executing party needs to confirm one or more subscription orders for the same financial instrument, then a SubscriptionBulkOrderConfirmation message must be used.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p3248, usage.**

> The SubscriptionOrderConfirmation message is used to confirm the execution of one or more individual orders.

**File p3248, usage.**

> A SubscriptionOrder message containing more than one individual order may be responded to by more than one SubscriptionOrderConfirmation message, as the valuation cycle of the financial instruments in each individual order may be different.

**File p3248, usage.**

> Reconciliation must be based on the references.

**File p3248, usage.**

> Each individual order confirmation specified is identified in DealReference.

**File p3248, usage.**

> The reference of the original individual order is specified in OrderReference.

**File p3248, usage.**

> The message identification of the SubscriptionOrder message in which the individual orders was conveyed may also be quoted in RelatedReference but this is not recommended.

**File p3248, usage.**

> A SubscriptionOrder must in all cases be responded to by a SubscriptionOrderConfirmation message and in no circumstances by a SubscriptionBulkOrderConfirmation message.

**File p3248, usage.**

> When the message is used to convey a confirmation amendment/s, the AmendmentIndicator must be present with the value 'true' or '1'.

**File p3248, usage.**

> When this is the case, the message must only contain a confirmation amendment/s and not contain both a confirmation amendment/s and a 'new' confirmation/s.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
