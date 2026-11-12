---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000378-servicing-party"
title: "Servicing Party — T2S SecuritiesReferenceData narrative scope"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
source_labels: ["servicing party"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["t2s-securities-reference-data"]
message_ids: ["reda.006.001.01", "reda.007.001.01", "reda.010.001.01", "reda.013.001.01"]
message_families: ["reda.006", "reda.007", "reda.010", "reda.013"]
flows: []
source_locations: [{"source_id": "src-000378", "heading": "2 reda.006.001.01 SecurityCreationRequestV01", "file_pages": [8], "evidence_id": "src-000378-reda.006.001.01-p8-c008"}, {"source_id": "src-000378", "heading": "3 reda.007.001.01 SecurityMaintenanceRequestV01", "file_pages": [21], "evidence_id": "src-000378-reda.007.001.01-p21-c007"}, {"source_id": "src-000378", "heading": "3 reda.007.001.01 SecurityMaintenanceRequestV01", "file_pages": [21], "evidence_id": "src-000378-reda.007.001.01-p21-c008"}, {"source_id": "src-000378", "heading": "6 reda.010.001.01 SecurityQueryV01", "file_pages": [77], "evidence_id": "src-000378-reda.010.001.01-p77-c007"}, {"source_id": "src-000378", "heading": "8 reda.013.001.01 SecurityDeletionRequestV01", "file_pages": [115], "evidence_id": "src-000378-reda.013.001.01-p115-c008"}]
search_terms: ["servicing party"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Servicing Party — T2S SecuritiesReferenceData

## Definition and applicable context

This source names **servicing party** in the Functionality of the messages listed below. The record is scoped to T2S SecuritiesReferenceData, March 2024. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The instructing party needs this security to be set-up at the executing / servicing party to perform its activities.

src-000378, file p8, 2 reda.006.001.01 SecurityCreationRequestV01, usage. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

No complete directed clause was assigned to this exact role label; the narrative evidence still establishes its stated context.

## Complete source evidence

<a id="src-000378-reda.006.001.01-p8-c008"></a>

### src-000378-reda.006.001.01-p8-c008

src-000378; file p8; 2 reda.006.001.01 SecurityCreationRequestV01; usage.

> The instructing party needs this security to be set-up at the executing / servicing party to perform its activities.

<a id="src-000378-reda.007.001.01-p21-c007"></a>

### src-000378-reda.007.001.01-p21-c007

src-000378; file p21; 3 reda.007.001.01 SecurityMaintenanceRequestV01; usage.

> The request is sent when the instructing party identified a gap in the security data within the executing/ servicing party system.

<a id="src-000378-reda.007.001.01-p21-c008"></a>

### src-000378-reda.007.001.01-p21-c008

src-000378; file p21; 3 reda.007.001.01 SecurityMaintenanceRequestV01; usage.

> The instructing party needs this security to be updated at the executing / servicing party to perform its activities.

<a id="src-000378-reda.010.001.01-p77-c007"></a>

### src-000378-reda.010.001.01-p77-c007

src-000378; file p77; 6 reda.010.001.01 SecurityQueryV01; usage.

> The request is sent when the instructing party needs to see data of a security data within the executing/ servicing party system.

<a id="src-000378-reda.013.001.01-p115-c008"></a>

### src-000378-reda.013.001.01-p115-c008

src-000378; file p115; 8 reda.013.001.01 SecurityDeletionRequestV01; usage.

> The instructing party needs this security to be removed from the executing /servicing party database.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| reda.006.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.006.001.01/roles.md) | src-000378-reda.006.001.01-p8-c008 |
| reda.007.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.007.001.01/roles.md) | src-000378-reda.007.001.01-p21-c007, src-000378-reda.007.001.01-p21-c008 |
| reda.010.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.010.001.01/roles.md) | src-000378-reda.010.001.01-p77-c007 |
| reda.013.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.013.001.01/roles.md) | src-000378-reda.013.001.01-p115-c008 |


[Message-set reference](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/march-2024/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `servicing party`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000378](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf` · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
