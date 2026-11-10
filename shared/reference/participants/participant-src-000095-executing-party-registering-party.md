---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
participant_id: "participant-src-000095-executing-party-registering-party"
title: "Executing Party / Registering Party"
source_labels: ["Executing Party / Registering Party"]
role_type: "activity participant; classification not established"
aliases: []
source_locations: [{"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Account Administration", "Account Opening"], "locator": "/w:document/w:body/w:tbl[37]/w:tr[3]", "paragraph_id": null, "table_id": "T37"}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Account Administration", "Account Opening"], "locator": "/w:document/w:body/w:tbl[37]/w:tr[5]", "paragraph_id": null, "table_id": "T37"}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Account Administration", "Account Modification"], "locator": "/w:document/w:body/w:tbl[38]/w:tr[3]", "paragraph_id": null, "table_id": "T38"}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Account Administration", "Account Modification"], "locator": "/w:document/w:body/w:tbl[38]/w:tr[5]", "paragraph_id": null, "table_id": "T38"}]
flows: ["flow-src-000095-p205-account-opening", "flow-src-000095-p207-account-modification"]
process_sections: []
message_ids: []
message_families: ["acmt.001", "acmt.003"]
search_terms: ["Executing Party / Registering Party", "acmt.001", "acmt.003"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000095-p205-account-opening", "flow-src-000095-p207-account-modification"]
---





# Executing Party / Registering Party

Business context: Investment Funds. Source classification: activity participant; classification not established.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Validate/Provide Status | The account opening instruction is validated, but if the account cannot be created immediately the executing party can send one or more status messages to the instructing party to keep it updated on progress so far. | Initiator | [T37](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0037.md) row 3 |
| Provide Confirmation | If the instruction is accepted by the executing party, the details of the successfully opened account are sent by the executing party to the instructing party. | Initiator | [T37](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0037.md) row 5 |
| Validate/Provide Status | The account modification instruction is validated and processed. The executing party can send one or more status messages to the instructing party to keep it updated on progress so far. | Initiator | [T38](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0038.md) row 3 |
| Provide Confirmation | If the instruction is accepted by the executing party, the details of the successfully modified account are sent by the executing party to the instructing party. | Initiator | [T38](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0038.md) row 5 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Account Opening](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p205-account-opening.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Account Modification](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p207-account-modification.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `acmt.001`, `acmt.003`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Executing Party / Registering Party`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000095](../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx).

<!-- FUNDS-PROCESS-fig-0009 -->
[Account Opening Flow](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0009.md) · [Flow responsibilities](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p205-account-opening.md)
<!-- /FUNDS-PROCESS-fig-0009 -->

<!-- FUNDS-PROCESS-fig-0010 -->
[Account Modification Flow](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0010.md) · [Flow responsibilities](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p207-account-modification.md)
<!-- /FUNDS-PROCESS-fig-0010 -->
