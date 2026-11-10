---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "reda.028.001.01 participant and direction evidence"
domain: "securities"
message_id: "reda.028.001.01"
message_family: "reda.028"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01"
source_ids: ["src-000233", "src-000283", "src-000354"]
message_sets: ["t2s", "t2s-collateral-management-reference-data"]
role_labels: ["an instructing party", "executing party", "instructing party", "the executing party"]
search_terms: ["an instructing party", "executing party", "instructing party", "the executing party"]
participant_ids: ["participant-narrative-src-000354-executing-party", "participant-src-000353-instructing-party"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "48 reda.028.001.01 CollateralDataStatusAdviceV01", "file_pages": [2193, 2202]}, {"source_id": "src-000354", "heading": "6 reda.028.001.01 CollateralDataStatusAdviceV01", "file_pages": [36, 45]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# reda.028.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000233 — 48 reda.028.001.01 CollateralDataStatusAdviceV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); Functionality file pp2193; publication August 2026.

### Direction and initiation clauses

#### src-000233-reda.028.001.01-p2193-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p2193, scope.

- Sender: **the executing party**. [the executing party](../../../../../shared/reference/participants/participant-narrative-src-000354-executing-party.md).
- Receiver: **an instructing party (the requestor)**. [an instructing party](../../../../../shared/reference/participants/participant-src-000353-instructing-party.md).

> The CollateralDataStatusAdvice message is sent by the executing party to an instructing party (the requestor) to provide information of a request on collateral management reference data.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-reda.028.001.01-p2193-c001 — file p2193, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-narrative-src-000354-executing-party.md); [instructing party](../../../../../shared/reference/participants/participant-src-000353-instructing-party.md).

Quoted above in src-000233-reda.028.001.01-p2193-c001-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p2193, usage.**

> It aims at informing about the status of the request.

## src-000354 — 6 reda.028.001.01 CollateralDataStatusAdviceV01

[src-000354](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`; Functionality file pp36; publication may-2025.

### Direction and initiation clauses

#### src-000354-reda.028.001.01-p36-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000354 file p36, scope.

- Sender: **the executing party**. [the executing party](../../../../../shared/reference/participants/participant-narrative-src-000354-executing-party.md).
- Receiver: **an instructing party (the requestor)**. [an instructing party](../../../../../shared/reference/participants/participant-src-000353-instructing-party.md).

> The CollateralDataStatusAdvice message is sent by the executing party to an instructing party (the requestor) to provide information of a request on collateral management reference data.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000354-reda.028.001.01-p36-c001 — file p36, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-narrative-src-000354-executing-party.md); [instructing party](../../../../../shared/reference/participants/participant-src-000353-instructing-party.md).

Quoted above in src-000354-reda.028.001.01-p36-c001-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p36, usage.**

> It aims at informing about the status of the request.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
