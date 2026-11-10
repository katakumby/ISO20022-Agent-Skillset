---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "secl.010.001.04 participant and direction evidence"
domain: "securities"
message_id: "secl.010.001.04"
message_family: "secl.010"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.010.001.04"
source_ids: ["src-000053", "src-000064"]
message_sets: ["ccp-clearing"]
role_labels: ["a clearing member", "central counterparty (CCP)", "clearing member", "receiving party", "the central counterparty", "third party"]
search_terms: ["a clearing member", "central counterparty (CCP)", "clearing member", "receiving party", "the central counterparty", "third party"]
participant_ids: ["participant-functionality-src-000053-recipient", "participant-narrative-src-000053-third-party", "participant-src-000052-central-counterparty", "participant-src-000052-individual-or-general-clearing-member"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000053", "heading": "11 MX secl.010.001.04 SettlementObligationReportV04", "file_pages": [316, 372]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# secl.010.001.04 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 4 uniquely resolved participant references.

## src-000053 — 11 MX secl.010.001.04 SettlementObligationReportV04

[src-000053](../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md); Functionality file pp316, 317; publication March 2026; Standards MX November 2026 release.

### Direction and initiation clauses

#### src-000053-secl.010.001.04-p316-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000053 file p316, scope.

- Sender: **the central counterparty (CCP)**. [the central counterparty](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md).
- Receiver: **a clearing member**. [a clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

> The SettlementObligationReport message is sent by the central counterparty (CCP) to a clearing member to report on the settlement obligation that will be submitted for settlement.

#### src-000053-secl.010.001.04-p316-c002-d1

Kind: receiver-only; message applicability: **current-message**; src-000053 file p316, usage.

- Receiver: **third party**. [third party](../../../../../shared/reference/participants/participant-narrative-src-000053-third-party.md).

> The SettlementObligationReport message may also be sent to a third party processing the settlement obligation(s) on behalf of more than one clearing member.

Conditional receiver processes settlement obligations on behalf of more than one clearing member; clearing members are not added as receivers by this sentence.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000053-secl.010.001.04-p316-c001 — file p316, scope.**

Mentioned roles: [central counterparty (CCP)](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md); [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

Quoted above in src-000053-secl.010.001.04-p316-c001-d1.

**src-000053-secl.010.001.04-p316-c002 — file p316, usage.**

Mentioned roles: [third party](../../../../../shared/reference/participants/participant-narrative-src-000053-third-party.md); [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000053-secl.010.001.04-p316-c002-d1.

**src-000053-secl.010.001.04-p316-c003 — file p316, usage.**

Mentioned roles: [receiving party](../../../../../shared/reference/participants/participant-functionality-src-000053-recipient.md).

Reviewed clause disposition: **report-coverage-not-receiver**. “Provided for” specifies the delivering/receiving-party coverage of the report. It does not assert that the covered party is the receiver.

> The report can be provided for one specific delivering party or one specific receiving party.

**src-000053-secl.010.001.04-p316-c004 — file p316, usage.**

Mentioned roles: [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

> It can also be generated per non clearing member.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p316, scope.**

> The message definition is intended for use with the ISO20022 Business Application Header.

**File p316, usage.**

> The Settlement Obligation Report message is provided per delivery account and per instrument.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
