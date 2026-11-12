---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
participant_id: "participant-src-000320-arm"
title: "ARM"
source_labels: ["ARM"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[11]", "paragraph_id": null, "table_id": "T11"}]
flows: ["flow-src-000320-p137-transaction-reporting-messages"]
process_sections: []
message_ids: []
message_families: []
search_terms: ["ARM"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: []
---

# ARM

Business context: Transactions and Financial Instruments Data Reporting. Source classification: business role.

## Definition

Approved Reporting Mechanism is a person authorised under the MiFID II Directive (DIRECTIVE 2014/65/EU) to provide the service of reporting details of transactions to domestic competent authorities or ESMA on behalf of investment firms.

Evidence: [T11](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0011.md), source row 11.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Reporting Entity](participant-src-000320-reporting-entity.md) | [T12](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0012.md) row 9, column 2 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Transaction Reporting Messages](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p137-transaction-reporting-messages.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `ARM`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000320](../../../evidence/omitted/b0e9dc6419046e4d0523e995.md).



<!-- FITRR-ACTIVITY-1 -->
[Business roles and functional participants — source notation](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0001.md)
<!-- /FITRR-ACTIVITY-1 -->
