---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
participant_id: "participant-src-000180-institutional-investor-issuer-agent"
title: "Institutional Investor/Issuer Agent"
source_labels: ["Institutional Investor/Issuer Agent"]
role_type: "activity participant named in responsibility column"
aliases: []
source_locations: [{"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Own Account Trade Type"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[6]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Own Account Trade Type"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[7]", "paragraph_id": null, "table_id": "T10"}]
flows: ["flow-src-000180-p153-own-account-trade-type"]
process_sections: []
message_ids: []
message_families: []
search_terms: ["Institutional Investor/Issuer Agent"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---

# Institutional Investor/Issuer Agent

Business context: Post-Trade Matching. Source classification: activity participant named in responsibility column.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Source activity row 6 | Disaffirmation: The Institutional Investor or Issuer Agent will compare the details of the confirmation with their details of the trade. If the details are irreconcilable, a disaffirmation message will be sent to JASDEC. | Institutional Investor/Issuer Agent | [T10](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0010.md) row 6 |
| Source activity row 7 | Affirmation: Should the Institutional Investor or Issuer Agent agree with the detail of the confirmation an affirmation message is sent to JASDEC.  The message will bind the parties to the trade details of the confirmation being affirmed. | Institutional Investor/Issuer Agent | [T10](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0010.md) row 7 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Own Account Trade Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p153-own-account-trade-type.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Institutional Investor/Issuer Agent`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000180](../../../evidence/omitted/620693d01e301c06503cea9a.md).
