---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "reda.013.001.01 participant and direction evidence"
domain: "securities"
message_id: "reda.013.001.01"
message_family: "reda.013"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.013.001.01"
source_ids: ["src-000233", "src-000268", "src-000378"]
message_sets: ["t2s", "t2s-securities-reference-data"]
role_labels: ["an executing/servicing party", "An instructing party", "Bank", "Corporate", "executing/servicing party", "instructing party", "Market Data Provider", "Market Infrastructure", "servicing party"]
search_terms: ["an executing/servicing party", "An instructing party", "Bank", "Corporate", "executing/servicing party", "instructing party", "Market Data Provider", "Market Infrastructure", "servicing party"]
participant_ids: ["participant-narrative-src-000378-bank", "participant-narrative-src-000378-corporate", "participant-narrative-src-000378-executing-servicing-party", "participant-narrative-src-000378-instructing-party", "participant-narrative-src-000378-market-data-provider", "participant-narrative-src-000378-market-infrastructure", "participant-narrative-src-000378-servicing-party"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "33 reda.013.001.01 SecurityDeletionRequestV01", "file_pages": [2039, 2042]}, {"source_id": "src-000378", "heading": "8 reda.013.001.01 SecurityDeletionRequestV01", "file_pages": [115, 118]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# reda.013.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 7 uniquely resolved participant references.

## src-000233 — 33 reda.013.001.01 SecurityDeletionRequestV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); Functionality file pp2039; publication August 2026.

### Direction and initiation clauses

#### src-000233-reda.013.001.01-p2039-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p2039, scope.

- Sender: **An instructing party**. [An instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md).
- Receiver: **an executing/servicing party**. [an executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

> An instructing party sends a SecurityDeletionRequest message to an executing/servicing party to advice the complete removal of a financial instrument entry from their system.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-reda.013.001.01-p2039-c001 — file p2039, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

Literal actions: instructing party sends.

Quoted above in src-000233-reda.013.001.01-p2039-c001-d1.

**src-000233-reda.013.001.01-p2039-c002 — file p2039, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

> The instructing party - executing/servicing party relationship may be:

**src-000233-reda.013.001.01-p2039-c003 — file p2039, scope.**

Mentioned roles: [Corporate](../../../../../shared/reference/participants/participant-narrative-src-000378-corporate.md).

> a Corporate, or

**src-000233-reda.013.001.01-p2039-c004 — file p2039, scope.**

Mentioned roles: [Bank](../../../../../shared/reference/participants/participant-narrative-src-000378-bank.md).

> a Bank, or

**src-000233-reda.013.001.01-p2039-c005 — file p2039, scope.**

Mentioned roles: [Market Infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000378-market-infrastructure.md).

> a Market Infrastructure, or

**src-000233-reda.013.001.01-p2039-c006 — file p2039, scope.**

Mentioned roles: [Market Data Provider](../../../../../shared/reference/participants/participant-narrative-src-000378-market-data-provider.md).

> a Market Data Provider.

**src-000233-reda.013.001.01-p2039-c007 — file p2039, usage.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

Reviewed clause disposition: **actor-or-condition-context**. The sentence describes actors, responsibilities, source/target data, prohibitions or conditions. Existing literal actions and the complete quote remain available; sending/receiving a different object or a negative assertion is not converted into an unconditional current-message direction.

> The request is sent when the instructing party identified that a security is wrongly created in the securities coverage of the executing/servicing party.

**src-000233-reda.013.001.01-p2039-c008 — file p2039, usage.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md); [servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-servicing-party.md).

> The instructing party needs this security to be removed from the executing /servicing party database.

**src-000233-reda.013.001.01-p2039-c009 — file p2039, usage.**

Mentioned roles: [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

> The result of this message is a complete removal of the security identification from the executing/servicing party's database.

**src-000233-reda.013.001.01-p2039-c010 — file p2039, usage.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md).

> Initiator: instructing party.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p2039, scope.**

> Central Securities Depositories (CSD) who would like to publish security static data, or

**File p2039, usage.**

> This message can be used when a security identification code was issued too quickly or if a security identification code needs to be reused (for example, in case of money market instrument).

## src-000378 — 8 reda.013.001.01 SecurityDeletionRequestV01

[src-000378](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`; Functionality file pp115; publication March 2024.

### Direction and initiation clauses

#### src-000378-reda.013.001.01-p115-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000378 file p115, scope.

- Sender: **An instructing party**. [An instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md).
- Receiver: **an executing/servicing party**. [an executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

> An instructing party sends a SecurityDeletionRequest message to an executing/servicing party to advice the complete removal of a financial instrument entry from their system.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000378-reda.013.001.01-p115-c001 — file p115, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

Literal actions: instructing party sends.

Quoted above in src-000378-reda.013.001.01-p115-c001-d1.

**src-000378-reda.013.001.01-p115-c002 — file p115, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

> The instructing party - executing/servicing party relationship may be:

**src-000378-reda.013.001.01-p115-c003 — file p115, scope.**

Mentioned roles: [Corporate](../../../../../shared/reference/participants/participant-narrative-src-000378-corporate.md).

> a Corporate, or

**src-000378-reda.013.001.01-p115-c004 — file p115, scope.**

Mentioned roles: [Bank](../../../../../shared/reference/participants/participant-narrative-src-000378-bank.md).

> a Bank, or

**src-000378-reda.013.001.01-p115-c005 — file p115, scope.**

Mentioned roles: [Market Infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000378-market-infrastructure.md).

> a Market Infrastructure, or

**src-000378-reda.013.001.01-p115-c006 — file p115, scope.**

Mentioned roles: [Market Data Provider](../../../../../shared/reference/participants/participant-narrative-src-000378-market-data-provider.md).

> a Market Data Provider.

**src-000378-reda.013.001.01-p115-c007 — file p115, usage.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

Reviewed clause disposition: **actor-or-condition-context**. The sentence describes actors, responsibilities, source/target data, prohibitions or conditions. Existing literal actions and the complete quote remain available; sending/receiving a different object or a negative assertion is not converted into an unconditional current-message direction.

> The request is sent when the instructing party identified that a security is wrongly created in the securities coverage of the executing/servicing party.

**src-000378-reda.013.001.01-p115-c008 — file p115, usage.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md); [servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-servicing-party.md).

> The instructing party needs this security to be removed from the executing /servicing party database.

**src-000378-reda.013.001.01-p115-c009 — file p115, usage.**

Mentioned roles: [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

> The result of this message is a complete removal of the security identification from the executing/servicing party's database.

**src-000378-reda.013.001.01-p115-c010 — file p115, usage.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md).

> Initiator: instructing party.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p115, scope.**

> Central Securities Depositories (CSD) who would like to publish security static data, or

**File p115, usage.**

> This message can be used when a security identification code was issued too quickly or if a security identification code needs to be reused (for example, in case of money market instrument).

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
