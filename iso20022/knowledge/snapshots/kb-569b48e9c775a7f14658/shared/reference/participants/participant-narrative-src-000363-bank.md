---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000363-bank"
title: "Bank — T2S LimitUtilisationJournal narrative scope"
source_ids: ["src-000363"]
source_editions: ["february-2025"]
source_labels: ["bank"]
aliases: []
role_type: "business role or institutional example in quoted Functionality context"
message_sets: ["t2s-limit-utilisation-journal"]
message_ids: ["camt.064.001.01", "camt.065.001.01"]
message_families: ["camt.064", "camt.065"]
flows: []
source_locations: [{"source_id": "src-000363", "heading": "2 camt.064.001.01 LimitUtilisationJournalQueryV01", "file_pages": [4], "evidence_id": "src-000363-camt.064.001.01-p4-c001"}, {"source_id": "src-000363", "heading": "3 camt.065.001.01 LimitUtilisationJournalReportV01", "file_pages": [9], "evidence_id": "src-000363-camt.065.001.01-p9-c001"}]
search_terms: ["bank"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Bank — T2S LimitUtilisationJournal

## Definition and applicable context

This source names **bank** in the Functionality of the messages listed below. The record is scoped to T2S LimitUtilisationJournal, february-2025. Classification: business role or institutional example in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The LimitUtilisationJournalQuery message is exchanged between a central securities depository or a directly connected system participant (the central securities depository participant granted direct access, like a bank or a central counter party) and the central system.

src-000363, file p4, 2 camt.064.001.01 LimitUtilisationJournalQueryV01, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

No complete directed clause was assigned to this exact role label; the narrative evidence still establishes its stated context.

## Complete source evidence

<a id="src-000363-camt.064.001.01-p4-c001"></a>

### src-000363-camt.064.001.01-p4-c001

src-000363; file p4; 2 camt.064.001.01 LimitUtilisationJournalQueryV01; scope.

> The LimitUtilisationJournalQuery message is exchanged between a central securities depository or a directly connected system participant (the central securities depository participant granted direct access, like a bank or a central counter party) and the central system.

<a id="src-000363-camt.065.001.01-p9-c001"></a>

### src-000363-camt.065.001.01-p9-c001

src-000363; file p9; 3 camt.065.001.01 LimitUtilisationJournalReportV01; scope.

> The LimitUtilisationJournalReport message is exchanged between the central system and a central securities depository or a directly connected system party (the central securities depository participant granted direct access, like a bank or central counter party) and is used to return information about the limit.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| camt.064.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/camt.064.001.01/roles.md) | src-000363-camt.064.001.01-p4-c001 |
| camt.065.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/camt.065.001.01/roles.md) | src-000363-camt.065.001.01-p9-c001 |


[Message-set flows](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `bank`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000363](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf` · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
