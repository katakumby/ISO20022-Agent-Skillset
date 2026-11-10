---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000378-executing-party"
title: "Executing Party — T2S SecuritiesReferenceData narrative scope"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
source_labels: ["executing party"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["t2s-securities-reference-data"]
message_ids: ["reda.009.001.01", "reda.033.001.01", "reda.034.001.01"]
message_families: ["reda.009", "reda.033", "reda.034"]
flows: []
source_locations: [{"source_id": "src-000378", "heading": "5 reda.009.001.01 SecurityActivityAdviceV01", "file_pages": [71], "evidence_id": "src-000378-reda.009.001.01-p71-c001"}, {"source_id": "src-000378", "heading": "11 reda.033.001.01 SecuritiesAuditTrailQueryV01", "file_pages": [129], "evidence_id": "src-000378-reda.033.001.01-p129-c001"}, {"source_id": "src-000378", "heading": "12 reda.034.001.01 SecuritiesAuditTrailReportV01", "file_pages": [134], "evidence_id": "src-000378-reda.034.001.01-p134-c001"}]
search_terms: ["executing party"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Executing Party — T2S SecuritiesReferenceData

## Definition and applicable context

This source names **executing party** in the Functionality of the messages listed below. The record is scoped to T2S SecuritiesReferenceData, March 2024. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The SecurityActivityReport message is sent by the executing party to an instructing party containing information about changes on securities reference data.

src-000378, file p71, 5 reda.009.001.01 SecurityActivityAdviceV01, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

| This participant in clause | Source message subject | Message applicability | Other roles / source expressions | Evidence |
| --- | --- | --- | --- | --- |
| sender | The SecurityActivityReport message | current-message-scope-name-variant | sender: the executing party ([the executing party](participant-narrative-src-000378-executing-party.md)); receiver: an instructing party ([an instructing party](participant-narrative-src-000378-instructing-party.md)) | [src-000378-reda.009.001.01-p71-c001-d1](#src-000378-reda.009.001.01-p71-c001); file p71 |
| receiver | The SecuritiesAuditTrailQuery message | current-message | sender: an instructing party ([an instructing party](participant-narrative-src-000378-instructing-party.md)); receiver: the executing party ([the executing party](participant-narrative-src-000378-executing-party.md)) | [src-000378-reda.033.001.01-p129-c001-d1](#src-000378-reda.033.001.01-p129-c001); file p129 |
| sender | The SecuritiesAuditTrailReport message | current-message | sender: the executing party ([the executing party](participant-narrative-src-000378-executing-party.md)); receiver: an instructing party ([an instructing party](participant-narrative-src-000378-instructing-party.md)) | [src-000378-reda.034.001.01-p134-c001-d1](#src-000378-reda.034.001.01-p134-c001); file p134 |


## Complete source evidence

<a id="src-000378-reda.009.001.01-p71-c001"></a>

### src-000378-reda.009.001.01-p71-c001

src-000378; file p71; 5 reda.009.001.01 SecurityActivityAdviceV01; scope.

> The SecurityActivityReport message is sent by the executing party to an instructing party containing information about changes on securities reference data.

<a id="src-000378-reda.033.001.01-p129-c001"></a>

### src-000378-reda.033.001.01-p129-c001

src-000378; file p129; 11 reda.033.001.01 SecuritiesAuditTrailQueryV01; scope.

> The SecuritiesAuditTrailQuery message is sent by an instructing party to the executing party to query for the securities audit trail recorded in the system.

<a id="src-000378-reda.034.001.01-p134-c001"></a>

### src-000378-reda.034.001.01-p134-c001

src-000378; file p134; 12 reda.034.001.01 SecuritiesAuditTrailReportV01; scope.

> The SecuritiesAuditTrailReport message is sent by the executing party to an instructing party to provide detailed information on the requested securities audit trail recorded in the system.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| reda.009.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.009.001.01/roles.md) | src-000378-reda.009.001.01-p71-c001 |
| reda.033.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.033.001.01/roles.md) | src-000378-reda.033.001.01-p129-c001 |
| reda.034.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.034.001.01/roles.md) | src-000378-reda.034.001.01-p134-c001 |


[Message-set reference](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/march-2024/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `executing party`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000378](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf` · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
