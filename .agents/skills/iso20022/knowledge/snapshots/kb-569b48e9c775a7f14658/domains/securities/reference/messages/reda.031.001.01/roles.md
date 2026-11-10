---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "reda.031.001.01 participant and direction evidence"
domain: "securities"
message_id: "reda.031.001.01"
message_family: "reda.031"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.031.001.01"
source_ids: ["src-000233", "src-000286", "src-000369"]
message_sets: ["t2s", "t2s-party-reference-data"]
role_labels: ["executing party", "instructing party", "the executing party", "the instructing party"]
search_terms: ["executing party", "instructing party", "the executing party", "the instructing party"]
participant_ids: ["participant-narrative-src-000369-executing-party", "participant-src-000368-instructing-party"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "51 reda.031.001.01 PartyDeletionRequestV01", "file_pages": [2213, 2215]}, {"source_id": "src-000369", "heading": "7 reda.031.001.01 PartyDeletionRequestV01", "file_pages": [76, 78]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# reda.031.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000233 — 51 reda.031.001.01 PartyDeletionRequestV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); Functionality file pp2213; publication August 2026.

### Direction and initiation clauses

#### src-000233-reda.031.001.01-p2213-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p2213, scope.

- Sender: **the instructing party**. [the instructing party](../../../../../shared/reference/participants/participant-src-000368-instructing-party.md).
- Receiver: **the executing party**. [the executing party](../../../../../shared/reference/participants/participant-narrative-src-000369-executing-party.md).

> The PartyDeletionRequest message is sent by the instructing party to the executing party to request a deletion of a party defined in the executing system.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-reda.031.001.01-p2213-c001 — file p2213, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000368-instructing-party.md); [executing party](../../../../../shared/reference/participants/participant-narrative-src-000369-executing-party.md).

Quoted above in src-000233-reda.031.001.01-p2213-c001-d1.

**src-000233-reda.031.001.01-p2213-c002 — file p2213, usage.**

> It aims at instructing the deletion of an existing party by providing its identification.

**src-000233-reda.031.001.01-p2213-c003 — file p2213, usage.**

> Processing of the party deletion request message is provided via a party status advice.

## src-000369 — 7 reda.031.001.01 PartyDeletionRequestV01

[src-000369](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`; Functionality file pp76; publication march-2024.

### Direction and initiation clauses

#### src-000369-reda.031.001.01-p76-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000369 file p76, scope.

- Sender: **the instructing party**. [the instructing party](../../../../../shared/reference/participants/participant-src-000368-instructing-party.md).
- Receiver: **the executing party**. [the executing party](../../../../../shared/reference/participants/participant-narrative-src-000369-executing-party.md).

> The PartyDeletionRequest message is sent by the instructing party to the executing party to request a deletion of a party defined in the executing system.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000369-reda.031.001.01-p76-c001 — file p76, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000368-instructing-party.md); [executing party](../../../../../shared/reference/participants/participant-narrative-src-000369-executing-party.md).

Quoted above in src-000369-reda.031.001.01-p76-c001-d1.

**src-000369-reda.031.001.01-p76-c002 — file p76, usage.**

> It aims at instructing the deletion of an existing party by providing its identification.

**src-000369-reda.031.001.01-p76-c003 — file p76, usage.**

> Processing of the party deletion request message is provided via a party status advice.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
