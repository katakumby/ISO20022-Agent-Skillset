---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000347"]
source_editions: ["december-2025"]
message_sets: ["t2s-billing"]
participant_id: "participant-src-000347-executing-servicing-party"
title: "Executing / Servicing Party"
source_labels: ["Executing / Servicing Party", "Executing/Servicing Party"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000347", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000347", "heading_path": ["Description of BusinessActivities", "Billing", "Query Billing Information"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[3]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000347", "heading_path": ["Description of BusinessActivities", "Billing", "Query Billing Information"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[4]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000347", "heading_path": ["Description of BusinessActivities", "Billing", "Query Billing Information"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[5]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000347", "heading_path": ["Description of BusinessActivities", "Billing", "Billing Report"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[2]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000347", "heading_path": ["Description of BusinessActivities", "Billing", "Billing Report"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[3]", "paragraph_id": null, "table_id": "T11"}]
flows: ["flow-src-000347-p110-billing-report", "flow-src-000347-p116-query-billing-information", "flow-src-000347-p121-billing-report", "flow-src-000347-p129-positive-scenario", "flow-src-000347-p142-negative-scenario", "flow-src-000347-p156-billing-report"]
process_sections: ["flow-src-000347-p129-positive-scenario", "flow-src-000347-p134-billing-report-request", "flow-src-000347-p142-negative-scenario", "flow-src-000347-p147-billing-report-request", "flow-src-000347-p156-billing-report", "flow-src-000347-p160-billing-report"]
message_ids: ["camt.076.001.01", "camt.077.001.01"]
message_families: ["camt.076", "camt.077"]
search_terms: ["Executing / Servicing Party", "camt.076", "camt.077"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---















# Executing / Servicing Party

Business context: T2S Billing. Source classification: functional participant role.

## Definition

Party that processes, monitors and reports on transactions received from the Instructing party and sends reports and communications to instructing party.

Evidence: [T5](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/documents/src-000347/tables/tbl-0005.md), source row 3.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Validate | Executing/Servicing Party system checks if this instruction is a new occurrence or not. <br>It also checks if this instruction is already handled or not.<br>If validation of the message fails, a status message “REJECTED” will be sent including the related errors and reason information. | Initiator | [T10](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/documents/src-000347/tables/tbl-0010.md) row 3 |
| Process | If the instruction is accepted, the Executing/Servicing Party processes the instruction and return the requested information to the Instructing Party. | Initiator | [T10](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/documents/src-000347/tables/tbl-0010.md) row 4 |
| Process Generate Error | Executing/Servicing Party informs the Instructing Party that this instruction is rejected and why. | Initiator | [T10](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/documents/src-000347/tables/tbl-0010.md) row 5 |
| Process Check Event | Executing/Servicing Party system checks if the event for the generation of billing data is reached.  | Initiator | [T11](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/documents/src-000347/tables/tbl-0011.md) row 2 |
| Process Generate Invoice, Generate Invoice Cancellation and Deliver | If the event is reached, the Executing/Servicing Party processes the invoice data and return the generated billing information to the Instructing Party.<br>This process is triggered periodically to return invoices to all subscribed Instructing Parties.  | Initiator | [T11](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/documents/src-000347/tables/tbl-0011.md) row 3 |

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
| [Billing Report](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p156-billing-report.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Billing Report](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p160-billing-report.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `camt.076`, `camt.077`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Executing / Servicing Party`, `Executing/Servicing Party`. No external identifier scheme or alias equivalence has been inferred.

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
