---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000369-central-securities-depository-participant"
title: "Central Securities Depository Participant — T2S PartyReferenceData narrative scope"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
source_labels: ["central securities depository participant"]
aliases: []
role_type: "business role or institutional example in quoted Functionality context"
message_sets: ["t2s-party-reference-data"]
message_ids: ["reda.015.001.01", "reda.017.001.02"]
message_families: ["reda.015", "reda.017"]
flows: []
source_locations: [{"source_id": "src-000369", "heading": "3 reda.015.001.01 PartyQueryV01", "file_pages": [18], "evidence_id": "src-000369-reda.015.001.01-p18-c001"}, {"source_id": "src-000369", "heading": "5 reda.017.001.02 PartyReportV02", "file_pages": [41], "evidence_id": "src-000369-reda.017.001.02-p41-c001"}]
search_terms: ["central securities depository participant"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Central Securities Depository Participant — T2S PartyReferenceData

## Definition and applicable context

This source names **central securities depository participant** in the Functionality of the messages listed below. The record is scoped to T2S PartyReferenceData, march-2024. Classification: business role or institutional example in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The PartyQuery message is sent by a central securities depository, a national central bank, a central securities depository participant, a central counter party, a payment bank, a trading party or a stock exchange to the executing party to query for the party reference data of a party defined in the system.

src-000369, file p18, 3 reda.015.001.01 PartyQueryV01, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

| This participant in clause | Source message subject | Message applicability | Other roles / source expressions | Evidence |
| --- | --- | --- | --- | --- |
| sender | The PartyQuery message | current-message | sender: a central securities depository, a national central bank, a central securities depository participant, a central counter party, a payment bank, a trading party or a stock exchange ([a central securities depository](participant-narrative-src-000369-central-securities-depository.md); [a central securities depository participant](participant-narrative-src-000369-central-securities-depository-participant.md); [a central counter party](participant-narrative-src-000369-central-counter-party.md); [a stock exchange](participant-narrative-src-000369-stock-exchange.md)); receiver: the executing party ([the executing party](participant-narrative-src-000369-executing-party.md)) | [src-000369-reda.015.001.01-p18-c001-d1](#src-000369-reda.015.001.01-p18-c001); file p18 |
| receiver | The PartyReport message | current-message | sender: the executing party ([the executing party](participant-narrative-src-000369-executing-party.md)); receiver: a central securities depository, a national central bank, a central securities depository participant, a central counter party, a payment bank, a trading party or a stock exchange ([a central securities depository](participant-narrative-src-000369-central-securities-depository.md); [a central securities depository participant](participant-narrative-src-000369-central-securities-depository-participant.md); [a central counter party](participant-narrative-src-000369-central-counter-party.md); [a stock exchange](participant-narrative-src-000369-stock-exchange.md)) | [src-000369-reda.017.001.02-p41-c001-d1](#src-000369-reda.017.001.02-p41-c001); file p41 |


## Complete source evidence

<a id="src-000369-reda.015.001.01-p18-c001"></a>

### src-000369-reda.015.001.01-p18-c001

src-000369; file p18; 3 reda.015.001.01 PartyQueryV01; scope.

> The PartyQuery message is sent by a central securities depository, a national central bank, a central securities depository participant, a central counter party, a payment bank, a trading party or a stock exchange to the executing party to query for the party reference data of a party defined in the system.

<a id="src-000369-reda.017.001.02-p41-c001"></a>

### src-000369-reda.017.001.02-p41-c001

src-000369; file p41; 5 reda.017.001.02 PartyReportV02; scope.

> The PartyReport message is sent by the executing party to a central securities depository, a national central bank, a central securities depository participant, a central counter party, a payment bank, a trading party or a stock exchange to provide detailed information on the requested party reference data of the party defined in the system.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| reda.015.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.015.001.01/roles.md) | src-000369-reda.015.001.01-p18-c001 |
| reda.017.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.017.001.02/roles.md) | src-000369-reda.017.001.02-p41-c001 |


[Message-set flows](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `central securities depository participant`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000369](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf` · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
