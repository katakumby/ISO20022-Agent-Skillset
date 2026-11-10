---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "reda.012.001.01 participant and direction evidence"
domain: "securities"
message_id: "reda.012.001.01"
message_family: "reda.012"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01"
source_ids: ["src-000233", "src-000267", "src-000378"]
message_sets: ["t2s", "t2s-securities-reference-data"]
role_labels: ["An executing/servicing party", "an instructing party", "Bank", "Corporate", "executing/servicing party", "instructing party", "Market Data Provider", "Market Infrastructure"]
search_terms: ["An executing/servicing party", "an instructing party", "Bank", "Corporate", "executing/servicing party", "instructing party", "Market Data Provider", "Market Infrastructure"]
participant_ids: ["participant-narrative-src-000378-bank", "participant-narrative-src-000378-corporate", "participant-narrative-src-000378-executing-servicing-party", "participant-narrative-src-000378-instructing-party", "participant-narrative-src-000378-market-data-provider", "participant-narrative-src-000378-market-infrastructure"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "32 reda.012.001.01 SecurityReportV01", "file_pages": [1784, 2038]}, {"source_id": "src-000378", "heading": "7 reda.012.001.01 SecurityReportV01", "file_pages": [94, 114]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# reda.012.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 4 direction/initiator/exchange clauses; 6 uniquely resolved participant references.

## src-000233 — 32 reda.012.001.01 SecurityReportV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); Functionality file pp1784; publication August 2026.

### Direction and initiation clauses

#### src-000233-reda.012.001.01-p1784-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p1784, scope.

- Sender: **An executing/servicing party**. [An executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).
- Receiver: **an instructing party**. [an instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md).

> An executing/servicing party sends a SecurityReport message to an instructing party to advise the last known image of securities data's.

#### src-000233-reda.012.001.01-p1784-c002-d1

Kind: sender-only; message applicability: **current-message**; src-000233 file p1784, scope.

- Sender: **executing/servicing party**. [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

> The report may be sent upon request (for example a query) of the instructing party or push by the executing/servicing party.

Source explicitly identifies the party for the push-report alternative; the request/push alternatives remain distinct.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-reda.012.001.01-p1784-c001 — file p1784, scope.**

Mentioned roles: [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md); [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md).

Literal actions: executing/servicing party sends.

Quoted above in src-000233-reda.012.001.01-p1784-c001-d1.

**src-000233-reda.012.001.01-p1784-c002 — file p1784, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

Literal actions: instructing party may request.

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000233-reda.012.001.01-p1784-c002-d1.

**src-000233-reda.012.001.01-p1784-c003 — file p1784, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

> The instructing party - executing/servicing party relationship may be:

**src-000233-reda.012.001.01-p1784-c004 — file p1784, scope.**

Mentioned roles: [Corporate](../../../../../shared/reference/participants/participant-narrative-src-000378-corporate.md).

> a Corporate, or

**src-000233-reda.012.001.01-p1784-c005 — file p1784, scope.**

Mentioned roles: [Bank](../../../../../shared/reference/participants/participant-narrative-src-000378-bank.md).

> a Bank, or

**src-000233-reda.012.001.01-p1784-c006 — file p1784, scope.**

Mentioned roles: [Market Infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000378-market-infrastructure.md).

> a Market Infrastructure, or

**src-000233-reda.012.001.01-p1784-c007 — file p1784, scope.**

Mentioned roles: [Market Data Provider](../../../../../shared/reference/participants/participant-narrative-src-000378-market-data-provider.md).

> a Market Data Provider.

**src-000233-reda.012.001.01-p1784-c008 — file p1784, scope.**

Mentioned roles: [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

> Initiator: executing/servicing party.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p1784, scope.**

> Central Securities Depositories (CSD) who would like to publish security static data, or

## src-000378 — 7 reda.012.001.01 SecurityReportV01

[src-000378](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`; Functionality file pp94; publication March 2024.

### Direction and initiation clauses

#### src-000378-reda.012.001.01-p94-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000378 file p94, scope.

- Sender: **An executing/servicing party**. [An executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).
- Receiver: **an instructing party**. [an instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md).

> An executing/servicing party sends a SecurityReport message to an instructing party to advise the last known image of securities data's.

#### src-000378-reda.012.001.01-p94-c002-d1

Kind: sender-only; message applicability: **current-message**; src-000378 file p94, scope.

- Sender: **executing/servicing party**. [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

> The report may be sent upon request (for example a query) of the instructing party or push by the executing/servicing party.

Source explicitly identifies the party for the push-report alternative; the request/push alternatives remain distinct.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000378-reda.012.001.01-p94-c001 — file p94, scope.**

Mentioned roles: [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md); [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md).

Literal actions: executing/servicing party sends.

Quoted above in src-000378-reda.012.001.01-p94-c001-d1.

**src-000378-reda.012.001.01-p94-c002 — file p94, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

Literal actions: instructing party may request.

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000378-reda.012.001.01-p94-c002-d1.

**src-000378-reda.012.001.01-p94-c003 — file p94, scope.**

Mentioned roles: [instructing party](../../../../../shared/reference/participants/participant-narrative-src-000378-instructing-party.md); [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

> The instructing party - executing/servicing party relationship may be:

**src-000378-reda.012.001.01-p94-c004 — file p94, scope.**

Mentioned roles: [Corporate](../../../../../shared/reference/participants/participant-narrative-src-000378-corporate.md).

> a Corporate, or

**src-000378-reda.012.001.01-p94-c005 — file p94, scope.**

Mentioned roles: [Bank](../../../../../shared/reference/participants/participant-narrative-src-000378-bank.md).

> a Bank, or

**src-000378-reda.012.001.01-p94-c006 — file p94, scope.**

Mentioned roles: [Market Infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000378-market-infrastructure.md).

> a Market Infrastructure, or

**src-000378-reda.012.001.01-p94-c007 — file p94, scope.**

Mentioned roles: [Market Data Provider](../../../../../shared/reference/participants/participant-narrative-src-000378-market-data-provider.md).

> a Market Data Provider.

**src-000378-reda.012.001.01-p94-c008 — file p94, scope.**

Mentioned roles: [executing/servicing party](../../../../../shared/reference/participants/participant-narrative-src-000378-executing-servicing-party.md).

> Initiator: executing/servicing party.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p94, scope.**

> Central Securities Depositories (CSD) who would like to publish security static data, or

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
