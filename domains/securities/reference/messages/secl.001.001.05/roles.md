---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "secl.001.001.05 participant and direction evidence"
domain: "securities"
message_id: "secl.001.001.05"
message_family: "secl.001"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.001.001.05"
source_ids: ["src-000053", "src-000055"]
message_sets: ["ccp-clearing"]
role_labels: ["a clearing member", "central counterparty (CCP)", "clearing member", "global clearing member of the buyer", "global clearing member of the seller", "The CCP", "the central counterparty", "the global clearing member of the buyer", "the global clearing member of the seller"]
search_terms: ["a clearing member", "central counterparty (CCP)", "clearing member", "global clearing member of the buyer", "global clearing member of the seller", "The CCP", "the central counterparty", "the global clearing member of the buyer", "the global clearing member of the seller"]
participant_ids: ["participant-functionality-src-000053-global-clearing-member-buyer", "participant-functionality-src-000053-global-clearing-member-seller", "participant-src-000052-central-counterparty", "participant-src-000052-individual-or-general-clearing-member"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000053", "heading": "2 MX secl.001.001.05 TradeLegNotificationV05", "file_pages": [6, 63]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# secl.001.001.05 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 3 direction/initiator/exchange clauses; 4 uniquely resolved participant references.

## src-000053 — 2 MX secl.001.001.05 TradeLegNotificationV05

[src-000053](../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf); Functionality file pp6, 7; publication March 2026; Standards MX November 2026 release.

### Direction and initiation clauses

#### src-000053-secl.001.001.05-p6-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000053 file p6, scope.

- Sender: **the central counterparty (CCP)**. [the central counterparty](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md).
- Receiver: **a clearing member**. [a clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

> The TradeLegNotification message is sent by the central counterparty (CCP) to a clearing member to report the trade that has been executed by the trading platform.

#### src-000053-secl.001.001.05-p6-c003-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000053 file p6, usage.

- Sender: **The CCP**. [The CCP](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md).
- Receiver: **the global clearing member of the seller**. [the global clearing member of the seller](../../../../../shared/reference/participants/participant-functionality-src-000053-global-clearing-member-seller.md).

> The CCP sends a message to the global clearing member of the seller and a message to the global clearing member of the buyer.

#### src-000053-secl.001.001.05-p6-c003-d2

Kind: sender-to-receiver; message applicability: **current-message**; src-000053 file p6, usage.

- Sender: **The CCP**. [The CCP](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md).
- Receiver: **the global clearing member of the buyer**. [the global clearing member of the buyer](../../../../../shared/reference/participants/participant-functionality-src-000053-global-clearing-member-buyer.md).

> The CCP sends a message to the global clearing member of the seller and a message to the global clearing member of the buyer.

The source explicitly sends a separate message to each named recipient; the two recipients are not merged into one participant label.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000053-secl.001.001.05-p6-c001 — file p6, scope.**

Mentioned roles: [central counterparty (CCP)](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md); [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

Quoted above in src-000053-secl.001.001.05-p6-c001-d1.

**src-000053-secl.001.001.05-p6-c002 — file p6, usage.**

Mentioned roles: [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

> The CCP reports both sides of the trade from the clearing member perspective.

**src-000053-secl.001.001.05-p6-c003 — file p6, usage.**

Mentioned roles: [global clearing member of the seller](../../../../../shared/reference/participants/participant-functionality-src-000053-global-clearing-member-seller.md); [global clearing member of the buyer](../../../../../shared/reference/participants/participant-functionality-src-000053-global-clearing-member-buyer.md).

Quoted above in src-000053-secl.001.001.05-p6-c003-d1, src-000053-secl.001.001.05-p6-c003-d2.

**src-000053-secl.001.001.05-p6-c004 — file p6, usage.**

Mentioned roles: [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

> Note: An individual clearing member only clear its own trades.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p6, scope.**

> The message definition is intended for use with the ISO20022 Business Application Header.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
