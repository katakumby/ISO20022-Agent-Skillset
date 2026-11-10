---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "reda.001.001.05 participant and direction evidence"
domain: "securities"
message_id: "reda.001.001.05"
message_family: "reda.001"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.001.001.05"
source_ids: ["src-000096", "src-000109"]
message_sets: ["investment-funds"]
role_labels: ["A report provider", "fund accountant", "fund management company", "market data provider", "other interested party", "regulator", "report provider", "report recipient", "the report provider", "the report recipient", "transfer agent"]
search_terms: ["A report provider", "fund accountant", "fund management company", "market data provider", "other interested party", "regulator", "report provider", "report recipient", "the report provider", "the report recipient", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-report-recipient", "participant-src-000095-fund-accountant", "participant-src-000095-fund-management-company", "participant-src-000095-market-data-provider", "participant-src-000095-other-interested-party", "participant-src-000095-regulator", "participant-src-000095-reporting-party", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "13 reda.001.001.05 PriceReportV05", "file_pages": [159, 221]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# reda.001.001.05 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 8 uniquely resolved participant references.

## src-000096 — 13 reda.001.001.05 PriceReportV05

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); Functionality file pp159, 160; publication May 2026.

### Direction and initiation clauses

#### src-000096-reda.001.001.05-p159-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p159, scope.

- Sender: **A report provider, for example, a transfer agent, fund accountant or market data provider**. [A report provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md).
- Receiver: **the report recipient, for example, a fund management company, transfer agent, market data provider, regulator or any other interested party**. [the report recipient](../../../../../shared/reference/participants/participant-functionality-src-000096-report-recipient.md).

> A report provider, for example, a transfer agent, fund accountant or market data provider, sends the PriceReport message to the report recipient, for example, a fund management company, transfer agent, market data provider, regulator or any other interested party to provide the net asset value and price information for financial instruments on specific trade dates and, optionally, to quote price variation information.

#### src-000096-reda.001.001.05-p159-c002-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p159, usage.

- Sender: **the report provider**. [the report provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md).
- Receiver: **the report recipient**. [the report recipient](../../../../../shared/reference/participants/participant-functionality-src-000096-report-recipient.md).

> The PriceReport message is sent by the report provider to the report recipient to:

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-reda.001.001.05-p159-c001 — file p159, scope.**

Mentioned roles: [report provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [fund accountant](../../../../../shared/reference/participants/participant-src-000095-fund-accountant.md); [market data provider](../../../../../shared/reference/participants/participant-src-000095-market-data-provider.md); [report recipient](../../../../../shared/reference/participants/participant-functionality-src-000096-report-recipient.md); [fund management company](../../../../../shared/reference/participants/participant-src-000095-fund-management-company.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [market data provider](../../../../../shared/reference/participants/participant-src-000095-market-data-provider.md); [regulator](../../../../../shared/reference/participants/participant-src-000095-regulator.md); [other interested party](../../../../../shared/reference/participants/participant-src-000095-other-interested-party.md).

Quoted above in src-000096-reda.001.001.05-p159-c001-d1.

**src-000096-reda.001.001.05-p159-c002 — file p159, usage.**

Mentioned roles: [report provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md); [report recipient](../../../../../shared/reference/participants/participant-functionality-src-000096-report-recipient.md).

Quoted above in src-000096-reda.001.001.05-p159-c002-d1.

**src-000096-reda.001.001.05-p159-c003 — file p159, usage.**

> inform another party that the quotation of a financial instrument is suspended,

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p159, usage.**

> report prices for one or several different financial instruments for one or several different trade dates,

**File p159, usage.**

> report statistical information about the valuation of a financial instrument,

**File p159, usage.**

> report prices that are used for other purposes than the execution of investment funds orders. .

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
