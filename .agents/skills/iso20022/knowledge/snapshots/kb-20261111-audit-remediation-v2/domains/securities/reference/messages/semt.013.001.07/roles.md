---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "semt.013.001.07 participant and direction evidence"
domain: "securities"
message_id: "semt.013.001.07"
message_family: "semt.013"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.013.001.07"
source_ids: ["src-000197", "src-000201"]
message_sets: ["settlement-and-reconciliation"]
role_labels: ["account owner", "account servicer", "agent", "An account owner", "an account servicer", "broker", "central securities depository", "central securities depository participant", "custodian", "global custodian", "investment management institution", "settlement market infrastructure", "sub-custodian", "third party"]
search_terms: ["account owner", "account servicer", "agent", "An account owner", "an account servicer", "broker", "central securities depository", "central securities depository participant", "custodian", "global custodian", "investment management institution", "settlement market infrastructure", "sub-custodian", "third party"]
participant_ids: ["participant-functionality-src-000197-agent", "participant-functionality-src-000197-message-copy-third-party", "participant-narrative-src-000197-broker", "participant-narrative-src-000197-central-securities-depository", "participant-narrative-src-000197-central-securities-depository-participant", "participant-narrative-src-000197-custodian", "participant-narrative-src-000197-global-custodian", "participant-narrative-src-000197-investment-management-institution", "participant-narrative-src-000197-settlement-market-infrastructure", "participant-narrative-src-000197-sub-custodian", "participant-settlement-reconciliation-account-owner", "participant-settlement-reconciliation-account-servicer"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000197", "heading": "4 semt.013.001.07 IntraPositionMovementInstructionV07", "file_pages": [135, 149]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# semt.013.001.07 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 12 uniquely resolved participant references.

## src-000197 — 4 semt.013.001.07 IntraPositionMovementInstructionV07

[src-000197](../../../../../evidence/omitted/e96bb98c659322ed5684b325.md); Functionality file pp135, 136; publication March 2026.

### Direction and initiation clauses

#### src-000197-semt.013.001.07-p135-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000197 file p135, scope.

- Sender: **An account owner**. [An account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md).
- Receiver: **an account servicer**. [an account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).

> An account owner sends a IntraPositionMovementInstruction to an account servicer to instruct the movement of securities within its holding from one sub-balance to another, for example, blocking of securities.

#### src-000197-semt.013.001.07-p135-c010-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000197 file p135, usage.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md).

> re-send to a third party a copy of a message for information. using the relevant elements in the Business Application Header.

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000197-semt.013.001.07-p135-c001 — file p135, scope.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md); [account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).

Literal actions: account owner sends.

Quoted above in src-000197-semt.013.001.07-p135-c001-d1.

**src-000197-semt.013.001.07-p135-c002 — file p135, scope.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md).

> The account owner/servicer relationship may be:

**src-000197-semt.013.001.07-p135-c003 — file p135, scope.**

Mentioned roles: [global custodian](../../../../../shared/reference/participants/participant-narrative-src-000197-global-custodian.md); [agent](../../../../../shared/reference/participants/participant-functionality-src-000197-agent.md); [sub-custodian](../../../../../shared/reference/participants/participant-narrative-src-000197-sub-custodian.md).

> a global custodian which has an account with its local agent (sub-custodian), or

**src-000197-semt.013.001.07-p135-c004 — file p135, scope.**

Mentioned roles: [investment management institution](../../../../../shared/reference/participants/participant-narrative-src-000197-investment-management-institution.md); [custodian](../../../../../shared/reference/participants/participant-narrative-src-000197-custodian.md).

> an investment management institution which manage a fund account opened at a custodian, or

**src-000197-semt.013.001.07-p135-c005 — file p135, scope.**

Mentioned roles: [broker](../../../../../shared/reference/participants/participant-narrative-src-000197-broker.md); [custodian](../../../../../shared/reference/participants/participant-narrative-src-000197-custodian.md).

> a broker which has an account with a custodian, or

**src-000197-semt.013.001.07-p135-c006 — file p135, scope.**

Mentioned roles: [central securities depository participant](../../../../../shared/reference/participants/participant-narrative-src-000197-central-securities-depository-participant.md); [central securities depository](../../../../../shared/reference/participants/participant-narrative-src-000197-central-securities-depository.md).

> a central securities depository participant which has an account with a central securities depository, or

**src-000197-semt.013.001.07-p135-c007 — file p135, scope.**

Mentioned roles: [central securities depository](../../../../../shared/reference/participants/participant-narrative-src-000197-central-securities-depository.md); [custodian](../../../../../shared/reference/participants/participant-narrative-src-000197-custodian.md); [central securities depository](../../../../../shared/reference/participants/participant-narrative-src-000197-central-securities-depository.md); [settlement market infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000197-settlement-market-infrastructure.md).

> a central securities depository which has an account with a custodian, another central securities depository or another settlement market infrastructure.

**src-000197-semt.013.001.07-p135-c008 — file p135, usage.**

Reviewed clause disposition: **resend-option-no-new-named-direction**. The source allows resending a previously sent message. This clause names no new sender or receiver; it is a usage option, not absent extraction of a direction.

> re-send a message previously sent,

**src-000197-semt.013.001.07-p135-c009 — file p135, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md).

> provide a third party with a copy of a message for information,

**src-000197-semt.013.001.07-p135-c010 — file p135, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000197-semt.013.001.07-p135-c010-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p135, usage.**

> The message may also be used to:

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
