---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "setr.044.001.04 participant and direction evidence"
domain: "securities"
message_id: "setr.044.001.04"
message_family: "setr.044"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04"
source_ids: ["src-000181", "src-000187"]
message_sets: ["post-trade-matching"]
role_labels: ["affirming party", "an executing party", "an instructing party", "broker/dealer", "Central Matching Utility", "Central Matching Utility (CMU)", "custodian", "executing party", "instructing party", "intermediary", "investment manager", "investors", "recipient"]
search_terms: ["affirming party", "an executing party", "an instructing party", "broker/dealer", "Central Matching Utility", "Central Matching Utility (CMU)", "custodian", "executing party", "instructing party", "intermediary", "investment manager", "investors", "recipient"]
participant_ids: ["participant-functionality-src-000181-recipient", "participant-narrative-src-000181-broker-dealer", "participant-narrative-src-000181-central-matching-utility", "participant-narrative-src-000181-executing-party", "participant-narrative-src-000181-intermediary", "participant-narrative-src-000181-investor", "participant-src-000180-affirming-party", "participant-src-000180-central-matching-utility-cmu", "participant-src-000180-custodian", "participant-src-000180-instructing-party", "participant-src-000180-investment-manager"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000181", "heading": "6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04", "file_pages": [162, 221]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# setr.044.001.04 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 11 uniquely resolved participant references.

## src-000181 — 6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04

[src-000181](../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf); Functionality file pp162, 163; publication February 2025.

### Direction and initiation clauses

#### src-000181-setr.044.001.04-p162-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000181 file p162, scope.

- Sender: **Central Matching Utility (CMU)**. [Central Matching Utility](../../../../../shared/reference/participants/participant-narrative-src-000181-central-matching-utility.md).
- Receiver: **an executing party or an instructing party**. [an executing party](../../../../../shared/reference/participants/participant-narrative-src-000181-executing-party.md); [an instructing party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md).

> This message is sent from Central Matching Utility (CMU) to an executing party or an instructing party to advise the status of the SecuritiesTradeConfirmation message previously sent by the party.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000181-setr.044.001.04-p162-c001 — file p162, scope.**

Mentioned roles: [Central Matching Utility (CMU)](../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md); [executing party](../../../../../shared/reference/participants/participant-narrative-src-000181-executing-party.md); [instructing party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md).

Quoted above in src-000181-setr.044.001.04-p162-c001-d1.

**src-000181-setr.044.001.04-p162-c002 — file p162, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md); [custodian](../../../../../shared/reference/participants/participant-src-000180-custodian.md); [affirming party](../../../../../shared/reference/participants/participant-src-000180-affirming-party.md).

> The status may be a processing, pending processing, affirmed or disaffirmed, cancel or replacement by an instructing party, a custodian or an affirming party, internal matching, and/or matching status.

**src-000181-setr.044.001.04-p162-c003 — file p162, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md); [investment manager](../../../../../shared/reference/participants/participant-src-000180-investment-manager.md); [intermediary](../../../../../shared/reference/participants/participant-narrative-src-000181-intermediary.md); [investment manager](../../../../../shared/reference/participants/participant-src-000180-investment-manager.md); [investors](../../../../../shared/reference/participants/participant-narrative-src-000181-investor.md).

> The instructing party is typically the investment manager or an intermediary system/vendor communicating on behalf of the investment manager or of other categories of investors.

**src-000181-setr.044.001.04-p162-c004 — file p162, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-narrative-src-000181-executing-party.md); [broker/dealer](../../../../../shared/reference/participants/participant-narrative-src-000181-broker-dealer.md); [intermediary](../../../../../shared/reference/participants/participant-narrative-src-000181-intermediary.md); [broker/dealer](../../../../../shared/reference/participants/participant-narrative-src-000181-broker-dealer.md).

> The executing party is typically the broker/dealer or an intermediary system/vendor communicating on behalf of the broker/dealer.

**src-000181-setr.044.001.04-p162-c005 — file p162, usage.**

Mentioned roles: [Central Matching Utility](../../../../../shared/reference/participants/participant-narrative-src-000181-central-matching-utility.md).

> Initiator: In central matching the Initiator is the Central Matching Utility.

**src-000181-setr.044.001.04-p162-c006 — file p162, usage.**

Mentioned roles: [recipient](../../../../../shared/reference/participants/participant-functionality-src-000181-recipient.md).

> Respondent: no response is needed by the recipient of the message.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p162, scope.**

> The ISO 20022 Business Application Header must be used

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
