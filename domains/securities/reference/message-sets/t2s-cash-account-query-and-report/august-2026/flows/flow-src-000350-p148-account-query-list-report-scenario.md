---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000350"]
source_editions: ["august-2026"]
message_sets: ["t2s-cash-account-query-and-report"]
flow_id: "flow-src-000350-p148-account-query-list-report-scenario"
title: "Account Query List/Report Scenario"
source_locations: [{"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Account Query List/Report Scenario"], "locator": "/w:document/w:body/w:p[148]", "paragraph_id": "P148", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Account Query List/Report Scenario"], "locator": "/w:document/w:body/w:p[149]", "paragraph_id": "P149", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Account Query List/Report Scenario"], "locator": "/w:document/w:body/w:p[150]", "paragraph_id": "P150", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Account Query List/Report Scenario"], "locator": "/w:document/w:body/w:p[151]", "paragraph_id": "P151", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Account Query List/Report Scenario"], "locator": "/w:document/w:body/w:p[152]", "paragraph_id": "P152", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Account Query List/Report Scenario"], "locator": "/w:document/w:body/w:p[153]", "paragraph_id": "P153", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Account Query List/Report Scenario"], "locator": "/w:document/w:body/w:p[154]", "paragraph_id": "P154", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Account Query List/Report Scenario"], "locator": "/w:document/w:body/w:p[155]", "paragraph_id": "P155", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Account Query List/Report Scenario"], "locator": "/w:document/w:body/w:p[156]", "paragraph_id": "P156", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Account Query List/Report Scenario"], "locator": "/w:document/w:body/w:p[157]", "paragraph_id": "P157", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Account Query List/Report Scenario"], "locator": "/w:document/w:body/w:p[158]", "paragraph_id": "P158", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Account Query List/Report Scenario"], "locator": "/w:document/w:body/w:p[159]", "paragraph_id": "P159", "table_id": null}, {"source_id": "src-000350", "heading_path": ["BusinessTransactions", "Query/Response Process", "Account Query List/Report Scenario"], "locator": "/w:document/w:body/w:p[160]", "paragraph_id": "P160", "table_id": null}]
participants: ["participant-src-000350-executing-servicing-party", "participant-src-000350-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000350", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Cash Account Query and report"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000350", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Cash Account Query and report"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["acmt.025.001.02", "acmt.026.001.02"]
message_families: ["acmt.025", "acmt.026"]
search_terms: ["Account Query List/Report Scenario", "Executing / Servicing Party", "Instructing Party", "acmt.025", "acmt.026"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
---



# Account Query List/Report Scenario

Source context: T2S CashAccountQueryAndReport. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000350-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000350-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0010](../documents/src-000350/diagrams/fig-0010.md). A canonical source reconstruction and actual review evidence are linked below.

**P152** Account Query List

**P153** The Instructing Party sends an instruction to the Executing/Servicing Party to run a query according to specified criteria.

**P155** Account List Report - Negative Scenario

**P156** Depending on the query criteria, it is possible that the processing will take more than a certain time or that the result of the query will be empty due to wrong combination of criteria or no result set. In this case, an error message within a query response message is sent to the Instructing Party.

**P158** Account List Report

**P159** The Executing/Servicing Party sends a query response that meets the specified criteria to the Instructing Party.

## Messages and alternative paths

Source-supported message family mentions: `acmt.025`, `acmt.026`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000350](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart1_Target2Securities_CashAccountQueryAndReport_v2.docx`. Heading path: BusinessTransactions / Query/Response Process / Account Query List/Report Scenario.

## Curated source flow

The source displays a query from Instructing Party to Executing/Servicing Party, a dashed ERROR response and a solid normal response in that vertical order. The narrative distinguishes negative and successful scenarios: excessive processing time, wrong criteria combination or no result may produce the error. Both response arrows are preserved as alternatives, not a requirement to send an error followed by a normal result. The audit-trail process retrieves a complete audit trail for the specified cash account; the account-query process returns data meeting its query criteria.

[Complete source diagram](../diagrams/curated/fig-0010.md).

### Adjacent source narrative

**P153** The Instructing Party sends an instruction to the Executing/Servicing Party to run a query according to specified criteria.

**P155** Account List Report - Negative Scenario

**P156** Depending on the query criteria, it is possible that the processing will take more than a certain time or that the result of the query will be empty due to wrong combination of criteria or no result set. In this case, an error message within a query response message is sent to the Instructing Party.

**P158** Account List Report

**P159** The Executing/Servicing Party sends a query response that meets the specified criteria to the Instructing Party.

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000350-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000350-executing-servicing-party.md).
