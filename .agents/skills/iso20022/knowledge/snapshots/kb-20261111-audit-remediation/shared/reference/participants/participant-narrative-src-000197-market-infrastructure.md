---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000197-market-infrastructure"
title: "Market Infrastructure — Settlement and Reconciliation narrative scope"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
source_labels: ["Market Infrastructure", "market infrastructure", "market infrastructures"]
aliases: []
role_type: "business role or institutional example in quoted Functionality context"
message_sets: ["settlement-and-reconciliation"]
message_ids: ["semt.022.001.07", "sese.030.001.10", "sese.038.001.11", "sese.040.001.06"]
message_families: ["semt.022", "sese.030", "sese.038", "sese.040"]
flows: []
source_locations: [{"source_id": "src-000197", "heading": "13 semt.022.001.07 SecuritiesSettlementTransactionAuditTrailReportV07", "file_pages": [433], "evidence_id": "src-000197-semt.022.001.07-p433-c001"}, {"source_id": "src-000197", "heading": "13 semt.022.001.07 SecuritiesSettlementTransactionAuditTrailReportV07", "file_pages": [433], "evidence_id": "src-000197-semt.022.001.07-p433-c002"}, {"source_id": "src-000197", "heading": "13 semt.022.001.07 SecuritiesSettlementTransactionAuditTrailReportV07", "file_pages": [433], "evidence_id": "src-000197-semt.022.001.07-p433-c003"}, {"source_id": "src-000197", "heading": "13 semt.022.001.07 SecuritiesSettlementTransactionAuditTrailReportV07", "file_pages": [433], "evidence_id": "src-000197-semt.022.001.07-p433-c004"}, {"source_id": "src-000197", "heading": "24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10", "file_pages": [783], "evidence_id": "src-000197-sese.030.001.10-p783-c011"}, {"source_id": "src-000197", "heading": "32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "file_pages": [1133], "evidence_id": "src-000197-sese.038.001.11-p1133-c003"}, {"source_id": "src-000197", "heading": "34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06", "file_pages": [1322], "evidence_id": "src-000197-sese.040.001.06-p1322-c006"}]
search_terms: ["Market Infrastructure", "market infrastructure", "market infrastructures"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Market Infrastructure — Settlement and Reconciliation

## Definition and applicable context

This source names **market infrastructure** in the Functionality of the messages listed below. The record is scoped to Settlement and Reconciliation, March 2026. Classification: business role or institutional example in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> This message is sent by the Market Infrastructure to the CSD to advise of the history of all the statuses, modifications, replacement and cancellation of a specific transaction during its whole life cycle when the instructing party is a direct participant to the Settlement Infrastructure.

src-000197, file p433, 13 semt.022.001.07 SecuritiesSettlementTransactionAuditTrailReportV07, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

| This participant in clause | Source message subject | Message applicability | Other roles / source expressions | Evidence |
| --- | --- | --- | --- | --- |
| sender | This message | current-message | sender: the Market Infrastructure ([the Market Infrastructure](participant-narrative-src-000197-market-infrastructure.md)); receiver: the CSD | [src-000197-semt.022.001.07-p433-c001-d1](#src-000197-semt.022.001.07-p433-c001); file p433 |


## Complete source evidence

<a id="src-000197-semt.022.001.07-p433-c001"></a>

### src-000197-semt.022.001.07-p433-c001

src-000197; file p433; 13 semt.022.001.07 SecuritiesSettlementTransactionAuditTrailReportV07; scope.

> This message is sent by the Market Infrastructure to the CSD to advise of the history of all the statuses, modifications, replacement and cancellation of a specific transaction during its whole life cycle when the instructing party is a direct participant to the Settlement Infrastructure.

<a id="src-000197-semt.022.001.07-p433-c002"></a>

### src-000197-semt.022.001.07-p433-c002

src-000197; file p433; 13 semt.022.001.07 SecuritiesSettlementTransactionAuditTrailReportV07; usage.

> re-send a message sent by the market infrastructure to the direct participant,

<a id="src-000197-semt.022.001.07-p433-c003"></a>

### src-000197-semt.022.001.07-p433-c003

src-000197; file p433; 13 semt.022.001.07 SecuritiesSettlementTransactionAuditTrailReportV07; usage.

> provide a third party with a copy of a message being sent by the market infrastructure for information,

<a id="src-000197-semt.022.001.07-p433-c004"></a>

### src-000197-semt.022.001.07-p433-c004

src-000197; file p433; 13 semt.022.001.07 SecuritiesSettlementTransactionAuditTrailReportV07; usage.

> re-send to a third party a copy of a message being sent by the market infrastructure for information using the relevant elements in the Business Application Header.

<a id="src-000197-sese.030.001.10-p783-c011"></a>

### src-000197-sese.030.001.10-p783-c011

src-000197; file p783; 24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10; usage.

> In markets where this applies (for example, securities market infrastructures with no pre-settlement matching process), it is used by a party to approve, cancel or reject a transaction instructed by the counterparty.

<a id="src-000197-sese.038.001.11-p1133-c003"></a>

### src-000197-sese.038.001.11-p1133-c003

src-000197; file p1133; 32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11; scope.

> a central securities depository participant which has an account with a central securities depository or a market infrastructure

<a id="src-000197-sese.040.001.06-p1322-c006"></a>

### src-000197-sese.040.001.06-p1322-c006

src-000197; file p1322; 34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06; scope.

> a central securities depository participant which has an account with a central securities depository or a market infrastructure

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| semt.022.001.07 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.022.001.07/roles.md) | src-000197-semt.022.001.07-p433-c001, src-000197-semt.022.001.07-p433-c002, src-000197-semt.022.001.07-p433-c003, src-000197-semt.022.001.07-p433-c004 |
| sese.030.001.10 | [Exact message-role evidence](../../../domains/securities/reference/messages/sese.030.001.10/roles.md) | src-000197-sese.030.001.10-p783-c011 |
| sese.038.001.11 | [Exact message-role evidence](../../../domains/securities/reference/messages/sese.038.001.11/roles.md) | src-000197-sese.038.001.11-p1133-c003 |
| sese.040.001.06 | [Exact message-role evidence](../../../domains/securities/reference/messages/sese.040.001.06/roles.md) | src-000197-sese.040.001.06-p1322-c006 |


[Message-set flows](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `Market Infrastructure`, `market infrastructure`, `market infrastructures`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000197](../../../evidence/omitted/e96bb98c659322ed5684b325.md) · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
