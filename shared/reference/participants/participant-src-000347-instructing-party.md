---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000347"]
source_editions: ["december-2025"]
message_sets: ["t2s-billing"]
participant_id: "participant-src-000347-instructing-party"
title: "Instructing Party"
source_labels: ["Instructing Party"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000347", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[2]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000347", "heading_path": ["Description of BusinessActivities", "Billing", "Query Billing Information"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[2]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000347", "heading_path": ["Description of BusinessActivities", "Billing", "Query Billing Information"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[6]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000347", "heading_path": ["Description of BusinessActivities", "Billing", "Billing Report"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[4]", "paragraph_id": null, "table_id": "T11"}]
flows: ["flow-src-000347-p110-billing-report", "flow-src-000347-p116-query-billing-information", "flow-src-000347-p121-billing-report", "flow-src-000347-p129-positive-scenario", "flow-src-000347-p142-negative-scenario", "flow-src-000347-p156-billing-report"]
process_sections: ["flow-src-000347-p129-positive-scenario", "flow-src-000347-p134-billing-report-request", "flow-src-000347-p142-negative-scenario", "flow-src-000347-p147-billing-report-request", "flow-src-000347-p160-billing-report"]
message_ids: ["camt.076.001.01", "camt.077.001.01"]
message_families: ["camt.076", "camt.077"]
search_terms: ["Instructing Party", "camt.076", "camt.077"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---















# Instructing Party

Business context: T2S Billing. Source classification: functional participant role.

## Definition

Party that instructs the executing/servicing party to process and monitor a transaction and receives reports and communications from executing/servicing party.

Evidence: [T5](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/documents/src-000347/tables/tbl-0005.md), source row 2.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Process Request Billing Data | Instruct the Executing/Servicing Party to return: <br>• Cumulative Billing Data<br>• Itemised Billing Data | Initiator | [T10](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/documents/src-000347/tables/tbl-0010.md) row 2 |
| Process Billing Data / Process Handle Error | Instructing Party monitors the status of the instruction. | Initiator | [T10](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/documents/src-000347/tables/tbl-0010.md) row 6 |
| Process Receive Invoice / Process Receive Invoice Cancellation | Instructing Party monitors the status of the generation of the invoice/invoice cancellation. | Initiator | [T11](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/documents/src-000347/tables/tbl-0011.md) row 4 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Query Billing Information](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p116-query-billing-information.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Billing Report](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p121-billing-report.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Positive Scenario](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p129-positive-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Billing Report Request](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p134-billing-report-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Negative Scenario](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p142-negative-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Billing Report Request](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p147-billing-report-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Billing Report](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p160-billing-report.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `camt.076`, `camt.077`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Instructing Party`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000347](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v2.docx`.

Billing source context: [Billing business roles and functional participants](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0001.md). Source role-matrix inconsistency remains open under issue-000038.

Billing source context: [Billing process overview](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0002.md). [Reusable flow](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p110-billing-report.md).

Billing source context: [Query billing information activity](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0007.md). [Reusable flow](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p116-query-billing-information.md).

Billing source context: [Billing report activity](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0008.md). [Reusable flow](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p121-billing-report.md).

Billing source context: [Successful billing information query](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0009.md). [Reusable flow](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p129-positive-scenario.md).

Billing source context: [Rejected billing information query](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0010.md). [Reusable flow](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p142-negative-scenario.md).

Billing source context: [Billing report push sequence](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0011.md). [Reusable flow](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p156-billing-report.md).
