---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000372-executing-party"
title: "Executing Party — T2S SecuritiesAccountReferenceData narrative scope"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
source_labels: ["executing party"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["t2s-securities-account-reference-data"]
message_ids: ["reda.018.001.01", "reda.019.001.01", "reda.020.001.01", "reda.021.001.01", "reda.023.001.01", "reda.032.001.01", "reda.035.001.01", "reda.036.001.01", "reda.037.001.01"]
message_families: ["reda.018", "reda.019", "reda.020", "reda.021", "reda.023", "reda.032", "reda.035", "reda.036", "reda.037"]
flows: []
source_locations: [{"source_id": "src-000372", "heading": "2 reda.018.001.01 SecuritiesAccountCreationRequestV01", "file_pages": [6], "evidence_id": "src-000372-reda.018.001.01-p6-c001"}, {"source_id": "src-000372", "heading": "3 reda.019.001.01 SecuritiesAccountQueryV01", "file_pages": [14], "evidence_id": "src-000372-reda.019.001.01-p14-c001"}, {"source_id": "src-000372", "heading": "4 reda.020.001.01 SecuritiesAccountStatusAdviceV01", "file_pages": [26], "evidence_id": "src-000372-reda.020.001.01-p26-c001"}, {"source_id": "src-000372", "heading": "5 reda.021.001.01 SecuritiesAccountReportV01", "file_pages": [32], "evidence_id": "src-000372-reda.021.001.01-p32-c001"}, {"source_id": "src-000372", "heading": "6 reda.023.001.01 SecuritiesAccountModificationRequestV01", "file_pages": [48], "evidence_id": "src-000372-reda.023.001.01-p48-c001"}, {"source_id": "src-000372", "heading": "7 reda.032.001.01 SecuritiesAccountDeletionRequestV01", "file_pages": [56], "evidence_id": "src-000372-reda.032.001.01-p56-c001"}, {"source_id": "src-000372", "heading": "8 reda.035.001.01 SecuritiesAccountActivityAdviceV01", "file_pages": [59], "evidence_id": "src-000372-reda.035.001.01-p59-c001"}, {"source_id": "src-000372", "heading": "9 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01", "file_pages": [64], "evidence_id": "src-000372-reda.036.001.01-p64-c001"}, {"source_id": "src-000372", "heading": "10 reda.037.001.01 SecuritiesAccountAuditTrailReportV01", "file_pages": [68], "evidence_id": "src-000372-reda.037.001.01-p68-c001"}]
search_terms: ["executing party"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Executing Party — T2S SecuritiesAccountReferenceData

## Definition and applicable context

This source names **executing party** in the Functionality of the messages listed below. The record is scoped to T2S SecuritiesAccountReferenceData, december-2019. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The SecuritiesAccountCreationRequest message message is sent by an instructing party to the executing party to instruct the creation of a new securities account with the required account attributes details.

src-000372, file p6, 2 reda.018.001.01 SecuritiesAccountCreationRequestV01, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

| This participant in clause | Source message subject | Message applicability | Other roles / source expressions | Evidence |
| --- | --- | --- | --- | --- |
| receiver | The SecuritiesAccountCreationRequest message message | current-message | sender: an instructing party ([an instructing party](participant-src-000371-instructing-party.md)); receiver: the executing party ([the executing party](participant-narrative-src-000372-executing-party.md)) | [src-000372-reda.018.001.01-p6-c001-d1](#src-000372-reda.018.001.01-p6-c001); file p6 |
| receiver | The SecuritiesAccountModificationRequest message | current-message | sender: an instructing party ([an instructing party](participant-src-000371-instructing-party.md)); receiver: the executing party ([the executing party](participant-narrative-src-000372-executing-party.md)) | [src-000372-reda.023.001.01-p48-c001-d1](#src-000372-reda.023.001.01-p48-c001); file p48 |
| receiver | The SecuritiesAccountDeletionRequest message | current-message | sender: an instructing party ([an instructing party](participant-src-000371-instructing-party.md)); receiver: the executing party ([the executing party](participant-narrative-src-000372-executing-party.md)) | [src-000372-reda.032.001.01-p56-c001-d1](#src-000372-reda.032.001.01-p56-c001); file p56 |
| sender | The SecuritieAccountActivityReport message | current-message-scope-name-variant | sender: the executing party ([the executing party](participant-narrative-src-000372-executing-party.md)); receiver: an instructing party ([an instructing party](participant-src-000371-instructing-party.md)) | [src-000372-reda.035.001.01-p59-c001-d1](#src-000372-reda.035.001.01-p59-c001); file p59 |
| receiver | The SecuritiesAccountAuditTrailQuery message | current-message | sender: an instructing party ([an instructing party](participant-src-000371-instructing-party.md)); receiver: the executing party ([the executing party](participant-narrative-src-000372-executing-party.md)) | [src-000372-reda.036.001.01-p64-c001-d1](#src-000372-reda.036.001.01-p64-c001); file p64 |
| sender | The SecuritiesAccountAuditTrailReport message | current-message | sender: the executing party ([the executing party](participant-narrative-src-000372-executing-party.md)); receiver: an instructing party ([an instructing party](participant-src-000371-instructing-party.md)) | [src-000372-reda.037.001.01-p68-c001-d1](#src-000372-reda.037.001.01-p68-c001); file p68 |


## Complete source evidence

<a id="src-000372-reda.018.001.01-p6-c001"></a>

### src-000372-reda.018.001.01-p6-c001

src-000372; file p6; 2 reda.018.001.01 SecuritiesAccountCreationRequestV01; scope.

> The SecuritiesAccountCreationRequest message message is sent by an instructing party to the executing party to instruct the creation of a new securities account with the required account attributes details.

<a id="src-000372-reda.019.001.01-p14-c001"></a>

### src-000372-reda.019.001.01-p14-c001

src-000372; file p14; 3 reda.019.001.01 SecuritiesAccountQueryV01; scope.

> The SecuritiesAccountQuery message sent by an instructing party to the executing party to request the details related to the securities account.

<a id="src-000372-reda.020.001.01-p26-c001"></a>

### src-000372-reda.020.001.01-p26-c001

src-000372; file p26; 4 reda.020.001.01 SecuritiesAccountStatusAdviceV01; scope.

> The SecuritiesAccountStatusAdvice message is send by the the executing party to an instructing party to provide the status of the execution of an creation, modification or deletion of securities account reference data.

<a id="src-000372-reda.021.001.01-p32-c001"></a>

### src-000372-reda.021.001.01-p32-c001

src-000372; file p32; 5 reda.021.001.01 SecuritiesAccountReportV01; scope.

> The SecuritiesAccountReport message sent by the executing party to an instructing party to provide the details of the securities account details as requested in the query.

<a id="src-000372-reda.023.001.01-p48-c001"></a>

### src-000372-reda.023.001.01-p48-c001

src-000372; file p48; 6 reda.023.001.01 SecuritiesAccountModificationRequestV01; scope.

> The SecuritiesAccountModificationRequest message is sent by an instructing party to the executing party to instruct the update of an existing securities account by amending its existing attributes or by providing additional attibutes details.

<a id="src-000372-reda.032.001.01-p56-c001"></a>

### src-000372-reda.032.001.01-p56-c001

src-000372; file p56; 7 reda.032.001.01 SecuritiesAccountDeletionRequestV01; scope.

> The SecuritiesAccountDeletionRequest message is sent by an instructing party to the executing party to request for the deletion of a securities account from the securities account reference data defined in the system of the executing party.

<a id="src-000372-reda.035.001.01-p59-c001"></a>

### src-000372-reda.035.001.01-p59-c001

src-000372; file p59; 8 reda.035.001.01 SecuritiesAccountActivityAdviceV01; scope.

> The SecuritieAccountActivityReport message is sent by the executing party to an instructing party containing information about changes on securities account reference data.

<a id="src-000372-reda.036.001.01-p64-c001"></a>

### src-000372-reda.036.001.01-p64-c001

src-000372; file p64; 9 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01; scope.

> The SecuritiesAccountAuditTrailQuery message is sent by an instructing party to the executing party to query for the securities account audit trail recorded in the system.

<a id="src-000372-reda.037.001.01-p68-c001"></a>

### src-000372-reda.037.001.01-p68-c001

src-000372; file p68; 10 reda.037.001.01 SecuritiesAccountAuditTrailReportV01; scope.

> The SecuritiesAccountAuditTrailReport message is sent by the executing party to an instructing party to provide detailed information on the requested securities account audit trail recorded in the system.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| reda.018.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.018.001.01/roles.md) | src-000372-reda.018.001.01-p6-c001 |
| reda.019.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.019.001.01/roles.md) | src-000372-reda.019.001.01-p14-c001 |
| reda.020.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.020.001.01/roles.md) | src-000372-reda.020.001.01-p26-c001 |
| reda.021.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.021.001.01/roles.md) | src-000372-reda.021.001.01-p32-c001 |
| reda.023.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.023.001.01/roles.md) | src-000372-reda.023.001.01-p48-c001 |
| reda.032.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.032.001.01/roles.md) | src-000372-reda.032.001.01-p56-c001 |
| reda.035.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.035.001.01/roles.md) | src-000372-reda.035.001.01-p59-c001 |
| reda.036.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.036.001.01/roles.md) | src-000372-reda.036.001.01-p64-c001 |
| reda.037.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.037.001.01/roles.md) | src-000372-reda.037.001.01-p68-c001 |


[Message-set flows](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `executing party`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000372](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf` · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
