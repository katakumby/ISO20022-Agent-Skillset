---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "auth.043.001.01 participant and direction evidence"
domain: "securities"
message_id: "auth.043.001.01"
message_family: "auth.043"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.043.001.01"
source_ids: ["src-000321", "src-000334"]
message_sets: ["fitrr"]
role_labels: ["National Competent Authorities"]
search_terms: ["National Competent Authorities"]
participant_ids: ["participant-src-000320-nca"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000321", "heading": "13 auth.043.001.01 FinancialInstrumentReportingReferenceDataIndexReportV01", "file_pages": [211, 216]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# auth.043.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 1 uniquely resolved participant references.

## src-000321 — 13 auth.043.001.01 FinancialInstrumentReportingReferenceDataIndexReportV01

[src-000321](../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md); Functionality file pp211; publication July 2025.

### Direction and initiation clauses

#### src-000321-auth.043.001.01-p211-c001-d1

Kind: sender-only; message applicability: **current-message**; src-000321 file p211, scope.

- Sender: **National Competent Authorities**. [National Competent Authorities](../../../../../shared/reference/participants/participant-src-000320-nca.md).

> This FinancialInstrumentReportingReferenceDataIndexReport message is sent by National Competent Authorities to express an interest in receiving data on European indices.

The clause supplies the sender and a purpose introduced by “to”; it does not explicitly name a receiver.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000321-auth.043.001.01-p211-c001 — file p211, scope.**

Mentioned roles: [National Competent Authorities](../../../../../shared/reference/participants/participant-src-000320-nca.md).

Quoted above in src-000321-auth.043.001.01-p211-c001-d1.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
