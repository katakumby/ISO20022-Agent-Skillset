---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "reda.005.001.03 participant and direction evidence"
domain: "securities"
message_id: "reda.005.001.03"
message_family: "reda.005"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.005.001.03"
source_ids: ["src-000096", "src-000112"]
message_sets: ["investment-funds"]
role_labels: ["a report user", "distributor", "fund management company", "fund promoter", "market data provider", "other interested party", "professional investor", "regulator", "report provider", "report user", "the report provider", "transfer agent"]
search_terms: ["a report user", "distributor", "fund management company", "fund promoter", "market data provider", "other interested party", "professional investor", "regulator", "report provider", "report user", "the report provider", "transfer agent"]
participant_ids: ["participant-src-000095-distributor", "participant-src-000095-fund-management-company", "participant-src-000095-fund-promoter", "participant-src-000095-market-data-provider", "participant-src-000095-other-interested-party", "participant-src-000095-professional-investor", "participant-src-000095-regulator", "participant-src-000095-reporting-party", "participant-src-000095-requesting-party", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "16 reda.005.001.03 InvestmentFundReportRequestV03", "file_pages": [365, 370]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# reda.005.001.03 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 10 uniquely resolved participant references.

## src-000096 — 16 reda.005.001.03 InvestmentFundReportRequestV03

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); Functionality file pp365; publication May 2026.

### Direction and initiation clauses

#### src-000096-reda.005.001.03-p365-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p365, scope.

- Sender: **a report user, for example, a professional investor, investment fund distributor, market data provider, regulator or other interested party**. [a report user](../../../../../shared/reference/participants/participant-src-000095-requesting-party.md).
- Receiver: **the report provider, for example, a fund promoter, fund management company, transfer agent, or market data provider**. [the report provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md).

> The InvestmentFundReportRequest message is sent by a report user, for example, a professional investor, investment fund distributor, market data provider, regulator or other interested party to the report provider, for example, a fund promoter, fund management company, transfer agent, or market data provider to request a report.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-reda.005.001.03-p365-c001 — file p365, scope.**

Mentioned roles: [report user](../../../../../shared/reference/participants/participant-src-000095-requesting-party.md); [professional investor](../../../../../shared/reference/participants/participant-src-000095-professional-investor.md); [distributor](../../../../../shared/reference/participants/participant-src-000095-distributor.md); [market data provider](../../../../../shared/reference/participants/participant-src-000095-market-data-provider.md); [regulator](../../../../../shared/reference/participants/participant-src-000095-regulator.md); [other interested party](../../../../../shared/reference/participants/participant-src-000095-other-interested-party.md); [report provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md); [fund promoter](../../../../../shared/reference/participants/participant-src-000095-fund-promoter.md); [fund management company](../../../../../shared/reference/participants/participant-src-000095-fund-management-company.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [market data provider](../../../../../shared/reference/participants/participant-src-000095-market-data-provider.md).

Quoted above in src-000096-reda.005.001.03-p365-c001-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p365, scope.**

> The Investment Fund Report Request message can be used to request one or many fund reference data report messages.

**File p365, usage.**

> If the InvestmentFundReportRequest message is used to request a fund reference data report then the request can specify the financial instrument for which the report is requested.

**File p365, usage.**

> Other appropriate parameters can also be included.

**File p365, usage.**

> It is also possible to indicate that the request is an open request, that is, there is no specific criteria for the report requested.

**File p365, usage.**

> For example, a request for a fund reference data report that is specified as "no criteria" means that the request is a request for a reference data report messages for all funds.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
