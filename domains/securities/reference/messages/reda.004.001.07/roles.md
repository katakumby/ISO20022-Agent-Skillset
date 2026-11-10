---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "reda.004.001.07 participant and direction evidence"
domain: "securities"
message_id: "reda.004.001.07"
message_family: "reda.004"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07"
source_ids: ["src-000096", "src-000111"]
message_sets: ["investment-funds"]
role_labels: ["a report provider", "distributor", "distributors", "fund management company", "fund manager", "fund promoter", "market data provider", "market infrastructure", "other interested party", "professional investor", "professional investors", "regulator", "regulators", "report provider", "Report Provider", "report recipient", "report user", "report users", "the report recipient", "transfer agent"]
search_terms: ["a report provider", "distributor", "distributors", "fund management company", "fund manager", "fund promoter", "market data provider", "market infrastructure", "other interested party", "professional investor", "professional investors", "regulator", "regulators", "report provider", "Report Provider", "report recipient", "report user", "report users", "the report recipient", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-report-recipient", "participant-narrative-src-000096-distributor", "participant-narrative-src-000096-market-infrastructure", "participant-src-000095-distributor", "participant-src-000095-fund-management-company", "participant-src-000095-fund-manager", "participant-src-000095-fund-promoter", "participant-src-000095-market-data-provider", "participant-src-000095-other-interested-party", "participant-src-000095-professional-investor", "participant-src-000095-regulator", "participant-src-000095-reporting-party", "participant-src-000095-requesting-party", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "15 reda.004.001.07 FundReferenceDataReportV07", "file_pages": [291, 364]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# reda.004.001.07 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 3 direction/initiator/exchange clauses; 14 uniquely resolved participant references.

## src-000096 — 15 reda.004.001.07 FundReferenceDataReportV07

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); Functionality file pp291, 292; publication May 2026.

### Direction and initiation clauses

#### src-000096-reda.004.001.07-p291-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p291, scope.

- Sender: **a report provider, for example, a fund promoter, fund management company, transfer agent, or market data provider**. [a report provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md).
- Receiver: **the report recipient, for example, a professional investor, investment fund distributor, market data provider, regulator or other interested party**. [the report recipient](../../../../../shared/reference/participants/participant-functionality-src-000096-report-recipient.md).

> The FundReferenceDataReport message is sent by a report provider, for example, a fund promoter, fund management company, transfer agent, or market data provider to the report recipient, for example, a professional investor, investment fund distributor, market data provider, regulator or other interested party, to provide the key reference data for financial instruments to facilitate trading.

#### src-000096-reda.004.001.07-p291-c004-d1

Kind: initiator; message applicability: **current-message-standalone-environment**; src-000096 file p291, usage.

- Initiator: **Report Provider**. [Report Provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md).

> in a standalone environment, for example, initiated by the Report Provider (fund promoter, fund manager and / or reference data vendors) sent on a regular frequency, or when changes are needed.

The report provider initiates the standalone reporting environment. Parenthetical fund-promoter/manager/vendor examples are retained without making them aliases.

#### src-000096-reda.004.001.07-p291-c005-d1

Kind: initiator; message applicability: **related-request-response-environment**; src-000096 file p291, usage.

- Initiator: **report users**. [report users](../../../../../shared/reference/participants/participant-src-000095-requesting-party.md).

> in a request / response environment, with the InvestmentFundReportRequest, for example, initiated by report users (data vendors, professional investors, regulators or investment fund distributors) in enabling the user to control the flow and updates of information.

Report users initiate the request/response environment involving InvestmentFundReportRequest; this is not automatically the sender of FundReferenceDataReport.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-reda.004.001.07-p291-c001 — file p291, scope.**

Mentioned roles: [report provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md); [fund promoter](../../../../../shared/reference/participants/participant-src-000095-fund-promoter.md); [fund management company](../../../../../shared/reference/participants/participant-src-000095-fund-management-company.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [market data provider](../../../../../shared/reference/participants/participant-src-000095-market-data-provider.md); [report recipient](../../../../../shared/reference/participants/participant-functionality-src-000096-report-recipient.md); [professional investor](../../../../../shared/reference/participants/participant-src-000095-professional-investor.md); [distributor](../../../../../shared/reference/participants/participant-src-000095-distributor.md); [market data provider](../../../../../shared/reference/participants/participant-src-000095-market-data-provider.md); [regulator](../../../../../shared/reference/participants/participant-src-000095-regulator.md); [other interested party](../../../../../shared/reference/participants/participant-src-000095-other-interested-party.md).

Quoted above in src-000096-reda.004.001.07-p291-c001-d1.

**src-000096-reda.004.001.07-p291-c002 — file p291, usage.**

Mentioned roles: [distributors](../../../../../shared/reference/participants/participant-narrative-src-000096-distributor.md).

> Each time the fund data changes, the 'product provider' must provide the data to a product user, for example, the distributors, by sending a new funds reference data report.

**src-000096-reda.004.001.07-p291-c003 — file p291, usage.**

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> When the FundReferenceDataReport message is sent to provide updated reference data, the message overwrites the previously sent data.

**src-000096-reda.004.001.07-p291-c004 — file p291, usage.**

Mentioned roles: [Report Provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md); [fund promoter](../../../../../shared/reference/participants/participant-src-000095-fund-promoter.md); [fund manager](../../../../../shared/reference/participants/participant-src-000095-fund-manager.md).

Literal actions: Report Provider initiated.

Reviewed clause disposition: **parsed-role-boundary-correction**. The original exact clause was read; actor label is separated from its parenthetical examples or preceding activity phrase.

Quoted above in src-000096-reda.004.001.07-p291-c004-d1.

**src-000096-reda.004.001.07-p291-c005 — file p291, usage.**

Mentioned roles: [report users](../../../../../shared/reference/participants/participant-src-000095-requesting-party.md); [professional investors](../../../../../shared/reference/participants/participant-src-000095-professional-investor.md); [regulators](../../../../../shared/reference/participants/participant-src-000095-regulator.md); [distributors](../../../../../shared/reference/participants/participant-narrative-src-000096-distributor.md).

Literal actions: report users initiated.

Reviewed clause disposition: **parsed-role-boundary-correction**. The original exact clause was read; actor label is separated from its parenthetical examples or preceding activity phrase.

Quoted above in src-000096-reda.004.001.07-p291-c005-d1.

**src-000096-reda.004.001.07-p291-c006 — file p291, usage.**

Mentioned roles: [market infrastructure](../../../../../shared/reference/participants/participant-narrative-src-000096-market-infrastructure.md).

> in a reference data vendor environment, for example, market infrastructure and reference data providers may collate and store all fund reference data information centrally for access via database or regular distribution information.

**src-000096-reda.004.001.07-p291-c007 — file p291, usage.**

Mentioned roles: [report provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md); [report user](../../../../../shared/reference/participants/participant-src-000095-requesting-party.md).

> A reference data vendor may assume the role of both report provider and report user.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p291, scope.**

> The message may also include reporting data concerning product governance, such as target market data, and a breakdown of the costs and fees.

**File p291, usage.**

> A FundReferenceDataReport message should be prepared for each class of unit/share (for which an individual ISIN should have been allocated), in respect of its "home" market.

**File p291, usage.**

> A single message may contain more than one report.

**File p291, usage.**

> The FundReferenceDataReport message may be used in various models or environments:

**File p291, usage.**

> The FundReferenceDataReport message may be used to provide data concerning product governance, such as target market data, and a breakdown of the costs and fees in the context of MiFID II, with respect to the European MiFID Template (EMT).

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
