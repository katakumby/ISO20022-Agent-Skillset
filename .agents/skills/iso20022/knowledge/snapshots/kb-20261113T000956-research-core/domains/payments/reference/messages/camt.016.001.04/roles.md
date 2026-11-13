---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.016.001.04 participant and direction evidence"
domain: "payments"
message_id: "camt.016.001.04"
message_family: "camt.016"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.016.001.04"
source_ids: ["src-000015", "src-000030"]
message_sets: ["cash-management"]
role_labels: ["a member", "member", "members", "the transaction administrator", "transaction administrator"]
search_terms: ["a member", "member", "members", "the transaction administrator", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "15 camt.016.001.04 GetCurrencyExchangeRateV04", "file_pages": [505, 510]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.016.001.04 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000015 — 15 camt.016.001.04 GetCurrencyExchangeRateV04

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); Functionality file pp505; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.016.001.04-p505-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p505, scope.

- Sender: **a member**. [a member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).
- Receiver: **the transaction administrator**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The GetCurrencyExchangeRate message is sent by a member to the transaction administrator.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.016.001.04-p505-c001 — file p505, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Quoted above in src-000015-camt.016.001.04-p505-c001-d1.

**src-000015-camt.016.001.04-p505-c002 — file p505, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator maintained.

> It is used to request information on static data maintained by the transaction administrator and related to currency exchange details as maintained for the system operations by the transaction administrator.

**src-000015-camt.016.001.04-p505-c003 — file p505, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> The transaction administrator is in charge of providing the members with business information.

**src-000015-camt.016.001.04-p505-c004 — file p505, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> When a system manages a pool of accounts in various currencies for a member, there is a need to maintain currency exchange details in between the various currencies and the reporting or base currency.

**src-000015-camt.016.001.04-p505-c005 — file p505, usage.**

Mentioned roles: [members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> The reporting or base currency is used to calculate the actual position of the members in terms of aggregate limits and balances and allow the system to contain risk within the defined and agreed boundaries.

**src-000015-camt.016.001.04-p505-c006 — file p505, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> At any point in time during operating hours of the system, the member can query the transaction administrator to get information about the static data related to a currency exchange details.

**src-000015-camt.016.001.04-p505-c007 — file p505, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: member request.

> The member can request information based on the following elements:

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p505, usage.**

> The term business information covers all information related to the management of the system, i.e., not related to the transactions created into the system.

**File p505, usage.**

> The type of business information available can vary depending on the system.

**File p505, usage.**

> The currency exchange details can be fixed for the entire operational day, or regularly updated according to near real time market feeds.

**File p505, usage.**

> the currency to be converted (source currency)

**File p505, usage.**

> the currency into which the amount is converted (target currency) This message will be replied to by a ReturnCurrencyExchangeRate message.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
