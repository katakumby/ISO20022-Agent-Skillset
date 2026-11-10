---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "payments"
participant_id: "participant-narrative-src-000015-account-servicer"
title: "Account Servicer — Cash Management narrative scope"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
source_labels: ["account servicer"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["cash-management"]
message_ids: ["camt.017.001.05"]
message_families: ["camt.017"]
flows: []
source_locations: [{"source_id": "src-000015", "heading": "16 camt.017.001.05 ReturnCurrencyExchangeRateV05", "file_pages": [511], "evidence_id": "src-000015-camt.017.001.05-p511-c003"}]
search_terms: ["account servicer"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Account Servicer — Cash Management

## Definition and applicable context

This source names **account servicer** in the Functionality of the messages listed below. The record is scoped to Cash Management, February 2025. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The ReturnCurrencyExchangeRate message can be sent as a response to a related GetCurrencyExchangeRate message (pull mode) or initiated by the account servicer (push mode).

src-000015, file p511, 16 camt.017.001.05 ReturnCurrencyExchangeRateV05, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

| This participant in clause | Source message subject | Message applicability | Other roles / source expressions | Evidence |
| --- | --- | --- | --- | --- |
| initiator | The ReturnCurrencyExchangeRate message can be sent as a response to a related GetCurrencyExchangeRate message (pull mode) or | current-message | initiator: the account servicer (push mode) ([the account servicer](participant-narrative-src-000015-account-servicer.md)) | [src-000015-camt.017.001.05-p511-c003-d1](#src-000015-camt.017.001.05-p511-c003); file p511 |


Literal action verbs: initiated. Their objects, conditions and message context are preserved in the quoted evidence, rather than inferred from the verb alone.

## Complete source evidence

<a id="src-000015-camt.017.001.05-p511-c003"></a>

### src-000015-camt.017.001.05-p511-c003

src-000015; file p511; 16 camt.017.001.05 ReturnCurrencyExchangeRateV05; scope.

> The ReturnCurrencyExchangeRate message can be sent as a response to a related GetCurrencyExchangeRate message (pull mode) or initiated by the account servicer (push mode).

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| camt.017.001.05 | [Exact message-role evidence](../../../domains/payments/reference/messages/camt.017.001.05/roles.md) | src-000015-camt.017.001.05-p511-c003 |


[Message-set flows](../../../domains/payments/reference/message-sets/cash-management/2024-2025/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `account servicer`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000015](../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf) · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
