---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "secl.005.001.02 participant and direction evidence"
domain: "securities"
message_id: "secl.005.001.02"
message_family: "secl.005"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02"
source_ids: ["src-000053", "src-000059"]
message_sets: ["ccp-clearing"]
role_labels: ["a clearing member", "central counterparty (CCP)", "clearing member", "the central counterparty"]
search_terms: ["a clearing member", "central counterparty (CCP)", "clearing member", "the central counterparty"]
participant_ids: ["participant-src-000052-central-counterparty", "participant-src-000052-individual-or-general-clearing-member"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000053", "heading": "6 MX secl.005.001.02 MarginReportV02", "file_pages": [232, 245]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# secl.005.001.02 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000053 — 6 MX secl.005.001.02 MarginReportV02

[src-000053](../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md); Functionality file pp232, 233; publication March 2026; Standards MX November 2026 release.

### Direction and initiation clauses

#### src-000053-secl.005.001.02-p232-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000053 file p232, scope.

- Sender: **the central counterparty (CCP)**. [the central counterparty](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md).
- Receiver: **a clearing member**. [a clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

> The MarginReport message is sent by the central counterparty (CCP) to a clearing member to report on:

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000053-secl.005.001.02-p232-c001 — file p232, scope.**

Mentioned roles: [central counterparty (CCP)](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md); [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

Quoted above in src-000053-secl.005.001.02-p232-c001-d1.

**src-000053-secl.005.001.02-p232-c002 — file p232, usage.**

Mentioned roles: [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md); [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

> per clearing member: the report will only show the information for the clearing member, or

**src-000053-secl.005.001.02-p232-c003 — file p232, usage.**

Mentioned roles: [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md); [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

> per clearing member and per financial instrument: the report will show the information for the clearing member, structured by security identification, or

**src-000053-secl.005.001.02-p232-c004 — file p232, usage.**

Mentioned roles: [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md); [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md); [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md); [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md); [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

> per clearing member and per non clearing member: the report will show the information for the clearing member (that is for global clearing member only) structured by non clearing member(s), or

**src-000053-secl.005.001.02-p232-c005 — file p232, usage.**

Mentioned roles: [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md); [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md); [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md); [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md); [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

> per clearing member and per non clearing member and per security identification: the report will show the information for the clearing member (global clearing member only) structured by non clearing member(s) and by security identification.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p232, scope.**

> the exposure resulting from the trade positions

**File p232, scope.**

> the value of the collateral held by the CCP (market value of this collateral) and

**File p232, scope.**

> the resulting difference representing the risk encountered by the CCP.

**File p232, scope.**

> The message definition is intended for use with the ISO20022 Business Application Header.

**File p232, usage.**

> There are four possibilities to report the above information.

**File p232, usage.**

> Indeed, the margin report may be structured as follows:

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
