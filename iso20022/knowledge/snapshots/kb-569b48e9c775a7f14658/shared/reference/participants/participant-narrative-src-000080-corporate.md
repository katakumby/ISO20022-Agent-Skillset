---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000080-corporate"
title: "Corporate — Corporate Actions narrative scope"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
source_labels: ["corporate"]
aliases: []
role_type: "business role or institutional example in quoted Functionality context"
message_sets: ["corporate-actions"]
message_ids: ["seev.031.001.16", "seev.032.001.09", "seev.033.001.14", "seev.034.001.16", "seev.036.001.17", "seev.039.001.13", "seev.040.001.13", "seev.042.001.14"]
message_families: ["seev.031", "seev.032", "seev.033", "seev.034", "seev.036", "seev.039", "seev.040", "seev.042"]
flows: []
source_locations: [{"source_id": "src-000080", "heading": "3 seev.031.001.16 CorporateActionNotificationV16", "file_pages": [23], "evidence_id": "src-000080-seev.031.001.16-p23-c001"}, {"source_id": "src-000080", "heading": "3 seev.031.001.16 CorporateActionNotificationV16", "file_pages": [23], "evidence_id": "src-000080-seev.031.001.16-p23-c004"}, {"source_id": "src-000080", "heading": "4 seev.032.001.09 CorporateActionEventProcessingStatusAdviceV09", "file_pages": [266], "evidence_id": "src-000080-seev.032.001.09-p266-c001"}, {"source_id": "src-000080", "heading": "4 seev.032.001.09 CorporateActionEventProcessingStatusAdviceV09", "file_pages": [266], "evidence_id": "src-000080-seev.032.001.09-p266-c002"}, {"source_id": "src-000080", "heading": "5 seev.033.001.14 CorporateActionInstructionV14", "file_pages": [274], "evidence_id": "src-000080-seev.033.001.14-p274-c001"}, {"source_id": "src-000080", "heading": "5 seev.033.001.14 CorporateActionInstructionV14", "file_pages": [274], "evidence_id": "src-000080-seev.033.001.14-p274-c002"}, {"source_id": "src-000080", "heading": "6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "file_pages": [320], "evidence_id": "src-000080-seev.034.001.16-p320-c001"}, {"source_id": "src-000080", "heading": "6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "file_pages": [320], "evidence_id": "src-000080-seev.034.001.16-p320-c002"}, {"source_id": "src-000080", "heading": "6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "file_pages": [320], "evidence_id": "src-000080-seev.034.001.16-p320-c003"}, {"source_id": "src-000080", "heading": "8 seev.036.001.17 CorporateActionMovementConfirmationV17", "file_pages": [540], "evidence_id": "src-000080-seev.036.001.17-p540-c001"}, {"source_id": "src-000080", "heading": "11 seev.039.001.13 CorporateActionCancellationAdviceV13", "file_pages": [701], "evidence_id": "src-000080-seev.039.001.13-p701-c001"}, {"source_id": "src-000080", "heading": "12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13", "file_pages": [719], "evidence_id": "src-000080-seev.040.001.13-p719-c001"}, {"source_id": "src-000080", "heading": "14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "file_pages": [757], "evidence_id": "src-000080-seev.042.001.14-p757-c001"}]
search_terms: ["corporate"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Corporate — Corporate Actions

## Definition and applicable context

This source names **corporate** in the Functionality of the messages listed below. The record is scoped to Corporate Actions, February 2026. Classification: business role or institutional example in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The CorporateActionNotification message is sent by an account servicer to an account owner or its designated agent to notify details of a corporate action event and optionally account information and preliminary information about eligible balance and entitlements.

src-000080, file p23, 3 seev.031.001.16 CorporateActionNotificationV16, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

No complete directed clause was assigned to this exact role label; the narrative evidence still establishes its stated context.

## Complete source evidence

<a id="src-000080-seev.031.001.16-p23-c001"></a>

### src-000080-seev.031.001.16-p23-c001

src-000080; file p23; 3 seev.031.001.16 CorporateActionNotificationV16; scope.

> The CorporateActionNotification message is sent by an account servicer to an account owner or its designated agent to notify details of a corporate action event and optionally account information and preliminary information about eligible balance and entitlements.

<a id="src-000080-seev.031.001.16-p23-c004"></a>

### src-000080-seev.031.001.16-p23-c004

src-000080; file p23; 3 seev.031.001.16 CorporateActionNotificationV16; scope.

> It may also be sent to an account owner or its designated agent, to remind of event details and/or of missing or incomplete instructions for a corporate action event.

<a id="src-000080-seev.032.001.09-p266-c001"></a>

### src-000080-seev.032.001.09-p266-c001

src-000080; file p266; 4 seev.032.001.09 CorporateActionEventProcessingStatusAdviceV09; scope.

> An account servicer sends the CorporateActionEventProcessingStatusAdvice message to an account owner or its designated agent to report processing status of a corporate action event.

<a id="src-000080-seev.032.001.09-p266-c002"></a>

### src-000080-seev.032.001.09-p266-c002

src-000080; file p266; 4 seev.032.001.09 CorporateActionEventProcessingStatusAdviceV09; scope.

> The account servicer uses this message to provide a reason as to why a corporate action event has not been completed by the announced payment dates.

<a id="src-000080-seev.033.001.14-p274-c001"></a>

### src-000080-seev.033.001.14-p274-c001

src-000080; file p274; 5 seev.033.001.14 CorporateActionInstructionV14; scope.

> The CorporateActionInstruction message is sent by an account owner to an account servicer to instruct election on a corporate action event.

<a id="src-000080-seev.033.001.14-p274-c002"></a>

### src-000080-seev.033.001.14-p274-c002

src-000080; file p274; 5 seev.033.001.14 CorporateActionInstructionV14; scope.

> This message is used to provide the custodian with instructions on how the account owner wishes to proceed with a corporate action event.

<a id="src-000080-seev.034.001.16-p320-c001"></a>

### src-000080-seev.034.001.16-p320-c001

src-000080; file p320; 6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16; scope.

> The CorporateActionInstructionStatusAdvice message is sent by an account servicer to an account owner or its designated agent, to report the status of a received corporate action election instruction.

<a id="src-000080-seev.034.001.16-p320-c002"></a>

### src-000080-seev.034.001.16-p320-c002

src-000080; file p320; 6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16; scope.

> This message is used to advise the status, or a change in status, of a corporate action-related transaction previously instructed by, or executed on behalf of, the account owner.

<a id="src-000080-seev.034.001.16-p320-c003"></a>

### src-000080-seev.034.001.16-p320-c003

src-000080; file p320; 6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16; scope.

> This will include the acknowledgement/rejection of a corporate action instruction.

<a id="src-000080-seev.036.001.17-p540-c001"></a>

### src-000080-seev.036.001.17-p540-c001

src-000080; file p540; 8 seev.036.001.17 CorporateActionMovementConfirmationV17; scope.

> The CorporateActionMovementConfirmation message is sent by an account servicer to an account owner or its designated agent to confirm the posting of securities or cash as a result of a corporate action event.

<a id="src-000080-seev.039.001.13-p701-c001"></a>

### src-000080-seev.039.001.13-p701-c001

src-000080; file p701; 11 seev.039.001.13 CorporateActionCancellationAdviceV13; scope.

> The CorporateActionCancellationAdvice message is sent by an account servicer to an account owner or its designated agent to cancel a previously announced corporate action event in case of error from the account servicer or in case of withdrawal by the issuer.

<a id="src-000080-seev.040.001.13-p719-c001"></a>

### src-000080-seev.040.001.13-p719-c001

src-000080; file p719; 12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13; scope.

> The CorporateActionInstructionCancellationRequest message is sent by an account owner to an account servicer to request cancellation of a previously sent corporate action election instruction.

<a id="src-000080-seev.042.001.14-p757-c001"></a>

### src-000080-seev.042.001.14-p757-c001

src-000080; file p757; 14 seev.042.001.14 CorporateActionInstructionStatementReportV14; scope.

> The CorporateActionInstructionStatementReport message is sent by an account servicer to an account owner or its designated agent to report balances at the safekeeping account level for one or more corporate action events or at the corporate action event level for one or more safekeeping accounts.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| seev.031.001.16 | [Exact message-role evidence](../../../domains/securities/reference/messages/seev.031.001.16/roles.md) | src-000080-seev.031.001.16-p23-c001, src-000080-seev.031.001.16-p23-c004 |
| seev.032.001.09 | [Exact message-role evidence](../../../domains/securities/reference/messages/seev.032.001.09/roles.md) | src-000080-seev.032.001.09-p266-c001, src-000080-seev.032.001.09-p266-c002 |
| seev.033.001.14 | [Exact message-role evidence](../../../domains/securities/reference/messages/seev.033.001.14/roles.md) | src-000080-seev.033.001.14-p274-c001, src-000080-seev.033.001.14-p274-c002 |
| seev.034.001.16 | [Exact message-role evidence](../../../domains/securities/reference/messages/seev.034.001.16/roles.md) | src-000080-seev.034.001.16-p320-c001, src-000080-seev.034.001.16-p320-c002, src-000080-seev.034.001.16-p320-c003 |
| seev.036.001.17 | [Exact message-role evidence](../../../domains/securities/reference/messages/seev.036.001.17/roles.md) | src-000080-seev.036.001.17-p540-c001 |
| seev.039.001.13 | [Exact message-role evidence](../../../domains/securities/reference/messages/seev.039.001.13/roles.md) | src-000080-seev.039.001.13-p701-c001 |
| seev.040.001.13 | [Exact message-role evidence](../../../domains/securities/reference/messages/seev.040.001.13/roles.md) | src-000080-seev.040.001.13-p719-c001 |
| seev.042.001.14 | [Exact message-role evidence](../../../domains/securities/reference/messages/seev.042.001.14/roles.md) | src-000080-seev.042.001.14-p757-c001 |


[Message-set flows](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `corporate`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000080](../../../evidence/omitted/dfb597659e5318b4c0abe01e.md) · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
