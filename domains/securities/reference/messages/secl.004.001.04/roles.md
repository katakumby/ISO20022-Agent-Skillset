---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "secl.004.001.04 participant and direction evidence"
domain: "securities"
message_id: "secl.004.001.04"
message_family: "secl.004"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.004.001.04"
source_ids: ["src-000053", "src-000058"]
message_sets: ["ccp-clearing"]
role_labels: ["a clearing member", "central counterparty", "central counterparty (CCP)", "clearing member", "Clearing member", "the central counterparty"]
search_terms: ["a clearing member", "central counterparty", "central counterparty (CCP)", "clearing member", "Clearing member", "the central counterparty"]
participant_ids: ["participant-src-000052-central-counterparty", "participant-src-000052-individual-or-general-clearing-member"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000053", "heading": "5 MX secl.004.001.04 NetPositionV04", "file_pages": [191, 231]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# secl.004.001.04 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000053 — 5 MX secl.004.001.04 NetPositionV04

[src-000053](../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf); Functionality file pp191; publication March 2026; Standards MX November 2026 release.

### Direction and initiation clauses

#### src-000053-secl.004.001.04-p191-c001-d1

Kind: sender-to-receiver; message applicability: **current-message-scope-name-variant**; src-000053 file p191, scope.

- Sender: **the central counterparty (CCP)**. [the central counterparty](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md).
- Receiver: **a clearing member**. [a clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

> The Net Position Report message is sent by the central counterparty (CCP) to a clearing member to confirm the net position of all trade legs reported during the day.

#### src-000053-secl.004.001.04-p191-c002-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000053 file p191, usage.

- Sender: **central counterparty**. [central counterparty](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md).
- Receiver: **Clearing member**. [Clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

> The central counterparty (CCP) nets all the positions per clearing account and sends the Net Position report message to the Clearing member.

The source names the central counterparty as actor of both netting and sending. The netting verb phrase is not part of its participant label.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000053-secl.004.001.04-p191-c001 — file p191, scope.**

Mentioned roles: [central counterparty (CCP)](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md); [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

Quoted above in src-000053-secl.004.001.04-p191-c001-d1.

**src-000053-secl.004.001.04-p191-c002 — file p191, usage.**

Mentioned roles: [central counterparty (CCP)](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md); [Clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

Reviewed clause disposition: **parsed-role-boundary-correction**. The original exact clause was read; actor label is separated from its parenthetical examples or preceding activity phrase.

Quoted above in src-000053-secl.004.001.04-p191-c002-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p191, scope.**

> The message definition is intended for use with the ISO 20022 Business Application Header.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
