---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "reda.016.001.01 participant and direction evidence"
domain: "securities"
message_id: "reda.016.001.01"
message_family: "reda.016"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.016.001.01"
source_ids: ["src-000233", "src-000271", "src-000369"]
message_sets: ["t2s", "t2s-party-reference-data"]
role_labels: ["executing party", "instructing party", "the executing party", "the instructing party"]
search_terms: ["executing party", "instructing party", "the executing party", "the instructing party"]
participant_ids: ["participant-narrative-src-000369-executing-party", "participant-src-000368-instructing-party"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "36 reda.016.001.01 PartyStatusAdviceV01", "file_pages": [2072, 2077]}, {"source_id": "src-000369", "heading": "4 reda.016.001.01 PartyStatusAdviceV01", "file_pages": [35, 40]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# reda.016.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000233 — 36 reda.016.001.01 PartyStatusAdviceV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); Functionality file pp2072; publication August 2026.

### Direction and initiation clauses

#### src-000233-reda.016.001.01-p2072-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p2072, scope.

- Sender: **the executing party**. [the executing party](../../../../../shared/reference/participants/participant-narrative-src-000369-executing-party.md).
- Receiver: **the instructing party**. [the instructing party](../../../../../shared/reference/participants/participant-src-000368-instructing-party.md).

> The PartyStatusAdvice message is sent by the executing party to the instructing party to provide details about the processing of a request on party reference data (create or update).

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-reda.016.001.01-p2072-c001 — file p2072, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-narrative-src-000369-executing-party.md); [instructing party](../../../../../shared/reference/participants/participant-src-000368-instructing-party.md).

Quoted above in src-000233-reda.016.001.01-p2072-c001-d1.

**src-000233-reda.016.001.01-p2072-c002 — file p2072, usage.**

> When processing is successfully performed, the message includes the related party identification.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p2072, usage.**

> When processing information is negative - a failure occurred in applying the changes the message accordingly also delivers information about the reason why the creation or update could not be processed.

## src-000369 — 4 reda.016.001.01 PartyStatusAdviceV01

[src-000369](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`; Functionality file pp35; publication march-2024.

### Direction and initiation clauses

#### src-000369-reda.016.001.01-p35-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000369 file p35, scope.

- Sender: **the executing party**. [the executing party](../../../../../shared/reference/participants/participant-narrative-src-000369-executing-party.md).
- Receiver: **the instructing party**. [the instructing party](../../../../../shared/reference/participants/participant-src-000368-instructing-party.md).

> The PartyStatusAdvice message is sent by the executing party to the instructing party to provide details about the processing of a request on party reference data (create or update).

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000369-reda.016.001.01-p35-c001 — file p35, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-narrative-src-000369-executing-party.md); [instructing party](../../../../../shared/reference/participants/participant-src-000368-instructing-party.md).

Quoted above in src-000369-reda.016.001.01-p35-c001-d1.

**src-000369-reda.016.001.01-p35-c002 — file p35, usage.**

> When processing is successfully performed, the message includes the related party identification.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p35, usage.**

> When processing information is negative - a failure occurred in applying the changes the message accordingly also delivers information about the reason why the creation or update could not be processed.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
