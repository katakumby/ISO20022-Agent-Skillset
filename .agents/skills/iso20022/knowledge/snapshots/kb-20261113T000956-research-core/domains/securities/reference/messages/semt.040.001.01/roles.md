---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "semt.040.001.01 participant and direction evidence"
domain: "securities"
message_id: "semt.040.001.01"
message_family: "semt.040"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.040.001.01"
source_ids: ["src-000233", "src-000318", "src-000375"]
message_sets: ["t2s", "t2s-securities-and-penalty-reporting"]
role_labels: ["a market infrastructure", "Account owner", "an instructing party", "instructing party", "market infrastructure", "sender", "third party"]
search_terms: ["a market infrastructure", "Account owner", "an instructing party", "instructing party", "market infrastructure", "sender", "third party"]
participant_ids: ["participant-functionality-src-000375-sender", "participant-narrative-src-000375-account-owner", "participant-narrative-src-000375-market-infrastructure", "participant-narrative-src-000375-third-party", "participant-src-000374-instructing-party"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "80 semt.040.001.01 SecuritiesAccountPositionResponseV01", "file_pages": [2748, 2760]}, {"source_id": "src-000375", "heading": "5 semt.040.001.01 SecuritiesAccountPositionResponseV01", "file_pages": [166, 178]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# semt.040.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 4 direction/initiator/exchange clauses; 5 uniquely resolved participant references.

## src-000233 — 80 semt.040.001.01 SecuritiesAccountPositionResponseV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); Functionality file pp2748, 2749; publication August 2026.

### Direction and initiation clauses

#### src-000233-semt.040.001.01-p2748-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p2748, scope.

- Sender: **a market infrastructure**. [a market infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000375-market-infrastructure.md).
- Receiver: **an instructing party**. [an instructing party](../../../../../shared/reference/participants/participant-src-000374-instructing-party.md).

> The SecuritiesAccountPositionResponse message is sent by a market infrastructure to an instructing party to report the securities positions for the given date period as requested in the query, for all securities across all accounts satisfying the query criteria.

#### src-000233-semt.040.001.01-p2748-c007-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000233 file p2748, usage.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-narrative-src-000375-third-party.md).

> re-send to a third party a copy of a message for information (the sub-function of the message is Copy Duplicate).

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-semt.040.001.01-p2748-c001 — file p2748, scope.**

Mentioned roles: [market infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000375-market-infrastructure.md); [instructing party](../../../../../shared/reference/participants/participant-src-000374-instructing-party.md).

Quoted above in src-000233-semt.040.001.01-p2748-c001-d1.

**src-000233-semt.040.001.01-p2748-c002 — file p2748, usage.**

> The message SecuritiesAccountPositionResponse will provide CSDs and T2S participants with a report corresponding to the SecuritiesAccountPositionQuery returning balances held in the list of specified securities accounts within the specified period satisfying the defined selection criteria.

**src-000233-semt.040.001.01-p2748-c003 — file p2748, usage.**

Mentioned roles: [Account owner](../../../../../shared/reference/participants/participant-narrative-src-000375-account-owner.md).

> Account owner

**src-000233-semt.040.001.01-p2748-c004 — file p2748, usage.**

Mentioned roles: [sender](../../../../../shared/reference/participants/participant-functionality-src-000375-sender.md).

> The free position Unless otherwise specified by the sender in the Securities Balance Query, T2S will only return non-zero securities positions in the accounts.

**src-000233-semt.040.001.01-p2748-c005 — file p2748, usage.**

Reviewed clause disposition: **resend-option-no-new-named-direction**. The source allows resending a previously sent message. This clause names no new sender or receiver; it is a usage option, not absent extraction of a direction.

> re-send a message previously sent (the sub-function of the message is Duplicate)

**src-000233-semt.040.001.01-p2748-c006 — file p2748, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-narrative-src-000375-third-party.md).

> provide a third party with a copy of a message for information (the sub-function of the message is Copy)

**src-000233-semt.040.001.01-p2748-c007 — file p2748, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-narrative-src-000375-third-party.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000233-semt.040.001.01-p2748-c007-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p2748, usage.**

