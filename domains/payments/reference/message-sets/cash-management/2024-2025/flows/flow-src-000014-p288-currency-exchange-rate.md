---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
flow_id: "flow-src-000014-p288-currency-exchange-rate"
title: "Currency Exchange Rate"
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessTransactions", "System Status ", "Currency Exchange Rate"], "locator": "/w:document/w:body/w:p[288]", "paragraph_id": "P288", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "System Status ", "Currency Exchange Rate"], "locator": "/w:document/w:body/w:p[289]", "paragraph_id": "P289", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "System Status ", "Currency Exchange Rate"], "locator": "/w:document/w:body/w:p[290]", "paragraph_id": "P290", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "System Status ", "Currency Exchange Rate"], "locator": "/w:document/w:body/w:p[291]", "paragraph_id": "P291", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "System Status ", "Currency Exchange Rate"], "locator": "/w:document/w:body/w:p[292]", "paragraph_id": "P292", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "System Status ", "Currency Exchange Rate"], "locator": "/w:document/w:body/w:p[293]", "paragraph_id": "P293", "table_id": null}]
participants: []
message_mapping_evidence: [{"source_id": "src-000014", "heading_path": ["Scope and Functionality", "Scope", "Groups", "System Status Management "], "locator": "/w:document/w:body/w:tbl[8]/w:tr[3]", "paragraph_id": null, "table_id": "T8"}]
message_ids: []
message_families: ["camt.017"]
search_terms: ["Currency Exchange Rate", "camt.017"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Currency Exchange Rate

Source context: Cash Management. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P289** The transaction administrator is in charge of providing the members with business information. The term business information covers all information related to the management of the system that is, not related to the transactions or requests created in the system. The type of business information available can vary depending on the system.

**P290** When a system manages a pool of accounts in various currencies for a member, it needs to maintain currency exchange details between the various currencies and the reporting on base currency. The reporting on base currency is used to calculate the actual position of the members in terms of aggregate limits and balances. It also allows the system to contain risk within defined and agreed boundaries.

**P291** The currency exchange details can be fixed for the entire operational day or regularly updated according to near real-time market feeds.

**P292** The member can request information about a currency exchange operation through a series of criteria, corresponding to the known information stored within the transaction administrator. Based on the criteria received within the request, the transaction administrator will select items that will match with the request and report them to the requestor.

**P293** The transaction administrator may also send a Return Currency Exchange Rate message with pre-defined information at times previously agreed with the member or to warn the member about a particular problem that may have arisen and which needs the member(s) attention.

## Messages and alternative paths

Source-supported message family mentions: `camt.017`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000014](../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx). Heading path: BusinessTransactions / System Status  / Currency Exchange Rate.
