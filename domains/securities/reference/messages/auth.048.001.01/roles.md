---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "auth.048.001.01 participant and direction evidence"
domain: "securities"
message_id: "auth.048.001.01"
message_family: "auth.048"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01"
source_ids: ["src-000321", "src-000338"]
message_sets: ["fitrr"]
role_labels: ["ESMA", "National Competent Authorities"]
search_terms: ["ESMA", "National Competent Authorities"]
participant_ids: ["participant-src-000320-esma", "participant-src-000320-nca"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000321", "heading": "17 auth.048.001.01 FinancialInstrumentReportingCurrencyCodeReportV01", "file_pages": [247, 251]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# auth.048.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000321 — 17 auth.048.001.01 FinancialInstrumentReportingCurrencyCodeReportV01

[src-000321](../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf); Functionality file pp247; publication July 2025.

### Direction and initiation clauses

#### src-000321-auth.048.001.01-p247-c001-d1

Kind: creation-and-distribution; message applicability: **current-message**; src-000321 file p247, scope.

- Creator: **ESMA**. [ESMA](../../../../../shared/reference/participants/participant-src-000320-esma.md).
- Distribution recipient: **National Competent Authorities**. [National Competent Authorities](../../../../../shared/reference/participants/participant-src-000320-nca.md).

> The MiFIRCurrencyCodeReport message provides the details the ISO 4217 currency codes and is created by ESMA for distribution to National Competent Authorities.

The source states creation/generation and intended distribution. Creator is not automatically equated with wire sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000321-auth.048.001.01-p247-c001 — file p247, scope.**

Mentioned roles: [National Competent Authorities](../../../../../shared/reference/participants/participant-src-000320-nca.md).

Reviewed clause disposition: **source-explicit-role-assertion**. Exact source Functionality was read. The retained role kind distinguishes creation/distribution/action from wire-message direction.

Quoted above in src-000321-auth.048.001.01-p247-c001-d1.

Functionality role scope was directly reviewed on 2026-11-09. No unstated sender/receiver is manufactured. Header composition, creation/distribution, source wording defects and action-only evidence remain distinct; curated Part1 flow evidence may supply broader context.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
