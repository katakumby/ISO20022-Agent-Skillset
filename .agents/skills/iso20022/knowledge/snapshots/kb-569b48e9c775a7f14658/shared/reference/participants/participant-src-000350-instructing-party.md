---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000350"]
source_editions: ["august-2026"]
message_sets: ["t2s-cash-account-query-and-report"]
participant_id: "participant-src-000350-instructing-party"
title: "Instructing Party"
source_labels: ["Instructing Party"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000350", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[2]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000350", "heading_path": ["Description of BusinessActivities", "Cash Account Query and Report", "Account Query List - Account List Response process"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[2]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000350", "heading_path": ["Description of BusinessActivities", "Cash Account Query and Report", "Account Query List - Account List Response process"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[5]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000350", "heading_path": ["Description of BusinessActivities", "Cash Account Query and Report", "Cash Account Activity Advice process"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[2]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000350", "heading_path": ["Description of BusinessActivities", "Cash Account Query and Report", "Cash Account Activity Advice process"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[5]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000350", "heading_path": ["Description of BusinessActivities", "Cash Account Query and Report", "Cash Account Audit Trail Query/Response process"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[2]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000350", "heading_path": ["Description of BusinessActivities", "Cash Account Query and Report", "Cash Account Audit Trail Query/Response process"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[5]", "paragraph_id": null, "table_id": "T14"}]
flows: ["flow-src-000350-p123-account-query-list", "flow-src-000350-p124-cash-account-audit-trail-query", "flow-src-000350-p125-cash-account-activity-advice", "flow-src-000350-p130-account-query-list-account-list-response-process", "flow-src-000350-p135-cash-account-activity-advice-process", "flow-src-000350-p140-cash-account-audit-trail-query-response-process", "flow-src-000350-p148-account-query-list-report-scenario", "flow-src-000350-p161-cash-account-activity-advice-process", "flow-src-000350-p166-cash-account-audit-trail-query-report-scenario"]
process_sections: ["flow-src-000350-p148-account-query-list-report-scenario", "flow-src-000350-p161-cash-account-activity-advice-process", "flow-src-000350-p166-cash-account-audit-trail-query-report-scenario"]
message_ids: ["acmt.025.001.02", "acmt.026.001.02", "reda.038.001.01", "reda.039.001.01", "reda.040.001.01"]
message_families: ["acmt.025", "acmt.026", "reda.038", "reda.039"]
search_terms: ["Instructing Party", "acmt.025", "acmt.026", "reda.038", "reda.039"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---















# Instructing Party

Business context: T2S CashAccountQueryAndReport. Source classification: functional participant role.

## Definition

Party that instructs the executing/servicing party to process and monitor a transaction.

Evidence: [T5](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000350/tables/tbl-0005.md), source row 2.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Instruction | Instructing Party instructs Executing/Servicing Party to run an Account query. | Initiator | [T12](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000350/tables/tbl-0012.md) row 2 |
| Monitor | Instructing Party monitors the status of the instruction | Initiator | [T12](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000350/tables/tbl-0012.md) row 5 |
| Instruction | Instructing Party might instruct Executing/Servicing Party to run a statement.<br>This is not covered by the current process as NO message will be created to cover this. | Initiator | [T13](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000350/tables/tbl-0013.md) row 2 |
| Monitor | Instructing Party monitors the status of the instruction | Initiator | [T13](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000350/tables/tbl-0013.md) row 5 |
| Instruction | Instructing Party instructs Executing/Servicing Party to run a Cash Account Audit Trail query. | Initiator | [T14](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000350/tables/tbl-0014.md) row 2 |
| Monitor | Instructing Party monitors the status of the instruction | Initiator | [T14](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000350/tables/tbl-0014.md) row 5 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Account Query List](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p123-account-query-list.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Cash Account Audit Trail Query](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p124-cash-account-audit-trail-query.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Account Query List - Account List Response process](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p130-account-query-list-account-list-response-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Cash Account Activity Advice process](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p135-cash-account-activity-advice-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Cash Account Audit Trail Query/Response process](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p140-cash-account-audit-trail-query-response-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Account Query List/Report Scenario](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p148-account-query-list-report-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Cash Account Activity Advice Process](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p161-cash-account-activity-advice-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Cash Account Audit Trail Query/ Report Scenario](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p166-cash-account-audit-trail-query-report-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `acmt.025`, `acmt.026`, `reda.038`, `reda.039`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Instructing Party`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000350](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart1_Target2Securities_CashAccountQueryAndReport_v2.docx`.

Cash-account source context: [Cash account business-role context](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/diagrams/curated/fig-0001.md). .

Cash-account source context: [Cash account query, report and advice overview](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/diagrams/curated/fig-0002.md). [flow Account Query List](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p123-account-query-list.md), [flow Cash Account Audit Trail Query](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p124-cash-account-audit-trail-query.md), [flow Cash Account Activity Advice](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p125-cash-account-activity-advice.md).

Cash-account source context: [Cash account query/response activity reused in two processes](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/diagrams/curated/fig-0007.md). [flow Account Query List - Account List Response process](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p130-account-query-list-account-list-response-process.md), [flow Cash Account Audit Trail Query/Response process](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p140-cash-account-audit-trail-query-response-process.md).

Cash-account source context: [Cash account activity advice activity](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/diagrams/curated/fig-0008.md). [flow Cash Account Activity Advice process](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p135-cash-account-activity-advice-process.md).

Cash-account source context: [Account query/list sequence](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/diagrams/curated/fig-0010.md). [flow Account Query List/Report Scenario](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p148-account-query-list-report-scenario.md).

Cash-account source context: [Cash account audit-trail query/response sequence](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/diagrams/curated/fig-0012.md). [flow Cash Account Audit Trail Query/ Report Scenario](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p166-cash-account-audit-trail-query-report-scenario.md).

Cash-account source context: [Cash account activity advice push sequence](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/diagrams/curated/fig-0011.md). [flow Cash Account Activity Advice Process](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p161-cash-account-activity-advice-process.md).
