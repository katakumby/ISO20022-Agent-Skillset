---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000321-reporting-agent"
title: "Reporting Agent — Transactions and Financial Instruments Data Reporting narrative scope"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
source_labels: ["reporting agent"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["fitrr"]
message_ids: ["auth.016.001.03", "auth.031.001.01"]
message_families: ["auth.016", "auth.031"]
flows: []
source_locations: [{"source_id": "src-000321", "heading": "2 auth.016.001.03 FinancialInstrumentReportingTransactionReportV03", "file_pages": [8], "evidence_id": "src-000321-auth.016.001.03-p8-c001"}, {"source_id": "src-000321", "heading": "4 auth.031.001.01 FinancialInstrumentReportingStatusAdviceV01", "file_pages": [39], "evidence_id": "src-000321-auth.031.001.01-p39-c001"}]
search_terms: ["reporting agent"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Reporting Agent — Transactions and Financial Instruments Data Reporting

## Definition and applicable context

This source names **reporting agent** in the Functionality of the messages listed below. The record is scoped to Transactions and Financial Instruments Data Reporting, July 2025. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The FinancialInstrumentReportingTransactionReport message is sent by the reporting agent to the competent authority to report on the securities transactions or by the competent authority to another competent authority when the transaction needs to be exchanged between the competent authorities.

src-000321, file p8, 2 auth.016.001.03 FinancialInstrumentReportingTransactionReportV03, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

| This participant in clause | Source message subject | Message applicability | Other roles / source expressions | Evidence |
| --- | --- | --- | --- | --- |
| sender | The FinancialInstrumentReportingTransactionReport message | current-message | sender: the reporting agent ([the reporting agent](participant-narrative-src-000321-reporting-agent.md)); receiver: the competent authority ([the competent authority](participant-src-000320-competent-authority.md)) | [src-000321-auth.016.001.03-p8-c001-d1](#src-000321-auth.016.001.03-p8-c001); file p8 |
| receiver | The FinancialInstrumentReportingStatusAdvice message | current-message | sender: the national competent authority; receiver: the reporting agent ([the reporting agent](participant-narrative-src-000321-reporting-agent.md)) | [src-000321-auth.031.001.01-p39-c001-d1](#src-000321-auth.031.001.01-p39-c001); file p39 |


## Complete source evidence

<a id="src-000321-auth.016.001.03-p8-c001"></a>

### src-000321-auth.016.001.03-p8-c001

src-000321; file p8; 2 auth.016.001.03 FinancialInstrumentReportingTransactionReportV03; scope.

> The FinancialInstrumentReportingTransactionReport message is sent by the reporting agent to the competent authority to report on the securities transactions or by the competent authority to another competent authority when the transaction needs to be exchanged between the competent authorities.

<a id="src-000321-auth.031.001.01-p39-c001"></a>

### src-000321-auth.031.001.01-p39-c001

src-000321; file p39; 4 auth.031.001.01 FinancialInstrumentReportingStatusAdviceV01; scope.

> The FinancialInstrumentReportingStatusAdvice message is sent by the national competent authority to the reporting agent to provide a status advice for the correctness, issues or errors that arise from the submitted report.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| auth.016.001.03 | [Exact message-role evidence](../../../domains/securities/reference/messages/auth.016.001.03/roles.md) | src-000321-auth.016.001.03-p8-c001 |
| auth.031.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/auth.031.001.01/roles.md) | src-000321-auth.031.001.01-p39-c001 |


[Message-set flows](../../../domains/securities/reference/message-sets/fitrr/2025/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `reporting agent`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000321](../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf) · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
