---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "auth.044.001.03 participant and direction evidence"
domain: "securities"
message_id: "auth.044.001.03"
message_family: "auth.044"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.044.001.03"
source_ids: ["src-000321", "src-000335"]
message_sets: ["fitrr"]
role_labels: ["authority", "entity"]
search_terms: ["authority", "entity"]
participant_ids: ["participant-functionality-src-000321-authority", "participant-functionality-src-000321-entity"]
role_extraction_status: "narrative-only-needs-review"
source_locations: [{"source_id": "src-000321", "heading": "14 auth.044.001.03 FinancialInstrumentReportingEquityTradingActivityResultV03", "file_pages": [217, 226]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# auth.044.001.03 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **narrative-only-needs-review**. 0 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000321 — 14 auth.044.001.03 FinancialInstrumentReportingEquityTradingActivityResultV03

[src-000321](../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf); Functionality file pp217; publication July 2025.

### Direction and initiation clauses

No complete sender/receiver pattern was resolved here. This does not establish that the message has no participants. Consult the remaining narrative evidence and original.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000321-auth.044.001.03-p217-c001 — file p217, scope.**

Mentioned roles: [entity](../../../../../shared/reference/participants/participant-functionality-src-000321-entity.md); [authority](../../../../../shared/reference/participants/participant-functionality-src-000321-authority.md).

Literal actions: entity uses; authority uses.

Reviewed clause disposition: **source-explicit-role-action**. Exact source Functionality was read. The retained role kind distinguishes creation/distribution/action from wire-message direction.

> The FinancialInstrumentReportingEquityTradingActivityResult message is used by an entity or an authority to provide information on computed results data of an equity specific trading activity.

### Unresolved extraction and interpretation

- source-does-not-state-complete-direction: Functionality was directly reviewed; it supplies content, actions, participant or header context without a complete named sender/receiver direction. Broader curated business/flow evidence remains available.

Functionality role scope was directly reviewed on 2026-11-09. No unstated sender/receiver is manufactured. Header composition, creation/distribution, source wording defects and action-only evidence remain distinct; curated Part1 flow evidence may supply broader context.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
