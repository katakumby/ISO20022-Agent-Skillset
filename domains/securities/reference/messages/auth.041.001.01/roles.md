---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "auth.041.001.01 participant and direction evidence"
domain: "securities"
message_id: "auth.041.001.01"
message_family: "auth.041"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.041.001.01"
source_ids: ["src-000321", "src-000332"]
message_sets: ["fitrr"]
role_labels: ["national competent authority", "the national competent authority", "the trading venue", "trading venue"]
search_terms: ["national competent authority", "the national competent authority", "the trading venue", "trading venue"]
participant_ids: ["participant-functionality-src-000321-trading-venue", "participant-src-000320-nca"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000321", "heading": "11 auth.041.001.01 FinancialInstrumentReportingNonEquityTradingActivityReportV01", "file_pages": [178, 183]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# auth.041.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000321 — 11 auth.041.001.01 FinancialInstrumentReportingNonEquityTradingActivityReportV01

[src-000321](../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf); Functionality file pp178; publication July 2025.

### Direction and initiation clauses

#### src-000321-auth.041.001.01-p178-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000321 file p178, scope.

- Sender: **the trading venue**. [the trading venue](../../../../../shared/reference/participants/participant-functionality-src-000321-trading-venue.md).
- Receiver: **the national competent authority**. [the national competent authority](../../../../../shared/reference/participants/participant-src-000320-nca.md).

> The FinancialInstrumentReportingNonEquityTradingActivityReport message is sent by the trading venue to the national competent authority to report on non-equity specific trading activity aggregated quantitative data, used for the transparency calculations.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000321-auth.041.001.01-p178-c001 — file p178, scope.**

Mentioned roles: [trading venue](../../../../../shared/reference/participants/participant-functionality-src-000321-trading-venue.md); [national competent authority](../../../../../shared/reference/participants/participant-src-000320-nca.md).

Quoted above in src-000321-auth.041.001.01-p178-c001-d1.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
