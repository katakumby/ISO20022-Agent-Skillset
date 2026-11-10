---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "reda.019.001.01 participant and direction evidence"
domain: "securities"
message_id: "reda.019.001.01"
message_family: "reda.019"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.019.001.01"
source_ids: ["src-000233", "src-000274", "src-000372"]
message_sets: ["t2s", "t2s-securities-account-reference-data"]
role_labels: ["executing party", "instructing party"]
search_terms: ["executing party", "instructing party"]
participant_ids: ["participant-narrative-src-000372-executing-party", "participant-src-000371-instructing-party"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "39 reda.019.001.01 SecuritiesAccountQueryV01", "file_pages": [2106, 2117]}, {"source_id": "src-000372", "heading": "3 reda.019.001.01 SecuritiesAccountQueryV01", "file_pages": [14, 25]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# reda.019.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000233 — 39 reda.019.001.01 SecuritiesAccountQueryV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); Functionality file pp2106; publication August 2026.

### Direction and initiation clauses

#### src-000233-reda.019.001.01-p2106-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p2106, scope.

- Sender: **instructing party**. [instructing party](../../../../../shared/reference/participants/participant-src-000371-instructing-party.md).
- Receiver: **executing party**. [executing party](../../../../../shared/reference/participants/participant-narrative-src-000372-executing-party.md).

> The SecuritiesAccountQuery message sent by an instructing party to the executing party to request the details related to the securities account.

The source omits the verb “is” before “sent”; the explicit by/to roles are retained literally.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-reda.019.001.01-p2106-c001 — file p2106, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000371-instructing-party.md); [executing party](../../../../../shared/reference/participants/participant-narrative-src-000372-executing-party.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000233-reda.019.001.01-p2106-c001-d1.

Functionality role scope was directly reviewed on 2026-11-09. No unstated sender/receiver is manufactured. Header composition, creation/distribution, source wording defects and action-only evidence remain distinct; curated Part1 flow evidence may supply broader context.

## src-000372 — 3 reda.019.001.01 SecuritiesAccountQueryV01

[src-000372](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`; Functionality file pp14; publication december-2019.

### Direction and initiation clauses

#### src-000372-reda.019.001.01-p14-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000372 file p14, scope.

- Sender: **instructing party**. [instructing party](../../../../../shared/reference/participants/participant-src-000371-instructing-party.md).
- Receiver: **executing party**. [executing party](../../../../../shared/reference/participants/participant-narrative-src-000372-executing-party.md).

> The SecuritiesAccountQuery message sent by an instructing party to the executing party to request the details related to the securities account.

The source omits the verb “is” before “sent”; the explicit by/to roles are retained literally.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000372-reda.019.001.01-p14-c001 — file p14, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000371-instructing-party.md); [executing party](../../../../../shared/reference/participants/participant-narrative-src-000372-executing-party.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000372-reda.019.001.01-p14-c001-d1.

Functionality role scope was directly reviewed on 2026-11-09. No unstated sender/receiver is manufactured. Header composition, creation/distribution, source wording defects and action-only evidence remain distinct; curated Part1 flow evidence may supply broader context.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
