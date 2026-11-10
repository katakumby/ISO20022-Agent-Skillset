---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000347"]
source_editions: ["december-2025"]
message_sets: ["t2s-billing"]
flow_id: "flow-src-000347-p147-billing-report-request"
title: "Billing Report Request"
source_locations: [{"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Query Billing Information", "Negative Scenario"], "locator": "/w:document/w:body/w:p[147]", "paragraph_id": "P147", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Query Billing Information", "Negative Scenario"], "locator": "/w:document/w:body/w:p[148]", "paragraph_id": "P148", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Query Billing Information", "Negative Scenario"], "locator": "/w:document/w:body/w:p[149]", "paragraph_id": "P149", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Query Billing Information", "Negative Scenario"], "locator": "/w:document/w:body/w:p[150]", "paragraph_id": "P150", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Query Billing Information", "Negative Scenario"], "locator": "/w:document/w:body/w:p[151]", "paragraph_id": "P151", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Query Billing Information", "Negative Scenario"], "locator": "/w:document/w:body/w:p[152]", "paragraph_id": "P152", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Query Billing Information", "Negative Scenario"], "locator": "/w:document/w:body/w:p[153]", "paragraph_id": "P153", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Query Billing Information", "Negative Scenario"], "locator": "/w:document/w:body/w:p[154]", "paragraph_id": "P154", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Query Billing Information", "Negative Scenario"], "locator": "/w:document/w:body/w:p[155]", "paragraph_id": "P155", "table_id": null}]
participants: ["participant-src-000347-executing-servicing-party", "participant-src-000347-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000347", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Billing"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000347", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Billing"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["camt.076", "camt.077"]
search_terms: ["Billing Report Request", "Executing / Servicing Party", "Instructing Party", "camt.076", "camt.077"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Billing Report Request

Source context: T2S Billing. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000347-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000347-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P148** The Instructing Party sends the query to the Executing/Servicing Party to obtain information about:

**P149** Cumulative Billing Data

**P150** Itemised Billing Data

**P152** This query contains information that clearly identifies a certain invoice, billing period or, in case of itemised queries, specific securities account, cash account or participant.

**P153** The Executing/Servicing Party informs the Instructing party that the Billing Report Query has been rejected (REJECTED). The Executing/Servicing Party present to the Instructing Party the business or operational error which caused the rejection.

## Messages and alternative paths

Source-supported message family mentions: `camt.076`, `camt.077`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000347](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v2.docx`. Heading path: BusinessTransactions / Query Billing Information / Negative Scenario.
