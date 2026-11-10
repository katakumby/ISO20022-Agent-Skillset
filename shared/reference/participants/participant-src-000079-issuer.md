---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
participant_id: "participant-src-000079-issuer"
title: "Issuer"
source_labels: ["Issuer"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[5]", "paragraph_id": null, "table_id": "T9"}]
flows: ["flow-src-000079-p170-mandatory-reorganisation-without-options", "flow-src-000079-p173-mandatory-reorganisation-with-options", "flow-src-000079-p195-corporate-action-event-withdrawal-process", "flow-src-000079-p217-announcement-and-cancellation-of-event", "flow-src-000079-p229-final-entitlement-replacement-scenario"]
process_sections: ["flow-src-000079-p217-announcement-and-cancellation-of-event", "flow-src-000079-p229-final-entitlement-replacement-scenario"]
message_ids: []
message_families: ["seev.031", "seev.035", "seev.039"]
search_terms: ["Issuer", "seev.031", "seev.035", "seev.039"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---









# Issuer

Business context: Corporate Actions. Source classification: business role.

## Definition

Legal Entity that has the right to issue securities

Evidence: [T9](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/documents/src-000079/tables/tbl-0009.md), source row 5.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Corporate Action Event Withdrawal Process](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p195-corporate-action-event-withdrawal-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Announcement and Cancellation of Event](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p217-announcement-and-cancellation-of-event.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Final Entitlement Replacement Scenario](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p229-final-entitlement-replacement-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `seev.031`, `seev.035`, `seev.039`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Issuer`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000079](../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx).

Related source activity flow: [Mandatory Reorganisation without Options](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p170-mandatory-reorganisation-without-options.md).

Related source activity flow: [Mandatory Reorganisation with Options](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p173-mandatory-reorganisation-with-options.md).
