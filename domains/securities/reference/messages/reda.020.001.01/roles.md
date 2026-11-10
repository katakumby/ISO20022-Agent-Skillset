---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "reda.020.001.01 participant and direction evidence"
domain: "securities"
message_id: "reda.020.001.01"
message_family: "reda.020"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.020.001.01"
source_ids: ["src-000233", "src-000275", "src-000372"]
message_sets: ["t2s", "t2s-securities-account-reference-data"]
role_labels: ["an instructing party", "executing party", "instructing party", "the the executing party"]
search_terms: ["an instructing party", "executing party", "instructing party", "the the executing party"]
participant_ids: ["participant-narrative-src-000372-executing-party", "participant-src-000371-instructing-party"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "40 reda.020.001.01 SecuritiesAccountStatusAdviceV01", "file_pages": [2118, 2123]}, {"source_id": "src-000372", "heading": "4 reda.020.001.01 SecuritiesAccountStatusAdviceV01", "file_pages": [26, 31]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# reda.020.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000233 — 40 reda.020.001.01 SecuritiesAccountStatusAdviceV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); Functionality file pp2118; publication August 2026.

### Direction and initiation clauses

#### src-000233-reda.020.001.01-p2118-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p2118, scope.

- Sender: **the the executing party**. [the the executing party](../../../../../shared/reference/participants/participant-narrative-src-000372-executing-party.md).
- Receiver: **an instructing party**. [an instructing party](../../../../../shared/reference/participants/participant-src-000371-instructing-party.md).

> The SecuritiesAccountStatusAdvice message is send by the the executing party to an instructing party to provide the status of the execution of an creation, modification or deletion of securities account reference data.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-reda.020.001.01-p2118-c001 — file p2118, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-narrative-src-000372-executing-party.md); [instructing party](../../../../../shared/reference/participants/participant-src-000371-instructing-party.md).

Quoted above in src-000233-reda.020.001.01-p2118-c001-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p2118, usage.**

> When processing information is negative - a failure occurred in applying the changes the message accordingly also delivers information about the reason why the creation or update could not be processed.

**File p2118, usage.**

> When the processing is succesfully performed, the message includes the related securities account identification.

## src-000372 — 4 reda.020.001.01 SecuritiesAccountStatusAdviceV01

[src-000372](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`; Functionality file pp26; publication december-2019.

### Direction and initiation clauses

#### src-000372-reda.020.001.01-p26-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000372 file p26, scope.

- Sender: **the the executing party**. [the the executing party](../../../../../shared/reference/participants/participant-narrative-src-000372-executing-party.md).
- Receiver: **an instructing party**. [an instructing party](../../../../../shared/reference/participants/participant-src-000371-instructing-party.md).

> The SecuritiesAccountStatusAdvice message is send by the the executing party to an instructing party to provide the status of the execution of an creation, modification or deletion of securities account reference data.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000372-reda.020.001.01-p26-c001 — file p26, scope.**

Mentioned roles: [executing party](../../../../../shared/reference/participants/participant-narrative-src-000372-executing-party.md); [instructing party](../../../../../shared/reference/participants/participant-src-000371-instructing-party.md).

Quoted above in src-000372-reda.020.001.01-p26-c001-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p26, usage.**

> When processing information is negative - a failure occurred in applying the changes the message accordingly also delivers information about the reason why the creation or update could not be processed.

**File p26, usage.**

> When the processing is succesfully performed, the message includes the related securities account identification.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
