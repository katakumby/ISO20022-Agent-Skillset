---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p670-order-confirmation-cancellation"
title: "Order Confirmation Cancellation"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation "], "locator": "/w:document/w:body/w:p[670]", "paragraph_id": "P670", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation "], "locator": "/w:document/w:body/w:p[671]", "paragraph_id": "P671", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation "], "locator": "/w:document/w:body/w:p[672]", "paragraph_id": "P672", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation "], "locator": "/w:document/w:body/w:p[673]", "paragraph_id": "P673", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation "], "locator": "/w:document/w:body/w:p[674]", "paragraph_id": "P674", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation "], "locator": "/w:document/w:body/w:p[675]", "paragraph_id": "P675", "table_id": null}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party", "participant-src-000095-transfer-agent", "participant-src-000095-intermediary", "participant-src-000095-distributor"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Order Confirmation Cancellation", "Instructing Party", "Executing Party", "Transfer Agent", "Intermediary", "Distributor"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Order Confirmation Cancellation

Source context: Investment Funds. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Executing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Transfer Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Intermediary | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Distributor | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-distributor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P671** This message flow section illustrates the use of the order confirmation cancellation messages in typical message sequencing scenarios. The different order confirmation cancellation instruction messages are sent by the executing party to the instructing party to cancel a previously sent subscription, redemption or order confirmation message. 

**P672** There may be one or more intermediaries in the transaction chain.

**P673** The order confirmation cancellation instruction message might be followed by an order confirmation message sent as an amendment (AmendmentIndicator set to 'true' or '1'), (see sequence diagrams related to order confirmation amendment).

**P674** The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

**P675** The intermediary party is, for example, a distributor.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Heading path: BusinessTransactions / Order Confirmation Cancellation .
