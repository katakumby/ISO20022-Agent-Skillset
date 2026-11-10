---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "semt.004.001.02 participant and direction evidence"
domain: "securities"
message_id: "semt.004.001.02"
message_family: "semt.004"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.004.001.02"
source_ids: ["src-000096", "src-000116"]
message_sets: ["investment-funds"]
role_labels: ["account owner", "account servicer", "An account servicer", "authorised representative", "investment manager", "the account owner", "transfer agent"]
search_terms: ["account owner", "account servicer", "An account servicer", "authorised representative", "investment manager", "the account owner", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-authorised-representative", "participant-narrative-src-000096-account-owner", "participant-narrative-src-000096-account-servicer", "participant-narrative-src-000096-investment-manager", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "20 semt.004.001.02 CustodyStatementOfHoldingsCancellationV02", "file_pages": [398, 402]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# semt.004.001.02 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 5 uniquely resolved participant references.

## src-000096 — 20 semt.004.001.02 CustodyStatementOfHoldingsCancellationV02

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); Functionality file pp398; publication May 2026.

### Direction and initiation clauses

#### src-000096-semt.004.001.02-p398-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p398, scope.

- Sender: **An account servicer, for example, a transfer agent**. [An account servicer](../../../../../shared/reference/participants/participant-narrative-src-000096-account-servicer.md).
- Receiver: **the account owner, for example, an investment manager or its authorised representative**. [the account owner](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md).

> An account servicer, for example, a transfer agent, sends the CustodyStatementOfHoldingsCancellation message to the account owner, for example, an investment manager or its authorised representative to cancel a previously sent CustodyStatementOfHoldings message.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-semt.004.001.02-p398-c001 — file p398, scope.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/participant-narrative-src-000096-account-servicer.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [account owner](../../../../../shared/reference/participants/participant-narrative-src-000096-account-owner.md); [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000096-investment-manager.md); [authorised representative](../../../../../shared/reference/participants/participant-functionality-src-000096-authorised-representative.md).

Quoted above in src-000096-semt.004.001.02-p398-c001-d1.

**src-000096-semt.004.001.02-p398-c002 — file p398, usage.**

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> The CustodyStatementOfHoldingsCancellation message is used to cancel a previously sent CustodyStatementOfHoldings message.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p398, usage.**

> This message must contain the reference of the message to be cancelled.

**File p398, usage.**

> This message may also contain details of the message to be cancelled, but this is not recommended.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
