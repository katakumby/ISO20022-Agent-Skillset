---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "shared"
source_ids: ["src-000343"]
source_editions: ["march-2024"]
message_sets: ["t2s-administration"]
participant_id: "participant-src-000343-payment-bank"
title: "Payment Bank"
source_labels: ["Payment Bank"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000343", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[11]", "paragraph_id": null, "table_id": "T6"}]
flows: ["flow-src-000343-p149-report-query-request-admi-005", "flow-src-000343-p154-resend-request-admi-006"]
process_sections: []
message_ids: []
message_families: ["admi.005", "admi.006"]
search_terms: ["Payment Bank", "admi.005", "admi.006"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---

# Payment Bank

Business context: T2S Administration. Source classification: business role.

## Definition

The payment bank role includes all T2S system users of payment banks that require access to the T2S dedicated cash account balances and postings of the T2S dedicated cash accounts they provide for the purpose of securities settlement.

Evidence: [T6](../message-sets/t2s-administration/march-2024/documents/src-000343/tables/tbl-0006.md), source row 11.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [System Member](participant-src-000343-system-member.md) | [T7](../message-sets/t2s-administration/march-2024/documents/src-000343/tables/tbl-0007.md) row 4, column 2 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Report Query Request (admi.005)](../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p149-report-query-request-admi-005.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Resend Request (admi.006)](../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p154-resend-request-admi-006.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `admi.005`, `admi.006`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Payment Bank`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000343](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart1_Target2Securities_Administration_2023_2024_v2.docx`.
