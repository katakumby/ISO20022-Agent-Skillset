---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
message_sets: ["bank-to-customer-cash-management"]
flow_id: "flow-src-000004-p128-reporting"
title: "Reporting"
source_locations: [{"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting"], "locator": "/w:document/w:body/w:p[128]", "paragraph_id": "P128", "table_id": null}, {"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting"], "locator": "/w:document/w:body/w:p[129]", "paragraph_id": "P129", "table_id": null}, {"source_id": "src-000004", "heading_path": ["BusinessTransactions", "Reporting"], "locator": "/w:document/w:body/w:p[130]", "paragraph_id": "P130", "table_id": null}]
participants: ["participant-src-000004-account-servicer", "participant-src-000004-account-owner", "participant-src-000004-recipient"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Reporting", "Account Servicer", "Account Owner", "Recipient"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---



# Reporting

Source context: Bank-to-Customer Cash Management. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Recipient | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-recipient.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P129** The Bank-to-Customer Cash Management messages are sent from the account servicer to the account owner, or a party authorised by the account owner to receive the account information (i.e. the Message Recipient).

**P130** The scenarios illustrate the reporting from account servicer to account owner.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000004](../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart1_BankToCustomerCashManagement_2025_2026_v2.docx). Heading path: BusinessTransactions / Reporting.
