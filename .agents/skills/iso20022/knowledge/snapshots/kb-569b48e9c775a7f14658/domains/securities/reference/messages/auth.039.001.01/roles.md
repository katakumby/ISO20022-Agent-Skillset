---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "auth.039.001.01 participant and direction evidence"
domain: "securities"
message_id: "auth.039.001.01"
message_family: "auth.039"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.039.001.01"
source_ids: ["src-000321", "src-000330"]
message_sets: ["fitrr"]
role_labels: ["competent authority", "reporting entity", "the competent authority", "the reporting entity"]
search_terms: ["competent authority", "reporting entity", "the competent authority", "the reporting entity"]
participant_ids: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000321", "heading": "9 auth.039.001.01 FinancialInstrumentReportingNonWorkingDayReportV01", "file_pages": [166, 169]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# auth.039.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000321 — 9 auth.039.001.01 FinancialInstrumentReportingNonWorkingDayReportV01

[src-000321](../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md); Functionality file pp166; publication July 2025.

### Direction and initiation clauses

#### src-000321-auth.039.001.01-p166-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000321 file p166, scope.

- Sender: **the reporting entity**. [the reporting entity](../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md).
- Receiver: **the competent authority**. [the competent authority](../../../../../shared/reference/participants/participant-src-000320-competent-authority.md).

> The FinancialInstrumentReportingNonWorkingDayReport message is sent by the reporting entity to the competent authority to report on non-working days.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000321-auth.039.001.01-p166-c001 — file p166, scope.**

Mentioned roles: [reporting entity](../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md); [competent authority](../../../../../shared/reference/participants/participant-src-000320-competent-authority.md).

Quoted above in src-000321-auth.039.001.01-p166-c001-d1.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
