---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "reda.022.001.02 participant and direction evidence"
domain: "securities"
message_id: "reda.022.001.02"
message_family: "reda.022"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.022.001.02"
source_ids: ["src-000233", "src-000277", "src-000369"]
message_sets: ["t2s", "t2s-party-reference-data"]
role_labels: ["executing party", "instructing party", "the executing party", "the instructing party"]
search_terms: ["executing party", "instructing party", "the executing party", "the instructing party"]
participant_ids: ["participant-narrative-src-000369-executing-party", "participant-src-000368-instructing-party"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "42 reda.022.001.02 PartyModificationRequestV02", "file_pages": [2140, 2154]}, {"source_id": "src-000369", "heading": "6 reda.022.001.02 PartyModificationRequestV02", "file_pages": [61, 75]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# reda.022.001.02 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000233 — 42 reda.022.001.02 PartyModificationRequestV02

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); Functionality file pp2140; publication August 2026.

### Direction and initiation clauses

#### src-000233-reda.022.001.02-p2140-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p2140, scope.

- Sender: **the instructing party**. [the instructing party](../../../../../shared/reference/participants/participant-src-000368-instructing-party.md).
- Receiver: **the executing party**. [the executing party](../../../../../shared/reference/participants/participant-narrative-src-000369-executing-party.md).

> The PartyModificationRequest message is sent by the instructing party to the executing party to request for an update of the party reference data of a party defined in the executing system.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-reda.022.001.02-p2140-c001 — file p2140, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000368-instructing-party.md); [executing party](../../../../../shared/reference/participants/participant-narrative-src-000369-executing-party.md).

Quoted above in src-000233-reda.022.001.02-p2140-c001-d1.

**src-000233-reda.022.001.02-p2140-c002 — file p2140, usage.**

> It aims at instructing the update of an existing party by amending its existing details or by providing additional details.

**src-000233-reda.022.001.02-p2140-c003 — file p2140, usage.**

> Processing and confirmation of the party modification request message are provided via a party status advice.

## src-000369 — 6 reda.022.001.02 PartyModificationRequestV02

[src-000369](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`; Functionality file pp61; publication march-2024.

### Direction and initiation clauses

#### src-000369-reda.022.001.02-p61-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000369 file p61, scope.

- Sender: **the instructing party**. [the instructing party](../../../../../shared/reference/participants/participant-src-000368-instructing-party.md).
- Receiver: **the executing party**. [the executing party](../../../../../shared/reference/participants/participant-narrative-src-000369-executing-party.md).

> The PartyModificationRequest message is sent by the instructing party to the executing party to request for an update of the party reference data of a party defined in the executing system.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000369-reda.022.001.02-p61-c001 — file p61, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000368-instructing-party.md); [executing party](../../../../../shared/reference/participants/participant-narrative-src-000369-executing-party.md).

Quoted above in src-000369-reda.022.001.02-p61-c001-d1.

**src-000369-reda.022.001.02-p61-c002 — file p61, usage.**

> It aims at instructing the update of an existing party by amending its existing details or by providing additional details.

**src-000369-reda.022.001.02-p61-c003 — file p61, usage.**

> Processing and confirmation of the party modification request message are provided via a party status advice.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
