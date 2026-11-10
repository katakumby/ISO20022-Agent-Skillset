---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000366-servicing-party"
title: "Servicing Party — T2S LinkReferenceData narrative scope"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
source_labels: ["servicing party"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["t2s-link-reference-data"]
message_ids: ["reda.045.001.01", "reda.050.001.01"]
message_families: ["reda.045", "reda.050"]
flows: []
source_locations: [{"source_id": "src-000366", "heading": "2 reda.045.001.01 SecurityCSDLinkCreationRequestV01", "file_pages": [6], "evidence_id": "src-000366-reda.045.001.01-p6-c009"}, {"source_id": "src-000366", "heading": "6 reda.050.001.01 AccountLinkMaintenanceRequestV01", "file_pages": [41], "evidence_id": "src-000366-reda.050.001.01-p41-c001"}, {"source_id": "src-000366", "heading": "6 reda.050.001.01 AccountLinkMaintenanceRequestV01", "file_pages": [41], "evidence_id": "src-000366-reda.050.001.01-p41-c009"}]
search_terms: ["servicing party"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Servicing Party — T2S LinkReferenceData

## Definition and applicable context

This source names **servicing party** in the Functionality of the messages listed below. The record is scoped to T2S LinkReferenceData, december-2024. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The instructing party needs this security CSD Link to be set-up at the executing /servicing party to perform its activities.

src-000366, file p6, 2 reda.045.001.01 SecurityCSDLinkCreationRequestV01, usage. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

No complete directed clause was assigned to this exact role label; the narrative evidence still establishes its stated context.

## Complete source evidence

<a id="src-000366-reda.045.001.01-p6-c009"></a>

### src-000366-reda.045.001.01-p6-c009

src-000366; file p6; 2 reda.045.001.01 SecurityCSDLinkCreationRequestV01; usage.

> The instructing party needs this security CSD Link to be set-up at the executing /servicing party to perform its activities.

<a id="src-000366-reda.050.001.01-p41-c001"></a>

### src-000366-reda.050.001.01-p41-c001

src-000366; file p41; 6 reda.050.001.01 AccountLinkMaintenanceRequestV01; scope.

> The AccountLinkMaintenanceRequest message is sent by the instructing party to the executing/ servicing party to request for the maintenance of an account link in their system.

<a id="src-000366-reda.050.001.01-p41-c009"></a>

### src-000366-reda.050.001.01-p41-c009

src-000366; file p41; 6 reda.050.001.01 AccountLinkMaintenanceRequestV01; usage.

> The instructing party needs this account link to be maintained at the executing /servicing party to perform its activities.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| reda.045.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.045.001.01/roles.md) | src-000366-reda.045.001.01-p6-c009 |
| reda.050.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.050.001.01/roles.md) | src-000366-reda.050.001.01-p41-c001, src-000366-reda.050.001.01-p41-c009 |


[Message-set flows](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `servicing party`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000366](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf` · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
