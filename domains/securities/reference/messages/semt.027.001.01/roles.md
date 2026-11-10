---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "semt.027.001.01 participant and direction evidence"
domain: "securities"
message_id: "semt.027.001.01"
message_family: "semt.027"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.027.001.01"
source_ids: ["src-000233", "src-000310", "src-000375"]
message_sets: ["t2s", "t2s-securities-and-penalty-reporting"]
role_labels: ["a settlement infrastructure", "account owner/requestor", "an account owner/requestor", "settlement infrastructure"]
search_terms: ["a settlement infrastructure", "account owner/requestor", "an account owner/requestor", "settlement infrastructure"]
participant_ids: ["participant-narrative-src-000375-account-owner-requestor", "participant-src-000374-settlement-infrastructure"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "file_pages": [2473, 2561]}, {"source_id": "src-000375", "heading": "4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "file_pages": [77, 165]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# semt.027.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000233 — 72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); Functionality file pp2473; publication August 2026.

### Direction and initiation clauses

#### src-000233-semt.027.001.01-p2473-c001-d1

Kind: sender-to-receiver; message applicability: **current-message-scope-name-variant**; src-000233 file p2473, scope.

- Sender: **a settlement infrastructure**. [a settlement infrastructure](../../../../../shared/reference/participants/participant-src-000374-settlement-infrastructure.md).
- Receiver: **an account owner/requestor**. [an account owner/requestor](../../../../../shared/reference/participants/participant-narrative-src-000375-account-owner-requestor.md).

> The SecuritiesSettlementResponse message is sent from a settlement infrastructure to an account owner/requestor to provide the details of the securities settlement instructions, as selected in the search criteria defined in the request.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-semt.027.001.01-p2473-c001 — file p2473, scope.**

Mentioned roles: [settlement infrastructure](../../../../../shared/reference/participants/participant-src-000374-settlement-infrastructure.md); [account owner/requestor](../../../../../shared/reference/participants/participant-narrative-src-000375-account-owner-requestor.md).

Quoted above in src-000233-semt.027.001.01-p2473-c001-d1.

## src-000375 — 4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01

[src-000375](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`; Functionality file pp77; publication march-2026.

### Direction and initiation clauses

#### src-000375-semt.027.001.01-p77-c001-d1

Kind: sender-to-receiver; message applicability: **current-message-scope-name-variant**; src-000375 file p77, scope.

- Sender: **a settlement infrastructure**. [a settlement infrastructure](../../../../../shared/reference/participants/participant-src-000374-settlement-infrastructure.md).
- Receiver: **an account owner/requestor**. [an account owner/requestor](../../../../../shared/reference/participants/participant-narrative-src-000375-account-owner-requestor.md).

> The SecuritiesSettlementResponse message is sent from a settlement infrastructure to an account owner/requestor to provide the details of the securities settlement instructions, as selected in the search criteria defined in the request.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000375-semt.027.001.01-p77-c001 — file p77, scope.**

Mentioned roles: [settlement infrastructure](../../../../../shared/reference/participants/participant-src-000374-settlement-infrastructure.md); [account owner/requestor](../../../../../shared/reference/participants/participant-narrative-src-000375-account-owner-requestor.md).

Quoted above in src-000375-semt.027.001.01-p77-c001-d1.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
