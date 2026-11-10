---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p232-trading-activity-result-business-transaction"
title: "Trading Activity Result BusinessTransaction"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Trading Activity Result BusinessTransaction"], "locator": "/w:document/w:body/w:p[232]", "paragraph_id": "P232", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Trading Activity Result BusinessTransaction"], "locator": "/w:document/w:body/w:p[233]", "paragraph_id": "P233", "table_id": null}]
participants: ["participant-src-000320-competent-authority", "participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Trading Activity Result BusinessTransaction", "CA", "SA"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Trading Activity Result BusinessTransaction

Source context: Transactions and Financial Instruments Data Reporting. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| CA | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-competent-authority.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| SA | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P233** The Transparency Trading Activity Result is captured to support performing calculations to identify a range of features on both Equity and Non-Equity instruments that are trading. Where a CA performs these calculations rather than an SA, there is a need to submit the result data to the SA to support publication of the full set of calculation results for all instruments.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000320](../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx). Heading path: BusinessTransactions / Trading Activity Result BusinessTransaction.
