---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p169-overview-of-reporting-classifications"
title: "Overview of Reporting Classifications"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Overview of Reporting Classifications"], "locator": "/w:document/w:body/w:p[169]", "paragraph_id": "P169", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Overview of Reporting Classifications"], "locator": "/w:document/w:body/w:p[170]", "paragraph_id": "P170", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Overview of Reporting Classifications"], "locator": "/w:document/w:body/w:p[171]", "paragraph_id": "P171", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Overview of Reporting Classifications"], "locator": "/w:document/w:body/w:p[172]", "paragraph_id": "P172", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Overview of Reporting Classifications"], "locator": "/w:document/w:body/w:p[173]", "paragraph_id": "P173", "table_id": null}]
participants: ["participant-src-000320-reporting-entity", "participant-src-000320-reporting-entity", "participant-src-000320-competent-authority", "participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Overview of Reporting Classifications", "Reporting Entity", "RE", "CA", "SA"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Overview of Reporting Classifications

Source context: Transactions and Financial Instruments Data Reporting. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Reporting Entity | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| RE | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| CA | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-competent-authority.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| SA | [Participant](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P170** Three classes of message transfer exist within Financial Instruments Regulatory Reporting

**P171** Direct Reporting - This is where the reporting entity submits data directly to the SA 

**P172** Proxy Reporting - This is where a reporting entity has to work with their CA to route data to the SA. In proxy reporting, the CA acts as a routing mechanism between the RE and the SA

**P173** Indirect Reporting - This is where a CA works and interacts with the reporting entity within their jurisdiction on all aspects of the message transfer process. The CA performs all operations the SA performs on the messages before routing the messages / an aggregated message to the SA

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md). Heading path: BusinessTransactions / Overview of Reporting Classifications.
