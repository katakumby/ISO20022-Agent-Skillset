---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
flow_id: "flow-src-000014-p337-standing-orders-business-transactions"
title: "Standing Orders BusinessTransactions"
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessTransactions", "Standing Orders BusinessTransactions"], "locator": "/w:document/w:body/w:p[337]", "paragraph_id": "P337", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "Standing Orders BusinessTransactions"], "locator": "/w:document/w:body/w:p[338]", "paragraph_id": "P338", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "Standing Orders BusinessTransactions"], "locator": "/w:document/w:body/w:p[339]", "paragraph_id": "P339", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "Standing Orders BusinessTransactions"], "locator": "/w:document/w:body/w:p[340]", "paragraph_id": "P340", "table_id": null}]
participants: ["participant-src-000014-rtgs"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Standing Orders BusinessTransactions", "RTGS"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Standing Orders BusinessTransactions

Source context: Cash Management. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| RTGS | [Participant](../../../../../../../shared/reference/participants/participant-src-000014-rtgs.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P338** Standing orders trigger a transfer of funds between two accounts belonging to the member in the books of the transaction administrator.

**P339** Standing orders are permanent transfer orders input by the member into the system. They allow the member to move funds from outside the system into its accounts with the transaction administrator that are used for specific purposes (for example, the settlement account for RTGS operations), objective of these transfers being for example to provide sufficient liquidity for the start of operations at the beginning of the business day.

**P340** The standing order may be pre-set by the system and the necessary amount necessary left to the discretion of the members, or the transaction administrator may effect a calculation and a call for funds for efficient use of the liquidity.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000014](../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx). Heading path: BusinessTransactions / Standing Orders BusinessTransactions.
