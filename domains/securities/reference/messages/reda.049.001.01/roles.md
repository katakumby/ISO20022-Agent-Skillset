---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "reda.049.001.01 participant and direction evidence"
domain: "securities"
message_id: "reda.049.001.01"
message_family: "reda.049"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.049.001.01"
source_ids: ["src-000233", "src-000303", "src-000366"]
message_sets: ["t2s", "t2s-link-reference-data"]
role_labels: ["Bank", "Central Securities Depositories (CSD)", "Corporate", "executing / servicing party", "executing/servicing party", "instructing party", "Market Data Provider", "Market Infrastructure", "the executing/servicing party", "the instructing party"]
search_terms: ["Bank", "Central Securities Depositories (CSD)", "Corporate", "executing / servicing party", "executing/servicing party", "instructing party", "Market Data Provider", "Market Infrastructure", "the executing/servicing party", "the instructing party"]
participant_ids: ["participant-src-000365-bank", "participant-src-000365-central-securities-depositories-csd", "participant-src-000365-corporate", "participant-src-000365-executing-servicing-party", "participant-src-000365-instructing-party", "participant-src-000365-market-data-provider", "participant-src-000365-market-infrastructure"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "65 reda.049.001.01 AccountLinkCreationRequestV01", "file_pages": [2369, 2374]}, {"source_id": "src-000366", "heading": "5 reda.049.001.01 AccountLinkCreationRequestV01", "file_pages": [35, 40]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# reda.049.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 7 uniquely resolved participant references.

## src-000233 — 65 reda.049.001.01 AccountLinkCreationRequestV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); Functionality file pp2369; publication August 2026.

### Direction and initiation clauses

#### src-000233-reda.049.001.01-p2369-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p2369, scope.

- Sender: **the instructing party**. [the instructing party](../../../../../shared/reference/participants/participant-src-000365-instructing-party.md).
- Receiver: **the executing/servicing party**. [the executing/servicing party](../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md).

> The AccountLinkCreationRequest message is sent by the instructing party to the executing/servicing party to request the creation of an account link between a securities account and a cash account in their system.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-reda.049.001.01-p2369-c001 — file p2369, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000365-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md).

Quoted above in src-000233-reda.049.001.01-p2369-c001-d1.

**src-000233-reda.049.001.01-p2369-c002 — file p2369, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000365-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md).

> The instructing party - executing/servicing party relationship may be:

**src-000233-reda.049.001.01-p2369-c003 — file p2369, scope.**

Mentioned roles: [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000365-central-securities-depositories-csd.md).

> Central Securities Depositories (CSD) who would like to publish account link static data, or

**src-000233-reda.049.001.01-p2369-c004 — file p2369, scope.**

Mentioned roles: [Corporate](../../../../../shared/reference/participants/participant-src-000365-corporate.md).

> a Corporate, or

**src-000233-reda.049.001.01-p2369-c005 — file p2369, scope.**

Mentioned roles: [Bank](../../../../../shared/reference/participants/participant-src-000365-bank.md).

> a Bank, or

**src-000233-reda.049.001.01-p2369-c006 — file p2369, scope.**

Mentioned roles: [Market Infrastructure](../../../../../shared/reference/participants/participant-src-000365-market-infrastructure.md).

> a Market Infrastructure, or

**src-000233-reda.049.001.01-p2369-c007 — file p2369, scope.**

Mentioned roles: [Market Data Provider](../../../../../shared/reference/participants/participant-src-000365-market-data-provider.md).

> a Market Data Provider.

**src-000233-reda.049.001.01-p2369-c008 — file p2369, usage.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000365-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md).

Reviewed clause disposition: **actor-or-condition-context**. The sentence describes actors, responsibilities, source/target data, prohibitions or conditions. Existing literal actions and the complete quote remain available; sending/receiving a different object or a negative assertion is not converted into an unconditional current-message direction.

> The request is sent when the instructing party identified a gap in the account link coverage of the executing/servicing party.

**src-000233-reda.049.001.01-p2369-c009 — file p2369, usage.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000365-instructing-party.md); [executing / servicing party](../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md).

> The instructing party needs this account link to be set-up at the executing / servicing party to perform its activities.

**src-000233-reda.049.001.01-p2369-c010 — file p2369, usage.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000365-instructing-party.md).

> Initiator: instructing party.

## src-000366 — 5 reda.049.001.01 AccountLinkCreationRequestV01

[src-000366](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`; Functionality file pp35; publication december-2024.

### Direction and initiation clauses

#### src-000366-reda.049.001.01-p35-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000366 file p35, scope.

- Sender: **the instructing party**. [the instructing party](../../../../../shared/reference/participants/participant-src-000365-instructing-party.md).
- Receiver: **the executing/servicing party**. [the executing/servicing party](../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md).

> The AccountLinkCreationRequest message is sent by the instructing party to the executing/servicing party to request the creation of an account link between a securities account and a cash account in their system.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000366-reda.049.001.01-p35-c001 — file p35, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000365-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md).

Quoted above in src-000366-reda.049.001.01-p35-c001-d1.

**src-000366-reda.049.001.01-p35-c002 — file p35, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000365-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md).

> The instructing party - executing/servicing party relationship may be:

**src-000366-reda.049.001.01-p35-c003 — file p35, scope.**

Mentioned roles: [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000365-central-securities-depositories-csd.md).

> Central Securities Depositories (CSD) who would like to publish account link static data, or

**src-000366-reda.049.001.01-p35-c004 — file p35, scope.**

Mentioned roles: [Corporate](../../../../../shared/reference/participants/participant-src-000365-corporate.md).

> a Corporate, or

**src-000366-reda.049.001.01-p35-c005 — file p35, scope.**

Mentioned roles: [Bank](../../../../../shared/reference/participants/participant-src-000365-bank.md).

> a Bank, or

**src-000366-reda.049.001.01-p35-c006 — file p35, scope.**

Mentioned roles: [Market Infrastructure](../../../../../shared/reference/participants/participant-src-000365-market-infrastructure.md).

> a Market Infrastructure, or

**src-000366-reda.049.001.01-p35-c007 — file p35, scope.**

Mentioned roles: [Market Data Provider](../../../../../shared/reference/participants/participant-src-000365-market-data-provider.md).

> a Market Data Provider.

**src-000366-reda.049.001.01-p35-c008 — file p35, usage.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000365-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md).

Reviewed clause disposition: **actor-or-condition-context**. The sentence describes actors, responsibilities, source/target data, prohibitions or conditions. Existing literal actions and the complete quote remain available; sending/receiving a different object or a negative assertion is not converted into an unconditional current-message direction.

> The request is sent when the instructing party identified a gap in the account link coverage of the executing/servicing party.

**src-000366-reda.049.001.01-p35-c009 — file p35, usage.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000365-instructing-party.md); [executing / servicing party](../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md).

> The instructing party needs this account link to be set-up at the executing / servicing party to perform its activities.

**src-000366-reda.049.001.01-p35-c010 — file p35, usage.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-src-000365-instructing-party.md).

> Initiator: instructing party.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
