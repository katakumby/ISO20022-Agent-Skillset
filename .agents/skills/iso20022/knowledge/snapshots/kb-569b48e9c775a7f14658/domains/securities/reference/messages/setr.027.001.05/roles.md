---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "setr.027.001.05 participant and direction evidence"
domain: "securities"
message_id: "setr.027.001.05"
message_family: "setr.027"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.027.001.05"
source_ids: ["src-000181", "src-000184"]
message_sets: ["post-trade-matching"]
role_labels: ["affirming party", "agent", "an executing party", "an instructing party", "broker/dealer", "Central Matching Utility (CMU)", "custodian", "executing party", "instructing party", "intermediary", "investment manager", "investors", "trustee"]
search_terms: ["affirming party", "agent", "an executing party", "an instructing party", "broker/dealer", "Central Matching Utility (CMU)", "custodian", "executing party", "instructing party", "intermediary", "investment manager", "investors", "trustee"]
participant_ids: ["participant-functionality-src-000181-agent", "participant-narrative-src-000181-broker-dealer", "participant-narrative-src-000181-executing-party", "participant-narrative-src-000181-intermediary", "participant-narrative-src-000181-investor", "participant-src-000180-affirming-party", "participant-src-000180-central-matching-utility-cmu", "participant-src-000180-custodian", "participant-src-000180-instructing-party", "participant-src-000180-investment-manager", "participant-src-000180-trustee"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000181", "heading": "3 setr.027.001.05 SecuritiesTradeConfirmationV05", "file_pages": [28, 139]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# setr.027.001.05 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 11 uniquely resolved participant references.

## src-000181 — 3 setr.027.001.05 SecuritiesTradeConfirmationV05

[src-000181](../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md); Functionality file pp28, 29, 30; publication February 2025.

### Direction and initiation clauses

#### src-000181-setr.027.001.05-p28-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000181 file p28, scope.

- Sender: **an executing party**. [an executing party](../../../../../shared/reference/participants/participant-narrative-src-000181-executing-party.md).
- Receiver: **an instructing party directly or through Central Matching Utility (CMU)**. [an instructing party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md).

> Sent by an executing party to an instructing party directly or through Central Matching Utility (CMU) to provide trade confirmation on a per-account basis based on instructions provided by the instructing party in the SecuritiesAllocationInstruction message.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000181-setr.027.001.05-p28-c001 — file p28, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-narrative-src-000181-executing-party.md); [instructing party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md); [Central Matching Utility (CMU)](../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md); [instructing party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md).

Literal actions: instructing party provided.

Quoted above in src-000181-setr.027.001.05-p28-c001-d1.

**src-000181-setr.027.001.05-p28-c002 — file p28, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-narrative-src-000181-executing-party.md); [instructing party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md); [custodian](../../../../../shared/reference/participants/participant-src-000180-custodian.md); [affirming party](../../../../../shared/reference/participants/participant-src-000180-affirming-party.md).

> It may also be used to provide trade confirmation on the trade level from an executing party or an instructing party to the custodian or an affirming party directly or through CMU.

**src-000181-setr.027.001.05-p28-c003 — file p28, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md); [investment manager](../../../../../shared/reference/participants/participant-src-000180-investment-manager.md); [intermediary](../../../../../shared/reference/participants/participant-narrative-src-000181-intermediary.md); [investment manager](../../../../../shared/reference/participants/participant-src-000180-investment-manager.md); [investors](../../../../../shared/reference/participants/participant-narrative-src-000181-investor.md).

> The instructing party is typically the investment manager or an intermediary system/vendor communicating on behalf of the investment manager or of other categories of investors.

**src-000181-setr.027.001.05-p28-c004 — file p28, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-narrative-src-000181-executing-party.md); [broker/dealer](../../../../../shared/reference/participants/participant-narrative-src-000181-broker-dealer.md); [intermediary](../../../../../shared/reference/participants/participant-narrative-src-000181-intermediary.md); [broker/dealer](../../../../../shared/reference/participants/participant-narrative-src-000181-broker-dealer.md).

> The executing party is typically the broker/dealer or an intermediary system/vendor communicating on behalf of the broker/dealer.

**src-000181-setr.027.001.05-p28-c005 — file p28, scope.**

Mentioned roles: [custodian](../../../../../shared/reference/participants/participant-src-000180-custodian.md); [affirming party](../../../../../shared/reference/participants/participant-src-000180-affirming-party.md); [custodian](../../../../../shared/reference/participants/participant-src-000180-custodian.md); [trustee](../../../../../shared/reference/participants/participant-src-000180-trustee.md); [intermediary](../../../../../shared/reference/participants/participant-narrative-src-000181-intermediary.md); [agent](../../../../../shared/reference/participants/participant-functionality-src-000181-agent.md).

> The custodian or the affirming party is typically the custodian, trustee, financial institution, intermediary system/vendor communicating on behalf of them, or their agent.

**src-000181-setr.027.001.05-p28-c006 — file p28, usage.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-narrative-src-000181-executing-party.md).

> Initiator: In local matching, the initiator of this message is always the executing party.

**src-000181-setr.027.001.05-p28-c007 — file p28, usage.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-narrative-src-000181-executing-party.md); [instructing party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md).

> In central matching the initiator may be either the executing party or instructing party.

**src-000181-setr.027.001.05-p28-c008 — file p28, usage.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md); [custodian](../../../../../shared/reference/participants/participant-src-000180-custodian.md); [affirming party](../../../../../shared/reference/participants/participant-src-000180-affirming-party.md).

> Respondent: instructing party, a custodian or an affirming party responds with SecuritiesTradeConfirmationResponse (accept or reject) message.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
