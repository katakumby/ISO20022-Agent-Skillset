---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "secl.006.001.02 participant and direction evidence"
domain: "securities"
message_id: "secl.006.001.02"
message_family: "secl.006"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.006.001.02"
source_ids: ["src-000053", "src-000060"]
message_sets: ["ccp-clearing"]
role_labels: ["a Clearing member", "central counterparty (CCP)", "Clearing member", "the central counterparty"]
search_terms: ["a Clearing member", "central counterparty (CCP)", "Clearing member", "the central counterparty"]
participant_ids: ["participant-src-000052-central-counterparty", "participant-src-000052-individual-or-general-clearing-member"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000053", "heading": "7 MX secl.006.001.02 DefaultFundContributionReportV02", "file_pages": [246, 253]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# secl.006.001.02 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000053 — 7 MX secl.006.001.02 DefaultFundContributionReportV02

[src-000053](../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md); Functionality file pp246; publication March 2026; Standards MX November 2026 release.

### Direction and initiation clauses

#### src-000053-secl.006.001.02-p246-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000053 file p246, scope.

- Sender: **the central counterparty (CCP)**. [the central counterparty](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md).
- Receiver: **a Clearing member**. [a Clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

> The DefaultFundContributionReport message is sent by the central counterparty (CCP) to a Clearing member to report on the calculation of the default fund contribution and the potential net excess or deficit.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000053-secl.006.001.02-p246-c001 — file p246, scope.**

Mentioned roles: [central counterparty (CCP)](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md); [Clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

Quoted above in src-000053-secl.006.001.02-p246-c001-d1.

**src-000053-secl.006.001.02-p246-c002 — file p246, usage.**

> CCPs require participants to post assets in a clearing fund that can be used in the event of a default by a participant, to compensate non-defaulting participants for losses they suffer due to this default.

**src-000053-secl.006.001.02-p246-c003 — file p246, usage.**

> The CCP evaluates each participant risk level based on their positions (monthly or daily) and calculate the excess of deficit of the default fund contribution.

**src-000053-secl.006.001.02-p246-c004 — file p246, usage.**

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> The DefaultFundContributionReport is usually sent on a monthly basis.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p246, scope.**

> The message definition is intended for use with the ISO20022 Business Application Header.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
