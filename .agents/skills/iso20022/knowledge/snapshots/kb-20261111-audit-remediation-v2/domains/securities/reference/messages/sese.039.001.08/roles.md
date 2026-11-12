---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "sese.039.001.08 participant and direction evidence"
domain: "securities"
message_id: "sese.039.001.08"
message_family: "sese.039"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.039.001.08"
source_ids: ["src-000197", "src-000230"]
message_sets: ["settlement-and-reconciliation"]
role_labels: ["account owner", "account servicer", "agent", "an account owner", "An account servicer", "central securities depository", "custodian", "settlement market infrastructure", "third party"]
search_terms: ["account owner", "account servicer", "agent", "an account owner", "An account servicer", "central securities depository", "custodian", "settlement market infrastructure", "third party"]
participant_ids: ["participant-functionality-src-000197-agent", "participant-functionality-src-000197-message-copy-third-party", "participant-narrative-src-000197-central-securities-depository", "participant-narrative-src-000197-custodian", "participant-narrative-src-000197-settlement-market-infrastructure", "participant-settlement-reconciliation-account-owner", "participant-settlement-reconciliation-account-servicer"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000197", "heading": "33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08", "file_pages": [1300, 1321]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# sese.039.001.08 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 4 direction/initiator/exchange clauses; 7 uniquely resolved participant references.

## src-000197 — 33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08

[src-000197](../../../../../evidence/omitted/e96bb98c659322ed5684b325.md); Functionality file pp1300, 1301; publication March 2026.

### Direction and initiation clauses

#### src-000197-sese.039.001.08-p1300-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000197 file p1300, scope.

- Sender: **An account servicer**. [An account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).
- Receiver: **an account owner**. [an account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md).

> An account servicer sends a SecuritiesSettlementTransactionModificationRequestStatusAdvice to an account owner to advise the status of a SecuritiesSettlementModificationRequest message previously sent by the account owner.

#### src-000197-sese.039.001.08-p1300-c005-d1

Kind: sender-to-receiver; message applicability: **original-message-in-duplicate-option**; src-000197 file p1300, usage.

- Sender: **account owner**. [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md).
- Receiver: **account servicer**. [account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).

> re-send a message sent by the account owner to the account servicer,

The clause explicitly identifies the original message direction within the Duplicate/resend option; it does not establish a different sender for a forwarded copy.

#### src-000197-sese.039.001.08-p1300-c006-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000197 file p1300, usage.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md).

> provide a third party with a copy of a message being sent by the account owner for information,

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

#### src-000197-sese.039.001.08-p1300-c007-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000197 file p1300, usage.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md).

> re-send to a third party a copy of a message being sent by the account owner for information using the relevant elements in the Business Application Header.

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000197-sese.039.001.08-p1300-c001 — file p1300, scope.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md); [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md); [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md).

Literal actions: account servicer sends.

Quoted above in src-000197-sese.039.001.08-p1300-c001-d1.

**src-000197-sese.039.001.08-p1300-c002 — file p1300, scope.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).

> The account servicer may be:

**src-000197-sese.039.001.08-p1300-c003 — file p1300, scope.**

Mentioned roles: [central securities depository](../../../../../shared/reference/participants/participant-narrative-src-000197-central-securities-depository.md); [settlement market infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000197-settlement-market-infrastructure.md).

> a central securities depository or another settlement market infrastructure managing securities settlement transactions on behalf of their participants

**src-000197-sese.039.001.08-p1300-c004 — file p1300, scope.**

Mentioned roles: [custodian](../../../../../shared/reference/participants/participant-narrative-src-000197-custodian.md); [agent](../../../../../shared/reference/participants/participant-functionality-src-000197-agent.md).

> an custodian acting as an accounting and/or settlement agent.

**src-000197-sese.039.001.08-p1300-c005 — file p1300, usage.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md); [account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000197-sese.039.001.08-p1300-c005-d1.

**src-000197-sese.039.001.08-p1300-c006 — file p1300, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md); [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000197-sese.039.001.08-p1300-c006-d1.

**src-000197-sese.039.001.08-p1300-c007 — file p1300, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md); [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000197-sese.039.001.08-p1300-c007-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p1300, usage.**

> The message may also be used to:

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
