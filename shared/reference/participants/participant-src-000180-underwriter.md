---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
participant_id: "participant-src-000180-underwriter"
title: "Underwriter"
source_labels: ["Underwriter"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000180", "heading_path": ["BusinessRoles and Participants"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[18]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Duplex Type"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[3]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Duplex Type"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[4]", "paragraph_id": null, "table_id": "T11"}]
flows: ["flow-src-000180-p153-own-account-trade-type", "flow-src-000180-p159-duplex-type", "flow-src-000180-p203-own-account-trade-type", "flow-src-000180-p208-own-account-trade-type-cancellation", "flow-src-000180-p214-duplex-type", "flow-src-000180-p218-duplex-type-rejection-by-transfer-agent", "flow-src-000180-p222-duplex-type-rejection-by-cash-correspondent"]
process_sections: ["flow-src-000180-p214-duplex-type", "flow-src-000180-p218-duplex-type-rejection-by-transfer-agent", "flow-src-000180-p222-duplex-type-rejection-by-cash-correspondent"]
message_ids: ["setr.027.001.05", "setr.029.001.02", "setr.044.001.04"]
message_families: []
search_terms: ["Underwriter"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---















# Underwriter

Business context: Post-Trade Matching. Source classification: business role.

## Definition

Company or other entity that administers the public issuance and distribution of securities from a corporation or other issuing body.

Evidence: [T7](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0007.md), source row 18.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Source activity row 3 | Confirmation: The Underwriter sends a trade confirmation to JASDEC.  | Underwriter | [T11](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0011.md) row 3 |
| Source activity row 4 | Cancel Confirmation: Should the parties decide, for whatever reason, to cancel the trade a cancellation of the confirmation is sent from the Underwriter to JASDEC. A new confirmation may be sent.<br> | Underwriter | [T11](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0011.md) row 4 |

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Instructing Party](participant-src-000180-instructing-party.md) | [T8](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0008.md) row 14, column 2 |
| Can play the functional participant role in this source context | [Executing/Servicing Party](participant-src-000180-executing-servicing-party.md) | [T8](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0008.md) row 14, column 3 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Own Account Trade Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p153-own-account-trade-type.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Duplex Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p159-duplex-type.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Duplex Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p214-duplex-type.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Duplex Type Rejection by Transfer Agent](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p218-duplex-type-rejection-by-transfer-agent.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Duplex Type Rejection by Cash Correspondent](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p222-duplex-type-rejection-by-cash-correspondent.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Underwriter`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000180](../../../raw-input/post_trade_matching/ISO20022_MDRPart1_PostTradeMatching_2024_2025_v2.docx).

Post-trade matching scenario: [Own Account Trade Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p203-own-account-trade-type.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0016.md). The source identifies this participant as an inactive lifeline or narrative alternative in this scenario.

Post-trade matching scenario: [Own Account Trade Type Cancellation](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p208-own-account-trade-type-cancellation.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0017.md). The source identifies this participant as an inactive lifeline or narrative alternative in this scenario.

Post-trade matching scenario: [Duplex Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p214-duplex-type.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0018.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Duplex Type Rejection by Transfer Agent](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p218-duplex-type-rejection-by-transfer-agent.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0019.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Duplex Type Rejection by Cash Correspondent](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p222-duplex-type-rejection-by-cash-correspondent.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0020.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Source context: [Own-account local matching activity](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0008.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p153-own-account-trade-type.md).

Source context: [Duplex local matching activity](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0009.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p159-duplex-type.md).
