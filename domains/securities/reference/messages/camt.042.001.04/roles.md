---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.042.001.04 participant and direction evidence"
domain: "securities"
message_id: "camt.042.001.04"
message_family: "camt.042"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.042.001.04"
source_ids: ["src-000096", "src-000105"]
message_sets: ["investment-funds"]
role_labels: ["A report provider", "agent", "fund management company", "investment manager", "report provider", "report user", "the report user", "transfer agent"]
search_terms: ["A report provider", "agent", "fund management company", "investment manager", "report provider", "report user", "the report user", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-agent", "participant-narrative-src-000096-investment-manager", "participant-src-000095-fund-management-company", "participant-src-000095-reporting-party", "participant-src-000095-requesting-party", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "9 camt.042.001.04 FundDetailedEstimatedCashForecastReportV04", "file_pages": [116, 125]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.042.001.04 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 6 uniquely resolved participant references.

## src-000096 — 9 camt.042.001.04 FundDetailedEstimatedCashForecastReportV04

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); Functionality file pp116, 117; publication May 2026.

### Direction and initiation clauses

#### src-000096-camt.042.001.04-p116-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p116, scope.

- Sender: **A report provider, such as a transfer agent**. [A report provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md).
- Receiver: **the report user, such as an investment manager or pricing agent**. [the report user](../../../../../shared/reference/participants/participant-src-000095-requesting-party.md).

> A report provider, such as a transfer agent, sends the FundDetailedEstimatedCashForecastReport message to the report user, such as an investment manager or pricing agent, to report the estimated cash incomings and outgoings, sorted by country, institution name or other criteria defined by the user of one or more share classes of an investment fund on one or more trade dates.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-camt.042.001.04-p116-c001 — file p116, scope.**

Mentioned roles: [report provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [report user](../../../../../shared/reference/participants/participant-src-000095-requesting-party.md); [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000096-investment-manager.md); [agent](../../../../../shared/reference/participants/participant-functionality-src-000096-agent.md).

Quoted above in src-000096-camt.042.001.04-p116-c001-d1.

**src-000096-camt.042.001.04-p116-c002 — file p116, usage.**

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> The FundDetailedEstimatedCashForecastReport is used to provide estimated cash movements, that is, it is sent prior to the cut-off time and/or the price valuation of the fund.

**src-000096-camt.042.001.04-p116-c003 — file p116, usage.**

Mentioned roles: [fund management company](../../../../../shared/reference/participants/participant-src-000095-fund-management-company.md); [report provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md).

> The FundDetailedEstimatedCashForecastReport message is used to report cash movements in or out of a fund, organised by party, such as fund management company, country, currency or by some other criteria defined by the report provider.

**src-000096-camt.042.001.04-p116-c004 — file p116, usage.**

> If the report is used to give the cash-in and cash-out for a party, then additional criteria, such as currency and country, can be specified.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p116, scope.**

> The cash movements may result from, for example, redemption, subscription, switch transactions or reinvestment of dividends.

**File p116, usage.**

> The message contains incoming and outgoing cash flows that are estimated, that is, the price has not been applied.

**File p116, usage.**

> If the price is definitive, then the FundDetailedConfirmedCashForecastReport message must be used.

**File p116, usage.**

> The message structure allows for the following uses:

**File p116, usage.**

> to provide cash in and cash out amounts for a fund/sub fund and one or more share classes (a FundOrSubFundDetails sequence and one or more EstimatedFundCashForecastDetails sequences are used),

**File p116, usage.**

> to provide cash in and cash out amounts for one or more share classes (one or more EstimatedFundCashForecastDetails sequences are used).

**File p116, usage.**

> If the report is to provide estimated cash in and cash out for a fund/sub fund only and not for one or more share classes, then the FundEstimatedCashForecastReport message must be used.

**File p116, usage.**

> In addition, the underlying transaction type for the cash-in or cash-out movement can be specified, as well as information about the cash movement's underlying orders, such as commission and charges.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
