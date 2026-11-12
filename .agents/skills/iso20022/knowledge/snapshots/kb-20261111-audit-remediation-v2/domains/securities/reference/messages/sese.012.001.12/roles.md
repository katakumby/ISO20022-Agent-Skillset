---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "sese.012.001.12 participant and direction evidence"
domain: "securities"
message_id: "sese.012.001.12"
message_family: "sese.012"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.012.001.12"
source_ids: ["src-000096", "src-000131"]
message_sets: ["investment-funds"]
role_labels: ["an instructing party", "corporate", "executing party", "initiating party", "instructing party", "investor", "investors", "the executing party", "transferee", "transferor"]
search_terms: ["an instructing party", "corporate", "executing party", "initiating party", "instructing party", "investor", "investors", "the executing party", "transferee", "transferor"]
participant_ids: ["participant-narrative-src-000096-corporate", "participant-narrative-src-000096-initiating-party", "participant-narrative-src-000096-investor", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-transferee", "participant-src-000095-transferor"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "35 sese.012.001.12 PortfolioTransferInstructionV12", "file_pages": [943, 1105]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# sese.012.001.12 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 7 uniquely resolved participant references.

## src-000096 — 35 sese.012.001.12 PortfolioTransferInstructionV12

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); Functionality file pp943, 944; publication May 2026.

### Direction and initiation clauses

#### src-000096-sese.012.001.12-p943-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p943, scope.

- Sender: **an instructing party, for example, a (new) plan manager (transferee)**. [an instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md).
- Receiver: **the executing party, for example, a (old) plan manager (transferor), on behalf of the initiating party, for example, an investor (client)**. [the executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).

> The PortfolioTransferInstruction message is sent by an instructing party, for example, a (new) plan manager (transferee), to the executing party, for example, a (old) plan manager (transferor), on behalf of the initiating party, for example, an investor (client), to instruct the transfer of financial instruments from the client's account at the old plan manager (transferor) to the clients account at the new plan manager (transferee).

#### src-000096-sese.012.001.12-p943-c004-d1

Kind: receiver-only; message applicability: **related-or-unspecified-message**; src-000096 file p943, usage.

- Receiver: **the executing party**. [the executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).

> If the instructing party does not have enough information to instruct the portfolio transfer, then it must first send an AccountHoldingInformationRequest message to the executing party in order to receive an AccountHoldingInformation message.

Sender is a pronoun/reference in this clause; it is retained in the quote and is not resolved automatically.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-sese.012.001.12-p943-c001 — file p943, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md); [transferee](../../../../../shared/reference/participants/participant-src-000095-transferee.md); [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md); [transferor](../../../../../shared/reference/participants/participant-src-000095-transferor.md); [initiating party](../../../../../shared/reference/participants/participant-narrative-src-000096-initiating-party.md); [investor](../../../../../shared/reference/participants/participant-narrative-src-000096-investor.md); [transferor](../../../../../shared/reference/participants/participant-src-000095-transferor.md); [transferee](../../../../../shared/reference/participants/participant-src-000095-transferee.md).

Quoted above in src-000096-sese.012.001.12-p943-c001-d1.

**src-000096-sese.012.001.12-p943-c002 — file p943, usage.**

> The PortfolioTransferInstruction message is used to instruct one or more portfolio transfers for one client.

**src-000096-sese.012.001.12-p943-c003 — file p943, usage.**

Mentioned roles: [investors](../../../../../shared/reference/participants/participant-narrative-src-000096-investor.md); [corporate](../../../../../shared/reference/participants/participant-narrative-src-000096-corporate.md); [investors](../../../../../shared/reference/participants/participant-narrative-src-000096-investor.md).

> The account may be owned by one or more individual investors or one or more corporate investors.

**src-000096-sese.012.001.12-p943-c004 — file p943, usage.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md); [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).

Quoted above in src-000096-sese.012.001.12-p943-c004-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p943, usage.**

> Each portfolio transfer is for delivery to the same account.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
