---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "semt.022.001.07 participant and direction evidence"
domain: "securities"
message_id: "semt.022.001.07"
message_family: "semt.022"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.022.001.07"
source_ids: ["src-000197", "src-000210"]
message_sets: ["settlement-and-reconciliation"]
role_labels: ["direct participant", "instructing party", "market infrastructure", "Market Infrastructure", "Settlement Infrastructure", "the CSD", "the Market Infrastructure", "third party"]
search_terms: ["direct participant", "instructing party", "market infrastructure", "Market Infrastructure", "Settlement Infrastructure", "the CSD", "the Market Infrastructure", "third party"]
participant_ids: ["participant-functionality-src-000197-csd", "participant-functionality-src-000197-direct-participant", "participant-functionality-src-000197-message-copy-third-party", "participant-narrative-src-000197-instructing-party", "participant-narrative-src-000197-market-infrastructure", "participant-settlement-reconciliation-settlement-infrastructure"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000197", "heading": "13 semt.022.001.07 SecuritiesSettlementTransactionAuditTrailReportV07", "file_pages": [433, 457]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# semt.022.001.07 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 4 direction/initiator/exchange clauses; 6 uniquely resolved participant references.

## src-000197 — 13 semt.022.001.07 SecuritiesSettlementTransactionAuditTrailReportV07

[src-000197](../../../../../evidence/omitted/e96bb98c659322ed5684b325.md); Functionality file pp433; publication March 2026.

### Direction and initiation clauses

#### src-000197-semt.022.001.07-p433-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000197 file p433, scope.

- Sender: **the Market Infrastructure**. [the Market Infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000197-market-infrastructure.md).
- Receiver: **the CSD**. [the CSD](../../../../../shared/reference/participants/participant-functionality-src-000197-csd.md).

> This message is sent by the Market Infrastructure to the CSD to advise of the history of all the statuses, modifications, replacement and cancellation of a specific transaction during its whole life cycle when the instructing party is a direct participant to the Settlement Infrastructure.

#### src-000197-semt.022.001.07-p433-c002-d1

Kind: sender-to-receiver; message applicability: **original-message-in-duplicate-option**; src-000197 file p433, usage.

- Sender: **market infrastructure**. [market infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000197-market-infrastructure.md).
- Receiver: **direct participant**. [direct participant](../../../../../shared/reference/participants/participant-functionality-src-000197-direct-participant.md).

> re-send a message sent by the market infrastructure to the direct participant,

Explicit original-message direction in the resend option; no new copy direction inferred.

#### src-000197-semt.022.001.07-p433-c003-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000197 file p433, usage.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md).

> provide a third party with a copy of a message being sent by the market infrastructure for information,

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

#### src-000197-semt.022.001.07-p433-c004-d1

Kind: receiver-only; message applicability: **current-message-copy-or-copyduplicate-option**; src-000197 file p433, usage.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md).

> re-send to a third party a copy of a message being sent by the market infrastructure for information using the relevant elements in the Business Application Header.

The third party receives an informational copy/resend under this usage option. The sender of the copy is not independently identified here. Any account-owner/market-infrastructure wording describes the original message and is retained without treating it as a new copy sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000197-semt.022.001.07-p433-c001 — file p433, scope.**

Mentioned roles: [Market Infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000197-market-infrastructure.md); [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000197-instructing-party.md); [direct participant](../../../../../shared/reference/participants/participant-functionality-src-000197-direct-participant.md); [Settlement Infrastructure](../../../../../shared/reference/participants/settlement-reconciliation-settlement-infrastructure.md).

Quoted above in src-000197-semt.022.001.07-p433-c001-d1.

**src-000197-semt.022.001.07-p433-c002 — file p433, usage.**

Mentioned roles: [market infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000197-market-infrastructure.md); [direct participant](../../../../../shared/reference/participants/participant-functionality-src-000197-direct-participant.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000197-semt.022.001.07-p433-c002-d1.

**src-000197-semt.022.001.07-p433-c003 — file p433, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md); [market infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000197-market-infrastructure.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000197-semt.022.001.07-p433-c003-d1.

**src-000197-semt.022.001.07-p433-c004 — file p433, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-functionality-src-000197-message-copy-third-party.md); [market infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000197-market-infrastructure.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000197-semt.022.001.07-p433-c004-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p433, usage.**

> The message may also be used to:

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
