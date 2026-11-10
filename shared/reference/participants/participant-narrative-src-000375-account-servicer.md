---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000375-account-servicer"
title: "Account Servicer — T2S SecuritiesAndPenaltyReporting narrative scope"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
source_labels: ["account servicer"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["t2s-securities-and-penalty-reporting"]
message_ids: ["semt.025.001.01"]
message_families: ["semt.025"]
flows: []
source_locations: [{"source_id": "src-000375", "heading": "2 semt.025.001.01 SecuritiesAccountPositionQueryV01", "file_pages": [5], "evidence_id": "src-000375-semt.025.001.01-p5-c001"}]
search_terms: ["account servicer"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Account Servicer — T2S SecuritiesAndPenaltyReporting

## Definition and applicable context

This source names **account servicer** in the Functionality of the messages listed below. The record is scoped to T2S SecuritiesAndPenaltyReporting, march-2026. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The SecuritiesAccountPositionQuery message is sent by an account owner to an account servicer or servicing party to request an account view on the position at a particular point in time period, or during a particular time period, where all positions are summarised in the account structure that is compatible with the query.

src-000375, file p5, 2 semt.025.001.01 SecuritiesAccountPositionQueryV01, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

| This participant in clause | Source message subject | Message applicability | Other roles / source expressions | Evidence |
| --- | --- | --- | --- | --- |
| receiver | The SecuritiesAccountPositionQuery message | current-message | sender: an account owner ([an account owner](participant-narrative-src-000375-account-owner.md)); receiver: an account servicer or servicing party ([an account servicer](participant-narrative-src-000375-account-servicer.md); [servicing party](participant-src-000374-servicing-party.md)) | [src-000375-semt.025.001.01-p5-c001-d1](#src-000375-semt.025.001.01-p5-c001); file p5 |


## Complete source evidence

<a id="src-000375-semt.025.001.01-p5-c001"></a>

### src-000375-semt.025.001.01-p5-c001

src-000375; file p5; 2 semt.025.001.01 SecuritiesAccountPositionQueryV01; scope.

> The SecuritiesAccountPositionQuery message is sent by an account owner to an account servicer or servicing party to request an account view on the position at a particular point in time period, or during a particular time period, where all positions are summarised in the account structure that is compatible with the query.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| semt.025.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.025.001.01/roles.md) | src-000375-semt.025.001.01-p5-c001 |


[Message-set flows](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `account servicer`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000375](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf` · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
