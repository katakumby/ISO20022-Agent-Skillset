---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "sese.037.001.09 participant and direction evidence"
domain: "securities"
message_id: "sese.037.001.09"
message_family: "sese.037"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.037.001.09"
source_ids: ["src-000197", "src-000228"]
message_sets: ["settlement-and-reconciliation"]
role_labels: ["account servicer", "agent", "an account servicer", "another account servicer", "broker/dealer", "client", "delivering account servicer", "global custodian", "investment management institution", "receiving account servicer", "third party"]
search_terms: ["account servicer", "agent", "an account servicer", "another account servicer", "broker/dealer", "client", "delivering account servicer", "global custodian", "investment management institution", "receiving account servicer", "third party"]
participant_ids: ["participant-functionality-src-000197-agent", "participant-functionality-src-000197-message-copy-third-party", "participant-narrative-src-000197-broker-dealer", "participant-narrative-src-000197-global-custodian", "participant-narrative-src-000197-investment-management-institution", "participant-settlement-reconciliation-account-servicer", "participant-settlement-reconciliation-portfolio-transfer-client"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000197", "heading": "31 sese.037.001.09 PortfolioTransferNotificationV09", "file_pages": [1094, 1132]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# sese.037.001.09 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 4 direction/initiator/exchange clauses; 7 uniquely resolved participant references.

## src-000197 — 31 sese.037.001.09 PortfolioTransferNotificationV09

[src-000197](../../../../../evidence/omitted/e96bb98c659322ed5684b325.md); Functionality file pp1094, 1095; publication March 2026.

### Direction and initiation clauses

#### src-000197-sese.037.001.09-p1094-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000197 file p1094, scope.

- Sender: **an account servicer**. [an account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).
- Receiver: **another account servicer**. [another account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).

> The PortfolioTransferNotification is sent by an account servicer to another account servicer to exchange transfer settlement details information during a retail or institutional client portfolio transfer.

#### src-000197-sese.037.001.09-p1094-c003-d1

Kind: sender-to-receiver; message applicability: **business-flow-settlement-data-exchange**; src-000197 file p1094, usage.

- Sender: **delivering account servicer**. [delivering account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).
- Receiver: **receiving account servicer**. [receiving account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).

> The exchange of transfer settlement details is the provision, by the delivering account servicer to the receiving account servicer, of the settlement data (such as trade date, settlement date, delivering settlement chain, quantities) of the individual transfers that will take place during a full or partial portfolio transfer.

Explicit business-flow provision of settlement data; scope is the source-defined exchange during a full/partial portfolio transfer.

#### src-000197-sese.037.001.09-p1094-c005-d1

Kind: sender-to-receiver; message applicability: **current-message-conditional-return**; src-000197 file p1094, usage.

- Sender: **receiving account servicer**. [receiving account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).
- Receiver: **delivering account servicer**. [delivering account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).

> In case the receiving settlement chain is not available to the delivering account servicer, the receiving account servicer may in return provide to the delivering account servicer the receiving settlement chain using the same message.

Applies only when the receiving settlement chain is unavailable to the delivering account servicer. The source explicitly says the same message is used in return.

#### src-000197-sese.037.001.09-p1094-c008-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000197 file p1094, usage.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md).

> re-send to a third party a copy of a message for information using the relevant elements in the Business Application Header.

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000197-sese.037.001.09-p1094-c001 — file p1094, scope.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md); [another account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md); [client](../../../../../shared/reference/participants/settlement-reconciliation-portfolio-transfer-client.md).

Quoted above in src-000197-sese.037.001.09-p1094-c001-d1.

**src-000197-sese.037.001.09-p1094-c002 — file p1094, scope.**

Mentioned roles: [account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md); [agent](../../../../../shared/reference/participants/participant-functionality-src-000197-agent.md); [global custodian](../../../../../shared/reference/participants/participant-narrative-src-000197-global-custodian.md); [investment management institution](../../../../../shared/reference/participants/participant-narrative-src-000197-investment-management-institution.md); [broker/dealer](../../../../../shared/reference/participants/participant-narrative-src-000197-broker-dealer.md); [client](../../../../../shared/reference/participants/settlement-reconciliation-portfolio-transfer-client.md).

> The account servicer will typically be local agent or global custodian acting on behalf of an investment management institution, a broker/dealer or a retail client.

**src-000197-sese.037.001.09-p1094-c003 — file p1094, usage.**

Mentioned roles: [delivering account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md); [receiving account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000197-sese.037.001.09-p1094-c003-d1.

**src-000197-sese.037.001.09-p1094-c004 — file p1094, usage.**

Mentioned roles: [delivering account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md); [client](../../../../../shared/reference/participants/settlement-reconciliation-portfolio-transfer-client.md).

Literal actions: client provided.

Reviewed clause disposition: **actor-or-condition-context**. The sentence describes actors, responsibilities, source/target data, prohibitions or conditions. Existing literal actions and the complete quote remain available; sending/receiving a different object or a negative assertion is not converted into an unconditional current-message direction.

> This delivering account servicer message may also include, for validation, the receiving settlement chain as provided by the client.

**src-000197-sese.037.001.09-p1094-c005 — file p1094, usage.**

Mentioned roles: [delivering account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md); [receiving account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md); [delivering account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000197-sese.037.001.09-p1094-c005-d1.

**src-000197-sese.037.001.09-p1094-c006 — file p1094, usage.**

Reviewed clause disposition: **resend-option-no-new-named-direction**. The source allows resending a previously sent message. This clause names no new sender or receiver; it is a usage option, not absent extraction of a direction.

> re-send a message previously sent,

**src-000197-sese.037.001.09-p1094-c007 — file p1094, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md).

> provide a third party with a copy of a message for information,

**src-000197-sese.037.001.09-p1094-c008 — file p1094, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000197-sese.037.001.09-p1094-c008-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p1094, usage.**

> The message may also be used to:

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
