---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "semt.025.001.01 participant and direction evidence"
domain: "securities"
message_id: "semt.025.001.01"
message_family: "semt.025"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.025.001.01"
source_ids: ["src-000233", "src-000308", "src-000375"]
message_sets: ["t2s", "t2s-securities-and-penalty-reporting"]
role_labels: ["account owner", "account servicer", "an account owner", "an account servicer", "servicing party", "third party"]
search_terms: ["account owner", "account servicer", "an account owner", "an account servicer", "servicing party", "third party"]
participant_ids: ["participant-narrative-src-000375-account-owner", "participant-narrative-src-000375-account-servicer", "participant-narrative-src-000375-third-party", "participant-src-000374-servicing-party"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "70 semt.025.001.01 SecuritiesAccountPositionQueryV01", "file_pages": [2401, 2408]}, {"source_id": "src-000375", "heading": "2 semt.025.001.01 SecuritiesAccountPositionQueryV01", "file_pages": [5, 12]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# semt.025.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 4 direction/initiator/exchange clauses; 4 uniquely resolved participant references.

## src-000233 — 70 semt.025.001.01 SecuritiesAccountPositionQueryV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); Functionality file pp2401; publication August 2026.

### Direction and initiation clauses

#### src-000233-semt.025.001.01-p2401-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p2401, scope.

- Sender: **an account owner**. [an account owner](../../../../../shared/reference/participants/participant-narrative-src-000375-account-owner.md).
- Receiver: **an account servicer or servicing party**. [an account servicer](../../../../../shared/reference/participants/participant-narrative-src-000375-account-servicer.md); [servicing party](../../../../../shared/reference/participants/participant-src-000374-servicing-party.md).

> The SecuritiesAccountPositionQuery message is sent by an account owner to an account servicer or servicing party to request an account view on the position at a particular point in time period, or during a particular time period, where all positions are summarised in the account structure that is compatible with the query.

#### src-000233-semt.025.001.01-p2401-c003-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000233 file p2401, usage.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-narrative-src-000375-third-party.md).

> provide a third party with a copy of a message for information (the sub-function of the message is Copy), -re-send to a third party a copy of a message for information (the sub-function of the message is CopyDuplicate).

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-semt.025.001.01-p2401-c001 — file p2401, scope.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/participant-narrative-src-000375-account-owner.md); [account servicer](../../../../../shared/reference/participants/participant-narrative-src-000375-account-servicer.md); [servicing party](../../../../../shared/reference/participants/participant-src-000374-servicing-party.md).

Quoted above in src-000233-semt.025.001.01-p2401-c001-d1.

**src-000233-semt.025.001.01-p2401-c002 — file p2401, usage.**

Reviewed clause disposition: **resend-option-no-new-named-direction**. The source allows resending a previously sent message. This clause names no new sender or receiver; it is a usage option, not absent extraction of a direction.

> The message may also be used to: -re-send a message previously sent (the sub-function of the message is Duplicate),

**src-000233-semt.025.001.01-p2401-c003 — file p2401, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-narrative-src-000375-third-party.md); [third party](../../../../../shared/reference/participants/participant-narrative-src-000375-third-party.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000233-semt.025.001.01-p2401-c003-d1.

## src-000375 — 2 semt.025.001.01 SecuritiesAccountPositionQueryV01

[src-000375](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`; Functionality file pp5; publication march-2026.

### Direction and initiation clauses

#### src-000375-semt.025.001.01-p5-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000375 file p5, scope.

- Sender: **an account owner**. [an account owner](../../../../../shared/reference/participants/participant-narrative-src-000375-account-owner.md).
- Receiver: **an account servicer or servicing party**. [an account servicer](../../../../../shared/reference/participants/participant-narrative-src-000375-account-servicer.md); [servicing party](../../../../../shared/reference/participants/participant-src-000374-servicing-party.md).

> The SecuritiesAccountPositionQuery message is sent by an account owner to an account servicer or servicing party to request an account view on the position at a particular point in time period, or during a particular time period, where all positions are summarised in the account structure that is compatible with the query.

#### src-000375-semt.025.001.01-p5-c003-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000375 file p5, usage.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-narrative-src-000375-third-party.md).

> provide a third party with a copy of a message for information (the sub-function of the message is Copy), -re-send to a third party a copy of a message for information (the sub-function of the message is CopyDuplicate).

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000375-semt.025.001.01-p5-c001 — file p5, scope.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/participant-narrative-src-000375-account-owner.md); [account servicer](../../../../../shared/reference/participants/participant-narrative-src-000375-account-servicer.md); [servicing party](../../../../../shared/reference/participants/participant-src-000374-servicing-party.md).

Quoted above in src-000375-semt.025.001.01-p5-c001-d1.

**src-000375-semt.025.001.01-p5-c002 — file p5, usage.**

Reviewed clause disposition: **resend-option-no-new-named-direction**. The source allows resending a previously sent message. This clause names no new sender or receiver; it is a usage option, not absent extraction of a direction.

> The message may also be used to: -re-send a message previously sent (the sub-function of the message is Duplicate),

**src-000375-semt.025.001.01-p5-c003 — file p5, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-narrative-src-000375-third-party.md); [third party](../../../../../shared/reference/participants/participant-narrative-src-000375-third-party.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000375-semt.025.001.01-p5-c003-d1.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
