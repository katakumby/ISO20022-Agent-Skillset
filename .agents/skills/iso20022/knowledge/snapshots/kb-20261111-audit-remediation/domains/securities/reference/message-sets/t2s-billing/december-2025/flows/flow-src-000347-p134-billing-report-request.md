---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000347"]
source_editions: ["december-2025"]
message_sets: ["t2s-billing"]
flow_id: "flow-src-000347-p134-billing-report-request"
title: "Billing Report Request"
source_locations: [{"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Query Billing Information", "Positive Scenario"], "locator": "/w:document/w:body/w:p[134]", "paragraph_id": "P134", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Query Billing Information", "Positive Scenario"], "locator": "/w:document/w:body/w:p[135]", "paragraph_id": "P135", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Query Billing Information", "Positive Scenario"], "locator": "/w:document/w:body/w:p[136]", "paragraph_id": "P136", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Query Billing Information", "Positive Scenario"], "locator": "/w:document/w:body/w:p[137]", "paragraph_id": "P137", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Query Billing Information", "Positive Scenario"], "locator": "/w:document/w:body/w:p[138]", "paragraph_id": "P138", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Query Billing Information", "Positive Scenario"], "locator": "/w:document/w:body/w:p[139]", "paragraph_id": "P139", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Query Billing Information", "Positive Scenario"], "locator": "/w:document/w:body/w:p[140]", "paragraph_id": "P140", "table_id": null}, {"source_id": "src-000347", "heading_path": ["BusinessTransactions", "Query Billing Information", "Positive Scenario"], "locator": "/w:document/w:body/w:p[141]", "paragraph_id": "P141", "table_id": null}]
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

**P135** The Instructing Party sends the query to the Executing/Servicing Party to obtain information about:

**P136** - Cumulative Billing Data

**P137** - Itemised Billing Data

**P139** This query contains information that clearly identifies a certain invoice, billing period or, in case of itemised queries, specific securities account, cash account or participant.

**P140** The Executing/Servicing Party informs the Instructing party that the Billing Report Query has been successfully processed (COMPLETED) by returning the requested information.

## Messages and alternative paths

Source-supported message family mentions: `camt.076`, `camt.077`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000347](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v2.docx`. Heading path: BusinessTransactions / Query Billing Information / Positive Scenario.
