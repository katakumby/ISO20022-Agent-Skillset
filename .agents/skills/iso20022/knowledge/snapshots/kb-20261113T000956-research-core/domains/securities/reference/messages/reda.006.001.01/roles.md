---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "reda.006.001.01 participant and direction evidence"
domain: "securities"
message_id: "reda.006.001.01"
message_family: "reda.006"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.006.001.01"
source_ids: ["src-000233", "src-000262", "src-000378"]
message_sets: ["t2s", "t2s-securities-reference-data"]
role_labels: ["an executing/servicing party", "An instructing party", "Bank", "Corporate", "executing/servicing party", "instructing party", "Market Data Provider", "Market Infrastructure", "servicing party"]
search_terms: ["an executing/servicing party", "An instructing party", "Bank", "Corporate", "executing/servicing party", "instructing party", "Market Data Provider", "Market Infrastructure", "servicing party"]
participant_ids: ["participant-narrative-src-000378-bank", "participant-narrative-src-000378-corporate", "participant-narrative-src-000378-executing-servicing-party", "participant-narrative-src-000378-instructing-party", "participant-narrative-src-000378-market-data-provider", "participant-narrative-src-000378-market-infrastructure", "participant-narrative-src-000378-servicing-party"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "27 reda.006.001.01 SecurityCreationRequestV01", "file_pages": [619, 824]}, {"source_id": "src-000378", "heading": "2 reda.006.001.01 SecurityCreationRequestV01", "file_pages": [8, 20]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# reda.006.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 7 uniquely resolved participant references.

## src-000233 — 27 reda.006.001.01 SecurityCreationRequestV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); Functionality file pp619; publication August 2026.

### Direction and initiation clauses

#### src-000233-reda.006.001.01-p619-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p619, scope.

- Sender: **An instructing party**. [An instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md).
- Receiver: **an executing/servicing party**. [an executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

> An instructing party sends a SecurityCreationRequest message to an executing/servicing party to request the creation of financial instrument static details in their system.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-reda.006.001.01-p619-c001 — file p619, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

Literal actions: instructing party sends.

Quoted above in src-000233-reda.006.001.01-p619-c001-d1.

**src-000233-reda.006.001.01-p619-c002 — file p619, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

> The instructing party - executing/servicing party relationship may be:

**src-000233-reda.006.001.01-p619-c003 — file p619, scope.**

Mentioned roles: [Corporate](../../../../../shared/reference/participants/participant-narrative-src-000378-corporate.md).

> a Corporate, or

**src-000233-reda.006.001.01-p619-c004 — file p619, scope.**

Mentioned roles: [Bank](../../../../../shared/reference/participants/participant-narrative-src-000378-bank.md).

> a Bank, or

**src-000233-reda.006.001.01-p619-c005 — file p619, scope.**

Mentioned roles: [Market Infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000378-market-infrastructure.md).

> a Market Infrastructure, or

**src-000233-reda.006.001.01-p619-c006 — file p619, scope.**

Mentioned roles: [Market Data Provider](../../../../../shared/reference/participants/participant-narrative-src-000378-market-data-provider.md).

> a Market Data Provider.

**src-000233-reda.006.001.01-p619-c007 — file p619, usage.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

Reviewed clause disposition: **actor-or-condition-context**. The sentence describes actors, responsibilities, source/target data, prohibitions or conditions. Existing literal actions and the complete quote remain available; sending/receiving a different object or a negative assertion is not converted into an unconditional current-message direction.

> The request is sent when the instructing party identified a gap in the securities coverage of the executing/servicing party.

**src-000233-reda.006.001.01-p619-c008 — file p619, usage.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md); [servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-servicing-party.md).

> The instructing party needs this security to be set-up at the executing / servicing party to perform its activities.

**src-000233-reda.006.001.01-p619-c009 — file p619, usage.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md).

> Initiator: instructing party.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p619, scope.**

> Central Securities Depositories (CSD) who would like to publish security static data, or

## src-000378 — 2 reda.006.001.01 SecurityCreationRequestV01

[src-000378](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`; Functionality file pp8; publication March 2024.

### Direction and initiation clauses

#### src-000378-reda.006.001.01-p8-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000378 file p8, scope.

- Sender: **An instructing party**. [An instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md).
- Receiver: **an executing/servicing party**. [an executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

> An instructing party sends a SecurityCreationRequest message to an executing/servicing party to request the creation of financial instrument static details in their system.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000378-reda.006.001.01-p8-c001 — file p8, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

Literal actions: instructing party sends.

Quoted above in src-000378-reda.006.001.01-p8-c001-d1.

**src-000378-reda.006.001.01-p8-c002 — file p8, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

> The instructing party - executing/servicing party relationship may be:

**src-000378-reda.006.001.01-p8-c003 — file p8, scope.**

Mentioned roles: [Corporate](../../../../../shared/reference/participants/participant-narrative-src-000378-corporate.md).

> a Corporate, or

**src-000378-reda.006.001.01-p8-c004 — file p8, scope.**

Mentioned roles: [Bank](../../../../../shared/reference/participants/participant-narrative-src-000378-bank.md).

> a Bank, or

**src-000378-reda.006.001.01-p8-c005 — file p8, scope.**

Mentioned roles: [Market Infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000378-market-infrastructure.md).

> a Market Infrastructure, or

**src-000378-reda.006.001.01-p8-c006 — file p8, scope.**

Mentioned roles: [Market Data Provider](../../../../../shared/reference/participants/participant-narrative-src-000378-market-data-provider.md).

> a Market Data Provider.

**src-000378-reda.006.001.01-p8-c007 — file p8, usage.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

Reviewed clause disposition: **actor-or-condition-context**. The sentence describes actors, responsibilities, source/target data, prohibitions or conditions. Existing literal actions and the complete quote remain available; sending/receiving a different object or a negative assertion is not converted into an unconditional current-message direction.

> The request is sent when the instructing party identified a gap in the securities coverage of the executing/servicing party.

**src-000378-reda.006.001.01-p8-c008 — file p8, usage.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md); [servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-servicing-party.md).

> The instructing party needs this security to be set-up at the executing / servicing party to perform its activities.

**src-000378-reda.006.001.01-p8-c009 — file p8, usage.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md).

> Initiator: instructing party.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p8, scope.**

> Central Securities Depositories (CSD) who would like to publish security static data, or

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
