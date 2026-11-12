---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "auth.047.001.01 participant and direction evidence"
domain: "securities"
message_id: "auth.047.001.01"
message_family: "auth.047"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.047.001.01"
source_ids: ["src-000321", "src-000337"]
message_sets: ["fitrr"]
role_labels: ["ESMA", "national competent authorities"]
search_terms: ["ESMA", "national competent authorities"]
participant_ids: ["participant-src-000320-esma", "participant-src-000320-nca"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000321", "heading": "16 auth.047.001.01 FinancialInstrumentReportingCountryCodeReportV01", "file_pages": [244, 246]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# auth.047.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000321 — 16 auth.047.001.01 FinancialInstrumentReportingCountryCodeReportV01

[src-000321](../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md); Functionality file pp244; publication July 2025.

### Direction and initiation clauses

#### src-000321-auth.047.001.01-p244-c001-d1

Kind: creation-and-distribution; message applicability: **current-message**; src-000321 file p244, scope.

- Creator: **ESMA**. [ESMA](../../../../../shared/reference/participants/participant-src-000320-esma.md).
- Distribution recipient: **national competent authorities**. [national competent authorities](../../../../../shared/reference/participants/participant-src-000320-nca.md).

> The FinancialInstrumentReportingCountryCodeReport message provides the details of the two character country codes and is created by ESMA for distribution to national competent authorities.

The source states creation/generation and intended distribution. Creator is not automatically equated with wire sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000321-auth.047.001.01-p244-c001 — file p244, scope.**

Mentioned roles: [national competent authorities](../../../../../shared/reference/participants/participant-src-000320-nca.md).

Reviewed clause disposition: **source-explicit-role-assertion**. Exact source Functionality was read. The retained role kind distinguishes creation/distribution/action from wire-message direction.

Quoted above in src-000321-auth.047.001.01-p244-c001-d1.

Functionality role scope was directly reviewed on 2026-11-09. No unstated sender/receiver is manufactured. Header composition, creation/distribution, source wording defects and action-only evidence remain distinct; curated Part1 flow evidence may supply broader context.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
