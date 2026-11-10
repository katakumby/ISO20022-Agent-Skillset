---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "payments"
participant_id: "participant-narrative-src-000005-bank"
title: "Bank — Bank-to-Customer Cash Management narrative scope"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
source_labels: ["Bank", "banks"]
aliases: []
role_type: "business role or institutional example in quoted Functionality context"
message_sets: ["bank-to-customer-cash-management"]
message_ids: ["camt.052.001.14", "camt.053.001.14"]
message_families: ["camt.052", "camt.053"]
flows: []
source_locations: [{"source_id": "src-000005", "heading": "2 camt.052.001.14 BankToCustomerAccountReportV14", "file_pages": [4], "evidence_id": "src-000005-camt.052.001.14-p4-c004"}, {"source_id": "src-000005", "heading": "3 camt.053.001.14 BankToCustomerStatementV14", "file_pages": [263], "evidence_id": "src-000005-camt.053.001.14-p263-c004"}]
search_terms: ["Bank", "bank", "banks"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Bank — Bank-to-Customer Cash Management

## Definition and applicable context

This source names **bank** in the Functionality of the messages listed below. The record is scoped to Bank-to-Customer Cash Management, March 2026. Classification: business role or institutional example in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> For a statement, the Bank-to-Customer Account Statement message should be used.

src-000005, file p4, 2 camt.052.001.14 BankToCustomerAccountReportV14, usage. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

No complete directed clause was assigned to this exact role label; the narrative evidence still establishes its stated context.

## Complete source evidence

<a id="src-000005-camt.052.001.14-p4-c004"></a>

### src-000005-camt.052.001.14-p4-c004

src-000005; file p4; 2 camt.052.001.14 BankToCustomerAccountReportV14; usage.

> For a statement, the Bank-to-Customer Account Statement message should be used.

<a id="src-000005-camt.053.001.14-p263-c004"></a>

### src-000005-camt.053.001.14-p263-c004

src-000005; file p263; 3 camt.053.001.14 BankToCustomerStatementV14; usage.

> Depending on services and schedule agreed between banks and their customers, statements may be generated and exchanged accordingly, for example for intraday or prior day periods.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| camt.052.001.14 | [Exact message-role evidence](../../../domains/payments/reference/messages/camt.052.001.14/roles.md) | src-000005-camt.052.001.14-p4-c004 |
| camt.053.001.14 | [Exact message-role evidence](../../../domains/payments/reference/messages/camt.053.001.14/roles.md) | src-000005-camt.053.001.14-p263-c004 |


[Message-set flows](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `Bank`, `banks`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000005](../../../evidence/omitted/4704d0f065c82a397d84d52d.md) · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
