---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
flow_id: "flow-src-000014-p273-business-day-information"
title: "Business Day Information"
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessTransactions", "System Status ", "Business Day Information"], "locator": "/w:document/w:body/w:p[273]", "paragraph_id": "P273", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "System Status ", "Business Day Information"], "locator": "/w:document/w:body/w:p[274]", "paragraph_id": "P274", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "System Status ", "Business Day Information"], "locator": "/w:document/w:body/w:p[275]", "paragraph_id": "P275", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "System Status ", "Business Day Information"], "locator": "/w:document/w:body/w:p[276]", "paragraph_id": "P276", "table_id": null}]
participants: []
message_mapping_evidence: [{"source_id": "src-000014", "heading_path": ["Scope and Functionality", "Scope", "Groups", "System Status Management "], "locator": "/w:document/w:body/w:tbl[8]/w:tr[5]", "paragraph_id": null, "table_id": "T8"}]
message_ids: []
message_families: ["camt.019"]
search_terms: ["Business Day Information", "camt.019"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Business Day Information

Source context: Cash Management. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P274** The transaction administrator is in charge of providing the members with business information. The term business day information covers all information related to the management of the system that is, not related to the transactions or requests created in the system. The type of business information available can vary depending on the system.

**P275** The member can request information about the static data of the system through a series of criteria, corresponding to the known information stored within the transaction administrator. Based on the criteria received within the request, the transaction administrator will select items that match the request and report them to the requester.

**P276** The transaction administrator may also send a ReturnBusinessDayInformation message with pre-defined information at times previously agreed with the member or to warn the member about a particular problem that may have arisen and which needs attention.

## Messages and alternative paths

Source-supported message family mentions: `camt.019`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000014](../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md). Heading path: BusinessTransactions / System Status  / Business Day Information.
