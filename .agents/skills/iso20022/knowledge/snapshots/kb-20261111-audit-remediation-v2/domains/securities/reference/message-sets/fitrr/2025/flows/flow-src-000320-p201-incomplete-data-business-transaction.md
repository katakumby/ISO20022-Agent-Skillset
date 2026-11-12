---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p201-incomplete-data-business-transaction"
title: "Incomplete Data BusinessTransaction"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Incomplete Data BusinessTransaction"], "locator": "/w:document/w:body/w:p[201]", "paragraph_id": "P201", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Incomplete Data BusinessTransaction"], "locator": "/w:document/w:body/w:p[202]", "paragraph_id": "P202", "table_id": null}]
participants: ["participant-src-000320-supervisory-authority", "participant-src-000320-reporting-entity", "participant-src-000320-if"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Incomplete Data BusinessTransaction", "Supervisory Authority", "Reporting Entity", "IF"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Incomplete Data BusinessTransaction

Source context: Transactions and Financial Instruments Data Reporting. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Supervisory Authority | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Reporting Entity | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| IF | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-if.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P202** Based on the number of venues that will submit data, the chance that not all data for a given day is submitted is high. As part of data quality, checks will be performed to see if all reporting entities for a specific dataset submitted all their data. Where not all data has been reported, a reminder will be sent to these venues informing them either that they made no data submission or of all instruments they failed to submit based on the data the supervisory authority is aware of. Where a reporting entity receives a reminder file, it is incumbent on them to fix the issue and submit complete data in the next submission window.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md). Heading path: BusinessTransactions / Incomplete Data BusinessTransaction.
