---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.053.001.14 participant and direction evidence"
domain: "payments"
message_id: "camt.053.001.14"
message_family: "camt.053"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.053.001.14"
source_ids: ["src-000005", "src-000008"]
message_sets: ["bank-to-customer-cash-management"]
role_labels: ["account owner", "account servicer", "an account owner", "banks", "customers", "party authorised by the account owner", "receiver", "recipient", "the account servicer", "to a party authorised by the account owner"]
search_terms: ["account owner", "account servicer", "an account owner", "banks", "customers", "party authorised by the account owner", "receiver", "recipient", "the account servicer", "to a party authorised by the account owner"]
participant_ids: ["participant-functionality-src-000005-party-authorised-by-account-owner", "participant-functionality-src-000005-recipient", "participant-narrative-src-000005-bank", "participant-narrative-src-000005-customer", "participant-src-000004-account-owner", "participant-src-000004-account-servicer", "participant-src-000004-recipient"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000005", "heading": "3 camt.053.001.14 BankToCustomerStatementV14", "file_pages": [263, 522]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.053.001.14 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 7 uniquely resolved participant references.

## src-000005 — 3 camt.053.001.14 BankToCustomerStatementV14

[src-000005](../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md); Functionality file pp263; publication March 2026.

### Direction and initiation clauses

#### src-000005-camt.053.001.14-p263-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000005 file p263, scope.

- Sender: **the account servicer**. [the account servicer](../../../../../shared/reference/participants/participant-src-000004-account-servicer.md).
- Receiver: **an account owner or to a party authorised by the account owner**. [an account owner](../../../../../shared/reference/participants/participant-src-000004-account-owner.md); [to a party authorised by the account owner](../../../../../shared/reference/participants/participant-functionality-src-000005-party-authorised-by-account-owner.md).

> The BankToCustomerStatement message is sent by the account servicer to an account owner or to a party authorised by the account owner to receive the message.

#### src-000005-camt.053.001.14-p263-c005-d1

Kind: receiver-only; message applicability: **current-message**; src-000005 file p263, usage.

- Receiver: **recipient**. [recipient](../../../../../shared/reference/participants/participant-src-000004-recipient.md).

> It is possible that the receiver of the message is not the account owner, but a party entitled through arrangement with the account owner to receive the account information (also known as recipient).

Conditional alternative recipient: the account owner may entitle another party to receive the information. This does not assert that the account owner is always excluded. The exact entitlement wording is retained.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000005-camt.053.001.14-p263-c001 — file p263, scope.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/participant-src-000004-account-servicer.md); [account owner](../../../../../shared/reference/participants/participant-src-000004-account-owner.md); [party authorised by the account owner](../../../../../shared/reference/participants/participant-functionality-src-000005-party-authorised-by-account-owner.md).

Quoted above in src-000005-camt.053.001.14-p263-c001-d1.

**src-000005-camt.053.001.14-p263-c002 — file p263, scope.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/participant-src-000004-account-owner.md).

> It is used to inform the account owner, or authorised party, of the entries booked to the account, and to provide the owner with balance information on the account at a given point in time.

**src-000005-camt.053.001.14-p263-c003 — file p263, usage.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/participant-src-000004-account-servicer.md); [account owner](../../../../../shared/reference/participants/participant-src-000004-account-owner.md).

> The message is exchanged as defined between the account servicer and the account owner.

**src-000005-camt.053.001.14-p263-c004 — file p263, usage.**

Mentioned roles: [banks](../../../../../shared/reference/participants/participant-narrative-src-000005-bank.md); [customers](../../../../../shared/reference/participants/participant-narrative-src-000005-customer.md).

> Depending on services and schedule agreed between banks and their customers, statements may be generated and exchanged accordingly, for example for intraday or prior day periods.

**src-000005-camt.053.001.14-p263-c005 — file p263, usage.**

Mentioned roles: [receiver](../../../../../shared/reference/participants/participant-functionality-src-000005-recipient.md); [account owner](../../../../../shared/reference/participants/participant-src-000004-account-owner.md); [account owner](../../../../../shared/reference/participants/participant-src-000004-account-owner.md); [recipient](../../../../../shared/reference/participants/participant-src-000004-recipient.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000005-camt.053.001.14-p263-c005-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p263, usage.**

> The BankToCustomerStatement message can contain reports for more than one account.

**File p263, usage.**

> It provides information for cash management and/or reconciliation.

**File p263, usage.**

> It contains information on booked entries only.

**File p263, usage.**

> It can include underlying details of transactions that have been included in the entry.

**File p263, usage.**

> It provides information on items that have been booked to the account and also balance information.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
