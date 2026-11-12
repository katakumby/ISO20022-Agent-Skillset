---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "head.002.001.01 participant and direction evidence"
domain: "shared"
message_id: "head.002.001.01"
message_family: "head.002"
namespace: "urn:iso:std:iso:20022:tech:xsd:head.002.001.01"
source_ids: ["src-000233", "src-000261", "src-000349"]
message_sets: ["t2s", "t2s-business-file-header"]
role_labels: ["receiving party", "sender of the file"]
search_terms: ["receiving party", "sender of the file"]
participant_ids: ["bfh-file-receiver", "bfh-file-sender"]
role_extraction_status: "narrative-only-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "26 head.002.001.01 BusinessFileHeaderV01", "file_pages": [614, 618]}, {"source_id": "src-000349", "heading": "2 head.002.001.01 BusinessFileHeaderV01", "file_pages": [4, 8]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# head.002.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **narrative-only-needs-review**. 0 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000233 — 26 head.002.001.01 BusinessFileHeaderV01

[src-000233](../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); Functionality file pp614; publication August 2026.

### Direction and initiation clauses

No complete sender/receiver pattern was resolved here. This does not establish that the message has no participants. Consult the remaining narrative evidence and original.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-head.002.001.01-p614-c001 — file p614, scope.**

> The Business File Header contains information about the parties involved in the file exchange, as well as information about the content and its structure.

**src-000233-head.002.001.01-p614-c002 — file p614, scope.**

Mentioned roles: [sender of the file](../../participants/bfh-file-sender.md).

> Provides information about the sender of the file.

**src-000233-head.002.001.01-p614-c003 — file p614, scope.**

Mentioned roles: [receiving party](../../participants/bfh-file-receiver.md).

Literal actions: receiving party receives processing information.

Reviewed clause disposition: **source-explicit-role-action**. The actor and action are named in this sentence; the action object and conditions are retained and are not automatically the indexed message.

> Provides processing information to the receiving party: that would be, for instance, the total number of messages included in the file.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p614, scope.**

> The Business File headers has four major functions:

**File p614, scope.**

> Identifies the file exchanged: each file must have a unique File Identifier.

**File p614, scope.**

> Describes the type of message(s) exchanged: by default, the type of messages contained in a file will be ISO 20022 message definitions.

**File p614, scope.**

> The Business File Header (head.002) is to be used exclusively in existing implementations, such as the Eurosystem, and will be replaced for general use by the upcoming next version defined as the Business File Envelope (nvlp.002).

**File p614, scope.**

> The Business File Header (head.002) will therefore not be maintained in the future and any new implementation must use the Business File Envelope (nvlp.002).

### Unresolved extraction and interpretation

- source-does-not-state-complete-direction: Functionality was directly reviewed; it supplies content, actions, participant or header context without a complete named sender/receiver direction. Broader curated business/flow evidence remains available.

Functionality role scope was directly reviewed on 2026-11-09. No unstated sender/receiver is manufactured. Header composition, creation/distribution, source wording defects and action-only evidence remain distinct; curated Part1 flow evidence may supply broader context.

## src-000349 — 2 head.002.001.01 BusinessFileHeaderV01

[src-000349](../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`; Functionality file pp4; publication june-2024.

### Direction and initiation clauses

No complete sender/receiver pattern was resolved here. This does not establish that the message has no participants. Consult the remaining narrative evidence and original.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000349-head.002.001.01-p4-c001 — file p4, scope.**

> The Business File Header contains information about the parties involved in the file exchange, as well as information about the content and its structure.

**src-000349-head.002.001.01-p4-c002 — file p4, scope.**

Mentioned roles: [sender of the file](../../participants/bfh-file-sender.md).

> Provides information about the sender of the file.

**src-000349-head.002.001.01-p4-c003 — file p4, scope.**

Mentioned roles: [receiving party](../../participants/bfh-file-receiver.md).

Literal actions: receiving party receives processing information.

Reviewed clause disposition: **source-explicit-role-action**. The actor and action are named in this sentence; the action object and conditions are retained and are not automatically the indexed message.

> Provides processing information to the receiving party: that would be, for instance, the total number of messages included in the file.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p4, scope.**

> The Business File headers has four major functions:

**File p4, scope.**

> Identifies the file exchanged: each file must have a unique File Identifier.

**File p4, scope.**

> Describes the type of message(s) exchanged: by default, the type of messages contained in a file will be ISO 20022 message definitions.

**File p4, scope.**

> The Business File Header (head.002) is to be used exclusively in existing implementations, such as the Eurosystem, and will be replaced for general use by the upcoming next version defined as the Business File Envelope (nvlp.002).

**File p4, scope.**

> The Business File Header (head.002) will therefore not be maintained in the future and any new implementation must use the Business File Envelope (nvlp.002).

### Unresolved extraction and interpretation

- source-does-not-state-complete-direction: Functionality was directly reviewed; it supplies content, actions, participant or header context without a complete named sender/receiver direction. Broader curated business/flow evidence remains available.

Functionality role scope was directly reviewed on 2026-11-09. No unstated sender/receiver is manufactured. Header composition, creation/distribution, source wording defects and action-only evidence remain distinct; curated Part1 flow evidence may supply broader context.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Curated message context](business.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../tracking/issues.md)
