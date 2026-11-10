---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "setr.030.001.03 participant and direction evidence"
domain: "securities"
message_id: "setr.030.001.03"
message_family: "setr.030"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.030.001.03"
source_ids: ["src-000181", "src-000186"]
message_sets: ["post-trade-matching"]
role_labels: ["a custodian", "affirming party", "Affirming party", "agent", "an affirming party", "an executing party", "an instructing party", "broker/dealer", "Central Matching Utility (CMU)", "Custodian", "custodian", "executing party", "Executing party", "Instructing Party", "instructing party", "intermediary", "investment manager", "investors", "to Central Matching Utility", "trustee"]
search_terms: ["a custodian", "affirming party", "Affirming party", "agent", "an affirming party", "an executing party", "an instructing party", "broker/dealer", "Central Matching Utility (CMU)", "Custodian", "custodian", "executing party", "Executing party", "Instructing Party", "instructing party", "intermediary", "investment manager", "investors", "to Central Matching Utility", "trustee"]
participant_ids: ["participant-functionality-src-000181-agent", "participant-narrative-src-000181-broker-dealer", "participant-narrative-src-000181-central-matching-utility", "participant-narrative-src-000181-executing-party", "participant-narrative-src-000181-intermediary", "participant-narrative-src-000181-investor", "participant-src-000180-affirming-party", "participant-src-000180-central-matching-utility-cmu", "participant-src-000180-custodian", "participant-src-000180-instructing-party", "participant-src-000180-investment-manager", "participant-src-000180-trustee"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000181", "heading": "5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03", "file_pages": [148, 161]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# setr.030.001.03 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 12 uniquely resolved participant references.

## src-000181 — 5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03

[src-000181](../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf); Functionality file pp148, 149; publication February 2025.

### Direction and initiation clauses

#### src-000181-setr.030.001.03-p148-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000181 file p148, scope.

- Sender: **an instructing party, a custodian or an affirming party**. [an instructing party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md); [a custodian](../../../../../shared/reference/participants/participant-src-000180-custodian.md); [an affirming party](../../../../../shared/reference/participants/participant-src-000180-affirming-party.md).
- Receiver: **an executing party (local matching) or to Central Matching Utility (CMU)**. [an executing party](../../../../../shared/reference/participants/participant-narrative-src-000181-executing-party.md); [to Central Matching Utility](../../../../../shared/reference/participants/participant-narrative-src-000181-central-matching-utility.md).

> Sent by an instructing party, a custodian or an affirming party to an executing party (local matching) or to Central Matching Utility (CMU) to affirm (accept) or disaffirm (reject) (central matching) the SecuritiesTradeConfirmation message.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000181-setr.030.001.03-p148-c001 — file p148, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md); [custodian](../../../../../shared/reference/participants/participant-src-000180-custodian.md); [affirming party](../../../../../shared/reference/participants/participant-src-000180-affirming-party.md); [executing party](../../../../../shared/reference/participants/participant-narrative-src-000181-executing-party.md); [Central Matching Utility (CMU)](../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md).

Quoted above in src-000181-setr.030.001.03-p148-c001-d1.

**src-000181-setr.030.001.03-p148-c002 — file p148, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-narrative-src-000181-executing-party.md); [broker/dealer](../../../../../shared/reference/participants/participant-narrative-src-000181-broker-dealer.md); [intermediary](../../../../../shared/reference/participants/participant-narrative-src-000181-intermediary.md); [broker/dealer](../../../../../shared/reference/participants/participant-narrative-src-000181-broker-dealer.md).

> The executing party is typically the broker/dealer or an intermediary system/vendor communicating on behalf of the broker/dealer.

**src-000181-setr.030.001.03-p148-c003 — file p148, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md); [investment manager](../../../../../shared/reference/participants/participant-src-000180-investment-manager.md); [intermediary](../../../../../shared/reference/participants/participant-narrative-src-000181-intermediary.md); [investment manager](../../../../../shared/reference/participants/participant-src-000180-investment-manager.md); [investors](../../../../../shared/reference/participants/participant-narrative-src-000181-investor.md).

> The instructing party is typically the investment manager or an intermediary system/vendor communicating on behalf of the investment manager or of other categories of investors.

**src-000181-setr.030.001.03-p148-c004 — file p148, scope.**

Mentioned roles: [custodian](../../../../../shared/reference/participants/participant-src-000180-custodian.md); [affirming party](../../../../../shared/reference/participants/participant-src-000180-affirming-party.md); [custodian](../../../../../shared/reference/participants/participant-src-000180-custodian.md); [trustee](../../../../../shared/reference/participants/participant-src-000180-trustee.md); [intermediary](../../../../../shared/reference/participants/participant-narrative-src-000181-intermediary.md); [agent](../../../../../shared/reference/participants/participant-functionality-src-000181-agent.md).

> The custodian or an affirming party is typically the custodian, trustee, financial institution, intermediary system/vendor communicating on behalf of them, or their agent.

**src-000181-setr.030.001.03-p148-c005 — file p148, usage.**

Mentioned roles: [Instructing Party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md); [Custodian](../../../../../shared/reference/participants/participant-src-000180-custodian.md); [Affirming party](../../../../../shared/reference/participants/participant-src-000180-affirming-party.md).

> Initiator: Both in local and central matching, the Initiator may be the Instructing Party, Custodian or Affirming party.

**src-000181-setr.030.001.03-p148-c006 — file p148, usage.**

Mentioned roles: [Executing party](../../../../../shared/reference/participants/participant-narrative-src-000181-executing-party.md).

> Respondent: Executing party does not need to respond if an affirmation.

**src-000181-setr.030.001.03-p148-c007 — file p148, usage.**

Mentioned roles: [Executing party](../../../../../shared/reference/participants/participant-narrative-src-000181-executing-party.md).

> Executing party may respond with modification or cancellation of the rejected SecuritiesTradeConfirmation message.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p148, scope.**

> If accepting the SecuritiesTradeConfirmation message, then the trade is ready for settlement processing.

**File p148, scope.**

> If rejecting the SecuritiesTradeConfirmation message, then the trade is not ready for settlement.

**File p148, scope.**

> The ISO 20022 Business Application Header must be used

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
