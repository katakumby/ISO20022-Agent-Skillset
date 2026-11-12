---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.070.001.06 participant and direction evidence"
domain: "payments"
message_id: "camt.070.001.06"
message_family: "camt.070"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.070.001.06"
source_ids: ["src-000015", "src-000046"]
message_sets: ["cash-management"]
role_labels: ["a member", "a transaction administrator", "member", "transaction administrator"]
search_terms: ["a member", "a transaction administrator", "member", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "31 camt.070.001.06 ReturnStandingOrderV06", "file_pages": [707, 737]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.070.001.06 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000015 — 31 camt.070.001.06 ReturnStandingOrderV06

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); Functionality file pp707; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.070.001.06-p707-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p707, scope.

- Sender: **a transaction administrator**. [a transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).
- Receiver: **a member**. [a member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> The ReturnStandingOrder message is sent by a transaction administrator to a member.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.070.001.06-p707-c001 — file p707, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Quoted above in src-000015-camt.070.001.06-p707-c001-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p707, scope.**

> It is used to provide information on the details of one or more standing orders, based on specific request and return criteria. in response to a request a on information on standing and predefined orders.

**File p707, usage.**

> The ReturnStandingOrder message lists the standing order based on the following possible return criteria:

**File p707, usage.**

> Generic standing order details,

**File p707, usage.**

> Details of a specific predefined or standing liquidity transfer orders,

**File p707, usage.**

> Details on the set to which the standing order belongs to,

**File p707, usage.**

> List of all predefined and standing liquidity transfer standing orders and/or per set,

**File p707, usage.**

> Total amount of predefined and standing liquidity transfer orders defined in the system.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
