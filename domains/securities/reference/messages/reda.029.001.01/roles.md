---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "reda.029.001.01 participant and direction evidence"
domain: "securities"
message_id: "reda.029.001.01"
message_family: "reda.029"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.029.001.01"
source_ids: ["src-000233", "src-000284", "src-000378"]
message_sets: ["t2s", "t2s-securities-reference-data"]
role_labels: ["An executing/servicing party", "an instructing party", "Bank", "Corporate", "executing/servicing party", "instructing party", "Market Data Provider", "Market Infrastructure"]
search_terms: ["An executing/servicing party", "an instructing party", "Bank", "Corporate", "executing/servicing party", "instructing party", "Market Data Provider", "Market Infrastructure"]
participant_ids: ["participant-narrative-src-000378-bank", "participant-narrative-src-000378-corporate", "participant-narrative-src-000378-executing-servicing-party", "participant-narrative-src-000378-instructing-party", "participant-narrative-src-000378-market-data-provider", "participant-narrative-src-000378-market-infrastructure"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "49 reda.029.001.01 SecurityMaintenanceStatusAdviceV01", "file_pages": [2203, 2207]}, {"source_id": "src-000378", "heading": "9 reda.029.001.01 SecurityMaintenanceStatusAdviceV01", "file_pages": [119, 123]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# reda.029.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 6 uniquely resolved participant references.

## src-000233 — 49 reda.029.001.01 SecurityMaintenanceStatusAdviceV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); Functionality file pp2203; publication August 2026.

### Direction and initiation clauses

#### src-000233-reda.029.001.01-p2203-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p2203, scope.

- Sender: **An executing/servicing party**. [An executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).
- Receiver: **an instructing party**. [an instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md).

> An executing/servicing party sends a SecurityMaintenanceStatusAdvice message to an instructing party to report the status of a SecurityMaintencanceRequest message previously sent by the instructing party.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-reda.029.001.01-p2203-c001 — file p2203, scope.**

Mentioned roles: [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md); [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md); [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md).

Literal actions: executing/servicing party sends.

Quoted above in src-000233-reda.029.001.01-p2203-c001-d1.

**src-000233-reda.029.001.01-p2203-c002 — file p2203, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md).

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> The SecurityMaintenanceStatusAdvice message may be sent as a response to the request of the instructing party or not.

**src-000233-reda.029.001.01-p2203-c003 — file p2203, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

> The instructing party - executing/servicing party relationship may be:

**src-000233-reda.029.001.01-p2203-c004 — file p2203, scope.**

Mentioned roles: [Corporate](../../../../../shared/reference/participants/participant-narrative-src-000378-corporate.md).

> a Corporate, or

**src-000233-reda.029.001.01-p2203-c005 — file p2203, scope.**

Mentioned roles: [Bank](../../../../../shared/reference/participants/participant-narrative-src-000378-bank.md).

> a Bank, or

**src-000233-reda.029.001.01-p2203-c006 — file p2203, scope.**

Mentioned roles: [Market Infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000378-market-infrastructure.md).

> a Market Infrastructure, or

**src-000233-reda.029.001.01-p2203-c007 — file p2203, scope.**

Mentioned roles: [Market Data Provider](../../../../../shared/reference/participants/participant-narrative-src-000378-market-data-provider.md).

> a Market Data Provider.

**src-000233-reda.029.001.01-p2203-c008 — file p2203, usage.**

Mentioned roles: [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

> Initiator: executing/servicing party.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p2203, scope.**

> Central Securities Depositories (CSD) who would like to publish security static data, or

## src-000378 — 9 reda.029.001.01 SecurityMaintenanceStatusAdviceV01

[src-000378](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`; Functionality file pp119; publication March 2024.

### Direction and initiation clauses

#### src-000378-reda.029.001.01-p119-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000378 file p119, scope.

- Sender: **An executing/servicing party**. [An executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).
- Receiver: **an instructing party**. [an instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md).

> An executing/servicing party sends a SecurityMaintenanceStatusAdvice message to an instructing party to report the status of a SecurityMaintencanceRequest message previously sent by the instructing party.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000378-reda.029.001.01-p119-c001 — file p119, scope.**

Mentioned roles: [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md); [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md); [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md).

Literal actions: executing/servicing party sends.

Quoted above in src-000378-reda.029.001.01-p119-c001-d1.

**src-000378-reda.029.001.01-p119-c002 — file p119, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md).

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> The SecurityMaintenanceStatusAdvice message may be sent as a response to the request of the instructing party or not.

**src-000378-reda.029.001.01-p119-c003 — file p119, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

> The instructing party - executing/servicing party relationship may be:

**src-000378-reda.029.001.01-p119-c004 — file p119, scope.**

Mentioned roles: [Corporate](../../../../../shared/reference/participants/participant-narrative-src-000378-corporate.md).

> a Corporate, or

**src-000378-reda.029.001.01-p119-c005 — file p119, scope.**

Mentioned roles: [Bank](../../../../../shared/reference/participants/participant-narrative-src-000378-bank.md).

> a Bank, or

**src-000378-reda.029.001.01-p119-c006 — file p119, scope.**

Mentioned roles: [Market Infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000378-market-infrastructure.md).

> a Market Infrastructure, or

**src-000378-reda.029.001.01-p119-c007 — file p119, scope.**

Mentioned roles: [Market Data Provider](../../../../../shared/reference/participants/participant-narrative-src-000378-market-data-provider.md).

> a Market Data Provider.

**src-000378-reda.029.001.01-p119-c008 — file p119, usage.**

Mentioned roles: [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

> Initiator: executing/servicing party.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p119, scope.**

> Central Securities Depositories (CSD) who would like to publish security static data, or

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
