---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "sese.009.001.09 participant and direction evidence"
domain: "securities"
message_id: "sese.009.001.09"
message_family: "sese.009"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.009.001.09"
source_ids: ["src-000096", "src-000128"]
message_sets: ["investment-funds"]
role_labels: ["an instructing party", "another party in the transfer transaction chain", "any party in the transfer transaction", "authorised representative", "executing party", "instructing party", "investment manager", "the executing party", "transfer agent"]
search_terms: ["an instructing party", "another party in the transfer transaction chain", "any party in the transfer transaction", "authorised representative", "executing party", "instructing party", "investment manager", "the executing party", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-authorised-representative", "participant-functionality-src-000096-transfer-transaction-party", "participant-narrative-src-000096-investment-manager", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "32 sese.009.001.09 RequestForTransferStatusReportV09", "file_pages": [784, 808]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# sese.009.001.09 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 6 uniquely resolved participant references.

## src-000096 — 32 sese.009.001.09 RequestForTransferStatusReportV09

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); Functionality file pp784; publication May 2026.

### Direction and initiation clauses

#### src-000096-sese.009.001.09-p784-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p784, scope.

- Sender: **an instructing party, for example, an investment manager or its authorised representative**. [an instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md).
- Receiver: **the executing party, for example, a transfer agent**. [the executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md).

> The RequestForTransferStatusReport is sent by an instructing party, for example, an investment manager or its authorised representative, to the executing party, for example, a transfer agent to request the status of a previously instructed transfer.

#### src-000096-sese.009.001.09-p784-c002-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p784, scope.

- Sender: **any party in the transfer transaction**. [any party in the transfer transaction](../../../../../shared/reference/participants/participant-functionality-src-000096-transfer-transaction-party.md).
- Receiver: **another party in the transfer transaction chain**. [another party in the transfer transaction chain](../../../../../shared/reference/participants/participant-functionality-src-000096-transfer-transaction-party.md).

> The RequestForTransferStatusReport may also be sent by any party in the transfer transaction to another party in the transfer transaction chain to request information relevant for the settlement of a transfer transaction.

The source deliberately uses generic contextual roles. No particular institution or named functional role is substituted.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-sese.009.001.09-p784-c001 — file p784, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md); [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000096-investment-manager.md); [authorised representative](../../../../../shared/reference/participants/participant-functionality-src-000096-authorised-representative.md); [executing party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md).

Quoted above in src-000096-sese.009.001.09-p784-c001-d1.

**src-000096-sese.009.001.09-p784-c002 — file p784, scope.**

Mentioned roles: [any party in the transfer transaction](../../../../../shared/reference/participants/participant-functionality-src-000096-transfer-transaction-party.md); [another party in the transfer transaction chain](../../../../../shared/reference/participants/participant-functionality-src-000096-transfer-transaction-party.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000096-sese.009.001.09-p784-c002-d1.

**src-000096-sese.009.001.09-p784-c003 — file p784, usage.**

> the status of one or several information requests or transfer instructions or,

**src-000096-sese.009.001.09-p784-c004 — file p784, usage.**

> the status of one or several transfer cancellation instructions, or

**src-000096-sese.009.001.09-p784-c005 — file p784, usage.**

> information relevant to one or more transfer instructions.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p784, usage.**

> The RequestForTransferStatusReport is used to request either:

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
