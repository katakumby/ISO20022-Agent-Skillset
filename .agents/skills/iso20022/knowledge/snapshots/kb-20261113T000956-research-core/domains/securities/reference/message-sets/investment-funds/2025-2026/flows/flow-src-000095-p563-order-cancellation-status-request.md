---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p563-order-cancellation-status-request"
title: "Order Cancellation Status Request"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request"], "locator": "/w:document/w:body/w:p[563]", "paragraph_id": "P563", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request"], "locator": "/w:document/w:body/w:p[564]", "paragraph_id": "P564", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request"], "locator": "/w:document/w:body/w:p[565]", "paragraph_id": "P565", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request"], "locator": "/w:document/w:body/w:p[566]", "paragraph_id": "P566", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request"], "locator": "/w:document/w:body/w:p[567]", "paragraph_id": "P567", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request"], "locator": "/w:document/w:body/w:p[568]", "paragraph_id": "P568", "table_id": null}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation Status Reporting"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[2]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000096", "locator": "file page 4109; 56 setr.016.001.05 OrderInstructionStatusReportV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation Status Reporting"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[3]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000096", "locator": "file page 4205; 57 setr.017.001.05 OrderCancellationStatusReportV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation Status Reporting"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[4]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000096", "locator": "file page 4232; 58 setr.018.001.05 RequestForOrderStatusReportV05"}]
message_ids: []
message_families: ["setr.016", "setr.017", "setr.018"]
search_terms: ["Order Cancellation Status Request", "Instructing Party", "Executing Party", "setr.016", "setr.017", "setr.018"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Order Cancellation Status Request

Source context: Investment Funds. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Executing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P564** The RequestForOrderStatusReport message is sent by the instructing party to the executing party. It is used to request the status of one or several order messages and/or order cancellation instruction messages. 

**P565** The reply to the RequestForOrderStatusReport message is one of the following:

**P566** an OrderInstructionStatusReport, or,

**P567** an OrderCancellationStatusReport. 

**P568** The scenarios below focus on cases where a OrderCancellationStatusReport message is used.

## Messages and alternative paths

Source-supported message family mentions: `setr.016`, `setr.017`, `setr.018`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Heading path: BusinessTransactions / Order Cancellation and Status  / Order Cancellation Status Request.
