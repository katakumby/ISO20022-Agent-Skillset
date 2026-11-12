---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "semt.023.001.02 participant and direction evidence"
domain: "securities"
message_id: "semt.023.001.02"
message_family: "semt.023"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02"
source_ids: ["src-000181", "src-000183"]
message_sets: ["post-trade-matching"]
role_labels: ["affirming party", "agent", "an affirming party", "an executing party", "an instructing party", "broker/dealer", "Central Matching Utility", "Central Matching Utility (CMU)", "Custodian", "custodian", "executing party", "Executing Party", "Instructing Party", "instructing party", "intermediary", "investment manager", "the custodian", "trustee"]
search_terms: ["affirming party", "agent", "an affirming party", "an executing party", "an instructing party", "broker/dealer", "Central Matching Utility", "Central Matching Utility (CMU)", "Custodian", "custodian", "executing party", "Executing Party", "Instructing Party", "instructing party", "intermediary", "investment manager", "the custodian", "trustee"]
participant_ids: ["participant-functionality-src-000181-agent", "participant-narrative-src-000181-broker-dealer", "participant-narrative-src-000181-central-matching-utility", "participant-narrative-src-000181-executing-party", "participant-narrative-src-000181-intermediary", "participant-src-000180-affirming-party", "participant-src-000180-central-matching-utility-cmu", "participant-src-000180-custodian", "participant-src-000180-instructing-party", "participant-src-000180-investment-manager", "participant-src-000180-trustee"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000181", "heading": "2 semt.023.001.02 SecuritiesEndOfProcessReportV02", "file_pages": [6, 27]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# semt.023.001.02 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 11 uniquely resolved participant references.

## src-000181 — 2 semt.023.001.02 SecuritiesEndOfProcessReportV02

[src-000181](../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md); Functionality file pp6; publication February 2025.

### Direction and initiation clauses

#### src-000181-semt.023.001.02-p6-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000181 file p6, scope.

- Sender: **an executing party or an instructing party**. [an executing party](../../../../../shared/reference/participants/participant-narrative-src-000181-executing-party.md); [an instructing party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md).
- Receiver: **the custodian or an affirming party**. [the custodian](../../../../../shared/reference/participants/participant-src-000180-custodian.md); [an affirming party](../../../../../shared/reference/participants/participant-src-000180-affirming-party.md).

> Sent by an executing party or an instructing party to the custodian or an affirming party to notify that all the necessary SecuritiesTradeConfirmation message or any other notification of the process have been sent.

#### src-000181-semt.023.001.02-p6-c002-d1

Kind: intermediary-routing; message applicability: **current-message-routing-option**; src-000181 file p6, scope.

- Intermediary: **Central Matching Utility**. [Central Matching Utility](../../../../../shared/reference/participants/participant-narrative-src-000181-central-matching-utility.md).

> It may also be sent through Central Matching Utility (CMU).

The source says the message may be sent through CMU; this identifies routing participation, not CMU as sender or receiver.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000181-semt.023.001.02-p6-c001 — file p6, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-narrative-src-000181-executing-party.md); [instructing party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md); [custodian](../../../../../shared/reference/participants/participant-src-000180-custodian.md); [affirming party](../../../../../shared/reference/participants/participant-src-000180-affirming-party.md).

Quoted above in src-000181-semt.023.001.02-p6-c001-d1.

**src-000181-semt.023.001.02-p6-c002 — file p6, scope.**

Mentioned roles: [Central Matching Utility (CMU)](../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000181-semt.023.001.02-p6-c002-d1.

**src-000181-semt.023.001.02-p6-c003 — file p6, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md); [investment manager](../../../../../shared/reference/participants/participant-src-000180-investment-manager.md); [intermediary](../../../../../shared/reference/participants/participant-narrative-src-000181-intermediary.md); [investment manager](../../../../../shared/reference/participants/participant-src-000180-investment-manager.md).

> The instructing party is typically the investment manager or an intermediary system/vendor communicating on behalf of the investment manager.

**src-000181-semt.023.001.02-p6-c004 — file p6, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-narrative-src-000181-executing-party.md); [broker/dealer](../../../../../shared/reference/participants/participant-narrative-src-000181-broker-dealer.md); [intermediary](../../../../../shared/reference/participants/participant-narrative-src-000181-intermediary.md); [broker/dealer](../../../../../shared/reference/participants/participant-narrative-src-000181-broker-dealer.md).

> The executing party is typically the broker/dealer or an intermediary system/vendor communicating on behalf of the broker/dealer.

**src-000181-semt.023.001.02-p6-c005 — file p6, scope.**

Mentioned roles: [custodian](../../../../../shared/reference/participants/participant-src-000180-custodian.md); [affirming party](../../../../../shared/reference/participants/participant-src-000180-affirming-party.md); [custodian](../../../../../shared/reference/participants/participant-src-000180-custodian.md); [trustee](../../../../../shared/reference/participants/participant-src-000180-trustee.md); [intermediary](../../../../../shared/reference/participants/participant-narrative-src-000181-intermediary.md); [agent](../../../../../shared/reference/participants/participant-functionality-src-000181-agent.md).

> The custodian or an affirming party is typically the custodian, trustee, financial institution, intermediary system/vendor communicating on behalf of them, or their agent.

**src-000181-semt.023.001.02-p6-c006 — file p6, usage.**

Mentioned roles: [Executing Party](../../../../../shared/reference/participants/participant-narrative-src-000181-executing-party.md); [Instructing Party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md); [Custodian](../../../../../shared/reference/participants/participant-src-000180-custodian.md); [affirming party](../../../../../shared/reference/participants/participant-src-000180-affirming-party.md).

> Initiator: Executing Party, CMU or Instructing Party Respondent: Custodian or an affirming party does not need to respond.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p6, scope.**

> The ISO 20022 Business Application Header must be used

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
