---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000350"]
source_editions: ["august-2026"]
message_sets: ["t2s-cash-account-query-and-report"]
flow_id: "flow-src-000350-p135-cash-account-activity-advice-process"
title: "Cash Account Activity Advice process"
source_locations: [{"source_id": "src-000350", "heading_path": ["Description of BusinessActivities", "Cash Account Query and Report", "Cash Account Activity Advice process"], "locator": "/w:document/w:body/w:p[135]", "paragraph_id": "P135", "table_id": null}, {"source_id": "src-000350", "heading_path": ["Description of BusinessActivities", "Cash Account Query and Report", "Cash Account Activity Advice process"], "locator": "/w:document/w:body/w:p[136]", "paragraph_id": "P136", "table_id": null}, {"source_id": "src-000350", "heading_path": ["Description of BusinessActivities", "Cash Account Query and Report", "Cash Account Activity Advice process"], "locator": "/w:document/w:body/w:p[137]", "paragraph_id": "P137", "table_id": null}, {"source_id": "src-000350", "heading_path": ["Description of BusinessActivities", "Cash Account Query and Report", "Cash Account Activity Advice process"], "locator": "/w:document/w:body/w:p[138]", "paragraph_id": "P138", "table_id": null}, {"source_id": "src-000350", "heading_path": ["Description of BusinessActivities", "Cash Account Query and Report", "Cash Account Activity Advice process"], "locator": "/w:document/w:body/w:tbl[13]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000350", "heading_path": ["Description of BusinessActivities", "Cash Account Query and Report", "Cash Account Activity Advice process"], "locator": "/w:document/w:body/w:p[139]", "paragraph_id": "P139", "table_id": null}]
participants: ["participant-src-000350-executing-servicing-party", "participant-src-000350-instructing-party", "participant-src-000350-recipient-party"]
message_mapping_evidence: [{"source_id": "src-000350", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Cash Account Query and report"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.038.001.01"]
message_families: ["reda.038"]
search_terms: ["Cash Account Activity Advice process", "Executing / Servicing Party", "Instructing Party", "reda.038"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
---



# Cash Account Activity Advice process

Source context: T2S CashAccountQueryAndReport. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000350-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000350-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0008](../documents/src-000350/diagrams/fig-0008.md). A canonical source reconstruction and actual review evidence are linked below.

Source table [T13](../documents/src-000350/tables/tbl-0013.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Instruction | Instructing Party might instruct Executing/Servicing Party to run a statement.<br>This is not covered by the current process as NO message will be created to cover this. | Instructing Party |
| Process Statement | Executing/Servicing Party processes the statement. | Executing/Servicing Party |
| Reporting | Executing/Servicing Party sends the statement to the Instructing Party. | Executing/Servicing Party |
| Monitor | Instructing Party monitors the status of the instruction | Instructing Party |

## Messages and alternative paths

Source-supported message family mentions: `reda.038`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000350](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart1_Target2Securities_CashAccountQueryAndReport_v2.docx`. Heading path: Description of BusinessActivities / Cash Account Query and Report / Cash Account Activity Advice process.

## Curated source flow

The source activity includes an Instruction arrow to Process Statement, then Reporting back to Monitor. T13 explicitly says a request to run a statement is outside the current process and NO message will be created for it. T10 supplies the actual standing-instruction precondition and automatic trigger, and P95/P164 says advice is pushed unilaterally to subscribing parties. The diagram is reconstructed as drawn while that scope exclusion remains explicit; no request message is invented.

[Complete source diagram](../diagrams/curated/fig-0008.md).

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000350-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000350-executing-servicing-party.md), [recipient party](../../../../../../../shared/reference/participants/participant-src-000350-recipient-party.md).