> The Securities Account Position Response will provide the following business attributes:

**File p2748, usage.**

> CSD

**File p2748, usage.**

> Securities Account Number

**File p2748, usage.**

> Securities Identifier (e.g.

**File p2748, usage.**

> ISIN)

**File p2748, usage.**

> Date

**File p2748, usage.**

> The total position

**File p2748, usage.**

> The blocked position

**File p2748, usage.**

> The message may also be used to:

**File p2748, usage.**

> Approved by the Securities and Payments SEGs under the leadership of the Securities SEG and by the Cross-SEG Harmonisation for the Business File Header (last message set approved on 18 June 2026). semt.040.001.01 SecuritiesAccountPositionResponseV01 Target2-Securities 2748 August 2026

## src-000375 — 5 semt.040.001.01 SecuritiesAccountPositionResponseV01

[src-000375](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`; Functionality file pp166, 167; publication march-2026.

### Direction and initiation clauses

#### src-000375-semt.040.001.01-p166-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000375 file p166, scope.

- Sender: **a market infrastructure**. [a market infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000375-market-infrastructure.md).
- Receiver: **an instructing party**. [an instructing party](../../../../../shared/reference/participants/participant-src-000374-instructing-party.md).

> The SecuritiesAccountPositionResponse message is sent by a market infrastructure to an instructing party to report the securities positions for the given date period as requested in the query, for all securities across all accounts satisfying the query criteria.

#### src-000375-semt.040.001.01-p166-c007-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000375 file p166, usage.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-narrative-src-000375-third-party.md).

> re-send to a third party a copy of a message for information (the sub-function of the message is Copy Duplicate).

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000375-semt.040.001.01-p166-c001 — file p166, scope.**

Mentioned roles: [market infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000375-market-infrastructure.md); [instructing party](../../../../../shared/reference/participants/participant-src-000374-instructing-party.md).

Quoted above in src-000375-semt.040.001.01-p166-c001-d1.

**src-000375-semt.040.001.01-p166-c002 — file p166, usage.**

> The message SecuritiesAccountPositionResponse will provide CSDs and T2S participants with a report corresponding to the SecuritiesAccountPositionQuery returning balances held in the list of specified securities accounts within the specified period satisfying the defined selection criteria.

**src-000375-semt.040.001.01-p166-c003 — file p166, usage.**

Mentioned roles: [Account owner](../../../../../shared/reference/participants/participant-narrative-src-000375-account-owner.md).

> Account owner

**src-000375-semt.040.001.01-p166-c004 — file p166, usage.**

Mentioned roles: [sender](../../../../../shared/reference/participants/participant-functionality-src-000375-sender.md).

> The free position Unless otherwise specified by the sender in the Securities Balance Query, T2S will only return non-zero securities positions in the accounts.

**src-000375-semt.040.001.01-p166-c005 — file p166, usage.**

Reviewed clause disposition: **resend-option-no-new-named-direction**. The source allows resending a previously sent message. This clause names no new sender or receiver; it is a usage option, not absent extraction of a direction.

> re-send a message previously sent (the sub-function of the message is Duplicate)

**src-000375-semt.040.001.01-p166-c006 — file p166, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-narrative-src-000375-third-party.md).

> provide a third party with a copy of a message for information (the sub-function of the message is Copy)

**src-000375-semt.040.001.01-p166-c007 — file p166, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-narrative-src-000375-third-party.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000375-semt.040.001.01-p166-c007-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p166, usage.**

> The Securities Account Position Response will provide the following business attributes:

**File p166, usage.**

> CSD

**File p166, usage.**

> Securities Account Number

**File p166, usage.**

> Securities Identifier (e.g.

**File p166, usage.**

> ISIN)

**File p166, usage.**

> Date

**File p166, usage.**

> The total position

**File p166, usage.**

> The blocked position

**File p166, usage.**

> The message may also be used to:

**File p166, usage.**

> Approved by the Securities SEG 19 February 2026. semt.040.001.01 SecuritiesAccountPositionResponseV01 Target2-Securities - Securities and Penalty Reporting 166 March 2026

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
