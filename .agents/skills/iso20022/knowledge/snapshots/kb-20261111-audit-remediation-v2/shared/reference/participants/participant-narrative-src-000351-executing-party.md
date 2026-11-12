---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000351-executing-party"
title: "Executing Party — T2S CashAccountQueryAndReport narrative scope"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
source_labels: ["executing party"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["t2s-cash-account-query-and-report"]
message_ids: ["reda.038.001.01", "reda.039.001.01", "reda.040.001.01"]
message_families: ["reda.038", "reda.039", "reda.040"]
flows: []
source_locations: [{"source_id": "src-000351", "heading": "4 reda.038.001.01 CashAccountActivityAdviceV01", "file_pages": [108], "evidence_id": "src-000351-reda.038.001.01-p108-c001"}, {"source_id": "src-000351", "heading": "5 reda.039.001.01 CashAccountAuditTrailQueryV01", "file_pages": [113], "evidence_id": "src-000351-reda.039.001.01-p113-c001"}, {"source_id": "src-000351", "heading": "6 reda.040.001.01 CashAccountAuditTrailReportV01", "file_pages": [118], "evidence_id": "src-000351-reda.040.001.01-p118-c001"}]
search_terms: ["executing party"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Executing Party — T2S CashAccountQueryAndReport

## Definition and applicable context

This source names **executing party** in the Functionality of the messages listed below. The record is scoped to T2S CashAccountQueryAndReport, august-2026. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The CashAccountActivityReport message is sent by the executing party to an instructing party containing information about changes on cash account reference data.

src-000351, file p108, 4 reda.038.001.01 CashAccountActivityAdviceV01, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

| This participant in clause | Source message subject | Message applicability | Other roles / source expressions | Evidence |
| --- | --- | --- | --- | --- |
| sender | The CashAccountActivityReport message | current-message-scope-name-variant | sender: the executing party ([the executing party](participant-narrative-src-000351-executing-party.md)); receiver: an instructing party ([an instructing party](participant-src-000350-instructing-party.md)) | [src-000351-reda.038.001.01-p108-c001-d1](#src-000351-reda.038.001.01-p108-c001); file p108 |
| receiver | The CashAccountAuditTrailQuery message | current-message | sender: an instructing party ([an instructing party](participant-src-000350-instructing-party.md)); receiver: the executing party ([the executing party](participant-narrative-src-000351-executing-party.md)) | [src-000351-reda.039.001.01-p113-c001-d1](#src-000351-reda.039.001.01-p113-c001); file p113 |
| sender | The CashAccountAuditTrailReport message | current-message | sender: the executing party ([the executing party](participant-narrative-src-000351-executing-party.md)); receiver: an instructing party ([an instructing party](participant-src-000350-instructing-party.md)) | [src-000351-reda.040.001.01-p118-c001-d1](#src-000351-reda.040.001.01-p118-c001); file p118 |


## Complete source evidence

<a id="src-000351-reda.038.001.01-p108-c001"></a>

### src-000351-reda.038.001.01-p108-c001

src-000351; file p108; 4 reda.038.001.01 CashAccountActivityAdviceV01; scope.

> The CashAccountActivityReport message is sent by the executing party to an instructing party containing information about changes on cash account reference data.

<a id="src-000351-reda.039.001.01-p113-c001"></a>

### src-000351-reda.039.001.01-p113-c001

src-000351; file p113; 5 reda.039.001.01 CashAccountAuditTrailQueryV01; scope.

> The CashAccountAuditTrailQuery message is sent by an instructing party to the executing party to query for the cash account audit trail recorded in the system.

<a id="src-000351-reda.040.001.01-p118-c001"></a>

### src-000351-reda.040.001.01-p118-c001

src-000351; file p118; 6 reda.040.001.01 CashAccountAuditTrailReportV01; scope.

> The CashAccountAuditTrailReport message is sent by the executing party to an instructing party to provide detailed information on the requested cash account audit trail recorded in the system.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| reda.038.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.038.001.01/roles.md) | src-000351-reda.038.001.01-p108-c001 |
| reda.039.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.039.001.01/roles.md) | src-000351-reda.039.001.01-p113-c001 |
| reda.040.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.040.001.01/roles.md) | src-000351-reda.040.001.01-p118-c001 |


[Message-set flows](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `executing party`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000351](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf` · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
