---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "reda.002.001.05 participant and direction evidence"
domain: "securities"
message_id: "reda.002.001.05"
message_family: "reda.002"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.002.001.05"
source_ids: ["src-000096", "src-000110"]
message_sets: ["investment-funds"]
role_labels: ["A report provider", "fund accountant", "fund management company", "market data provider", "other interested party", "regulator", "report provider", "report recipient", "the report recipient", "transfer agent"]
search_terms: ["A report provider", "fund accountant", "fund management company", "market data provider", "other interested party", "regulator", "report provider", "report recipient", "the report recipient", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-report-recipient", "participant-src-000095-fund-accountant", "participant-src-000095-fund-management-company", "participant-src-000095-market-data-provider", "participant-src-000095-other-interested-party", "participant-src-000095-regulator", "participant-src-000095-reporting-party", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "14 reda.002.001.05 PriceReportCancellationV05", "file_pages": [222, 290]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# reda.002.001.05 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 8 uniquely resolved participant references.

## src-000096 — 14 reda.002.001.05 PriceReportCancellationV05

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); Functionality file pp222, 223; publication May 2026.

### Direction and initiation clauses

#### src-000096-reda.002.001.05-p222-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p222, scope.

- Sender: **A report provider, for example, a transfer agent, fund accountant or market data provider**. [A report provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md).
- Receiver: **the report recipient, for example, a fund management company, transfer agent, market data provider, regulator or any other interested party**. [the report recipient](../../../../../shared/reference/participants/participant-functionality-src-000096-report-recipient.md).

> A report provider, for example, a transfer agent, fund accountant or market data provider, sends the PriceReportCancellation message to the report recipient, for example, a fund management company, transfer agent, market data provider, regulator or any other interested party to cancel previously sent prices.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-reda.002.001.05-p222-c001 — file p222, scope.**

Mentioned roles: [report provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [fund accountant](../../../../../shared/reference/participants/participant-src-000095-fund-accountant.md); [market data provider](../../../../../shared/reference/participants/participant-src-000095-market-data-provider.md); [report recipient](../../../../../shared/reference/participants/participant-functionality-src-000096-report-recipient.md); [fund management company](../../../../../shared/reference/participants/participant-src-000095-fund-management-company.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [market data provider](../../../../../shared/reference/participants/participant-src-000095-market-data-provider.md); [regulator](../../../../../shared/reference/participants/participant-src-000095-regulator.md); [other interested party](../../../../../shared/reference/participants/participant-src-000095-other-interested-party.md).

Quoted above in src-000096-reda.002.001.05-p222-c001-d1.

**src-000096-reda.002.001.05-p222-c002 — file p222, usage.**

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> cancel an entire PriceReport that was previously sent (by quoting the business reference of the original price report in the PriceReportIdentification element), or,

**src-000096-reda.002.001.05-p222-c003 — file p222, usage.**

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> cancel one or more individual prices from a previously sent price report (by using the PriceDetailsToBeCancelled sequence).

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p222, usage.**

> The PriceReportCancellation message is used to either:

**File p222, usage.**

> Technically, it is possible to cancel all the prices individually by using the PriceDetailsToBeCancelled sequence, but this is not recommended.

**File p222, usage.**

> The cancellation should not contain the cancellation of prices for more than one NAV date.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
