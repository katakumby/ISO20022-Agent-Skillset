---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "reda.026.001.01 participant and direction evidence"
domain: "securities"
message_id: "reda.026.001.01"
message_family: "reda.026"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01"
source_ids: ["src-000233", "src-000281", "src-000354"]
message_sets: ["t2s", "t2s-collateral-management-reference-data"]
role_labels: ["an instructing party", "executing party", "instructing party", "the executing party"]
search_terms: ["an instructing party", "executing party", "instructing party", "the executing party"]
participant_ids: ["participant-narrative-src-000354-executing-party", "participant-src-000353-instructing-party"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "46 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01", "file_pages": [2179, 2186]}, {"source_id": "src-000354", "heading": "4 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01", "file_pages": [22, 29]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# reda.026.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000233 — 46 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); Functionality file pp2179; publication August 2026.

### Direction and initiation clauses

#### src-000233-reda.026.001.01-p2179-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p2179, scope.

- Sender: **an instructing party**. [an instructing party](../../../../../shared/reference/participants/participant-src-000353-instructing-party.md).
- Receiver: **the executing party**. [the executing party](../../../../../shared/reference/participants/participant-narrative-src-000354-executing-party.md).

> The EligibleCounterpartCSDCreationRequest message is sent by an instructing party to the executing party to request for the creation of an eligible counterpart CSD in the executing system collateral management reference data.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-reda.026.001.01-p2179-c001 — file p2179, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000353-instructing-party.md); [executing party](../../../../../shared/reference/participants/participant-narrative-src-000354-executing-party.md).

Quoted above in src-000233-reda.026.001.01-p2179-c001-d1.

**src-000233-reda.026.001.01-p2179-c002 — file p2179, usage.**

> It aims at instructing the creation of a new eligible counterpart CSD with corresponding details.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p2179, usage.**

> Processing and confirmation of the eligible counterpart CSD creation request message are provided via a collateral management status advice.

## src-000354 — 4 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01

[src-000354](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`; Functionality file pp22; publication may-2025.

### Direction and initiation clauses

#### src-000354-reda.026.001.01-p22-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000354 file p22, scope.

- Sender: **an instructing party**. [an instructing party](../../../../../shared/reference/participants/participant-src-000353-instructing-party.md).
- Receiver: **the executing party**. [the executing party](../../../../../shared/reference/participants/participant-narrative-src-000354-executing-party.md).

> The EligibleCounterpartCSDCreationRequest message is sent by an instructing party to the executing party to request for the creation of an eligible counterpart CSD in the executing system collateral management reference data.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000354-reda.026.001.01-p22-c001 — file p22, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000353-instructing-party.md); [executing party](../../../../../shared/reference/participants/participant-narrative-src-000354-executing-party.md).

Quoted above in src-000354-reda.026.001.01-p22-c001-d1.

**src-000354-reda.026.001.01-p22-c002 — file p22, usage.**

> It aims at instructing the creation of a new eligible counterpart CSD with corresponding details.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p22, usage.**

> Processing and confirmation of the eligible counterpart CSD creation request message are provided via a collateral management status advice.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
