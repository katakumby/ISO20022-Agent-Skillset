---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "sese.040.001.06 participant and direction evidence"
domain: "securities"
message_id: "sese.040.001.06"
message_family: "sese.040"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.040.001.06"
source_ids: ["src-000197", "src-000231"]
message_sets: ["settlement-and-reconciliation"]
role_labels: ["account owner", "account servicer", "agent", "An account owner", "broker/dealer", "central securities depository", "central securities depository participant", "client", "custodian", "global custodian customer", "investment management institution", "market infrastructure", "settlement market infrastructure", "sub-custodian", "third party"]
search_terms: ["account owner", "account servicer", "agent", "An account owner", "broker/dealer", "central securities depository", "central securities depository participant", "client", "custodian", "global custodian customer", "investment management institution", "market infrastructure", "settlement market infrastructure", "sub-custodian", "third party"]
participant_ids: ["participant-functionality-src-000197-agent", "participant-functionality-src-000197-allegement-client", "participant-functionality-src-000197-global-custodian-customer", "participant-functionality-src-000197-message-copy-third-party", "participant-narrative-src-000197-broker-dealer", "participant-narrative-src-000197-central-securities-depository", "participant-narrative-src-000197-central-securities-depository-participant", "participant-narrative-src-000197-custodian", "participant-narrative-src-000197-investment-management-institution", "participant-narrative-src-000197-market-infrastructure", "participant-narrative-src-000197-settlement-market-infrastructure", "participant-narrative-src-000197-sub-custodian", "participant-settlement-reconciliation-account-owner", "participant-settlement-reconciliation-account-servicer"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000197", "heading": "34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06", "file_pages": [1322, 1339]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# sese.040.001.06 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 4 direction/initiator/exchange clauses; 14 uniquely resolved participant references.

## src-000197 — 34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06

[src-000197](../../../../../evidence/omitted/e96bb98c659322ed5684b325.md); Functionality file pp1322, 1323; publication March 2026.

### Direction and initiation clauses

#### src-000197-sese.040.001.06-p1322-c001-d1

Kind: sender-only; message applicability: **current-message**; src-000197 file p1322, scope.

- Sender: **An account owner**. [An account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md).

> An account owner sends a SecuritiesSettlementTransactionCounterpartyResponse to advise the account servicer that:

The clause supplies the sender and a purpose introduced by “to”; it does not explicitly name a receiver.

#### src-000197-sese.040.001.06-p1322-c009-d1

Kind: sender-to-receiver; message applicability: **original-message-in-duplicate-option**; src-000197 file p1322, usage.

- Sender: **account owner**. [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md).
- Receiver: **account servicer**. [account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).

> re-send a message sent by the account owner to the account servicer,

The clause explicitly identifies the original message direction within the Duplicate/resend option; it does not establish a different sender for a forwarded copy.

#### src-000197-sese.040.001.06-p1322-c010-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000197 file p1322, usage.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md).

> provide a third party with a copy of a message being sent by the account owner for information,

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

#### src-000197-sese.040.001.06-p1322-c011-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000197 file p1322, usage.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md).

> re-send to a third party a copy of a message being sent by the account owner for information using the relevant elements in the Business Application Header.

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000197-sese.040.001.06-p1322-c001 — file p1322, scope.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md); [account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).

Literal actions: account owner sends.

Quoted above in src-000197-sese.040.001.06-p1322-c001-d1.

**src-000197-sese.040.001.06-p1322-c002 — file p1322, scope.**

Mentioned roles: [client](../../../../../shared/reference/participants/participant-functionality-src-000197-allegement-client.md).

Reviewed clause disposition: **actor-or-condition-context**. The sentence describes actors, responsibilities, source/target data, prohibitions or conditions. Existing literal actions and the complete quote remain available; sending/receiving a different object or a negative assertion is not converted into an unconditional current-message direction.

> the allegement received is either rejected (that is counterparty's transaction is unknown) or accepted (i.e. either the allegement was passed to the client or the transaction is know with or without mismatches)

**src-000197-sese.040.001.06-p1322-c003 — file p1322, scope.**

Reviewed clause disposition: **actor-or-condition-context**. The sentence describes actors, responsibilities, source/target data, prohibitions or conditions. Existing literal actions and the complete quote remain available; sending/receiving a different object or a negative assertion is not converted into an unconditional current-message direction.

> the modification or cancellation request sent by the counterparty for a matched transaction is affirmed or not.

**src-000197-sese.040.001.06-p1322-c004 — file p1322, scope.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).

> The account servicer will therefore proceed or not with the counterparty's request to modify or cancel the transaction.

**src-000197-sese.040.001.06-p1322-c005 — file p1322, scope.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md); [central securities depository](../../../../../shared/reference/participants/participant-narrative-src-000197-central-securities-depository.md); [settlement market infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000197-settlement-market-infrastructure.md); [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md).

> The account servicer may be a central securities depository or another settlement market infrastructure acting on behalf of their participants The account owner may be:

**src-000197-sese.040.001.06-p1322-c006 — file p1322, scope.**

Mentioned roles: [central securities depository participant](../../../../../shared/reference/participants/participant-narrative-src-000197-central-securities-depository-participant.md); [central securities depository](../../../../../shared/reference/participants/participant-narrative-src-000197-central-securities-depository.md); [market infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000197-market-infrastructure.md).

> a central securities depository participant which has an account with a central securities depository or a market infrastructure

**src-000197-sese.040.001.06-p1322-c007 — file p1322, scope.**

Mentioned roles: [agent](../../../../../shared/reference/participants/participant-functionality-src-000197-agent.md); [sub-custodian](../../../../../shared/reference/participants/participant-narrative-src-000197-sub-custodian.md); [global custodian customer](../../../../../shared/reference/participants/participant-functionality-src-000197-global-custodian-customer.md).

> an agent (sub-custodian) acting on behalf of their global custodian customer, or

**src-000197-sese.040.001.06-p1322-c008 — file p1322, scope.**

Mentioned roles: [custodian](../../../../../shared/reference/participants/participant-narrative-src-000197-custodian.md); [investment management institution](../../../../../shared/reference/participants/participant-narrative-src-000197-investment-management-institution.md); [broker/dealer](../../../../../shared/reference/participants/participant-narrative-src-000197-broker-dealer.md).

> a custodian acting on behalf of an investment management institution or a broker/dealer.

**src-000197-sese.040.001.06-p1322-c009 — file p1322, usage.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md); [account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000197-sese.040.001.06-p1322-c009-d1.

**src-000197-sese.040.001.06-p1322-c010 — file p1322, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md); [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000197-sese.040.001.06-p1322-c010-d1.

**src-000197-sese.040.001.06-p1322-c011 — file p1322, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md); [account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000197-sese.040.001.06-p1322-c011-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p1322, usage.**

> The message may also be used to:

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
