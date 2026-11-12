---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.072.001.02 participant and direction evidence"
domain: "securities"
message_id: "camt.072.001.02"
message_family: "camt.072"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.072.001.02"
source_ids: ["src-000233", "src-000245", "src-000360"]
message_sets: ["t2s", "t2s-intra-balance-movement"]
role_labels: ["a settlement infrastructure", "account owner/requestor", "an account owner/requestor", "settlement infrastructure", "third party"]
search_terms: ["a settlement infrastructure", "account owner/requestor", "an account owner/requestor", "settlement infrastructure", "third party"]
participant_ids: ["participant-narrative-src-000360-account-owner-requestor", "participant-src-000359-settlement-infrastructure", "participant-src-000359-third-party"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "10 camt.072.001.02 IntraBalanceMovementModificationRequestV02", "file_pages": [149, 172]}, {"source_id": "src-000360", "heading": "5 camt.072.001.02 IntraBalanceMovementModificationRequestV02", "file_pages": [66, 89]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.072.001.02 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 4 direction/initiator/exchange clauses; 3 uniquely resolved participant references.

## src-000233 — 10 camt.072.001.02 IntraBalanceMovementModificationRequestV02

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); Functionality file pp149, 150; publication August 2026.

### Direction and initiation clauses

#### src-000233-camt.072.001.02-p149-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p149, scope.

- Sender: **an account owner/requestor**. [an account owner/requestor](../../../../../shared/reference/participants/participant-narrative-src-000360-account-owner-requestor.md).
- Receiver: **a settlement infrastructure**. [a settlement infrastructure](../../../../../shared/reference/participants/participant-src-000359-settlement-infrastructure.md).

> The IntraBalanceMovementModificationRequest message is sent from an account owner/requestor to a settlement infrastructure to request the modification of a processing indicator on a previously sent IntraBalanceMovementInstruction message.

#### src-000233-camt.072.001.02-p149-c004-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000233 file p149, usage.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-src-000359-third-party.md).

> re-send to a third party a copy of a message for information (the sub-function of the message is "CopyDuplicate").

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-camt.072.001.02-p149-c001 — file p149, scope.**

Mentioned roles: [account owner/requestor](../../../../../shared/reference/participants/participant-narrative-src-000360-account-owner-requestor.md); [settlement infrastructure](../../../../../shared/reference/participants/participant-src-000359-settlement-infrastructure.md).

Quoted above in src-000233-camt.072.001.02-p149-c001-d1.

**src-000233-camt.072.001.02-p149-c002 — file p149, usage.**

Reviewed clause disposition: **resend-option-no-new-named-direction**. The source allows resending a previously sent message. This clause names no new sender or receiver; it is a usage option, not absent extraction of a direction.

> re-send a message previously sent (the sub-function of the message is "Duplicate")

**src-000233-camt.072.001.02-p149-c003 — file p149, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-src-000359-third-party.md).

> provide a third party with a copy of a message for information (the sub-function of the message is "Copy")

**src-000233-camt.072.001.02-p149-c004 — file p149, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-src-000359-third-party.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000233-camt.072.001.02-p149-c004-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p149, usage.**

> The message may be used to:

## src-000360 — 5 camt.072.001.02 IntraBalanceMovementModificationRequestV02

[src-000360](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`; Functionality file pp66, 67; publication march-2024.

### Direction and initiation clauses

#### src-000360-camt.072.001.02-p66-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000360 file p66, scope.

- Sender: **an account owner/requestor**. [an account owner/requestor](../../../../../shared/reference/participants/participant-narrative-src-000360-account-owner-requestor.md).
- Receiver: **a settlement infrastructure**. [a settlement infrastructure](../../../../../shared/reference/participants/participant-src-000359-settlement-infrastructure.md).

> The IntraBalanceMovementModificationRequest message is sent from an account owner/requestor to a settlement infrastructure to request the modification of a processing indicator on a previously sent IntraBalanceMovementInstruction message.

#### src-000360-camt.072.001.02-p66-c004-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000360 file p66, usage.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-src-000359-third-party.md).

> re-send to a third party a copy of a message for information (the sub-function of the message is "CopyDuplicate").

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000360-camt.072.001.02-p66-c001 — file p66, scope.**

Mentioned roles: [account owner/requestor](../../../../../shared/reference/participants/participant-narrative-src-000360-account-owner-requestor.md); [settlement infrastructure](../../../../../shared/reference/participants/participant-src-000359-settlement-infrastructure.md).

Quoted above in src-000360-camt.072.001.02-p66-c001-d1.

**src-000360-camt.072.001.02-p66-c002 — file p66, usage.**

Reviewed clause disposition: **resend-option-no-new-named-direction**. The source allows resending a previously sent message. This clause names no new sender or receiver; it is a usage option, not absent extraction of a direction.

> re-send a message previously sent (the sub-function of the message is "Duplicate")

**src-000360-camt.072.001.02-p66-c003 — file p66, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-src-000359-third-party.md).

> provide a third party with a copy of a message for information (the sub-function of the message is "Copy")

**src-000360-camt.072.001.02-p66-c004 — file p66, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-src-000359-third-party.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000360-camt.072.001.02-p66-c004-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p66, usage.**

> The message may be used to:

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
