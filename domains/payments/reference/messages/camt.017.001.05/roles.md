---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.017.001.05 participant and direction evidence"
domain: "payments"
message_id: "camt.017.001.05"
message_family: "camt.017"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05"
source_ids: ["src-000015", "src-000031"]
message_sets: ["cash-management"]
role_labels: ["a member of the system", "account servicer", "member", "member of the system", "members", "the account servicer", "the transaction administrator", "transaction administrator"]
search_terms: ["a member of the system", "account servicer", "member", "member of the system", "members", "the account servicer", "the transaction administrator", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-account-servicer", "participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "16 camt.017.001.05 ReturnCurrencyExchangeRateV05", "file_pages": [511, 521]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.017.001.05 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 3 direction/initiator/exchange clauses; 3 uniquely resolved participant references.

## src-000015 — 16 camt.017.001.05 ReturnCurrencyExchangeRateV05

[src-000015](../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf); Functionality file pp511, 512; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.017.001.05-p511-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p511, scope.

- Sender: **the transaction administrator**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).
- Receiver: **a member of the system**. [a member of the system](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> The ReturnCurrencyExchangeRate message is sent by the transaction administrator to a member of the system.

#### src-000015-camt.017.001.05-p511-c003-d1

Kind: initiator; message applicability: **current-message**; src-000015 file p511, scope.

- Initiator: **the account servicer (push mode)**. [the account servicer](../../../../../shared/reference/participants/participant-narrative-src-000015-account-servicer.md).

> The ReturnCurrencyExchangeRate message can be sent as a response to a related GetCurrencyExchangeRate message (pull mode) or initiated by the account servicer (push mode).

#### src-000015-camt.017.001.05-p511-c009-d1

Kind: sender-only; message applicability: **current-message**; src-000015 file p511, usage.

- Sender: **transaction administrator**. [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The transaction administrator may also send a Return Currency Exchange Rate message with pre- defined information at times previously agreed with the member or to warn the member about a particular problem that may have arisen and which needs the member(s) attention.

Source explicitly names the sender. Scheduling, warning/preliminary usage and information content remain in the quote; no receiver is supplied by this clause.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.017.001.05-p511-c001 — file p511, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [member of the system](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Quoted above in src-000015-camt.017.001.05-p511-c001-d1.

**src-000015-camt.017.001.05-p511-c002 — file p511, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> It is used to provide information on static data and related to currency exchange details as maintained for system operations by the transaction administrator.

**src-000015-camt.017.001.05-p511-c003 — file p511, scope.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/participant-narrative-src-000015-account-servicer.md).

Literal actions: account servicer initiated.

Quoted above in src-000015-camt.017.001.05-p511-c003-d1.

**src-000015-camt.017.001.05-p511-c004 — file p511, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> The transaction administrator is in charge of providing the members with business information.

**src-000015-camt.017.001.05-p511-c005 — file p511, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> When a system manages a pool of accounts in various currencies for a member, it needs to maintain currency exchange details between the various currencies and the reporting on base currency.

**src-000015-camt.017.001.05-p511-c006 — file p511, usage.**

Mentioned roles: [members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> The reporting on base currency is used to calculate the actual position of the members in terms of aggregate limits and balances.

**src-000015-camt.017.001.05-p511-c007 — file p511, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: member request.

> The member can request information about a currency exchange operation through a series of criteria, corresponding to the known information stored within the transaction administrator.

**src-000015-camt.017.001.05-p511-c008 — file p511, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Reviewed clause disposition: **actor-or-condition-context**. The sentence describes actors, responsibilities, source/target data, prohibitions or conditions. Existing literal actions and the complete quote remain available; sending/receiving a different object or a negative assertion is not converted into an unconditional current-message direction.

> Based on the criteria received within the request, the transaction administrator will select items that will match with the request and report them to the requestor.

**src-000015-camt.017.001.05-p511-c009 — file p511, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: transaction administrator send.

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000015-camt.017.001.05-p511-c009-d1.

**src-000015-camt.017.001.05-p511-c010 — file p511, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The message from the transaction administrator will contain information based on the following elements:

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p511, scope.**

> The push of information can take place either at prearranged times or as a warning or alarm when a problem has occurred.

**File p511, usage.**

> The term business information covers all information related to the management of the system, that is, not related to the transactions or requests created in the system.

**File p511, usage.**

> The type of business information available can vary depending on the system.

**File p511, usage.**

> It also allows the system to contain risk within defined and agreed boundaries.

**File p511, usage.**

> The currency exchange details can be fixed for the entire operational day or regularly updated according to near real-time market feeds.

**File p511, usage.**

> the currency to be converted (source currency)

**File p511, usage.**

> the currency into which the amount is converted (target currency)

**File p511, usage.**

> the exchange rate

**File p511, 512, usage.**

> the quotation date and currency Approved by the Payments SEG on 04 February 2025 camt.017.001.05 ReturnCurrencyExchangeRateV05 Cash Management - Maintenance 2024 - 2025 511 February 2025 Additional information on the generic design of the Get/Return messages can be found in the MDR Part 1 section How to Use the Cash Management Messages.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
