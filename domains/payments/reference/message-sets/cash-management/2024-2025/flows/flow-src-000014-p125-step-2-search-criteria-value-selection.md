---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
flow_id: "flow-src-000014-p125-step-2-search-criteria-value-selection"
title: "Step 2 - Search Criteria Value Selection"
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Building a Get Message"], "locator": "/w:document/w:body/w:p[125]", "paragraph_id": "P125", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Building a Get Message"], "locator": "/w:document/w:body/w:p[126]", "paragraph_id": "P126", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Building a Get Message"], "locator": "/w:document/w:body/w:p[127]", "paragraph_id": "P127", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Building a Get Message"], "locator": "/w:document/w:body/w:p[128]", "paragraph_id": "P128", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Building a Get Message"], "locator": "/w:document/w:body/w:p[129]", "paragraph_id": "P129", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Building a Get Message"], "locator": "/w:document/w:body/w:p[130]", "paragraph_id": "P130", "table_id": null}, {"source_id": "src-000014", "heading_path": ["BusinessTransactions", "How to use the Cash Management Messages", "Building a Get Message"], "locator": "/w:document/w:body/w:p[131]", "paragraph_id": "P131", "table_id": null}]
participants: []
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Step 2 - Search Criteria Value Selection"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Step 2 - Search Criteria Value Selection

Source context: Cash Management. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P126** For each used search criterion, the value(s) that will be used to retrieve information must be defined.

**P127** Each value may be expressed as:

**P128** a discrete value, for example, a date, an amount, an account identifier, an indicator (true versus false, credit versus debit)

**P129** corresponding to the logical operator 'EQUAL TO',

**P130** a set of values corresponding to more complex logical operators, for example, values from x to y both inclusive, less than or equal to x, greater than or equal to x, etc.

**P131** When the same search criterion is used more than once, (that is, when different values for the same search criterion are requested), these must be interpreted as an 'OR' operator. For example, a matching transaction may be selected on search criterion status with value 1 OR value 2. In this case, all transactions with the specific status value 1 OR value 2 will be returned.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000014](../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx). Heading path: BusinessTransactions / How to use the Cash Management Messages / Building a Get Message.
