---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.060.001.07 participant and direction evidence"
domain: "payments"
message_id: "camt.060.001.07"
message_family: "camt.060"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.060.001.07"
source_ids: ["src-000005", "src-000010"]
message_sets: ["bank-to-customer-cash-management"]
role_labels: ["account owner", "account servicing institution", "forwarding agent", "one of its account servicing institutions", "the account owner"]
search_terms: ["account owner", "account servicing institution", "forwarding agent", "one of its account servicing institutions", "the account owner"]
participant_ids: ["participant-functionality-src-000005-account-servicing-institution", "participant-src-000004-account-owner", "participant-src-000004-forwarding-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000005", "heading": "5 camt.060.001.07 AccountReportingRequestV07", "file_pages": [781, 795]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.060.001.07 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 3 uniquely resolved participant references.

## src-000005 — 5 camt.060.001.07 AccountReportingRequestV07

[src-000005](../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf); Functionality file pp781; publication March 2026.

### Direction and initiation clauses

#### src-000005-camt.060.001.07-p781-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000005 file p781, scope.

- Sender: **the account owner, either directly or through a forwarding agent**. [the account owner](../../../../../shared/reference/participants/participant-src-000004-account-owner.md).
- Receiver: **one of its account servicing institutions**. [one of its account servicing institutions](../../../../../shared/reference/participants/participant-functionality-src-000005-account-servicing-institution.md).

> The AccountReportingRequest message is sent by the account owner, either directly or through a forwarding agent, to one of its account servicing institutions.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000005-camt.060.001.07-p781-c001 — file p781, scope.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/participant-src-000004-account-owner.md); [forwarding agent](../../../../../shared/reference/participants/participant-src-000004-forwarding-agent.md); [one of its account servicing institutions](../../../../../shared/reference/participants/participant-functionality-src-000005-account-servicing-institution.md).

Quoted above in src-000005-camt.060.001.07-p781-c001-d1.

**src-000005-camt.060.001.07-p781-c002 — file p781, scope.**

Mentioned roles: [account servicing institution](../../../../../shared/reference/participants/participant-functionality-src-000005-account-servicing-institution.md); [account owner](../../../../../shared/reference/participants/participant-src-000004-account-owner.md).

Literal actions: account servicing institution is asked to send.

Reviewed clause disposition: **source-explicit-role-action**. The actor and action are named in this sentence; the action object and conditions are retained and are not automatically the indexed message.

> It is used to ask the account servicing institution to send a report on the account owner's account in a BankToCustomerAccountReport (camt.052), a BankToCustomerStatement (camt.053) or a BankToCustomerDebitCreditNotification (camt.054).

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
