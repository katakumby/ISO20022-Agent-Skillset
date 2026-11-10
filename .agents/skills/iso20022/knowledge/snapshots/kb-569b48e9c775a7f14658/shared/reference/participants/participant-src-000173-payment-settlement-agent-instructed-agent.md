---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
participant_id: "participant-src-000173-payment-settlement-agent-instructed-agent"
title: "Payment Settlement Agent Instructed Agent)"
source_labels: ["Payment Settlement Agent Instructed Agent) "]
role_type: "functional participant role"
aliases: ["Instructed Agent", "Payment Settlement Agent"]
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[13]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000173", "locator": "T6 row13; T8 row13"}, {"source_id": "src-000173", "locator": "T8 row13"}]
flows: []
process_sections: []
message_ids: []
message_families: []
search_terms: ["Payment Settlement Agent Instructed Agent)"]
limitations: ["Scoped to supplied Payments Initiation source. Terminology conflict remains issue-000044.", "No cross-source equivalence or fixed institution/functional-role identity is inferred."]
issue_ids: ["issue-000044"]
manual_curated: true
definition_review: {"date": "2026-11-09", "result": "pass", "scope": "T6 definition/T8 mapping and cited narrative reviewed; classification ambiguity remains."}
---



# Payment Settlement Agent Instructed Agent)

Business context: Payments Initiation. Source classification: functional participant role.

## Definition

Agent that executes the instruction upon the request of the previous party in the chain (either an agreement party, or a clearing agent). 

Evidence: [T6](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/documents/src-000173/tables/tbl-0006.md), source row 13.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Payment Settlement Agent Instructed Agent)`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000173](../../../evidence/omitted/baf7abf3460122a33db6052d.md).

<!-- INITIATION-ROLE-REVIEW -->
## Curated responsibilities and role relationships

Executes instruction at request of previous party, which may be agreement party or clearing agent. T6 literal label is Payment Settlement Agent Instructed Agent), with missing opening parenthesis. (T6 row13; T8 row13)

T8 row13 marks the participant under: BusinessRole / Financial Institution, BusinessRole / Clearing System. This source mapping does not make the functional participant identical to a particular institution.

T1 and P98–100 use BusinessRole/Participant terminology inconsistently (issue-000044). The literal T6 definitions and T8 mapping are preserved. No identifier scheme is asserted beyond a source requirement.
<!-- /INITIATION-ROLE-REVIEW -->
