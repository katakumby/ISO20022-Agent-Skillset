---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000197-designated-agent"
title: "Designated Agent — Settlement and Reconciliation narrative scope"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
source_labels: ["designated agent"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["settlement-and-reconciliation"]
message_ids: ["semt.002.001.12", "semt.003.001.12"]
message_families: ["semt.002", "semt.003"]
flows: []
source_locations: [{"source_id": "src-000197", "heading": "2 semt.002.001.12 SecuritiesBalanceCustodyReportV12", "file_pages": [19], "evidence_id": "src-000197-semt.002.001.12-p19-c006"}, {"source_id": "src-000197", "heading": "3 semt.003.001.12 SecuritiesBalanceAccountingReportV12", "file_pages": [78], "evidence_id": "src-000197-semt.003.001.12-p78-c004"}]
search_terms: ["designated agent"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Designated Agent — Settlement and Reconciliation

## Definition and applicable context

This source names **designated agent** in the Functionality of the messages listed below. The record is scoped to Settlement and Reconciliation, March 2026. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> a transfer agent acting on behalf of a fund manager or an account owner's designated agent.

src-000197, file p19, 2 semt.002.001.12 SecuritiesBalanceCustodyReportV12, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

No complete directed clause was assigned to this exact role label; the narrative evidence still establishes its stated context.

## Complete source evidence

<a id="src-000197-semt.002.001.12-p19-c006"></a>

### src-000197-semt.002.001.12-p19-c006

src-000197; file p19; 2 semt.002.001.12 SecuritiesBalanceCustodyReportV12; scope.

> a transfer agent acting on behalf of a fund manager or an account owner's designated agent.

<a id="src-000197-semt.003.001.12-p78-c004"></a>

### src-000197-semt.003.001.12-p78-c004

src-000197; file p78; 3 semt.003.001.12 SecuritiesBalanceAccountingReportV12; scope.

> a transfer agent acting on behalf of a fund manager or an account owner's designated agent.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| semt.002.001.12 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.002.001.12/roles.md) | src-000197-semt.002.001.12-p19-c006 |
| semt.003.001.12 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.003.001.12/roles.md) | src-000197-semt.003.001.12-p78-c004 |


[Message-set flows](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `designated agent`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000197](../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf) · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
