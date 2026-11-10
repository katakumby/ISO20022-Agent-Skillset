---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000356"]
source_editions: ["march-2024"]
message_sets: ["t2s-collateral-reporting"]
participant_id: "participant-src-000356-system-transaction-administrator"
title: "System Transaction Administrator"
source_labels: ["System Transaction Administrator  ", "System Transaction Administrator"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000356", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[2]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000356", "heading_path": ["Description of BusinessActivities", "Query Management Process"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[3]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000356", "heading_path": ["Description of BusinessActivities", "Query Management Process"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[4]", "paragraph_id": null, "table_id": "T9"}]
flows: ["flow-src-000356-p138-query-management-process"]
process_sections: []
message_ids: ["colr.001.001.02", "colr.002.001.02"]
message_families: ["colr.001"]
search_terms: ["System Transaction Administrator", "colr.001"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---









# System Transaction Administrator

Business context: T2S CollateralReporting. Source classification: functional participant role.

## Definition

In a central system, the entity or neutral body, in charge of providing services to the system's members. It is in charge of performing specified tasks on behalf and under the responsibility of the system's direct members. It can be a matching engine, a settlement engine, or a financial institution. It also maintains accounts or netting balances for the direct members of the system, registers transactions, performs checks and validations, and manages the settlement cycle or other value added processes, as specified in the functional specifications of the system. 

Evidence: [T5](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/documents/src-000356/tables/tbl-0005.md), source row 2.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Rejection | Informs the instruction party (by error and description) in case if the instruction of a collateral value query was not valid for processing.<br>There could be three different reasons for a rejection message:<br>plausibility check not successful<br>permission check not successful<br>extracting process not successful | Initiator | [T9](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/documents/src-000356/tables/tbl-0009.md) row 3 |
| Response | Delivers the requested data, if available, to the infrastructure of the requesting system member Party of the completeness of this instruction. | Initiator | [T9](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/documents/src-000356/tables/tbl-0009.md) row 4 |

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [Settlement Infrastructure](participant-src-000356-settlement-infrastructure.md) | [T7](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/documents/src-000356/tables/tbl-0007.md) row 5, column 3 |
| Business role listed for this functional participant | [Executing/Servicing Party](participant-src-000356-executing-servicing-party.md) | [T7](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/documents/src-000356/tables/tbl-0007.md) row 8, column 3 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Query Management Process](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/flows/flow-src-000356-p138-query-management-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `colr.001`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `System Transaction Administrator`, `System Transaction Administrator`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000356](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralReporting_2023_2024_v2.docx`.

Collateral-reporting source context: [Collateral-query processing with data stores](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/diagrams/curated/fig-0003.md). [flow Query Management Process](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/flows/flow-src-000356-p138-query-management-process.md).

Collateral-reporting source context: [Collateral-query member and administrator activity](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/diagrams/curated/fig-0008.md). [flow Query Management Process](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/flows/flow-src-000356-p138-query-management-process.md).

Collateral-reporting source context: [Collateral-value communication overview](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/diagrams/curated/fig-0009.md). [flow Query Management Process](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/flows/flow-src-000356-p138-query-management-process.md).

Collateral-reporting source context: [Collateral-value query rejection or execution sequence](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/diagrams/curated/fig-0010.md). [flow Query Management Process](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/flows/flow-src-000356-p138-query-management-process.md).
