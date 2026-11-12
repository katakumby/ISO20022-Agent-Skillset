---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.045.001.03 participant and direction evidence"
domain: "securities"
message_id: "camt.045.001.03"
message_family: "camt.045"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03"
source_ids: ["src-000096", "src-000108"]
message_sets: ["investment-funds"]
role_labels: ["A report provider", "fund accountant", "investment manager", "other interested party", "report provider", "report user", "the report user", "transfer agent"]
search_terms: ["A report provider", "fund accountant", "investment manager", "other interested party", "report provider", "report user", "the report user", "transfer agent"]
participant_ids: ["participant-narrative-src-000096-investment-manager", "participant-src-000095-fund-accountant", "participant-src-000095-other-interested-party", "participant-src-000095-reporting-party", "participant-src-000095-requesting-party", "participant-src-000095-transfer-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000096", "heading": "12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "file_pages": [153, 158]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.045.001.03 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 6 uniquely resolved participant references.

## src-000096 — 12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); Functionality file pp153; publication May 2026.

### Direction and initiation clauses

#### src-000096-camt.045.001.03-p153-c001-d1

Kind: sender-to-receiver; message applicability: **current-message-scope-name-variant**; src-000096 file p153, scope.

- Sender: **A report provider, such as a transfer agent**. [A report provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md).
- Receiver: **the report user, such as an investment manager, fund accountant or any other interested party**. [the report user](../../../../../shared/reference/participants/participant-src-000095-requesting-party.md).

> A report provider, such as a transfer agent, sends the FundDetailedConfirmedCashForecastReportCancellation messages to the report user, such as an investment manager, fund accountant or any other interested party, to cancel a previously sent FundDetailedConfirmedCashForecastReport.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000096-camt.045.001.03-p153-c001 — file p153, scope.**

Mentioned roles: [report provider](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md); [transfer agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md); [report user](../../../../../shared/reference/participants/participant-src-000095-requesting-party.md); [investment manager](../../../../../shared/reference/participants/participant-narrative-src-000096-investment-manager.md); [fund accountant](../../../../../shared/reference/participants/participant-src-000095-fund-accountant.md); [other interested party](../../../../../shared/reference/participants/participant-src-000095-other-interested-party.md).

Quoted above in src-000096-camt.045.001.03-p153-c001-d1.

**src-000096-camt.045.001.03-p153-c002 — file p153, usage.**

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> The FundDetailedConfirmedCashForecastReportCancellation message is used to cancel an entire FundDetailedConfirmedCashForecastReport message that was previously sent.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p153, usage.**

> This message must contain the reference of the message to be cancelled.

**File p153, usage.**

> This message may also contain details of the message to be cancelled, but this is not recommended.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
