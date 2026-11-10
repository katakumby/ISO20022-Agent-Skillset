---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.040.001.04 participant and direction evidence"
domain: "securities"
message_id: "camt.040.001.04"
message_family: "camt.040"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.040.001.04"
source_ids: ["src-000096", "src-000103"]
message_sets: ["investment-funds"]
role_labels: ["A report provider", "agent", "investment manager", "report provider", "report user", "Sender", "the report user", "transfer agent"]
search_terms: ["A report provider", "agent", "investment manager", "report provider", "report user", "Sender", "the report user", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-agent", "participant-functionality-src-000096-sender", "participant-narrative-src-000096-investment-manager", "participant-src-000095-reporting-party", "participant-src-000095-requesting-party", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "7 camt.040.001.04 FundEstimatedCashForecastReportV04", "file_pages": [94, 104]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.040.001.04 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 6 uniquely resolved participant references.

## src-000096 — 7 camt.040.001.04 FundEstimatedCashForecastReportV04

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); Functionality file pp94, 95; publication May 2026.

### Direction and initiation clauses

#### src-000096-camt.040.001.04-p94-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p94, scope.

- Sender: **A report provider, such as a transfer agent**. [A report provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md).
- Receiver: **the report user, such as an investment manager or pricing agent**. [the report user](../../../../../shared/reference/participants/participant-src-000095-requesting-party.md).

> A report provider, such as a transfer agent, sends the FundEstimatedCashForecastReport message to the report user, such as an investment manager or pricing agent, to report the estimated cash incomings and outgoings of one or more share classes of an investment fund on one or more trade dates.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-camt.040.001.04-p94-c001 — file p94, scope.**

Mentioned roles: [report provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [report user](../../../../../shared/reference/participants/participant-src-000095-requesting-party.md); [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000096-investment-manager.md); [agent](../../../../../shared/reference/participants/participant-functionality-src-000096-agent.md).

Quoted above in src-000096-camt.040.001.04-p94-c001-d1.

**src-000096-camt.040.001.04-p94-c002 — file p94, usage.**

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> The FundEstimatedCashForecastReport is used to report estimated cash movements, that is, it is sent prior to the cut-off time and/or the price valuation of the fund.

**src-000096-camt.040.001.04-p94-c003 — file p94, usage.**

Mentioned roles: [report provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md); [Sender](../../../../../shared/reference/participants/participant-functionality-src-000096-sender.md).

> This message allows the report provider to report estimated cash movements in or out of a fund, but does not allow the Sender to categorise these movements, for example by country, or to give details of the underlying orders, commission or charges.

**src-000096-camt.040.001.04-p94-c004 — file p94, usage.**

Mentioned roles: [report provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md).

> If the report provider wishes to give detailed information related to estimated cash movements, then the FundDetailedEstimatedCashForecastReport message must be used.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p94, scope.**

> The cash movements may result from, for example, redemption, subscription, switch transactions or reinvestment of dividends.

**File p94, usage.**

> The message contains incoming and outgoing cash flows that are estimated, that is, the price has not been applied.

**File p94, usage.**

> If the price is definitive, then the FundConfirmedCashForecastReport message must be used.

**File p94, usage.**

> The message structure allows for the following uses:

**File p94, usage.**

> to provide cash in and cash out amounts for a fund/sub fund (FundOrSubFundDetails sequence is used),

**File p94, usage.**

> to provide cash in and cash out amounts for a fund/sub fund and one or more share classes (a FundOrSubFundDetails sequence and one or more EstimatedFundCashForecastDetails sequences are used),

**File p94, usage.**

> to provide cash in and cash out amounts for one or more share classes (one or more EstimatedFundCashForecastDetails sequences are used).

**File p94, usage.**

> to provide cash in and cash out amounts for more than one fund/sub fund, and more than one share classes (two or more FundOrSubFundDetails sequences and two or more EstimatedFundCashForecastDetails sequences and used); however, it should be noted that, in this usage, there is no way to determine which share class belongs to which fund/sub fund from the message content itself, which may not be desirable and the use of this kind of combination should be bilaterally agreed.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
