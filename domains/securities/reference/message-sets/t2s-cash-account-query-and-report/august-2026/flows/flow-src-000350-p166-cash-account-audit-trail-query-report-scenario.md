---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000350"]
source_editions: ["august-2026"]
message_sets: ["t2s-cash-account-query-and-report"]
flow_id: "flow-src-000350-p166-cash-account-audit-trail-query-report-scenario"
title: "Cash Account Audit Trail Query/ Report Scenario"
source_locations: [{"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Cash Account Audit Trail Query/ Report Scenario"], "locator": "/w:document/w:body/w:p[166]", "paragraph_id": "P166", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Cash Account Audit Trail Query/ Report Scenario"], "locator": "/w:document/w:body/w:p[167]", "paragraph_id": "P167", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Cash Account Audit Trail Query/ Report Scenario"], "locator": "/w:document/w:body/w:p[168]", "paragraph_id": "P168", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Cash Account Audit Trail Query/ Report Scenario"], "locator": "/w:document/w:body/w:p[169]", "paragraph_id": "P169", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Cash Account Audit Trail Query/ Report Scenario"], "locator": "/w:document/w:body/w:p[170]", "paragraph_id": "P170", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Cash Account Audit Trail Query/ Report Scenario"], "locator": "/w:document/w:body/w:p[171]", "paragraph_id": "P171", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Cash Account Audit Trail Query/ Report Scenario"], "locator": "/w:document/w:body/w:p[172]", "paragraph_id": "P172", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Cash Account Audit Trail Query/ Report Scenario"], "locator": "/w:document/w:body/w:p[173]", "paragraph_id": "P173", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Cash Account Audit Trail Query/ Report Scenario"], "locator": "/w:document/w:body/w:p[174]", "paragraph_id": "P174", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Cash Account Audit Trail Query/ Report Scenario"], "locator": "/w:document/w:body/w:p[175]", "paragraph_id": "P175", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Cash Account Audit Trail Query/ Report Scenario"], "locator": "/w:document/w:body/w:p[176]", "paragraph_id": "P176", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Cash Account Audit Trail Query/ Report Scenario"], "locator": "/w:document/w:body/w:p[177]", "paragraph_id": "P177", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Cash Account Audit Trail Query/ Report Scenario"], "locator": "/w:document/w:body/w:p[178]", "paragraph_id": "P178", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Cash Account Audit Trail Query/ Report Scenario"], "locator": "/w:document/w:body/w:p[179]", "paragraph_id": "P179", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Cash Account Audit Trail Query/ Report Scenario"], "locator": "/w:document/w:body/w:p[180]", "paragraph_id": "P180", "table_id": null}]
participants: ["participant-src-000350-executing-servicing-party", "participant-src-000350-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000350", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Cash Account Query and report"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.039.001.01", "reda.040.001.01"]
message_families: ["reda.039", "reda.040"]
search_terms: ["Cash Account Audit Trail Query/ Report Scenario", "Executing / Servicing Party", "Instructing Party", "reda.039"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
---



# Cash Account Audit Trail Query/ Report Scenario

Source context: T2S CashAccountQueryAndReport. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000350-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000350-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0012](../documents/src-000350/diagrams/fig-0012.md). A canonical source reconstruction and actual review evidence are linked below.

**P168** Cash Account Audit Trail Query

**P170** The Instructing Party sends an instruction to the Executing/Servicing Party to run a query according to specified criteria’s to retrieve the complete audit trail on a specific cash account.

**P172** Cash Account Audit Trail Report - Negative scenario

**P173** Depending on the query criteria, it is possible that the processing will take more than a certain time or that the result of the query will be empty due to wrong combination of criteria or no result set. In this case, an error message within a query response message is sent to the Instructing Party.

**P175** Cash Account  Audit Trail Report

**P176** The Executing/Servicing Party sends a query response that meets the specified criteria to the Instructing Party.

## Messages and alternative paths

Source-supported message family mentions: `reda.039`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000350](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart1_Target2Securities_CashAccountQueryAndReport_v2.docx`. Heading path: BusinessTransactions / Query/Response Process / Cash Account Audit Trail Query/ Report Scenario.

## Curated source flow

The source displays a query from Instructing Party to Executing/Servicing Party, a dashed ERROR response and a solid normal response in that vertical order. The narrative distinguishes negative and successful scenarios: excessive processing time, wrong criteria combination or no result may produce the error. Both response arrows are preserved as alternatives, not a requirement to send an error followed by a normal result. The audit-trail process retrieves a complete audit trail for the specified cash account; the account-query process returns data meeting its query criteria.

[Complete source diagram](../diagrams/curated/fig-0012.md).

### Adjacent source narrative

**P170** The Instructing Party sends an instruction to the Executing/Servicing Party to run a query according to specified criteria’s to retrieve the complete audit trail on a specific cash account.

**P172** Cash Account Audit Trail Report - Negative scenario

**P173** Depending on the query criteria, it is possible that the processing will take more than a certain time or that the result of the query will be empty due to wrong combination of criteria or no result set. In this case, an error message within a query response message is sent to the Instructing Party.

**P174**  

**P175** Cash Account  Audit Trail Report

**P176** The Executing/Servicing Party sends a query response that meets the specified criteria to the Instructing Party.

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000350-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000350-executing-servicing-party.md).
