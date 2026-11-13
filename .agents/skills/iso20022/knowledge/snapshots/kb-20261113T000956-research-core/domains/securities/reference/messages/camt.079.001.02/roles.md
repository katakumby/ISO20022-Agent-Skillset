---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.079.001.02 participant and direction evidence"
domain: "securities"
message_id: "camt.079.001.02"
message_family: "camt.079"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.079.001.02"
source_ids: ["src-000233", "src-000252", "src-000360"]
message_sets: ["t2s", "t2s-intra-balance-movement"]
role_labels: ["a settlement infrastructure", "account owner", "account owner/requestor", "account servicer", "an account owner/requestor", "settlement infrastructure", "third party"]
search_terms: ["a settlement infrastructure", "account owner", "account owner/requestor", "account servicer", "an account owner/requestor", "settlement infrastructure", "third party"]
participant_ids: ["participant-narrative-src-000360-account-owner", "participant-narrative-src-000360-account-owner-requestor", "participant-narrative-src-000360-account-servicer", "participant-src-000359-settlement-infrastructure", "participant-src-000359-third-party"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "17 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "file_pages": [381, 422]}, {"source_id": "src-000360", "heading": "10 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "file_pages": [190, 231]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.079.001.02 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 8 direction/initiator/exchange clauses; 5 uniquely resolved participant references.

## src-000233 — 17 camt.079.001.02 IntraBalanceMovementQueryResponseV02

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); Functionality file pp381; publication August 2026.

### Direction and initiation clauses

#### src-000233-camt.079.001.02-p381-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p381, scope.

- Sender: **a settlement infrastructure**. [a settlement infrastructure](../../../../../shared/reference/participants/participant-src-000359-settlement-infrastructure.md).
- Receiver: **an account owner/requestor**. [an account owner/requestor](../../../../../shared/reference/participants/participant-narrative-src-000360-account-owner-requestor.md).

> The IntraBalanceMovementQueryResponse message is sent from a settlement infrastructure to an account owner/requestor to provide all intra-balance movement instructions satisfying the selection criteria, as defined within the query, returning current attributes and latest status.

#### src-000233-camt.079.001.02-p381-c002-d1

Kind: sender-to-receiver; message applicability: **original-message-in-duplicate-option**; src-000233 file p381, scope.

- Sender: **account owner**. [account owner](../../../../../shared/reference/participants/participant-narrative-src-000360-account-owner.md).
- Receiver: **account servicer**. [account servicer](../../../../../shared/reference/participants/participant-narrative-src-000360-account-servicer.md).

> re-send a message sent by the account owner to the account servicer (the sub-function of the message is "Duplicate")

The clause explicitly identifies the original message direction within the Duplicate/resend option; it does not establish a different sender for a forwarded copy.

#### src-000233-camt.079.001.02-p381-c003-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000233 file p381, scope.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-src-000359-third-party.md).

> provide a third party with a copy of a message being sent by the account owner for information (the sub-function of the message is "Copy")

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

#### src-000233-camt.079.001.02-p381-c004-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000233 file p381, scope.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-src-000359-third-party.md).

> re-send to a third party a copy of a message being sent by the account owner for information (the sub- function of the message is "Copy Duplicate").

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-camt.079.001.02-p381-c001 — file p381, scope.**

Mentioned roles: [settlement infrastructure](../../../../../shared/reference/participants/participant-src-000359-settlement-infrastructure.md); [account owner/requestor](../../../../../shared/reference/participants/participant-narrative-src-000360-account-owner-requestor.md).

Quoted above in src-000233-camt.079.001.02-p381-c001-d1.

**src-000233-camt.079.001.02-p381-c002 — file p381, scope.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/participant-narrative-src-000360-account-owner.md); [account servicer](../../../../../shared/reference/participants/participant-narrative-src-000360-account-servicer.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000233-camt.079.001.02-p381-c002-d1.

**src-000233-camt.079.001.02-p381-c003 — file p381, scope.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-src-000359-third-party.md); [account owner](../../../../../shared/reference/participants/participant-narrative-src-000360-account-owner.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000233-camt.079.001.02-p381-c003-d1.

**src-000233-camt.079.001.02-p381-c004 — file p381, scope.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-src-000359-third-party.md); [account owner](../../../../../shared/reference/participants/participant-narrative-src-000360-account-owner.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000233-camt.079.001.02-p381-c004-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p381, scope.**

> The message may also be used to:

## src-000360 — 10 camt.079.001.02 IntraBalanceMovementQueryResponseV02

[src-000360](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`; Functionality file pp190; publication march-2024.

### Direction and initiation clauses

#### src-000360-camt.079.001.02-p190-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000360 file p190, scope.

- Sender: **a settlement infrastructure**. [a settlement infrastructure](../../../../../shared/reference/participants/participant-src-000359-settlement-infrastructure.md).
- Receiver: **an account owner/requestor**. [an account owner/requestor](../../../../../shared/reference/participants/participant-narrative-src-000360-account-owner-requestor.md).

> The IntraBalanceMovementQueryResponse message is sent from a settlement infrastructure to an account owner/requestor to provide all intra-balance movement instructions satisfying the selection criteria, as defined within the query, returning current attributes and latest status.

#### src-000360-camt.079.001.02-p190-c002-d1

Kind: sender-to-receiver; message applicability: **original-message-in-duplicate-option**; src-000360 file p190, scope.

- Sender: **account owner**. [account owner](../../../../../shared/reference/participants/participant-narrative-src-000360-account-owner.md).
- Receiver: **account servicer**. [account servicer](../../../../../shared/reference/participants/participant-narrative-src-000360-account-servicer.md).

> re-send a message sent by the account owner to the account servicer (the sub-function of the message is "Duplicate")

The clause explicitly identifies the original message direction within the Duplicate/resend option; it does not establish a different sender for a forwarded copy.

#### src-000360-camt.079.001.02-p190-c003-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000360 file p190, scope.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-src-000359-third-party.md).

> provide a third party with a copy of a message being sent by the account owner for information (the sub-function of the message is "Copy")

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

#### src-000360-camt.079.001.02-p190-c004-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000360 file p190, scope.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-src-000359-third-party.md).

> re-send to a third party a copy of a message being sent by the account owner for information (the sub- function of the message is "Copy Duplicate").

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000360-camt.079.001.02-p190-c001 — file p190, scope.**

Mentioned roles: [settlement infrastructure](../../../../../shared/reference/participants/participant-src-000359-settlement-infrastructure.md); [account owner/requestor](../../../../../shared/reference/participants/participant-narrative-src-000360-account-owner-requestor.md).

Quoted above in src-000360-camt.079.001.02-p190-c001-d1.

**src-000360-camt.079.001.02-p190-c002 — file p190, scope.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/participant-narrative-src-000360-account-owner.md); [account servicer](../../../../../shared/reference/participants/participant-narrative-src-000360-account-servicer.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000360-camt.079.001.02-p190-c002-d1.

**src-000360-camt.079.001.02-p190-c003 — file p190, scope.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-src-000359-third-party.md); [account owner](../../../../../shared/reference/participants/participant-narrative-src-000360-account-owner.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000360-camt.079.001.02-p190-c003-d1.

**src-000360-camt.079.001.02-p190-c004 — file p190, scope.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-src-000359-third-party.md); [account owner](../../../../../shared/reference/participants/participant-narrative-src-000360-account-owner.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000360-camt.079.001.02-p190-c004-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p190, scope.**

> The message may also be used to:

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
