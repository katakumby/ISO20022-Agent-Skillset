---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "reda.025.001.01 participant and direction evidence"
domain: "securities"
message_id: "reda.025.001.01"
message_family: "reda.025"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.025.001.01"
source_ids: ["src-000233", "src-000280", "src-000354"]
message_sets: ["t2s", "t2s-collateral-management-reference-data"]
role_labels: ["an instructing party", "executing party", "instructing party", "the executing party"]
search_terms: ["an instructing party", "executing party", "instructing party", "the executing party"]
participant_ids: ["participant-narrative-src-000354-executing-party", "participant-src-000353-instructing-party"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "45 reda.025.001.01 EligibleSecuritiesCreationRequestV01", "file_pages": [2173, 2178]}, {"source_id": "src-000354", "heading": "3 reda.025.001.01 EligibleSecuritiesCreationRequestV01", "file_pages": [16, 21]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# reda.025.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000233 — 45 reda.025.001.01 EligibleSecuritiesCreationRequestV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); Functionality file pp2173; publication August 2026.

### Direction and initiation clauses

#### src-000233-reda.025.001.01-p2173-c001-d1

Kind: exchange-participants; message applicability: **current-message**; src-000233 file p2173, scope.

- Exchange participants: **an instructing party and the executing party**. [an instructing party](../../../../../shared/reference/participants/participant-src-000353-instructing-party.md); [the executing party](../../../../../shared/reference/participants/participant-narrative-src-000354-executing-party.md).

> The EligibleSecuritiesCreationRequest message is exchanged between an instructing party and the executing party to request for the creation of an eligible securities in the executing system collateral management reference data.

An exchange-between statement establishes participation, not sender/receiver direction.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-reda.025.001.01-p2173-c001 — file p2173, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000353-instructing-party.md); [executing party](../../../../../shared/reference/participants/participant-narrative-src-000354-executing-party.md).

Quoted above in src-000233-reda.025.001.01-p2173-c001-d1.

**src-000233-reda.025.001.01-p2173-c002 — file p2173, usage.**

> It aims at instructing the creation of a new eligible securities with corresponding details.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p2173, usage.**

> Processing and confirmation of the eligible securities creation request message are provided via a collateral management status advice.

## src-000354 — 3 reda.025.001.01 EligibleSecuritiesCreationRequestV01

[src-000354](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`; Functionality file pp16; publication may-2025.

### Direction and initiation clauses

#### src-000354-reda.025.001.01-p16-c001-d1

Kind: exchange-participants; message applicability: **current-message**; src-000354 file p16, scope.

- Exchange participants: **an instructing party and the executing party**. [an instructing party](../../../../../shared/reference/participants/participant-src-000353-instructing-party.md); [the executing party](../../../../../shared/reference/participants/participant-narrative-src-000354-executing-party.md).

> The EligibleSecuritiesCreationRequest message is exchanged between an instructing party and the executing party to request for the creation of an eligible securities in the executing system collateral management reference data.

An exchange-between statement establishes participation, not sender/receiver direction.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000354-reda.025.001.01-p16-c001 — file p16, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000353-instructing-party.md); [executing party](../../../../../shared/reference/participants/participant-narrative-src-000354-executing-party.md).

Quoted above in src-000354-reda.025.001.01-p16-c001-d1.

**src-000354-reda.025.001.01-p16-c002 — file p16, usage.**

> It aims at instructing the creation of a new eligible securities with corresponding details.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p16, usage.**

> Processing and confirmation of the eligible securities creation request message are provided via a collateral management status advice.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
