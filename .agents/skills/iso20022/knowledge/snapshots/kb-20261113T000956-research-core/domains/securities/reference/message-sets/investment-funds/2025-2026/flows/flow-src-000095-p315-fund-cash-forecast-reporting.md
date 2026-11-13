---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p315-fund-cash-forecast-reporting"
title: "Fund Cash Forecast Reporting"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Fund Cash Forecast Reporting"], "locator": "/w:document/w:body/w:p[315]", "paragraph_id": "P315", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Fund Cash Forecast Reporting"], "locator": "/w:document/w:body/w:p[316]", "paragraph_id": "P316", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Fund Cash Forecast Reporting"], "locator": "/w:document/w:body/w:p[317]", "paragraph_id": "P317", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Fund Cash Forecast Reporting"], "locator": "/w:document/w:body/w:p[318]", "paragraph_id": "P318", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Fund Cash Forecast Reporting"], "locator": "/w:document/w:body/w:p[319]", "paragraph_id": "P319", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Fund Cash Forecast Reporting"], "locator": "/w:document/w:body/w:p[320]", "paragraph_id": "P320", "table_id": null}]
participants: ["participant-src-000095-market-data-provider", "participant-src-000095-fund-accountant", "participant-src-000095-transfer-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Fund Cash Forecast Reporting", "Market Data Provider", "Fund Accountant", "Transfer Agent"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Fund Cash Forecast Reporting

Source context: Investment Funds. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Market Data Provider | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-market-data-provider.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Fund Accountant | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-fund-accountant.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Transfer Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P316** This message flow section illustrates the use of the fund cash forecast messages in typical message sequencing scenarios. The fund cash forecast messages are sent by a report provider to the report user.

**P317** The report provider is, for example, a fund accountant, transfer agent, market data provider, or any other interested party.

**P318** The report user is, for example, a fund management company, a transfer agent, market data provider, regulator or any other interested party.

**P319** The difference between estimated and confirmed cash forecast reports is that estimated reports are sent before the cut-off time and/or the price valuation, whereas confirmed cash forecast reports contain definitive prices. 

**P320** The difference between detailed and non-detailed cash forecast reports is in the level of information that can be provided. In the detailed reports, the cash flow amounts can be sorted according to pre-defined or user-defined criteria and it is possible to breakdown cash forecast amounts by, for example, investment fund transaction types.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Heading path: BusinessTransactions / Fund Cash Forecast Reporting.
