---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "secl.003.001.05 participant and direction evidence"
domain: "securities"
message_id: "secl.003.001.05"
message_family: "secl.003"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.003.001.05"
source_ids: ["src-000053", "src-000057"]
message_sets: ["ccp-clearing"]
role_labels: ["a clearing member", "central counterparty (CCP)", "clearing member", "the central counterparty"]
search_terms: ["a clearing member", "central counterparty (CCP)", "clearing member", "the central counterparty"]
participant_ids: ["participant-src-000052-central-counterparty", "participant-src-000052-individual-or-general-clearing-member"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000053", "heading": "4 MX secl.003.001.05 TradeLegStatementV05", "file_pages": [124, 190]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# secl.003.001.05 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000053 — 4 MX secl.003.001.05 TradeLegStatementV05

[src-000053](../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md); Functionality file pp124; publication March 2026; Standards MX November 2026 release.

### Direction and initiation clauses

#### src-000053-secl.003.001.05-p124-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000053 file p124, scope.

- Sender: **the central counterparty (CCP)**. [the central counterparty](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md).
- Receiver: **a clearing member**. [a clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

> The TradeLegStatement message is sent by the central counterparty (CCP) to a clearing member to report all trades that have been executed by the trading platform.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000053-secl.003.001.05-p124-c001 — file p124, scope.**

Mentioned roles: [central counterparty (CCP)](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md); [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

Quoted above in src-000053-secl.003.001.05-p124-c001-d1.

**src-000053-secl.003.001.05-p124-c002 — file p124, usage.**

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> The TradeLegStatement message may be either sent:

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p124, scope.**

> The message definition is intended for use with the ISO20022 Business Application Header.

**File p124, usage.**

> during the day (to report trades execution by batch) or

**File p124, usage.**

> as an end of day report.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
