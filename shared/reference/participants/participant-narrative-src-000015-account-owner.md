---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "payments"
participant_id: "participant-narrative-src-000015-account-owner"
title: "Account Owner — Cash Management narrative scope"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
source_labels: ["account owner"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["cash-management"]
message_ids: ["camt.023.001.07", "camt.024.001.08", "camt.069.001.05"]
message_families: ["camt.023", "camt.024", "camt.069"]
flows: []
source_locations: [{"source_id": "src-000015", "heading": "21 camt.023.001.07 BackupPaymentV07", "file_pages": [577], "evidence_id": "src-000015-camt.023.001.07-p577-c009"}, {"source_id": "src-000015", "heading": "21 camt.023.001.07 BackupPaymentV07", "file_pages": [577], "evidence_id": "src-000015-camt.023.001.07-p577-c010"}, {"source_id": "src-000015", "heading": "22 camt.024.001.08 ModifyStandingOrderV08", "file_pages": [591], "evidence_id": "src-000015-camt.024.001.08-p591-c004"}, {"source_id": "src-000015", "heading": "30 camt.069.001.05 GetStandingOrderV05", "file_pages": [686], "evidence_id": "src-000015-camt.069.001.05-p686-c003"}]
search_terms: ["account owner"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Account Owner — Cash Management

## Definition and applicable context

This source names **account owner** in the Functionality of the messages listed below. The record is scoped to Cash Management, February 2025. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> party (account owner) that will receive the funds

src-000015, file p577, 21 camt.023.001.07 BackupPaymentV07, usage. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

No complete directed clause was assigned to this exact role label; the narrative evidence still establishes its stated context.

## Complete source evidence

<a id="src-000015-camt.023.001.07-p577-c009"></a>

### src-000015-camt.023.001.07-p577-c009

src-000015; file p577; 21 camt.023.001.07 BackupPaymentV07; usage.

> party (account owner) that will receive the funds

<a id="src-000015-camt.023.001.07-p577-c010"></a>

### src-000015-camt.023.001.07-p577-c010

src-000015; file p577; 21 camt.023.001.07 BackupPaymentV07; usage.

> the financial institution that will receive the funds on behalf of the account owner Based on the criteria received within the BackupPayment message, the transaction administrator will execute or reject the requested funds transfer.

<a id="src-000015-camt.024.001.08-p591-c004"></a>

### src-000015-camt.024.001.08-p591-c004

src-000015; file p591; 22 camt.024.001.08 ModifyStandingOrderV08; usage.

> account owner (for on behalf scenario)

<a id="src-000015-camt.069.001.05-p686-c003"></a>

### src-000015-camt.069.001.05-p686-c003

src-000015; file p686; 30 camt.069.001.05 GetStandingOrderV05; usage.

> account owner (for on behalf scenario)

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| camt.023.001.07 | [Exact message-role evidence](../../../domains/payments/reference/messages/camt.023.001.07/roles.md) | src-000015-camt.023.001.07-p577-c009, src-000015-camt.023.001.07-p577-c010 |
| camt.024.001.08 | [Exact message-role evidence](../../../domains/payments/reference/messages/camt.024.001.08/roles.md) | src-000015-camt.024.001.08-p591-c004 |
| camt.069.001.05 | [Exact message-role evidence](../../../domains/payments/reference/messages/camt.069.001.05/roles.md) | src-000015-camt.069.001.05-p686-c003 |


[Message-set flows](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `account owner`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000015](../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf) · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
