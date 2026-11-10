---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000375-third-party"
title: "Third Party — T2S SecuritiesAndPenaltyReporting narrative scope"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
source_labels: ["third party"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["t2s-securities-and-penalty-reporting"]
message_ids: ["semt.025.001.01", "semt.040.001.01"]
message_families: ["semt.025", "semt.040"]
flows: []
source_locations: [{"source_id": "src-000375", "heading": "2 semt.025.001.01 SecuritiesAccountPositionQueryV01", "file_pages": [5], "evidence_id": "src-000375-semt.025.001.01-p5-c003"}, {"source_id": "src-000375", "heading": "5 semt.040.001.01 SecuritiesAccountPositionResponseV01", "file_pages": [166], "evidence_id": "src-000375-semt.040.001.01-p166-c006"}, {"source_id": "src-000375", "heading": "5 semt.040.001.01 SecuritiesAccountPositionResponseV01", "file_pages": [166], "evidence_id": "src-000375-semt.040.001.01-p166-c007"}]
search_terms: ["third party"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Third Party — T2S SecuritiesAndPenaltyReporting

## Definition and applicable context

This source names **third party** in the Functionality of the messages listed below. The record is scoped to T2S SecuritiesAndPenaltyReporting, march-2026. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> provide a third party with a copy of a message for information (the sub-function of the message is Copy), -re-send to a third party a copy of a message for information (the sub-function of the message is CopyDuplicate).

src-000375, file p5, 2 semt.025.001.01 SecuritiesAccountPositionQueryV01, usage. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

No complete directed clause was assigned to this exact role label; the narrative evidence still establishes its stated context.

## Complete source evidence

<a id="src-000375-semt.025.001.01-p5-c003"></a>

### src-000375-semt.025.001.01-p5-c003

src-000375; file p5; 2 semt.025.001.01 SecuritiesAccountPositionQueryV01; usage.

> provide a third party with a copy of a message for information (the sub-function of the message is Copy), -re-send to a third party a copy of a message for information (the sub-function of the message is CopyDuplicate).

<a id="src-000375-semt.040.001.01-p166-c006"></a>

### src-000375-semt.040.001.01-p166-c006

src-000375; file p166; 5 semt.040.001.01 SecuritiesAccountPositionResponseV01; usage.

> provide a third party with a copy of a message for information (the sub-function of the message is Copy)

<a id="src-000375-semt.040.001.01-p166-c007"></a>

### src-000375-semt.040.001.01-p166-c007

src-000375; file p166; 5 semt.040.001.01 SecuritiesAccountPositionResponseV01; usage.

> re-send to a third party a copy of a message for information (the sub-function of the message is Copy Duplicate).

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| semt.025.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.025.001.01/roles.md) | src-000375-semt.025.001.01-p5-c003 |
| semt.040.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.040.001.01/roles.md) | src-000375-semt.040.001.01-p166-c006, src-000375-semt.040.001.01-p166-c007 |


[Message-set flows](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `third party`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000375](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf` · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
