---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000346-system-transaction-administrator"
title: "System Transaction Administrator — T2S Billing narrative scope"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
source_labels: ["system transaction administrator"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["t2s-billing"]
message_ids: ["camt.076.001.01", "camt.077.001.01"]
message_families: ["camt.076", "camt.077"]
flows: []
source_locations: [{"source_id": "src-000346", "heading": "2 camt.076.001.01 BillingReportRequestV01", "file_pages": [4], "evidence_id": "src-000346-camt.076.001.01-p4-c001"}, {"source_id": "src-000346", "heading": "3 camt.077.001.01 BillingReportV01", "file_pages": [11], "evidence_id": "src-000346-camt.077.001.01-p11-c001"}]
search_terms: ["system transaction administrator"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# System Transaction Administrator — T2S Billing

## Definition and applicable context

This source names **system transaction administrator** in the Functionality of the messages listed below. The record is scoped to T2S Billing, december-2025. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The BillingReportRequest message is sent by the system member to the system transaction administrator to request cumulative or itemised billing data.

src-000346, file p4, 2 camt.076.001.01 BillingReportRequestV01, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

| This participant in clause | Source message subject | Message applicability | Other roles / source expressions | Evidence |
| --- | --- | --- | --- | --- |
| receiver | The BillingReportRequest message | current-message | sender: the system member ([the system member](participant-narrative-src-000346-system-member.md)); receiver: the system transaction administrator ([the system transaction administrator](participant-narrative-src-000346-system-transaction-administrator.md)) | [src-000346-camt.076.001.01-p4-c001-d1](#src-000346-camt.076.001.01-p4-c001); file p4 |
| exchange_participants | The BillingReport message | current-message | exchange_participants: the system transaction administrator and a system member ([the system transaction administrator](participant-narrative-src-000346-system-transaction-administrator.md); [a system member](participant-narrative-src-000346-system-member.md)) | [src-000346-camt.077.001.01-p11-c001-d1](#src-000346-camt.077.001.01-p11-c001); file p11 |


## Complete source evidence

<a id="src-000346-camt.076.001.01-p4-c001"></a>

### src-000346-camt.076.001.01-p4-c001

src-000346; file p4; 2 camt.076.001.01 BillingReportRequestV01; scope.

> The BillingReportRequest message is sent by the system member to the system transaction administrator to request cumulative or itemised billing data.

<a id="src-000346-camt.077.001.01-p11-c001"></a>

### src-000346-camt.077.001.01-p11-c001

src-000346; file p11; 3 camt.077.001.01 BillingReportV01; scope.

> The BillingReport message is exchanged between the system transaction administrator and a system member.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| camt.076.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/camt.076.001.01/roles.md) | src-000346-camt.076.001.01-p4-c001 |
| camt.077.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/camt.077.001.01/roles.md) | src-000346-camt.077.001.01-p11-c001 |


[Message-set flows](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `system transaction administrator`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000346](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf` · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
