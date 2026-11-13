---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "semt.026.001.01 participant and direction evidence"
domain: "securities"
message_id: "semt.026.001.01"
message_family: "semt.026"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.026.001.01"
source_ids: ["src-000233", "src-000309", "src-000375"]
message_sets: ["t2s", "t2s-securities-and-penalty-reporting"]
role_labels: ["a settlement infrastructure", "account owner/requestor", "an account owner/requestor", "settlement infrastructure"]
search_terms: ["a settlement infrastructure", "account owner/requestor", "an account owner/requestor", "settlement infrastructure"]
participant_ids: ["participant-narrative-src-000375-account-owner-requestor", "participant-src-000374-settlement-infrastructure"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "71 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "file_pages": [2409, 2472]}, {"source_id": "src-000375", "heading": "3 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "file_pages": [13, 76]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# semt.026.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000233 — 71 semt.026.001.01 SecuritiesSettlementTransactionQueryV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); Functionality file pp2409; publication August 2026.

### Direction and initiation clauses

#### src-000233-semt.026.001.01-p2409-c001-d1

Kind: sender-to-receiver; message applicability: **current-message-scope-name-variant**; src-000233 file p2409, scope.

- Sender: **an account owner/requestor**. [an account owner/requestor](../../../../../shared/reference/participants/participant-narrative-src-000375-account-owner-requestor.md).
- Receiver: **a settlement infrastructure**. [a settlement infrastructure](../../../../../shared/reference/participants/participant-src-000374-settlement-infrastructure.md).

> The SecuritiesSettlementInstructionQuery message is sent from an account owner/requestor to a settlement infrastructure.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-semt.026.001.01-p2409-c001 — file p2409, scope.**

Mentioned roles: [account owner/requestor](../../../../../shared/reference/participants/participant-narrative-src-000375-account-owner-requestor.md); [settlement infrastructure](../../../../../shared/reference/participants/participant-src-000374-settlement-infrastructure.md).

Quoted above in src-000233-semt.026.001.01-p2409-c001-d1.

**src-000233-semt.026.001.01-p2409-c002 — file p2409, scope.**

> The message is used to query information on the securities settlement instructions, that satisfy the defined selection criteria.

## src-000375 — 3 semt.026.001.01 SecuritiesSettlementTransactionQueryV01

[src-000375](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`; Functionality file pp13; publication march-2026.

### Direction and initiation clauses

#### src-000375-semt.026.001.01-p13-c001-d1

Kind: sender-to-receiver; message applicability: **current-message-scope-name-variant**; src-000375 file p13, scope.

- Sender: **an account owner/requestor**. [an account owner/requestor](../../../../../shared/reference/participants/participant-narrative-src-000375-account-owner-requestor.md).
- Receiver: **a settlement infrastructure**. [a settlement infrastructure](../../../../../shared/reference/participants/participant-src-000374-settlement-infrastructure.md).

> The SecuritiesSettlementInstructionQuery message is sent from an account owner/requestor to a settlement infrastructure.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000375-semt.026.001.01-p13-c001 — file p13, scope.**

Mentioned roles: [account owner/requestor](../../../../../shared/reference/participants/participant-narrative-src-000375-account-owner-requestor.md); [settlement infrastructure](../../../../../shared/reference/participants/participant-src-000374-settlement-infrastructure.md).

Quoted above in src-000375-semt.026.001.01-p13-c001-d1.

**src-000375-semt.026.001.01-p13-c002 — file p13, scope.**

> The message is used to query information on the securities settlement instructions, that satisfy the defined selection criteria.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
