---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "semt.034.001.01 participant and direction evidence"
domain: "securities"
message_id: "semt.034.001.01"
message_family: "semt.034"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.034.001.01"
source_ids: ["src-000233", "src-000317", "src-000381"]
message_sets: ["t2s", "t2s-settlement-restrictions"]
role_labels: ["account owner", "account owner/request", "account servicer", "settlement infrastructure", "third party"]
search_terms: ["account owner", "account owner/request", "account servicer", "settlement infrastructure", "third party"]
participant_ids: ["participant-functionality-src-000381-account-owner-request-literal", "participant-narrative-src-000381-account-owner", "participant-narrative-src-000381-account-servicer", "participant-narrative-src-000381-third-party", "participant-src-000380-settlement-infrastructure"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "79 semt.034.001.01 IntraPositionMovementPendingReportV01", "file_pages": [2724, 2747]}, {"source_id": "src-000381", "heading": "8 semt.034.001.01 IntraPositionMovementPendingReportV01", "file_pages": [169, 192]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# semt.034.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 8 direction/initiator/exchange clauses; 5 uniquely resolved participant references.

## src-000233 — 79 semt.034.001.01 IntraPositionMovementPendingReportV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); Functionality file pp2724; publication August 2026.

### Direction and initiation clauses

#### src-000233-semt.034.001.01-p2724-c001-d1

Kind: sender-to-receiver; message applicability: **current-message-qualified-source-wording**; src-000233 file p2724, scope.

- Sender: **settlement infrastructure**. [settlement infrastructure](../../../../../shared/reference/participants/participant-src-000380-settlement-infrastructure.md).
- Receiver: **account owner/request**. [account owner/request](../../../../../shared/reference/participants/participant-functionality-src-000381-account-owner-request-literal.md).

> This IntraPositionMovementPendingReport message is sent from a settlement infrastructure to an account owner/request to report the intra-position movement instructions, previously sent by the account owner, that have a pending status.

The supplied source literally says account owner/request, confirmed in child src-000360 file page 358 or src-000381 file page 169 and preserved in the combined publication. issue-000062 records the unresolved intended role wording. This is not silently equated with requestor; Duplicate/Copy source statements retain their separate original-message scope.

#### src-000233-semt.034.001.01-p2724-c002-d1

Kind: sender-to-receiver; message applicability: **original-message-in-duplicate-option**; src-000233 file p2724, scope.

- Sender: **account owner**. [account owner](../../../../../shared/reference/participants/participant-narrative-src-000381-account-owner.md).
- Receiver: **account servicer**. [account servicer](../../../../../shared/reference/participants/participant-narrative-src-000381-account-servicer.md).

> re-send a message sent by the account owner to the account servicer (the sub-function of the message is "Duplicate")

The clause explicitly identifies the original message direction within the Duplicate/resend option; it does not establish a different sender for a forwarded copy.

#### src-000233-semt.034.001.01-p2724-c003-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000233 file p2724, scope.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-narrative-src-000381-third-party.md).

> provide a third party with a copy of a message being sent by the account owner for information (the sub-function of the message is "Copy")

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

#### src-000233-semt.034.001.01-p2724-c004-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000233 file p2724, scope.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-narrative-src-000381-third-party.md).

> re-send to a third party a copy of a message being sent by the account owner for information (the sub- function of the message is "Copy Duplicate").

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-semt.034.001.01-p2724-c001 — file p2724, scope.**

Mentioned roles: [settlement infrastructure](../../../../../shared/reference/participants/participant-src-000380-settlement-infrastructure.md); [account owner/request](../../../../../shared/reference/participants/participant-functionality-src-000381-account-owner-request-literal.md); [account owner](../../../../../shared/reference/participants/participant-narrative-src-000381-account-owner.md).

Reviewed clause disposition: **source-wording-qualification**. The exact source role wording is retained with its explicit qualification; no missing word is supplied.

Quoted above in src-000233-semt.034.001.01-p2724-c001-d1.

**src-000233-semt.034.001.01-p2724-c002 — file p2724, scope.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/participant-narrative-src-000381-account-owner.md); [account servicer](../../../../../shared/reference/participants/participant-narrative-src-000381-account-servicer.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000233-semt.034.001.01-p2724-c002-d1.

**src-000233-semt.034.001.01-p2724-c003 — file p2724, scope.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-narrative-src-000381-third-party.md); [account owner](../../../../../shared/reference/participants/participant-narrative-src-000381-account-owner.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000233-semt.034.001.01-p2724-c003-d1.

**src-000233-semt.034.001.01-p2724-c004 — file p2724, scope.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-narrative-src-000381-third-party.md); [account owner](../../../../../shared/reference/participants/participant-narrative-src-000381-account-owner.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000233-semt.034.001.01-p2724-c004-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p2724, scope.**

> The message may also be used to:

## src-000381 — 8 semt.034.001.01 IntraPositionMovementPendingReportV01

[src-000381](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`; Functionality file pp169; publication september-2025.

### Direction and initiation clauses

#### src-000381-semt.034.001.01-p169-c001-d1

Kind: sender-to-receiver; message applicability: **current-message-qualified-source-wording**; src-000381 file p169, scope.

- Sender: **settlement infrastructure**. [settlement infrastructure](../../../../../shared/reference/participants/participant-src-000380-settlement-infrastructure.md).
- Receiver: **account owner/request**. [account owner/request](../../../../../shared/reference/participants/participant-functionality-src-000381-account-owner-request-literal.md).

> This IntraPositionMovementPendingReport message is sent from a settlement infrastructure to an account owner/request to report the intra-position movement instructions, previously sent by the account owner, that have a pending status.

The supplied source literally says account owner/request, confirmed in child src-000360 file page 358 or src-000381 file page 169 and preserved in the combined publication. issue-000062 records the unresolved intended role wording. This is not silently equated with requestor; Duplicate/Copy source statements retain their separate original-message scope.

#### src-000381-semt.034.001.01-p169-c002-d1

Kind: sender-to-receiver; message applicability: **original-message-in-duplicate-option**; src-000381 file p169, scope.

- Sender: **account owner**. [account owner](../../../../../shared/reference/participants/participant-narrative-src-000381-account-owner.md).
- Receiver: **account servicer**. [account servicer](../../../../../shared/reference/participants/participant-narrative-src-000381-account-servicer.md).

> re-send a message sent by the account owner to the account servicer (the sub-function of the message is "Duplicate")

The clause explicitly identifies the original message direction within the Duplicate/resend option; it does not establish a different sender for a forwarded copy.

#### src-000381-semt.034.001.01-p169-c003-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000381 file p169, scope.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-narrative-src-000381-third-party.md).

> provide a third party with a copy of a message being sent by the account owner for information (the sub-function of the message is "Copy")

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

#### src-000381-semt.034.001.01-p169-c004-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000381 file p169, scope.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-narrative-src-000381-third-party.md).

> re-send to a third party a copy of a message being sent by the account owner for information (the sub- function of the message is "Copy Duplicate").

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000381-semt.034.001.01-p169-c001 — file p169, scope.**

Mentioned roles: [settlement infrastructure](../../../../../shared/reference/participants/participant-src-000380-settlement-infrastructure.md); [account owner/request](../../../../../shared/reference/participants/participant-functionality-src-000381-account-owner-request-literal.md); [account owner](../../../../../shared/reference/participants/participant-narrative-src-000381-account-owner.md).

Reviewed clause disposition: **source-wording-qualification**. The exact source role wording is retained with its explicit qualification; no missing word is supplied.

Quoted above in src-000381-semt.034.001.01-p169-c001-d1.

**src-000381-semt.034.001.01-p169-c002 — file p169, scope.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/participant-narrative-src-000381-account-owner.md); [account servicer](../../../../../shared/reference/participants/participant-narrative-src-000381-account-servicer.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000381-semt.034.001.01-p169-c002-d1.

**src-000381-semt.034.001.01-p169-c003 — file p169, scope.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-narrative-src-000381-third-party.md); [account owner](../../../../../shared/reference/participants/participant-narrative-src-000381-account-owner.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000381-semt.034.001.01-p169-c003-d1.

**src-000381-semt.034.001.01-p169-c004 — file p169, scope.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-narrative-src-000381-third-party.md); [account owner](../../../../../shared/reference/participants/participant-narrative-src-000381-account-owner.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000381-semt.034.001.01-p169-c004-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p169, scope.**

> The message may also be used to:

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
