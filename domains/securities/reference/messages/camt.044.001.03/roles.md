---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.044.001.03 participant and direction evidence"
domain: "securities"
message_id: "camt.044.001.03"
message_family: "camt.044"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.044.001.03"
source_ids: ["src-000096", "src-000107"]
message_sets: ["investment-funds"]
role_labels: ["A report provider", "agent", "investment manager", "report provider", "report user", "the report user", "transfer agent"]
search_terms: ["A report provider", "agent", "investment manager", "report provider", "report user", "the report user", "transfer agent"]
participant_ids: ["participant-functionality-src-000096-agent", "participant-narrative-src-000096-investment-manager", "participant-src-000095-reporting-party", "participant-src-000095-requesting-party", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "11 camt.044.001.03 FundConfirmedCashForecastReportCancellationV03", "file_pages": [146, 152]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.044.001.03 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 5 uniquely resolved participant references.

## src-000096 — 11 camt.044.001.03 FundConfirmedCashForecastReportCancellationV03

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); Functionality file pp146; publication May 2026.

### Direction and initiation clauses

#### src-000096-camt.044.001.03-p146-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000096 file p146, scope.

- Sender: **A report provider, such as a transfer agent**. [A report provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md).
- Receiver: **the report user, such as an investment manager or pricing agent**. [the report user](../../../../../shared/reference/participants/participant-src-000095-requesting-party.md).

> A report provider, such as a transfer agent, sends the FundConfirmedCashForecastReportCancellation message to the report user, such as an investment manager or pricing agent, to cancel a previously sent FundConfirmedCashForecastReport message.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-camt.044.001.03-p146-c001 — file p146, scope.**

Mentioned roles: [report provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [report user](../../../../../shared/reference/participants/participant-src-000095-requesting-party.md); [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000096-investment-manager.md); [agent](../../../../../shared/reference/participants/participant-functionality-src-000096-agent.md).

Quoted above in src-000096-camt.044.001.03-p146-c001-d1.

**src-000096-camt.044.001.03-p146-c002 — file p146, usage.**

Mentioned roles: [report provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md).

Reviewed clause disposition: **usage-condition-or-related-message-context**. The sentence supplies purpose, response linkage, timing, content, status or a condition. It does not independently identify an additional complete current-message sender/receiver direction. Its full literal wording remains available.

> The FundConfirmedCashForecastReportCancellation message is used to cancel an entire FundConfirmedCashForecastReport message that was previously sent by the report provider.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p146, usage.**

> This message must contain reference to the of the message being cancelled.

**File p146, usage.**

> This message may also contain details of the message to be cancelled, but this is not recommended.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
