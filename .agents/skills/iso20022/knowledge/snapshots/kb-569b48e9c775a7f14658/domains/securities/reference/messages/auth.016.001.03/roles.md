---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "auth.016.001.03 participant and direction evidence"
domain: "securities"
message_id: "auth.016.001.03"
message_family: "auth.016"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03"
source_ids: ["src-000321", "src-000323"]
message_sets: ["fitrr"]
role_labels: ["competent authority", "reporting agent", "the competent authority", "the reporting agent"]
search_terms: ["competent authority", "reporting agent", "the competent authority", "the reporting agent"]
participant_ids: ["participant-narrative-src-000321-reporting-agent", "participant-src-000320-competent-authority"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000321", "heading": "2 auth.016.001.03 FinancialInstrumentReportingTransactionReportV03", "file_pages": [8, 14]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# auth.016.001.03 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000321 — 2 auth.016.001.03 FinancialInstrumentReportingTransactionReportV03

[src-000321](../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md); Functionality file pp8; publication July 2025.

### Direction and initiation clauses

#### src-000321-auth.016.001.03-p8-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000321 file p8, scope.

- Sender: **the reporting agent**. [the reporting agent](../../../../../shared/reference/participants/participant-narrative-src-000321-reporting-agent.md).
- Receiver: **the competent authority**. [the competent authority](../../../../../shared/reference/participants/participant-src-000320-competent-authority.md).

> The FinancialInstrumentReportingTransactionReport message is sent by the reporting agent to the competent authority to report on the securities transactions or by the competent authority to another competent authority when the transaction needs to be exchanged between the competent authorities.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000321-auth.016.001.03-p8-c001 — file p8, scope.**

Mentioned roles: [reporting agent](../../../../../shared/reference/participants/participant-narrative-src-000321-reporting-agent.md); [competent authority](../../../../../shared/reference/participants/participant-src-000320-competent-authority.md); [competent authority](../../../../../shared/reference/participants/participant-src-000320-competent-authority.md); [competent authority](../../../../../shared/reference/participants/participant-src-000320-competent-authority.md).

Quoted above in src-000321-auth.016.001.03-p8-c001-d1.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
