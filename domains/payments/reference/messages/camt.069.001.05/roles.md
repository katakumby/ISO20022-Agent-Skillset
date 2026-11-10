---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.069.001.05 participant and direction evidence"
domain: "payments"
message_id: "camt.069.001.05"
message_family: "camt.069"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05"
source_ids: ["src-000015", "src-000045"]
message_sets: ["cash-management"]
role_labels: ["a member", "account owner", "member", "the transaction administrator", "transaction administrator"]
search_terms: ["a member", "account owner", "member", "the transaction administrator", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-account-owner", "participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "30 camt.069.001.05 GetStandingOrderV05", "file_pages": [686, 706]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.069.001.05 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 3 uniquely resolved participant references.

## src-000015 — 30 camt.069.001.05 GetStandingOrderV05

[src-000015](../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf); Functionality file pp686; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.069.001.05-p686-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p686, scope.

- Sender: **a member**. [a member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).
- Receiver: **the transaction administrator**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The GetStandingOrder message is sent by a member to the transaction administrator.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.069.001.05-p686-c001 — file p686, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Quoted above in src-000015-camt.069.001.05-p686-c001-d1.

**src-000015-camt.069.001.05-p686-c002 — file p686, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: member request.

> The member can request information based on the following elements:

**src-000015-camt.069.001.05-p686-c003 — file p686, usage.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/participant-narrative-src-000015-account-owner.md).

> account owner (for on behalf scenario)

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p686, scope.**

> It is used to request information on the details of one or more standing orders, based on specific request criteria, especially to query the amount of the overall liquidity available.

**File p686, scope.**

> It will allow to query both reserved liquidity and liquidity available for normal operations.

**File p686, usage.**

> individual standing orders (predefined or standing liquidity transfer orders)

**File p686, usage.**

> amount

**File p686, usage.**

> account to be credited

**File p686, usage.**

> account to be debited

**File p686, usage.**

> frequency of payment

**File p686, usage.**

> daytime or overnight processing

**File p686, usage.**

> dates when the standing order begins and ceases to be effective This message will be answered by a ReturnStandingOrder message.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
