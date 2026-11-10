---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
participant_id: "participant-src-000079-issuer-agent"
title: "Issuer Agent"
source_labels: ["Issuer Agent"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[6]", "paragraph_id": null, "table_id": "T9"}]
flows: []
process_sections: ["flow-src-000079-p201-business-transactions"]
message_ids: []
message_families: []
search_terms: ["Issuer Agent"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---

# Issuer Agent

Business context: Corporate Actions. Source classification: business role.

## Definition

Organisation appointed by the issuer for the purposes of administration of a security issue or processing of a corporate action or a meeting event. In some cases, the issuer acts as its own agent.

Evidence: [T9](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/documents/src-000079/tables/tbl-0009.md), source row 6.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [BusinessTransactions](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p201-business-transactions.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Issuer Agent`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000079](../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx).
