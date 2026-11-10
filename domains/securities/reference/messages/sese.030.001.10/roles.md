---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "sese.030.001.10 participant and direction evidence"
domain: "securities"
message_id: "sese.030.001.10"
message_family: "sese.030"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.030.001.10"
source_ids: ["src-000197", "src-000221"]
message_sets: ["settlement-and-reconciliation"]
role_labels: ["account owner", "account servicer", "agent", "An account owner", "an account servicer", "broker", "central securities depository", "central securities depository participant", "custodian", "global custodian", "investment management institution", "market infrastructures", "settlement market infrastructure", "sub-custodian", "third party"]
search_terms: ["account owner", "account servicer", "agent", "An account owner", "an account servicer", "broker", "central securities depository", "central securities depository participant", "custodian", "global custodian", "investment management institution", "market infrastructures", "settlement market infrastructure", "sub-custodian", "third party"]
participant_ids: ["participant-functionality-src-000197-agent", "participant-functionality-src-000197-message-copy-third-party", "participant-narrative-src-000197-broker", "participant-narrative-src-000197-central-securities-depository", "participant-narrative-src-000197-central-securities-depository-participant", "participant-narrative-src-000197-custodian", "participant-narrative-src-000197-global-custodian", "participant-narrative-src-000197-investment-management-institution", "participant-narrative-src-000197-market-infrastructure", "participant-narrative-src-000197-settlement-market-infrastructure", "participant-narrative-src-000197-sub-custodian", "participant-settlement-reconciliation-account-owner", "participant-settlement-reconciliation-account-servicer"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000197", "heading": "24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10", "file_pages": [783, 801]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# sese.030.001.10 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 13 uniquely resolved participant references.

## src-000197 — 24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10

[src-000197](../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf); Functionality file pp783, 784; publication March 2026.

### Direction and initiation clauses

#### src-000197-sese.030.001.10-p783-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000197 file p783, scope.

- Sender: **An account owner**. [An account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md).
- Receiver: **an account servicer**. [an account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).

> An account owner sends a SecuritiesSettlementConditionsModificationRequest to an account servicer to request the modification of a processing indicator or another non-matching information.

#### src-000197-sese.030.001.10-p783-c010-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000197 file p783, usage.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md).

> re-send to a third party a copy of a message for information using the relevant elements in the Business Application Header.

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000197-sese.030.001.10-p783-c001 — file p783, scope.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md); [account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).

Literal actions: account owner sends.

Quoted above in src-000197-sese.030.001.10-p783-c001-d1.

**src-000197-sese.030.001.10-p783-c002 — file p783, scope.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md).

> The account owner/servicer relationship may be:

**src-000197-sese.030.001.10-p783-c003 — file p783, scope.**

Mentioned roles: [central securities depository participant](../../../../../shared/reference/participants/participant-narrative-src-000197-central-securities-depository-participant.md); [central securities depository](../../../../../shared/reference/participants/participant-narrative-src-000197-central-securities-depository.md).

> a central securities depository participant which has an account with a central securities depository.

**src-000197-sese.030.001.10-p783-c004 — file p783, scope.**

Mentioned roles: [global custodian](../../../../../shared/reference/participants/participant-narrative-src-000197-global-custodian.md); [agent](../../../../../shared/reference/participants/participant-functionality-src-000197-agent.md); [sub-custodian](../../../../../shared/reference/participants/participant-narrative-src-000197-sub-custodian.md).

> a global custodian which has an account with its local agent (sub-custodian), or

**src-000197-sese.030.001.10-p783-c005 — file p783, scope.**

Mentioned roles: [investment management institution](../../../../../shared/reference/participants/participant-narrative-src-000197-investment-management-institution.md); [custodian](../../../../../shared/reference/participants/participant-narrative-src-000197-custodian.md).

> an investment management institution which manage a fund account opened at a custodian, or

**src-000197-sese.030.001.10-p783-c006 — file p783, scope.**

Mentioned roles: [broker](../../../../../shared/reference/participants/participant-narrative-src-000197-broker.md); [custodian](../../../../../shared/reference/participants/participant-narrative-src-000197-custodian.md).

> a broker which has an account with a custodian, or

**src-000197-sese.030.001.10-p783-c007 — file p783, scope.**

Mentioned roles: [central securities depository](../../../../../shared/reference/participants/participant-narrative-src-000197-central-securities-depository.md); [custodian](../../../../../shared/reference/participants/participant-narrative-src-000197-custodian.md); [central securities depository](../../../../../shared/reference/participants/participant-narrative-src-000197-central-securities-depository.md); [settlement market infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000197-settlement-market-infrastructure.md).

> a central securities depository which has an account with a custodian, another central securities depository or another settlement market infrastructure.

**src-000197-sese.030.001.10-p783-c008 — file p783, usage.**

Reviewed clause disposition: **resend-option-no-new-named-direction**. The source allows resending a previously sent message. This clause names no new sender or receiver; it is a usage option, not absent extraction of a direction.

> re-send a message previously sent,

**src-000197-sese.030.001.10-p783-c009 — file p783, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md).

> provide a third party with a copy of a message for information,

**src-000197-sese.030.001.10-p783-c010 — file p783, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000197-sese.030.001.10-p783-c010-d1.

**src-000197-sese.030.001.10-p783-c011 — file p783, usage.**

Mentioned roles: [market infrastructures](../../../../../shared/reference/participants/participant-narrative-src-000197-market-infrastructure.md).

> In markets where this applies (for example, securities market infrastructures with no pre-settlement matching process), it is used by a party to approve, cancel or reject a transaction instructed by the counterparty.

**src-000197-sese.030.001.10-p783-c012 — file p783, usage.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md); [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md).

> The use of AdditionalInformation and its fields must be pre-agreed between account servicer and account owner.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p783, scope.**

> It could also be, if agreed in a service level agreement:

**File p783, usage.**

> The message may also be used to:

**File p783, usage.**

> This message cannot be used to request the modification of trade or event details.

**File p783, usage.**

> The fields in that sequence cannot be used to amend a trade or event detail unless authorised by country market practice.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
