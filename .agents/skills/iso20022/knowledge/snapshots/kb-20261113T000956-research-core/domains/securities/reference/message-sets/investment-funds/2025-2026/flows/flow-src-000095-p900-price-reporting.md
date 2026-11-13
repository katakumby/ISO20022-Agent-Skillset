---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p900-price-reporting"
title: "Price Reporting"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Price Reporting"], "locator": "/w:document/w:body/w:p[900]", "paragraph_id": "P900", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Price Reporting"], "locator": "/w:document/w:body/w:p[901]", "paragraph_id": "P901", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Price Reporting"], "locator": "/w:document/w:body/w:p[902]", "paragraph_id": "P902", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Price Reporting"], "locator": "/w:document/w:body/w:p[903]", "paragraph_id": "P903", "table_id": null}]
participants: ["participant-src-000095-market-data-provider", "participant-src-000095-fund-accountant", "participant-src-000095-transfer-agent"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Price Report "], "locator": "/w:document/w:body/w:tbl[14]/w:tr[2]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000096", "locator": "file page 159; 13 reda.001.001.05 PriceReportV05"}]
message_ids: []
message_families: ["reda.001"]
search_terms: ["Price Reporting", "Market Data Provider", "Fund Accountant", "Transfer Agent", "reda.001"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Price Reporting

Source context: Investment Funds. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Market Data Provider | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-market-data-provider.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Fund Accountant | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-fund-accountant.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Transfer Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P901** This message flow section illustrates the use of the price report messages in typical message sequencing scenarios. The price report messages are sent by a report provider to the report user.

**P902** The report provider is, for example, a fund accountant, transfer agent, market data provider, or any other interested party.

**P903** The report user is, for example, a fund management company, a transfer agent, market data provider, regulator or any other interested party.

## Messages and alternative paths

Source-supported message family mentions: `reda.001`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Heading path: BusinessTransactions / Price Reporting.
