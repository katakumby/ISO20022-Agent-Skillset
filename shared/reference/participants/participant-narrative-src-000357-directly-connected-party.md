---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000357-directly-connected-party"
title: "Directly Connected Party — T2S CollateralReporting narrative scope"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
source_labels: ["directly connected party"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["t2s-collateral-reporting"]
message_ids: ["colr.001.001.02", "colr.002.001.02"]
message_families: ["colr.001", "colr.002"]
flows: []
source_locations: [{"source_id": "src-000357", "heading": "2 colr.001.001.02 CollateralValueQueryV02", "file_pages": [4], "evidence_id": "src-000357-colr.001.001.02-p4-c001"}, {"source_id": "src-000357", "heading": "3 colr.002.001.02 CollateralValueReportV02", "file_pages": [16], "evidence_id": "src-000357-colr.002.001.02-p16-c001"}]
search_terms: ["directly connected party"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Directly Connected Party — T2S CollateralReporting

## Definition and applicable context

This source names **directly connected party** in the Functionality of the messages listed below. The record is scoped to T2S CollateralReporting, march-2024. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The CollateralValueQuery message is sent by a system member (such as a directly connected party) to the system transaction administrator to query the current available value of securities for auto collateralisation for one specific or several cash accounts.

src-000357, file p4, 2 colr.001.001.02 CollateralValueQueryV02, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

No complete directed clause was assigned to this exact role label; the narrative evidence still establishes its stated context.

## Complete source evidence

<a id="src-000357-colr.001.001.02-p4-c001"></a>

### src-000357-colr.001.001.02-p4-c001

src-000357; file p4; 2 colr.001.001.02 CollateralValueQueryV02; scope.

> The CollateralValueQuery message is sent by a system member (such as a directly connected party) to the system transaction administrator to query the current available value of securities for auto collateralisation for one specific or several cash accounts.

<a id="src-000357-colr.002.001.02-p16-c001"></a>

### src-000357-colr.002.001.02-p16-c001

src-000357; file p16; 3 colr.002.001.02 CollateralValueReportV02; scope.

> The CollateralValueReport message is sent by the system transaction administrator to a system member (such as a directly connected party) to provide further information the current available value of securities for auto collateralisation for one specific or several cash accounts.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| colr.001.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/colr.001.001.02/roles.md) | src-000357-colr.001.001.02-p4-c001 |
| colr.002.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/colr.002.001.02/roles.md) | src-000357-colr.002.001.02-p16-c001 |


[Message-set flows](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `directly connected party`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000357](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf` · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
