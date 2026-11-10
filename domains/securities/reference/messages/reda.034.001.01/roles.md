---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "reda.034.001.01 participant and direction evidence"
domain: "securities"
message_id: "reda.034.001.01"
message_family: "reda.034"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.034.001.01"
source_ids: ["src-000233", "src-000289", "src-000378"]
message_sets: ["t2s", "t2s-securities-reference-data"]
role_labels: ["an instructing party", "executing party", "instructing party", "the executing party"]
search_terms: ["an instructing party", "executing party", "instructing party", "the executing party"]
participant_ids: ["participant-narrative-src-000378-executing-party", "participant-narrative-src-000378-instructing-party"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "54 reda.034.001.01 SecuritiesAuditTrailReportV01", "file_pages": [2224, 2235]}, {"source_id": "src-000378", "heading": "12 reda.034.001.01 SecuritiesAuditTrailReportV01", "file_pages": [134, 145]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# reda.034.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000233 — 54 reda.034.001.01 SecuritiesAuditTrailReportV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); Functionality file pp2224; publication August 2026.

### Direction and initiation clauses

#### src-000233-reda.034.001.01-p2224-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p2224, scope.

- Sender: **the executing party**. [the executing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-party.md).
- Receiver: **an instructing party**. [an instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md).

> The SecuritiesAuditTrailReport message is sent by the executing party to an instructing party to provide detailed information on the requested securities audit trail recorded in the system.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-reda.034.001.01-p2224-c001 — file p2224, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-party.md); [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md).

Quoted above in src-000233-reda.034.001.01-p2224-c001-d1.

## src-000378 — 12 reda.034.001.01 SecuritiesAuditTrailReportV01

[src-000378](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`; Functionality file pp134; publication March 2024.

### Direction and initiation clauses

#### src-000378-reda.034.001.01-p134-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000378 file p134, scope.

- Sender: **the executing party**. [the executing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-party.md).
- Receiver: **an instructing party**. [an instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md).

> The SecuritiesAuditTrailReport message is sent by the executing party to an instructing party to provide detailed information on the requested securities audit trail recorded in the system.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000378-reda.034.001.01-p134-c001 — file p134, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-party.md); [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md).

Quoted above in src-000378-reda.034.001.01-p134-c001-d1.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
