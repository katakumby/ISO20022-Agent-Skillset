---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
message_sets: ["t2s-link-reference-data"]
participant_id: "participant-src-000365-csd"
title: "CSD"
source_labels: ["CSD"]
role_type: "business role (matrix label; definition not extracted)"
aliases: []
source_locations: []
flows: []
process_sections: ["flow-src-000365-p177-confirmation-scenario", "flow-src-000365-p197-rejection-scenario"]
message_ids: []
message_families: ["reda.046", "reda.047", "reda.050", "reda.051"]
search_terms: ["CSD", "reda.046", "reda.047", "reda.050", "reda.051"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---

# CSD

Business context: T2S LinkReferenceData. Source classification: business role (matrix label; definition not extracted).

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Instructing Party](participant-src-000365-instructing-party.md) | [T7](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/documents/src-000365/tables/tbl-0007.md) row 5, column 2 |
| Can play the functional participant role in this source context | [Executing / Servicing Party](participant-src-000365-executing-servicing-party.md) | [T7](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/documents/src-000365/tables/tbl-0007.md) row 5, column 3 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Confirmation Scenario](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p177-confirmation-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Rejection Scenario](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p197-rejection-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `reda.046`, `reda.047`, `reda.050`, `reda.051`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `CSD`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000365](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`.
