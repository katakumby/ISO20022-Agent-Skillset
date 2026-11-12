---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.064.001.01 participant and direction evidence"
domain: "securities"
message_id: "camt.064.001.01"
message_family: "camt.064"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01"
source_ids: ["src-000233", "src-000240", "src-000363"]
message_sets: ["t2s", "t2s-limit-utilisation-journal"]
role_labels: ["a central securities depository", "a directly connected system participant", "bank", "central counter party", "central securities depository", "central securities depository participant", "central system", "directly connected system participant", "system participant", "the central system"]
search_terms: ["a central securities depository", "a directly connected system participant", "bank", "central counter party", "central securities depository", "central securities depository participant", "central system", "directly connected system participant", "system participant", "the central system"]
participant_ids: ["participant-functionality-src-000363-central-system", "participant-narrative-src-000363-bank", "participant-narrative-src-000363-central-counter-party", "participant-narrative-src-000363-central-securities-depository", "participant-narrative-src-000363-central-securities-depository-participant", "participant-narrative-src-000363-directly-connected-system-participant", "participant-narrative-src-000363-system-participant"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "5 camt.064.001.01 LimitUtilisationJournalQueryV01", "file_pages": [68, 72]}, {"source_id": "src-000363", "heading": "2 camt.064.001.01 LimitUtilisationJournalQueryV01", "file_pages": [4, 8]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.064.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 7 uniquely resolved participant references.

## src-000233 — 5 camt.064.001.01 LimitUtilisationJournalQueryV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); Functionality file pp68; publication August 2026.

### Direction and initiation clauses

#### src-000233-camt.064.001.01-p68-c001-d1

Kind: exchange-participants; message applicability: **current-message**; src-000233 file p68, scope.

- Exchange participants: **a central securities depository or a directly connected system participant (the central securities depository participant granted direct access, like a bank or a central counter party) and the central system**. [a central securities depository](../../../../../shared/reference/participants/participant-narrative-src-000363-central-securities-depository.md); [a directly connected system participant](../../../../../shared/reference/participants/participant-narrative-src-000363-directly-connected-system-participant.md); [the central system](../../../../../shared/reference/participants/participant-functionality-src-000363-central-system.md).

> The LimitUtilisationJournalQuery message is exchanged between a central securities depository or a directly connected system participant (the central securities depository participant granted direct access, like a bank or a central counter party) and the central system.

An exchange-between statement establishes participation, not sender/receiver direction.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-camt.064.001.01-p68-c001 — file p68, scope.**

Mentioned roles: [central securities depository](../../../../../shared/reference/participants/participant-narrative-src-000363-central-securities-depository.md); [directly connected system participant](../../../../../shared/reference/participants/participant-narrative-src-000363-directly-connected-system-participant.md); [central securities depository participant](../../../../../shared/reference/participants/participant-narrative-src-000363-central-securities-depository-participant.md); [bank](../../../../../shared/reference/participants/participant-narrative-src-000363-bank.md); [central counter party](../../../../../shared/reference/participants/participant-narrative-src-000363-central-counter-party.md); [central system](../../../../../shared/reference/participants/participant-functionality-src-000363-central-system.md).

Quoted above in src-000233-camt.064.001.01-p68-c001-d1.

**src-000233-camt.064.001.01-p68-c002 — file p68, scope.**

Mentioned roles: [system participant](../../../../../shared/reference/participants/participant-narrative-src-000363-system-participant.md).

> Its purpose is to query information regarding the journal of transaction impacting the utilisation of limits that have been defined by the system participant.

## src-000363 — 2 camt.064.001.01 LimitUtilisationJournalQueryV01

[src-000363](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`; Functionality file pp4; publication february-2025.

### Direction and initiation clauses

#### src-000363-camt.064.001.01-p4-c001-d1

Kind: exchange-participants; message applicability: **current-message**; src-000363 file p4, scope.

- Exchange participants: **a central securities depository or a directly connected system participant (the central securities depository participant granted direct access, like a bank or a central counter party) and the central system**. [a central securities depository](../../../../../shared/reference/participants/participant-narrative-src-000363-central-securities-depository.md); [a directly connected system participant](../../../../../shared/reference/participants/participant-narrative-src-000363-directly-connected-system-participant.md); [the central system](../../../../../shared/reference/participants/participant-functionality-src-000363-central-system.md).

> The LimitUtilisationJournalQuery message is exchanged between a central securities depository or a directly connected system participant (the central securities depository participant granted direct access, like a bank or a central counter party) and the central system.

An exchange-between statement establishes participation, not sender/receiver direction.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000363-camt.064.001.01-p4-c001 — file p4, scope.**

Mentioned roles: [central securities depository](../../../../../shared/reference/participants/participant-narrative-src-000363-central-securities-depository.md); [directly connected system participant](../../../../../shared/reference/participants/participant-narrative-src-000363-directly-connected-system-participant.md); [central securities depository participant](../../../../../shared/reference/participants/participant-narrative-src-000363-central-securities-depository-participant.md); [bank](../../../../../shared/reference/participants/participant-narrative-src-000363-bank.md); [central counter party](../../../../../shared/reference/participants/participant-narrative-src-000363-central-counter-party.md); [central system](../../../../../shared/reference/participants/participant-functionality-src-000363-central-system.md).

Quoted above in src-000363-camt.064.001.01-p4-c001-d1.

**src-000363-camt.064.001.01-p4-c002 — file p4, scope.**

Mentioned roles: [system participant](../../../../../shared/reference/participants/participant-narrative-src-000363-system-participant.md).

> Its purpose is to query information regarding the journal of transaction impacting the utilisation of limits that have been defined by the system participant.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
