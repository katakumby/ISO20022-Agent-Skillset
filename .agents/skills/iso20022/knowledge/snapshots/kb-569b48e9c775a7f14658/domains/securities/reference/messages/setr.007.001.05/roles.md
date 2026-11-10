---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "setr.007.001.05 participant and direction evidence"
domain: "securities"
message_id: "setr.007.001.05"
message_family: "setr.007"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.007.001.05"
source_ids: ["src-000096", "src-000143"]
message_sets: ["investment-funds"]
role_labels: ["account owners", "an instructing party", "authorised representative", "executing party", "instructing party", "investment manager", "the executing party", "transfer agent"]
search_terms: ["account owners", "an instructing party", "authorised representative", "executing party", "instructing party", "investment manager", "the executing party", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-authorised-representative", "participant-narrative-src-000096-account-owner", "participant-narrative-src-000096-investment-manager", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "47 setr.007.001.05 SubscriptionBulkOrderV05", "file_pages": [2523, 2760]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# setr.007.001.05 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 6 uniquely resolved participant references.

## src-000096 — 47 setr.007.001.05 SubscriptionBulkOrderV05

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); Functionality file pp2523; publication May 2026.

### Direction and initiation clauses

#### src-000096-setr.007.001.05-p2523-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p2523, scope.

- Sender: **an instructing party, for example, an investment manager or its authorised representative**. [an instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md).
- Receiver: **the executing party, for example, a transfer agent**. [the executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).

> The SubscriptionBulkOrder message is sent by an instructing party, for example, an investment manager or its authorised representative, to the executing party, for example, a transfer agent, to instruct a subscription to a financial instrument for two or more accounts.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-setr.007.001.05-p2523-c001 — file p2523, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md); [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000096-investment-manager.md); [authorised representative](../../../../../shared/reference/participants/participant-functionality-src-000096-authorised-representative.md); [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md).

Quoted above in src-000096-setr.007.001.05-p2523-c001-d1.

**src-000096-setr.007.001.05-p2523-c002 — file p2523, usage.**

Mentioned roles: [account owners](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md).

> The individual orders come from different instructing parties, that is, account owners, but are for the same financial instrument.

**src-000096-setr.007.001.05-p2523-c003 — file p2523, usage.**

> This message will typically be used by a party collecting orders and bulking these individual orders into one bulk order before sending it to another party.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p2523, usage.**

> The SubscriptionBulkOrder message is used to bulk several individual orders into one bulk order.

**File p2523, usage.**

> For a single subscription order, the SubscriptionOrder message, not the SubscriptionBulkOrder message, must be used.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
