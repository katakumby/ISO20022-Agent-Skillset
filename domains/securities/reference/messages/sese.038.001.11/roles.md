---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "sese.038.001.11 participant and direction evidence"
domain: "securities"
message_id: "sese.038.001.11"
message_family: "sese.038"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.038.001.11"
source_ids: ["src-000197", "src-000229"]
message_sets: ["settlement-and-reconciliation"]
role_labels: ["account owner", "account servicer", "agent", "an account owner", "an account servicer", "central securities depository", "central securities depository participant", "custodian", "investment manager", "market infrastructure", "third party"]
search_terms: ["account owner", "account servicer", "agent", "an account owner", "an account servicer", "central securities depository", "central securities depository participant", "custodian", "investment manager", "market infrastructure", "third party"]
participant_ids: ["participant-functionality-src-000197-agent", "participant-functionality-src-000197-message-copy-third-party", "participant-narrative-src-000197-central-securities-depository", "participant-narrative-src-000197-central-securities-depository-participant", "participant-narrative-src-000197-custodian", "participant-narrative-src-000197-investment-manager", "participant-narrative-src-000197-market-infrastructure", "participant-settlement-reconciliation-account-owner", "participant-settlement-reconciliation-account-servicer"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000197", "heading": "32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "file_pages": [1133, 1299]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# sese.038.001.11 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 4 direction/initiator/exchange clauses; 9 uniquely resolved participant references.

## src-000197 — 32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11

[src-000197](../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf); Functionality file pp1133; publication March 2026.

### Direction and initiation clauses

#### src-000197-sese.038.001.11-p1133-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000197 file p1133, scope.

- Sender: **an account owner**. [an account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md).
- Receiver: **an account servicer**. [an account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).

> The SecuritiesSettlementTransactionModificationRequest is sent by an account owner to an account servicer.

#### src-000197-sese.038.001.11-p1133-c006-d1

Kind: sender-to-receiver; message applicability: **original-message-in-duplicate-option**; src-000197 file p1133, usage.

- Sender: **account owner**. [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md).
- Receiver: **account servicer**. [account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).

> re-send a message sent by the account owner to the account servicer,

The clause explicitly identifies the original message direction within the Duplicate/resend option; it does not establish a different sender for a forwarded copy.

#### src-000197-sese.038.001.11-p1133-c007-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000197 file p1133, usage.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md).

> provide a third party with a copy of a message being sent by the account owner for information,

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

#### src-000197-sese.038.001.11-p1133-c008-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000197 file p1133, usage.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md).

> re-send to a third party a copy of a message being sent by the account owner for information using the relevant elements in the Business Application Header.

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000197-sese.038.001.11-p1133-c001 — file p1133, scope.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md); [account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).

Quoted above in src-000197-sese.038.001.11-p1133-c001-d1.

**src-000197-sese.038.001.11-p1133-c002 — file p1133, scope.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md).

> The account owner will generally be:

**src-000197-sese.038.001.11-p1133-c003 — file p1133, scope.**

Mentioned roles: [central securities depository participant](../../../../../shared/reference/participants/participant-narrative-src-000197-central-securities-depository-participant.md); [central securities depository](../../../../../shared/reference/participants/participant-narrative-src-000197-central-securities-depository.md); [market infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000197-market-infrastructure.md).

> a central securities depository participant which has an account with a central securities depository or a market infrastructure

**src-000197-sese.038.001.11-p1133-c004 — file p1133, scope.**

Mentioned roles: [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000197-investment-manager.md); [custodian](../../../../../shared/reference/participants/participant-narrative-src-000197-custodian.md); [agent](../../../../../shared/reference/participants/participant-functionality-src-000197-agent.md).

> an investment manager which has an account with a custodian acting as accounting and/or settlement agent.

**src-000197-sese.038.001.11-p1133-c005 — file p1133, scope.**

> It is used to request the modification of non core business data (matching or non-matching) information in a pending or settled instruction.

**src-000197-sese.038.001.11-p1133-c006 — file p1133, usage.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md); [account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000197-sese.038.001.11-p1133-c006-d1.

**src-000197-sese.038.001.11-p1133-c007 — file p1133, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md); [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000197-sese.038.001.11-p1133-c007-d1.

**src-000197-sese.038.001.11-p1133-c008 — file p1133, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md); [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000197-sese.038.001.11-p1133-c008-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p1133, scope.**

> It can also be used for the enrichment of an incomplete transaction.

**File p1133, usage.**

> The modification must only contain the data to be modified.

**File p1133, usage.**

> The message may also be used to:

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
