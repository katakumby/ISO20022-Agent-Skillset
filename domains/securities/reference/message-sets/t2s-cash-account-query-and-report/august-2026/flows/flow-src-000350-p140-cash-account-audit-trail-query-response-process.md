---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000350"]
source_editions: ["august-2026"]
message_sets: ["t2s-cash-account-query-and-report"]
flow_id: "flow-src-000350-p140-cash-account-audit-trail-query-response-process"
title: "Cash Account Audit Trail Query/Response process"
source_locations: [{"source_id": "src-000350", "heading_path": ["Description of BusinessActivities", "Cash Account Query and Report", "Cash Account Audit Trail Query/Response process"], "locator": "/w:document/w:body/w:p[140]", "paragraph_id": "P140", "table_id": null}, {"source_id": "src-000350", "heading_path": ["Description of BusinessActivities", "Cash Account Query and Report", "Cash Account Audit Trail Query/Response process"], "locator": "/w:document/w:body/w:p[141]", "paragraph_id": "P141", "table_id": null}, {"source_id": "src-000350", "heading_path": ["Description of BusinessActivities", "Cash Account Query and Report", "Cash Account Audit Trail Query/Response process"], "locator": "/w:document/w:body/w:p[142]", "paragraph_id": "P142", "table_id": null}, {"source_id": "src-000350", "heading_path": ["Description of BusinessActivities", "Cash Account Query and Report", "Cash Account Audit Trail Query/Response process"], "locator": "/w:document/w:body/w:tbl[14]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000350", "heading_path": ["Description of BusinessActivities", "Cash Account Query and Report", "Cash Account Audit Trail Query/Response process"], "locator": "/w:document/w:body/w:p[143]", "paragraph_id": "P143", "table_id": null}, {"source_id": "src-000350", "heading_path": ["Description of BusinessActivities", "Cash Account Query and Report", "Cash Account Audit Trail Query/Response process"], "locator": "/w:document/w:body/w:p[144]", "paragraph_id": "P144", "table_id": null}]
participants: ["participant-src-000350-executing-servicing-party", "participant-src-000350-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000350", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Cash Account Query and report"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.039.001.01", "reda.040.001.01"]
message_families: ["reda.039", "reda.040"]
search_terms: ["Cash Account Audit Trail Query/Response process", "Executing / Servicing Party", "Instructing Party", "reda.039"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
---





# Cash Account Audit Trail Query/Response process

Source context: T2S CashAccountQueryAndReport. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000350-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000350-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0009](../documents/src-000350/diagrams/fig-0009.md). A canonical source reconstruction and actual review evidence are linked below.

Source table [T14](../documents/src-000350/tables/tbl-0014.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Instruction | Instructing Party instructs Executing/Servicing Party to run a Cash Account Audit Trail query. | Instructing Party |
| Process Query | Executing/Servicing Party processes the request.<br>In case the processing of the query takes too much time or cannot give any positive response, the Executing/Servicing Party sends an error message back to the Instructing Party with the error code and the related explanation. | Executing/Servicing Party |
| Response | Executing/Servicing Party sends the response to the Instructing Party according to query results. | Executing/Servicing Party |
| Monitor | Instructing Party monitors the status of the instruction | Instructing Party |

## Messages and alternative paths

Source-supported message family mentions: `reda.039`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000350](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart1_Target2Securities_CashAccountQueryAndReport_v2.docx`. Heading path: Description of BusinessActivities / Cash Account Query and Report / Cash Account Audit Trail Query/Response process.

## Curated source flow

Instructing Party Instruction goes to Executing Party Process Query, followed by Response returning to Instructing Party Monitor. This exact source media is reused at P132 for Account Query List and P141 for Cash Account Audit Trail Query/Response. T12 and T14 retain separate business scope while sharing these four actions. Excessive processing time or inability to provide a positive response causes an error with code and explanation; those narrative alternatives are not drawn as separate branches here. No extra decision is invented.

[Complete source diagram](../diagrams/curated/fig-0007.md).

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000350-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000350-executing-servicing-party.md).

Exact definitions applicable to this flow: [reda.039.001.01](../../../../messages/reda.039.001.01/index.md), [reda.040.001.01](../../../../messages/reda.040.001.01/index.md). Other messages in the shared overview belong to their separately linked processes.
