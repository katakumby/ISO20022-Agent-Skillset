---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "seev.031.001.16 participant and direction evidence"
domain: "securities"
message_id: "seev.031.001.16"
message_family: "seev.031"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.031.001.16"
source_ids: ["src-000080", "src-000082"]
message_sets: ["corporate-actions"]
role_labels: ["account owner", "account servicer", "an account owner", "an account servicer", "corporate", "its designated agent", "third party"]
search_terms: ["account owner", "account servicer", "an account owner", "an account servicer", "corporate", "its designated agent", "third party"]
participant_ids: ["participant-corporate-actions-designated-agent", "participant-narrative-src-000080-corporate", "participant-narrative-src-000080-third-party", "participant-src-000079-account-owner", "participant-src-000079-account-servicer"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000080", "heading": "3 seev.031.001.16 CorporateActionNotificationV16", "file_pages": [23, 265]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# seev.031.001.16 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 4 direction/initiator/exchange clauses; 5 uniquely resolved participant references.

## src-000080 — 3 seev.031.001.16 CorporateActionNotificationV16

[src-000080](../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md); Functionality file pp23, 24, 25; publication February 2026.

### Direction and initiation clauses

#### src-000080-seev.031.001.16-p23-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000080 file p23, scope.

- Sender: **an account servicer**. [an account servicer](../../../../../shared/reference/participants/participant-src-000079-account-servicer.md).
- Receiver: **an account owner or its designated agent**. [an account owner](../../../../../shared/reference/participants/participant-src-000079-account-owner.md); [its designated agent](../../../../../shared/reference/participants/participant-corporate-actions-designated-agent.md).

> The CorporateActionNotification message is sent by an account servicer to an account owner or its designated agent to notify details of a corporate action event and optionally account information and preliminary information about eligible balance and entitlements.

#### src-000080-seev.031.001.16-p23-c003-d1

Kind: sender-only; message applicability: **current-message**; src-000080 file p23, scope.

- Sender: **account servicer**. [account servicer](../../../../../shared/reference/participants/participant-src-000079-account-servicer.md).

> The account servicer can initially send the CorporateActionNotification message as a preliminary advice, subsequently replaced by another CorporateActionNotification message with complete or confirmed information.

Source explicitly names the sender. Scheduling, warning/preliminary usage and information content remain in the quote; no receiver is supplied by this clause.

#### src-000080-seev.031.001.16-p23-c004-d1

Kind: receiver-only; message applicability: **current-message-local-anaphoric-option**; src-000080 file p23, scope.

- Receiver: **account owner or its designated agent**. [account owner](../../../../../shared/reference/participants/participant-src-000079-account-owner.md); [its designated agent](../../../../../shared/reference/participants/participant-corporate-actions-designated-agent.md).

> It may also be sent to an account owner or its designated agent, to remind of event details and/or of missing or incomplete instructions for a corporate action event.

In the CorporateActionNotification Functionality, “It” continues the immediately preceding notification statement. This is the reminder option for event details or missing/incomplete instructions.

#### src-000080-seev.031.001.16-p23-c007-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000080 file p23, usage.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-narrative-src-000080-third-party.md).

> re-send to a third party a copy of a message for information (the sub-function of the message is Copy Duplicate), using the relevant elements in the business application header (BAH).

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000080-seev.031.001.16-p23-c001 — file p23, scope.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/participant-src-000079-account-servicer.md); [account owner](../../../../../shared/reference/participants/participant-src-000079-account-owner.md); [its designated agent](../../../../../shared/reference/participants/participant-corporate-actions-designated-agent.md); [corporate](../../../../../shared/reference/participants/participant-narrative-src-000080-corporate.md).

Quoted above in src-000080-seev.031.001.16-p23-c001-d1.

**src-000080-seev.031.001.16-p23-c002 — file p23, scope.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/participant-src-000079-account-owner.md).

> It may also include possible elections or choices available to the account owner.

**src-000080-seev.031.001.16-p23-c003 — file p23, scope.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/participant-src-000079-account-servicer.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000080-seev.031.001.16-p23-c003-d1.

**src-000080-seev.031.001.16-p23-c004 — file p23, scope.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/participant-src-000079-account-owner.md); [its designated agent](../../../../../shared/reference/participants/participant-corporate-actions-designated-agent.md); [corporate](../../../../../shared/reference/participants/participant-narrative-src-000080-corporate.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000080-seev.031.001.16-p23-c004-d1.

**src-000080-seev.031.001.16-p23-c005 — file p23, usage.**

Reviewed clause disposition: **resend-option-no-new-named-direction**. The source allows resending a previously sent message. This clause names no new sender or receiver; it is a usage option, not absent extraction of a direction.

> re-send a message previously sent (the sub-function of the message is Duplicate),

**src-000080-seev.031.001.16-p23-c006 — file p23, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-narrative-src-000080-third-party.md).

> provide a third party with a copy of a message for information (the sub-function of the message is Copy),

**src-000080-seev.031.001.16-p23-c007 — file p23, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-narrative-src-000080-third-party.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000080-seev.031.001.16-p23-c007-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p23, usage.**

> The message may also be used to:

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
