---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "semt.003.001.12 participant and direction evidence"
domain: "securities"
message_id: "semt.003.001.12"
message_family: "semt.003"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.003.001.12"
source_ids: ["src-000197", "src-000200"]
message_sets: ["settlement-and-reconciliation"]
role_labels: ["account owner", "account servicer", "agent", "an account owner", "An account servicer", "designated agent", "intermediary", "third party", "transfer agent"]
search_terms: ["account owner", "account servicer", "agent", "an account owner", "An account servicer", "designated agent", "intermediary", "third party", "transfer agent"]
participant_ids: ["participant-functionality-src-000197-agent", "participant-functionality-src-000197-message-copy-third-party", "participant-narrative-src-000197-designated-agent", "participant-narrative-src-000197-intermediary", "participant-narrative-src-000197-transfer-agent", "participant-settlement-reconciliation-account-owner", "participant-settlement-reconciliation-account-servicer"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000197", "heading": "3 semt.003.001.12 SecuritiesBalanceAccountingReportV12", "file_pages": [78, 134]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# semt.003.001.12 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 7 uniquely resolved participant references.

## src-000197 — 3 semt.003.001.12 SecuritiesBalanceAccountingReportV12

[src-000197](../../../../../evidence/omitted/e96bb98c659322ed5684b325.md); Functionality file pp78, 79; publication March 2026.

### Direction and initiation clauses

#### src-000197-semt.003.001.12-p78-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000197 file p78, scope.

- Sender: **An account servicer**. [An account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).
- Receiver: **an account owner**. [an account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md).

> An account servicer sends a SecuritiesBalanceAccountingReport to an account owner to provide, at a moment in time, valuations of the portfolio together with details of each financial instrument holding.

#### src-000197-semt.003.001.12-p78-c010-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000197 file p78, usage.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md).

> re-send to a third party a copy of a message for information using the relevant elements in the Business Application Header.

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000197-semt.003.001.12-p78-c001 — file p78, scope.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md); [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md).

Literal actions: account servicer sends.

Quoted above in src-000197-semt.003.001.12-p78-c001-d1.

**src-000197-semt.003.001.12-p78-c002 — file p78, scope.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).

> The account servicer/owner relationship may be:

**src-000197-semt.003.001.12-p78-c003 — file p78, scope.**

Mentioned roles: [agent](../../../../../shared/reference/participants/participant-functionality-src-000197-agent.md); [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md).

> an accounting agent acting on behalf of an account owner, or

**src-000197-semt.003.001.12-p78-c004 — file p78, scope.**

Mentioned roles: [transfer agent](../../../../../shared/reference/participants/participant-narrative-src-000197-transfer-agent.md); [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md); [designated agent](../../../../../shared/reference/participants/participant-narrative-src-000197-designated-agent.md).

> a transfer agent acting on behalf of a fund manager or an account owner's designated agent.

**src-000197-semt.003.001.12-p78-c005 — file p78, usage.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md); [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md).

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> The message should be sent at a frequency agreed bi-laterally between the account servicer and the account owner.

**src-000197-semt.003.001.12-p78-c006 — file p78, usage.**

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> The message can be sent either audited or un-audited and may be provided on a trade date, contractual or settlement date basis.

**src-000197-semt.003.001.12-p78-c007 — file p78, usage.**

Mentioned roles: [intermediary](../../../../../shared/reference/participants/participant-narrative-src-000197-intermediary.md); [intermediary](../../../../../shared/reference/participants/participant-narrative-src-000197-intermediary.md); [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md); [account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).

> There may be one or more intermediary parties, for example, an intermediary or a concentrator between the account owner and account servicer.

**src-000197-semt.003.001.12-p78-c008 — file p78, usage.**

Reviewed clause disposition: **resend-option-no-new-named-direction**. The source allows resending a previously sent message. This clause names no new sender or receiver; it is a usage option, not absent extraction of a direction.

> re-send a message previously sent,

**src-000197-semt.003.001.12-p78-c009 — file p78, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md).

> provide a third party with a copy of a message for information,

**src-000197-semt.003.001.12-p78-c010 — file p78, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000197-semt.003.001.12-p78-c010-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p78, usage.**

> This message can only be used to list the holdings of a single (master) account.

**File p78, usage.**

> However, it is possible to break down these holdings into one or several sub-accounts.

**File p78, usage.**

> Therefore, the message can be used to either specify holdings at

**File p78, usage.**

> the main account level, or,

**File p78, usage.**

> the sub-account level.

**File p78, usage.**

> This message can be used to report where the financial instruments are safe-kept, physically or notionally.

**File p78, usage.**

> If a security is held in more than one safekeeping place, this can also be indicated.

**File p78, usage.**

> The SecuritiesBalanceAccountingReport message should not be used for trading purposes.

**File p78, usage.**

> The message may also be used to:

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
