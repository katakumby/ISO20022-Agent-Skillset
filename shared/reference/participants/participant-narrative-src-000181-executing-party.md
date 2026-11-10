---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000181-executing-party"
title: "Executing Party — Post-Trade Matching narrative scope"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
source_labels: ["executing party", "Executing Party", "Executing party"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["post-trade-matching"]
message_ids: ["semt.023.001.02", "setr.027.001.05", "setr.029.001.02", "setr.030.001.03", "setr.044.001.04"]
message_families: ["semt.023", "setr.027", "setr.029", "setr.030", "setr.044"]
flows: []
source_locations: [{"source_id": "src-000181", "heading": "2 semt.023.001.02 SecuritiesEndOfProcessReportV02", "file_pages": [6], "evidence_id": "src-000181-semt.023.001.02-p6-c001"}, {"source_id": "src-000181", "heading": "2 semt.023.001.02 SecuritiesEndOfProcessReportV02", "file_pages": [6], "evidence_id": "src-000181-semt.023.001.02-p6-c004"}, {"source_id": "src-000181", "heading": "2 semt.023.001.02 SecuritiesEndOfProcessReportV02", "file_pages": [6], "evidence_id": "src-000181-semt.023.001.02-p6-c006"}, {"source_id": "src-000181", "heading": "3 setr.027.001.05 SecuritiesTradeConfirmationV05", "file_pages": [28], "evidence_id": "src-000181-setr.027.001.05-p28-c001"}, {"source_id": "src-000181", "heading": "3 setr.027.001.05 SecuritiesTradeConfirmationV05", "file_pages": [28], "evidence_id": "src-000181-setr.027.001.05-p28-c002"}, {"source_id": "src-000181", "heading": "3 setr.027.001.05 SecuritiesTradeConfirmationV05", "file_pages": [28], "evidence_id": "src-000181-setr.027.001.05-p28-c004"}, {"source_id": "src-000181", "heading": "3 setr.027.001.05 SecuritiesTradeConfirmationV05", "file_pages": [28], "evidence_id": "src-000181-setr.027.001.05-p28-c006"}, {"source_id": "src-000181", "heading": "3 setr.027.001.05 SecuritiesTradeConfirmationV05", "file_pages": [28], "evidence_id": "src-000181-setr.027.001.05-p28-c007"}, {"source_id": "src-000181", "heading": "4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02", "file_pages": [140], "evidence_id": "src-000181-setr.029.001.02-p140-c001"}, {"source_id": "src-000181", "heading": "4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02", "file_pages": [140], "evidence_id": "src-000181-setr.029.001.02-p140-c003"}, {"source_id": "src-000181", "heading": "4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02", "file_pages": [140], "evidence_id": "src-000181-setr.029.001.02-p140-c004"}, {"source_id": "src-000181", "heading": "4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02", "file_pages": [140], "evidence_id": "src-000181-setr.029.001.02-p140-c005"}, {"source_id": "src-000181", "heading": "5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03", "file_pages": [148], "evidence_id": "src-000181-setr.030.001.03-p148-c001"}, {"source_id": "src-000181", "heading": "5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03", "file_pages": [148], "evidence_id": "src-000181-setr.030.001.03-p148-c002"}, {"source_id": "src-000181", "heading": "5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03", "file_pages": [148], "evidence_id": "src-000181-setr.030.001.03-p148-c006"}, {"source_id": "src-000181", "heading": "5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03", "file_pages": [148], "evidence_id": "src-000181-setr.030.001.03-p148-c007"}, {"source_id": "src-000181", "heading": "6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04", "file_pages": [162], "evidence_id": "src-000181-setr.044.001.04-p162-c001"}, {"source_id": "src-000181", "heading": "6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04", "file_pages": [162], "evidence_id": "src-000181-setr.044.001.04-p162-c004"}]
search_terms: ["Executing Party", "Executing party", "executing party"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Executing Party — Post-Trade Matching

## Definition and applicable context

This source names **executing party** in the Functionality of the messages listed below. The record is scoped to Post-Trade Matching, February 2025. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> Sent by an executing party or an instructing party to the custodian or an affirming party to notify that all the necessary SecuritiesTradeConfirmation message or any other notification of the process have been sent.

src-000181, file p6, 2 semt.023.001.02 SecuritiesEndOfProcessReportV02, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

| This participant in clause | Source message subject | Message applicability | Other roles / source expressions | Evidence |
| --- | --- | --- | --- | --- |
| sender | This message | current-message | sender: an executing party or an instructing party ([an executing party](participant-narrative-src-000181-executing-party.md); [an instructing party](participant-src-000180-instructing-party.md)); receiver: the custodian or an affirming party ([the custodian](participant-src-000180-custodian.md); [an affirming party](participant-src-000180-affirming-party.md)) | [src-000181-semt.023.001.02-p6-c001-d1](#src-000181-semt.023.001.02-p6-c001); file p6 |
| sender | This message | current-message | sender: an executing party ([an executing party](participant-narrative-src-000181-executing-party.md)); receiver: an instructing party directly or through Central Matching Utility (CMU) ([an instructing party](participant-src-000180-instructing-party.md)) | [src-000181-setr.027.001.05-p28-c001-d1](#src-000181-setr.027.001.05-p28-c001); file p28 |
| sender | This message | current-message | sender: an executing party ([an executing party](participant-narrative-src-000181-executing-party.md)); receiver: an instructing party directly or through Central Matching Utility (CMU) ([an instructing party](participant-src-000180-instructing-party.md)) | [src-000181-setr.029.001.02-p140-c001-d1](#src-000181-setr.029.001.02-p140-c001); file p140 |
| receiver | This message | current-message | sender: an instructing party, a custodian or an affirming party ([an instructing party](participant-src-000180-instructing-party.md); [a custodian](participant-src-000180-custodian.md); [an affirming party](participant-src-000180-affirming-party.md)); receiver: an executing party (local matching) or to Central Matching Utility (CMU) ([an executing party](participant-narrative-src-000181-executing-party.md); [to Central Matching Utility](participant-narrative-src-000181-central-matching-utility.md)) | [src-000181-setr.030.001.03-p148-c001-d1](#src-000181-setr.030.001.03-p148-c001); file p148 |
| receiver | This message | current-message | sender: Central Matching Utility (CMU) ([Central Matching Utility](participant-narrative-src-000181-central-matching-utility.md)); receiver: an executing party or an instructing party ([an executing party](participant-narrative-src-000181-executing-party.md); [an instructing party](participant-src-000180-instructing-party.md)) | [src-000181-setr.044.001.04-p162-c001-d1](#src-000181-setr.044.001.04-p162-c001); file p162 |


## Complete source evidence

<a id="src-000181-semt.023.001.02-p6-c001"></a>

### src-000181-semt.023.001.02-p6-c001

src-000181; file p6; 2 semt.023.001.02 SecuritiesEndOfProcessReportV02; scope.

> Sent by an executing party or an instructing party to the custodian or an affirming party to notify that all the necessary SecuritiesTradeConfirmation message or any other notification of the process have been sent.

<a id="src-000181-semt.023.001.02-p6-c004"></a>

### src-000181-semt.023.001.02-p6-c004

src-000181; file p6; 2 semt.023.001.02 SecuritiesEndOfProcessReportV02; scope.

> The executing party is typically the broker/dealer or an intermediary system/vendor communicating on behalf of the broker/dealer.

<a id="src-000181-semt.023.001.02-p6-c006"></a>

### src-000181-semt.023.001.02-p6-c006

src-000181; file p6; 2 semt.023.001.02 SecuritiesEndOfProcessReportV02; usage.

> Initiator: Executing Party, CMU or Instructing Party Respondent: Custodian or an affirming party does not need to respond.

<a id="src-000181-setr.027.001.05-p28-c001"></a>

### src-000181-setr.027.001.05-p28-c001

src-000181; file p28; 3 setr.027.001.05 SecuritiesTradeConfirmationV05; scope.

> Sent by an executing party to an instructing party directly or through Central Matching Utility (CMU) to provide trade confirmation on a per-account basis based on instructions provided by the instructing party in the SecuritiesAllocationInstruction message.

<a id="src-000181-setr.027.001.05-p28-c002"></a>

### src-000181-setr.027.001.05-p28-c002

src-000181; file p28; 3 setr.027.001.05 SecuritiesTradeConfirmationV05; scope.

> It may also be used to provide trade confirmation on the trade level from an executing party or an instructing party to the custodian or an affirming party directly or through CMU.

<a id="src-000181-setr.027.001.05-p28-c004"></a>

### src-000181-setr.027.001.05-p28-c004

src-000181; file p28; 3 setr.027.001.05 SecuritiesTradeConfirmationV05; scope.

> The executing party is typically the broker/dealer or an intermediary system/vendor communicating on behalf of the broker/dealer.

<a id="src-000181-setr.027.001.05-p28-c006"></a>

### src-000181-setr.027.001.05-p28-c006

src-000181; file p28; 3 setr.027.001.05 SecuritiesTradeConfirmationV05; usage.

> Initiator: In local matching, the initiator of this message is always the executing party.

<a id="src-000181-setr.027.001.05-p28-c007"></a>

### src-000181-setr.027.001.05-p28-c007

src-000181; file p28; 3 setr.027.001.05 SecuritiesTradeConfirmationV05; usage.

> In central matching the initiator may be either the executing party or instructing party.

<a id="src-000181-setr.029.001.02-p140-c001"></a>

### src-000181-setr.029.001.02-p140-c001

src-000181; file p140; 4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02; scope.

> Sent by an executing party to an instructing party directly or through Central Matching Utility (CMU) to cancel the referenced SecuritiesTradeConfirmation message that was previously sent.

<a id="src-000181-setr.029.001.02-p140-c003"></a>

### src-000181-setr.029.001.02-p140-c003

src-000181; file p140; 4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02; scope.

> The executing party is typically the broker/dealer or an intermediary system/vendor communicating on behalf of the broker/dealer.

<a id="src-000181-setr.029.001.02-p140-c004"></a>

### src-000181-setr.029.001.02-p140-c004

src-000181; file p140; 4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02; scope.

> It may also be used to cancel the trade confirmation previously sent from an executing party or an instructing party to a custodian or an affirming party directly or through CMU.

<a id="src-000181-setr.029.001.02-p140-c005"></a>

### src-000181-setr.029.001.02-p140-c005

src-000181; file p140; 4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02; usage.

> Initiator: Both in local and central matching, the Initiator may be either the Executing Party or Instructing Party.

<a id="src-000181-setr.030.001.03-p148-c001"></a>

### src-000181-setr.030.001.03-p148-c001

src-000181; file p148; 5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03; scope.

> Sent by an instructing party, a custodian or an affirming party to an executing party (local matching) or to Central Matching Utility (CMU) to affirm (accept) or disaffirm (reject) (central matching) the SecuritiesTradeConfirmation message.

<a id="src-000181-setr.030.001.03-p148-c002"></a>

### src-000181-setr.030.001.03-p148-c002

src-000181; file p148; 5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03; scope.

> The executing party is typically the broker/dealer or an intermediary system/vendor communicating on behalf of the broker/dealer.

<a id="src-000181-setr.030.001.03-p148-c006"></a>

### src-000181-setr.030.001.03-p148-c006

src-000181; file p148; 5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03; usage.

> Respondent: Executing party does not need to respond if an affirmation.

<a id="src-000181-setr.030.001.03-p148-c007"></a>

### src-000181-setr.030.001.03-p148-c007

src-000181; file p148; 5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03; usage.

> Executing party may respond with modification or cancellation of the rejected SecuritiesTradeConfirmation message.

<a id="src-000181-setr.044.001.04-p162-c001"></a>

### src-000181-setr.044.001.04-p162-c001

src-000181; file p162; 6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04; scope.

> This message is sent from Central Matching Utility (CMU) to an executing party or an instructing party to advise the status of the SecuritiesTradeConfirmation message previously sent by the party.

<a id="src-000181-setr.044.001.04-p162-c004"></a>

### src-000181-setr.044.001.04-p162-c004

src-000181; file p162; 6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04; scope.

> The executing party is typically the broker/dealer or an intermediary system/vendor communicating on behalf of the broker/dealer.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| semt.023.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.023.001.02/roles.md) | src-000181-semt.023.001.02-p6-c001, src-000181-semt.023.001.02-p6-c004, src-000181-semt.023.001.02-p6-c006 |
| setr.027.001.05 | [Exact message-role evidence](../../../domains/securities/reference/messages/setr.027.001.05/roles.md) | src-000181-setr.027.001.05-p28-c001, src-000181-setr.027.001.05-p28-c002, src-000181-setr.027.001.05-p28-c004, src-000181-setr.027.001.05-p28-c006, src-000181-setr.027.001.05-p28-c007 |
| setr.029.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/setr.029.001.02/roles.md) | src-000181-setr.029.001.02-p140-c001, src-000181-setr.029.001.02-p140-c003, src-000181-setr.029.001.02-p140-c004, src-000181-setr.029.001.02-p140-c005 |
| setr.030.001.03 | [Exact message-role evidence](../../../domains/securities/reference/messages/setr.030.001.03/roles.md) | src-000181-setr.030.001.03-p148-c001, src-000181-setr.030.001.03-p148-c002, src-000181-setr.030.001.03-p148-c006, src-000181-setr.030.001.03-p148-c007 |
| setr.044.001.04 | [Exact message-role evidence](../../../domains/securities/reference/messages/setr.044.001.04/roles.md) | src-000181-setr.044.001.04-p162-c001, src-000181-setr.044.001.04-p162-c004 |


[Message-set flows](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `Executing Party`, `Executing party`, `executing party`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000181](../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf) · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
