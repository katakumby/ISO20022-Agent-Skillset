---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000356"]
source_editions: ["march-2024"]
message_sets: ["t2s-collateral-reporting"]
participant_id: "participant-src-000356-system-member"
title: "System Member"
source_labels: ["System Member"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000356", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000356", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[10]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000356", "heading_path": ["Description of BusinessActivities", "Query Management Process"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[2]", "paragraph_id": null, "table_id": "T9"}]
flows: ["flow-src-000356-p138-query-management-process"]
process_sections: []
message_ids: ["colr.001.001.02", "colr.002.001.02"]
message_families: ["colr.001"]
search_terms: ["System Member", "colr.001"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---











# System Member

Business context: T2S CollateralReporting. Source classification: functional participant role.

## Definition

The party that is entitled to make full or partial use of the system transaction administrator, to make it perform business processes on its behalf. A member can submit transactions, and request and/or receive information. A member can be a direct or indirect member.

Evidence: [T5](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/documents/src-000356/tables/tbl-0005.md), source row 3.

The party that is entitled to make full or partial use of the system transaction administrator, to make it perform business processes on its behalf. A member can submit transactions, and request and/or receive information. A member can be a direct or indirect member.

Evidence: [T6](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/documents/src-000356/tables/tbl-0006.md), source row 10.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Query<br> | Request for Information concerning collateral values on a specific account | Initiator | [T9](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/documents/src-000356/tables/tbl-0009.md) row 2 |

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [T2S operator](participant-src-000356-t2s-operator.md) | [T7](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/documents/src-000356/tables/tbl-0007.md) row 2, column 2 |
| Business role listed for this functional participant | [National Central Bank](participant-src-000356-national-central-bank.md) | [T7](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/documents/src-000356/tables/tbl-0007.md) row 3, column 2 |
| Business role listed for this functional participant | [Payment Bank](participant-src-000356-payment-bank.md) | [T7](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/documents/src-000356/tables/tbl-0007.md) row 4, column 2 |
| Business role listed for this functional participant | [Settlement Infrastructure Direct Participant](participant-src-000356-settlement-infrastructure-direct-participant.md) | [T7](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/documents/src-000356/tables/tbl-0007.md) row 6, column 2 |
| Business role listed for this functional participant | [Instructing Party](participant-src-000356-instructing-party.md) | [T7](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/documents/src-000356/tables/tbl-0007.md) row 7, column 2 |
| Business role listed for this functional participant | [Executing/Servicing Party](participant-src-000356-executing-servicing-party.md) | [T7](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/documents/src-000356/tables/tbl-0007.md) row 8, column 2 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Query Management Process](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/flows/flow-src-000356-p138-query-management-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `colr.001`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `System Member`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000356](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralReporting_2023_2024_v2.docx`.

Collateral-reporting source context: [Collateral-query processing with data stores](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/diagrams/curated/fig-0003.md). [flow Query Management Process](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/flows/flow-src-000356-p138-query-management-process.md).

Collateral-reporting source context: [Collateral-query member and administrator activity](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/diagrams/curated/fig-0008.md). [flow Query Management Process](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/flows/flow-src-000356-p138-query-management-process.md).

Collateral-reporting source context: [Collateral-value communication overview](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/diagrams/curated/fig-0009.md). [flow Query Management Process](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/flows/flow-src-000356-p138-query-management-process.md).

Collateral-reporting source context: [Collateral-value query rejection or execution sequence](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/diagrams/curated/fig-0010.md). [flow Query Management Process](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/flows/flow-src-000356-p138-query-management-process.md).

Classification nuance: T5 defines System Member as a participant, while T6 repeats that definition in Business Roles and labels Instructing/Executing parties there. T7 supplies the explicit mappings. These source classifications are preserved as context, not collapsed into an institution identity.
