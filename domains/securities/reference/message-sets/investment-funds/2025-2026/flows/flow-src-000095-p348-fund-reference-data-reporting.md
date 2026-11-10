---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p348-fund-reference-data-reporting"
title: "Fund Reference Data Reporting"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Fund Reference Data Reporting"], "locator": "/w:document/w:body/w:p[348]", "paragraph_id": "P348", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Fund Reference Data Reporting"], "locator": "/w:document/w:body/w:p[349]", "paragraph_id": "P349", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Fund Reference Data Reporting"], "locator": "/w:document/w:body/w:p[350]", "paragraph_id": "P350", "table_id": null}]
participants: ["participant-src-000095-market-data-provider", "participant-src-000095-transfer-agent", "participant-src-000095-distributor"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Fund Reference Data"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[2]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000096", "locator": "file page 291; 15 reda.004.001.07 FundReferenceDataReportV07"}]
message_ids: []
message_families: ["reda.004"]
search_terms: ["Fund Reference Data Reporting", "Market Data Provider", "Transfer Agent", "Distributor", "reda.004"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Fund Reference Data Reporting

Source context: Investment Funds. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Market Data Provider | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-market-data-provider.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Transfer Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Distributor | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-distributor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P349** This message flow section illustrates the use of the fund reference data messages in typical message sequencing scenarios. The fund reference data reports are exchanged between a report provider and the report user. 

**P350** The report provider is, for example, a fund promoter, fund management company, transfer agent or market data provider. The report user is, for example, a professional investor, investment fund distributor, market data provider, regulator or other interested party.

## Messages and alternative paths

Source-supported message family mentions: `reda.004`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Heading path: BusinessTransactions / Fund Reference Data Reporting.
