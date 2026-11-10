---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "reda.051.001.01 participant and direction evidence"
domain: "securities"
message_id: "reda.051.001.01"
message_family: "reda.051"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.051.001.01"
source_ids: ["src-000233", "src-000305", "src-000366"]
message_sets: ["t2s", "t2s-link-reference-data"]
role_labels: ["Bank", "Central Securities Depositories (CSD)", "Corporate", "executing/servicing party", "instructing party", "Market Data Provider", "Market Infrastructure", "the executing/servicing party", "the instructing party"]
search_terms: ["Bank", "Central Securities Depositories (CSD)", "Corporate", "executing/servicing party", "instructing party", "Market Data Provider", "Market Infrastructure", "the executing/servicing party", "the instructing party"]
participant_ids: ["participant-src-000365-bank", "participant-src-000365-central-securities-depositories-csd", "participant-src-000365-corporate", "participant-src-000365-executing-servicing-party", "participant-src-000365-instructing-party", "participant-src-000365-market-data-provider", "participant-src-000365-market-infrastructure"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "67 reda.051.001.01 AccountLinkStatusAdviceV01", "file_pages": [2381, 2388]}, {"source_id": "src-000366", "heading": "7 reda.051.001.01 AccountLinkStatusAdviceV01", "file_pages": [47, 54]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# reda.051.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 7 uniquely resolved participant references.

## src-000233 — 67 reda.051.001.01 AccountLinkStatusAdviceV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); Functionality file pp2381; publication August 2026.

### Direction and initiation clauses

#### src-000233-reda.051.001.01-p2381-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p2381, scope.

- Sender: **the executing/servicing party**. [the executing/servicing party](../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md).
- Receiver: **the instructing party**. [the instructing party](../../../../../shared/reference/participants/participant-src-000365-instructing-party.md).

> The AccountLinkStatusAdvice message is sent by the executing/servicing party to the instructing party to provide details about the processing of a request on account link reference data (create or update).

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-reda.051.001.01-p2381-c001 — file p2381, scope.**

Mentioned roles: [executing/servicing party](../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md); [instructing party](../../../../../shared/reference/participants/participant-src-000365-instructing-party.md).

Quoted above in src-000233-reda.051.001.01-p2381-c001-d1.

**src-000233-reda.051.001.01-p2381-c002 — file p2381, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000365-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md).

> The instructing party - executing/servicing party relationship may be:

**src-000233-reda.051.001.01-p2381-c003 — file p2381, scope.**

Mentioned roles: [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000365-central-securities-depositories-csd.md).

> Central Securities Depositories (CSD) who would like to publish account link static data, or

**src-000233-reda.051.001.01-p2381-c004 — file p2381, scope.**

Mentioned roles: [Corporate](../../../../../shared/reference/participants/participant-src-000365-corporate.md).

> a Corporate, or

**src-000233-reda.051.001.01-p2381-c005 — file p2381, scope.**

Mentioned roles: [Bank](../../../../../shared/reference/participants/participant-src-000365-bank.md).

> a Bank, or

**src-000233-reda.051.001.01-p2381-c006 — file p2381, scope.**

Mentioned roles: [Market Infrastructure](../../../../../shared/reference/participants/participant-src-000365-market-infrastructure.md).

> a Market Infrastructure, or

**src-000233-reda.051.001.01-p2381-c007 — file p2381, scope.**

Mentioned roles: [Market Data Provider](../../../../../shared/reference/participants/participant-src-000365-market-data-provider.md).

> a Market Data Provider.

**src-000233-reda.051.001.01-p2381-c008 — file p2381, usage.**

Mentioned roles: [executing/servicing party](../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md).

> Initiator: executing/servicing party When processing information is negative - a failure occurred in applying the changes the message accordingly also delivers information about the reason why the creation or update could not be processed.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p2381, usage.**

> When the processing is successfully performed, the message includes the related account link identification.

## src-000366 — 7 reda.051.001.01 AccountLinkStatusAdviceV01

[src-000366](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`; Functionality file pp47; publication december-2024.

### Direction and initiation clauses

#### src-000366-reda.051.001.01-p47-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000366 file p47, scope.

- Sender: **the executing/servicing party**. [the executing/servicing party](../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md).
- Receiver: **the instructing party**. [the instructing party](../../../../../shared/reference/participants/participant-src-000365-instructing-party.md).

> The AccountLinkStatusAdvice message is sent by the executing/servicing party to the instructing party to provide details about the processing of a request on account link reference data (create or update).

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000366-reda.051.001.01-p47-c001 — file p47, scope.**

Mentioned roles: [executing/servicing party](../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md); [instructing party](../../../../../shared/reference/participants/participant-src-000365-instructing-party.md).

Quoted above in src-000366-reda.051.001.01-p47-c001-d1.

**src-000366-reda.051.001.01-p47-c002 — file p47, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000365-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md).

> The instructing party - executing/servicing party relationship may be:

**src-000366-reda.051.001.01-p47-c003 — file p47, scope.**

Mentioned roles: [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000365-central-securities-depositories-csd.md).

> Central Securities Depositories (CSD) who would like to publish account link static data, or

**src-000366-reda.051.001.01-p47-c004 — file p47, scope.**

Mentioned roles: [Corporate](../../../../../shared/reference/participants/participant-src-000365-corporate.md).

> a Corporate, or

**src-000366-reda.051.001.01-p47-c005 — file p47, scope.**

Mentioned roles: [Bank](../../../../../shared/reference/participants/participant-src-000365-bank.md).

> a Bank, or

**src-000366-reda.051.001.01-p47-c006 — file p47, scope.**

Mentioned roles: [Market Infrastructure](../../../../../shared/reference/participants/participant-src-000365-market-infrastructure.md).

> a Market Infrastructure, or

**src-000366-reda.051.001.01-p47-c007 — file p47, scope.**

Mentioned roles: [Market Data Provider](../../../../../shared/reference/participants/participant-src-000365-market-data-provider.md).

> a Market Data Provider.

**src-000366-reda.051.001.01-p47-c008 — file p47, usage.**

Mentioned roles: [executing/servicing party](../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md).

> Initiator: executing/servicing party When processing information is negative - a failure occurred in applying the changes the message accordingly also delivers information about the reason why the creation or update could not be processed.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p47, usage.**

> When the processing is successfully performed, the message includes the related account link identification.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
