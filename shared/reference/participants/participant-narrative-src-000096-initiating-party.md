---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000096-initiating-party"
title: "Initiating Party — Investment Funds narrative scope"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
source_labels: ["initiating party"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["investment-funds"]
message_ids: ["sese.012.001.12", "sese.019.001.09"]
message_families: ["sese.012", "sese.019"]
flows: []
source_locations: [{"source_id": "src-000096", "heading": "35 sese.012.001.12 PortfolioTransferInstructionV12", "file_pages": [943], "evidence_id": "src-000096-sese.012.001.12-p943-c001"}, {"source_id": "src-000096", "heading": "39 sese.019.001.09 AccountHoldingInformationRequestV09", "file_pages": [1442], "evidence_id": "src-000096-sese.019.001.09-p1442-c001"}]
search_terms: ["initiating party"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Initiating Party — Investment Funds

## Definition and applicable context

This source names **initiating party** in the Functionality of the messages listed below. The record is scoped to Investment Funds, May 2026. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The PortfolioTransferInstruction message is sent by an instructing party, for example, a (new) plan manager (transferee), to the executing party, for example, a (old) plan manager (transferor), on behalf of the initiating party, for example, an investor (client), to instruct the transfer of financial instruments from the client's account at the old plan manager (transferor) to the clients account at the new plan manager (transferee).

src-000096, file p943, 35 sese.012.001.12 PortfolioTransferInstructionV12, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

No complete directed clause was assigned to this exact role label; the narrative evidence still establishes its stated context.

## Complete source evidence

<a id="src-000096-sese.012.001.12-p943-c001"></a>

### src-000096-sese.012.001.12-p943-c001

src-000096; file p943; 35 sese.012.001.12 PortfolioTransferInstructionV12; scope.

> The PortfolioTransferInstruction message is sent by an instructing party, for example, a (new) plan manager (transferee), to the executing party, for example, a (old) plan manager (transferor), on behalf of the initiating party, for example, an investor (client), to instruct the transfer of financial instruments from the client's account at the old plan manager (transferor) to the clients account at the new plan manager (transferee).

<a id="src-000096-sese.019.001.09-p1442-c001"></a>

### src-000096-sese.019.001.09-p1442-c001

src-000096; file p1442; 39 sese.019.001.09 AccountHoldingInformationRequestV09; scope.

> The AccountHoldingInformationRequest message is sent by an instructing party, for example, a (new) plan manager (transferee), to the executing party, for example, a (old) plan manager (transferor), on behalf of the initiating party, for example, an investor (client), to request information about financial instruments held on behalf of the client.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| sese.012.001.12 | [Exact message-role evidence](../../../domains/securities/reference/messages/sese.012.001.12/roles.md) | src-000096-sese.012.001.12-p943-c001 |
| sese.019.001.09 | [Exact message-role evidence](../../../domains/securities/reference/messages/sese.019.001.09/roles.md) | src-000096-sese.019.001.09-p1442-c001 |


[Message-set flows](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `initiating party`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000096](../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf) · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
