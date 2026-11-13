---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "secl.008.001.03 participant and direction evidence"
domain: "securities"
message_id: "secl.008.001.03"
message_family: "secl.008"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.008.001.03"
source_ids: ["src-000053", "src-000062"]
message_sets: ["ccp-clearing"]
role_labels: ["central counterparty", "clearing member", "the central counterparty", "the clearing member"]
search_terms: ["central counterparty", "clearing member", "the central counterparty", "the clearing member"]
participant_ids: ["participant-src-000052-central-counterparty", "participant-src-000052-individual-or-general-clearing-member"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000053", "heading": "9 MX secl.008.001.03 BuyInResponseV03", "file_pages": [274, 293]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# secl.008.001.03 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000053 — 9 MX secl.008.001.03 BuyInResponseV03

[src-000053](../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md); Functionality file pp274; publication March 2026; Standards MX November 2026 release.

### Direction and initiation clauses

#### src-000053-secl.008.001.03-p274-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000053 file p274, scope.

- Sender: **the clearing member**. [the clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).
- Receiver: **the central counterparty**. [the central counterparty](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md).

> The BuyInResponse message is sent by the clearing member to the central counterparty as a response to the previous buy-in notification message.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000053-secl.008.001.03-p274-c001 — file p274, scope.**

Mentioned roles: [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md); [central counterparty](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md).

Quoted above in src-000053-secl.008.001.03-p274-c001-d1.

**src-000053-secl.008.001.03-p274-c002 — file p274, usage.**

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> The BuyInResponse may be sent in response to the BuyInNotification message.

**src-000053-secl.008.001.03-p274-c003 — file p274, usage.**

Mentioned roles: [central counterparty](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md).

> However, the use of this message in the buy in process is optional and depends on the rules set by each central counterparty.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p274, scope.**

> The message definition is intended for use with the ISO 20022 Business Application Header.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
