---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
participant_id: "participant-src-000320-esma"
title: "ESMA"
source_labels: ["ESMA"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[2]", "paragraph_id": null, "table_id": "T11"}]
flows: ["flow-src-000320-p127-reference-data", "flow-src-000320-p131-transparency-data"]
process_sections: ["flow-src-000320-p198-data-distribution-business-transaction"]
message_ids: []
message_families: []
search_terms: ["ESMA"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---

# ESMA

Business context: Transactions and Financial Instruments Data Reporting. Source classification: business role.

## Definition

European Securities and Markets Authority 
A Supervisory Authority performing regulatory tasks.
In some specific cases, ESMA also undertakes regulatory tasks that have been delegated by some National Competent Authorities (such as direct collection of data from reporting entities, as well as transparency calculations).

Evidence: [T11](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0011.md), source row 2.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Supervisory Authority](participant-src-000320-supervisory-authority.md) | [T12](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0012.md) row 11, column 4 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Reference Data](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p127-reference-data.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transparency Data](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p131-transparency-data.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Data Distribution BusinessTransaction](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p198-data-distribution-business-transaction.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `ESMA`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000320](../../../evidence/omitted/b0e9dc6419046e4d0523e995.md).
