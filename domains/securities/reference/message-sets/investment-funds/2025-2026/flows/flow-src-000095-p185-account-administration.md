---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p185-account-administration"
title: "Account Administration"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[185]", "paragraph_id": "P185", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[21]", "paragraph_id": null, "table_id": "T21"}]
participants: ["participant-src-000095-intermediary"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Account Administration", "Intermediary"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Account Administration

Source context: Investment Funds. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The account servicer creates and maintains an accounting record for the account owner/intermediary with the fund and records static information relating to the account owner/intermediary, for example, name, address, credit limit, anti-money laundering checks, tax and residency status, income distribution instructions, settlement instructions and terms and intermediary.

Evidence: [T21](../documents/src-000095/tables/tbl-0021.md), source row 2.

### Trigger

investor wants to make an investment in a fund
account owner wants to open, maintain or close its account

Evidence: [T21](../documents/src-000095/tables/tbl-0021.md), source row 3.

### Pre-conditions

formal demand from the account owner to open, maintain or close an account
if the account is to be closed, then a zero balance in the account

Evidence: [T21](../documents/src-000095/tables/tbl-0021.md), source row 4.

### Post-conditions

anti-money laundering, legal documentation or other documentation is available 
credit limit is set
account identification is attributed
direct debit mandates are set up
power of attorney is added
reporting is defined
commission schedule is defined
confirmation of account details is provided to the account owner or its intermediary
relevant tax authorities are informed
account is open, updated or closed

Evidence: [T21](../documents/src-000095/tables/tbl-0021.md), source row 5.

### Role

Account servicer

Evidence: [T21](../documents/src-000095/tables/tbl-0021.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Intermediary | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T21](../documents/src-000095/tables/tbl-0021.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Heading path: BusinessProcess Description.
