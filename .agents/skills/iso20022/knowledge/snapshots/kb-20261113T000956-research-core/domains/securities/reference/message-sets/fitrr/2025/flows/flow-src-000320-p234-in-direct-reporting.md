---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p234-in-direct-reporting"
title: "Trading activity results — authority reporting"
source_locations: [{"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Trading Activity Result BusinessTransaction", "In-Direct Reporting"], "locator": "/w:document/w:body/w:p[234]", "paragraph_id": "P234", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Trading Activity Result BusinessTransaction", "In-Direct Reporting"], "locator": "/w:document/w:body/w:p[235]", "paragraph_id": "P235", "table_id": null}, {"source_id": "src-000320", "heading_path": ["BusinessTransactions", "Trading Activity Result BusinessTransaction", "In-Direct Reporting"], "locator": "/w:document/w:body/w:p[236]", "paragraph_id": "P236", "table_id": null}]
participants: ["participant-src-000320-competent-authority", "participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: ["auth.044.001.03", "auth.045.001.03", "auth.031.001.01"]
message_families: ["auth.044", "auth.045", "auth.031"]
search_terms: ["In-Direct Reporting", "CA", "SA"]
limitations: ["T18 names Supervisory Authority in its Role row, but the definition, P233–P235 and this figure assign submission of non-delegated calculation results to the Competent Authority. Both statements are retained; issue-000032.", "Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.", "The described flow is scoped to this publication; it is not advice on current regulation."]
participant_ids: ["participant-src-000320-competent-authority", "participant-src-000320-supervisory-authority"]
manual_curated: true
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0032.md"]
---

# Trading activity results — authority reporting

[src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md); BusinessTransactions / Trading Activity Result BusinessTransaction / In-Direct Reporting.

## Purpose, trigger, preconditions and outcomes

Source process definition [T18](../documents/src-000320/tables/tbl-0018.md) (the overall process conditions also apply to its reporting variant):

| Item | Description |
| --- | --- |
| Definition | CAs that have not delegated calculation operations to ESMA must perform and distribute the results of the transparency calculations they perform to ESMA for publication. |
| Trigger | Transparency calculations must be performed by specific cut-off times, defined by MiFIR regulations. At the cut-off, the venue (CA) performs the specified calculations. |
| Pre-conditions | The CA has captured all data it requires to perform the transparency calculation. |
| Post-conditions | The transparency calculation has been performed by the CA with the result data submitted to ESMA for publication along with all other Transparency results. |
| Role | Supervisory Authority |


## Participants and responsibilities

- [Competent Authority](../../../../../../../shared/reference/participants/participant-src-000320-competent-authority.md)
- [Supervisory Authority](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md)

Initiation and responsibility follow the explicit message directions and narrative below; a participant appearing on a lifeline is not automatically a sender.

## Ordered exchanges and decision points

| Order | Sender | Receiver | Literal source message / exchange | Source condition or fragment |
| --- | --- | --- | --- | --- |
| 1 | Competent Authority | Supervisory Authority | FinancialInstrumentReportingEquityTradingActivityResult OR FinancialInstrumentReportingNonEquityTradingActivityResult | Outside conditional frame |
| 2 | Supervisory Authority | Competent Authority | FinancialInstrumentReportingStatusAdvice | Outside conditional frame |


[Reconstructed sequence and retained original](../diagrams/fitrr-sequences/fig-0032.md)

## Source narrative and additional participants

**P233** The Transparency Trading Activity Result is captured to support performing calculations to identify a range of features on both Equity and Non-Equity instruments that are trading. Where a CA performs these calculations rather than an SA, there is a need to submit the result data to the SA to support publication of the full set of calculation results for all instruments.

**P235** This flow describes a CA submitting a transparency trading activity result message to the SA. For each message submitted to the SA, a Status Advice message is generated.

## Supplied message definitions

- [auth.044.001.03 — FinancialInstrumentReportingEquityTradingActivityResultV03](../../../../messages/auth.044.001.03/index.md)
- [auth.045.001.03 — FinancialInstrumentReportingNonEquityTradingActivityResultV03](../../../../messages/auth.045.001.03/index.md)
- [auth.031.001.01 — FinancialInstrumentReportingStatusAdviceV01](../../../../messages/auth.031.001.01/index.md)

Family mappings are grounded in Part1 tables T4–T9 and the matching supplied message catalog. The figure names remain literal; a family link does not turn an unversioned diagram into evidence for a particular schema version.

## Alternative and exceptional paths

The source conditions and narrative above define the applicable alternatives. Repeated arrows and all error branches are retained; no additional cancellation or reversal route is invented.

## Limitations

- T18 names Supervisory Authority in its Role row, but the definition, P233–P235 and this figure assign submission of non-delegated calculation results to the Competent Authority. Both statements are retained; issue-000032.
- Exact message links identify supplied definitions for the cited family; the source sequence itself does not state an exact schema version.
- The described flow is scoped to this publication; it is not advice on current regulation.
