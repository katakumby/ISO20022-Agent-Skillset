---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "semt.001.001.03 participant and direction evidence"
domain: "securities"
message_id: "semt.001.001.03"
message_family: "semt.001"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.001.001.03"
source_ids: ["src-000096", "src-000113"]
message_sets: ["investment-funds"]
role_labels: ["account owner", "account servicer", "agent", "An account servicer", "authorised representative", "bank", "custodian", "executing party", "instructing party", "investment manager", "investor", "Receiver", "receiver", "registrar", "Sender", "the account owner", "transfer agent"]
search_terms: ["account owner", "account servicer", "agent", "An account servicer", "authorised representative", "bank", "custodian", "executing party", "instructing party", "investment manager", "investor", "Receiver", "receiver", "registrar", "Sender", "the account owner", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-agent", "participant-functionality-src-000096-authorised-representative", "participant-functionality-src-000096-recipient", "participant-functionality-src-000096-sender", "participant-narrative-src-000096-account-owner", "participant-narrative-src-000096-account-servicer", "participant-narrative-src-000096-bank", "participant-narrative-src-000096-investment-manager", "participant-narrative-src-000096-investor", "participant-narrative-src-000096-registrar", "participant-src-000095-custodian", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "17 semt.001.001.03 SecuritiesMessageRejectionV03", "file_pages": [371, 374]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# semt.001.001.03 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 14 uniquely resolved participant references.

## src-000096 — 17 semt.001.001.03 SecuritiesMessageRejectionV03

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); Functionality file pp371; publication May 2026.

### Direction and initiation clauses

#### src-000096-semt.001.001.03-p371-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p371, scope.

- Sender: **An account servicer, for example, a registrar, transfer agent or custodian bank**. [An account servicer](../../../../../shared/reference/participants/participant-narrative-src-000096-account-servicer.md).
- Receiver: **the account owner, for example, an investor or its authorised agent**. [the account owner](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md).

> An account servicer, for example, a registrar, transfer agent or custodian bank, sends the SecuritiesMessageRejection message to the account owner, for example, an investor or its authorised agent, to reject a previously received message on which action cannot be taken.

#### src-000096-semt.001.001.03-p371-c002-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p371, scope.

- Sender: **executing party**. [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).
- Receiver: **instructing party**. [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md).

> The message may also be sent by an executing party, for example, transfer agent to the instructing party, for example, investment manager or its authorised representative to reject a previously received message on which action cannot be taken.

Alternative rejection direction; transfer agent, investment manager and authorised representative remain source examples rather than universal identities.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-semt.001.001.03-p371-c001 — file p371, scope.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/participant-narrative-src-000096-account-servicer.md); [registrar](../../../../../shared/reference/participants/participant-narrative-src-000096-registrar.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [custodian](../../../../../shared/reference/participants/participant-src-000095-custodian.md); [bank](../../../../../shared/reference/participants/participant-narrative-src-000096-bank.md); [account owner](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md); [investor](../../../../../shared/reference/participants/participant-narrative-src-000096-investor.md); [agent](../../../../../shared/reference/participants/participant-functionality-src-000096-agent.md).

Quoted above in src-000096-semt.001.001.03-p371-c001-d1.

**src-000096-semt.001.001.03-p371-c002 — file p371, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md); [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000096-investment-manager.md); [authorised representative](../../../../../shared/reference/participants/participant-functionality-src-000096-authorised-representative.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000096-semt.001.001.03-p371-c002-d1.

**src-000096-semt.001.001.03-p371-c003 — file p371, usage.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md); [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).

> the executing party does not recognise the linked reference, so the executing party cannot process the message

**src-000096-semt.001.001.03-p371-c004 — file p371, usage.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md).

Reviewed clause disposition: **actor-or-condition-context**. The sentence describes actors, responsibilities, source/target data, prohibitions or conditions. Existing literal actions and the complete quote remain available; sending/receiving a different object or a negative assertion is not converted into an unconditional current-message direction.

> the instructing party should not have sent the message.

**src-000096-semt.001.001.03-p371-c005 — file p371, usage.**

Mentioned roles: [receiver](../../../../../shared/reference/participants/participant-functionality-src-000096-recipient.md); [Sender](../../../../../shared/reference/participants/participant-functionality-src-000096-sender.md); [Receiver](../../../../../shared/reference/participants/participant-functionality-src-000096-recipient.md).

Reviewed clause disposition: **actor-or-condition-context**. The sentence describes actors, responsibilities, source/target data, prohibitions or conditions. Existing literal actions and the complete quote remain available; sending/receiving a different object or a negative assertion is not converted into an unconditional current-message direction.

> Reasons that a receiver does not expect a message include no SLA in place between the Sender and the Receiver.

**src-000096-semt.001.001.03-p371-c006 — file p371, usage.**

> The SecuritiesMessageRejection message must not be used to reject an instruction message that cannot be processed for business reasons, for example, if information is missing in an instruction message or because securities are not available for settlement.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p371, usage.**

> The SecuritiesMessageRejection message is used for the following reasons:

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
