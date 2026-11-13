---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "reda.036.001.01 participant and direction evidence"
domain: "securities"
message_id: "reda.036.001.01"
message_family: "reda.036"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01"
source_ids: ["src-000233", "src-000291", "src-000372"]
message_sets: ["t2s", "t2s-securities-account-reference-data"]
role_labels: ["an instructing party", "executing party", "instructing party", "the executing party"]
search_terms: ["an instructing party", "executing party", "instructing party", "the executing party"]
participant_ids: ["participant-narrative-src-000372-executing-party", "participant-src-000371-instructing-party"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "56 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01", "file_pages": [2241, 2244]}, {"source_id": "src-000372", "heading": "9 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01", "file_pages": [64, 67]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# reda.036.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000233 — 56 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); Functionality file pp2241; publication August 2026.

### Direction and initiation clauses

#### src-000233-reda.036.001.01-p2241-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p2241, scope.

- Sender: **an instructing party**. [an instructing party](../../../../../shared/reference/participants/participant-src-000371-instructing-party.md).
- Receiver: **the executing party**. [the executing party](../../../../../shared/reference/participants/participant-narrative-src-000372-executing-party.md).

> The SecuritiesAccountAuditTrailQuery message is sent by an instructing party to the executing party to query for the securities account audit trail recorded in the system.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-reda.036.001.01-p2241-c001 — file p2241, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000371-instructing-party.md); [executing party](../../../../../shared/reference/participants/participant-narrative-src-000372-executing-party.md).

Quoted above in src-000233-reda.036.001.01-p2241-c001-d1.

## src-000372 — 9 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01

[src-000372](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`; Functionality file pp64; publication december-2019.

### Direction and initiation clauses

#### src-000372-reda.036.001.01-p64-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000372 file p64, scope.

- Sender: **an instructing party**. [an instructing party](../../../../../shared/reference/participants/participant-src-000371-instructing-party.md).
- Receiver: **the executing party**. [the executing party](../../../../../shared/reference/participants/participant-narrative-src-000372-executing-party.md).

> The SecuritiesAccountAuditTrailQuery message is sent by an instructing party to the executing party to query for the securities account audit trail recorded in the system.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000372-reda.036.001.01-p64-c001 — file p64, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000371-instructing-party.md); [executing party](../../../../../shared/reference/participants/participant-narrative-src-000372-executing-party.md).

Quoted above in src-000372-reda.036.001.01-p64-c001-d1.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
