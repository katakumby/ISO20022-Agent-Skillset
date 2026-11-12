---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p612-order-confirmation-amendment"
title: "Order Confirmation Amendment"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment "], "locator": "/w:document/w:body/w:p[612]", "paragraph_id": "P612", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment "], "locator": "/w:document/w:body/w:p[613]", "paragraph_id": "P613", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment "], "locator": "/w:document/w:body/w:p[614]", "paragraph_id": "P614", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment "], "locator": "/w:document/w:body/w:p[615]", "paragraph_id": "P615", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment "], "locator": "/w:document/w:body/w:p[616]", "paragraph_id": "P616", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment "], "locator": "/w:document/w:body/w:p[617]", "paragraph_id": "P617", "table_id": null}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party", "participant-src-000095-transfer-agent", "participant-src-000095-intermediary", "participant-src-000095-distributor"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Order Confirmation Amendment", "Instructing Party", "Executing Party", "Transfer Agent", "Intermediary", "Distributor"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Order Confirmation Amendment

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

**P613** This message flow section illustrates the use of the messages for the amendment of an order confirmation in typical message sequencing scenarios.

**P614** More than one message detail can be amended. The order confirmation, when sent as an amendment (AmendmentIndicator set to 'true' or '1'), might follow an order confirmation cancellation instruction message, if, in the order confirmation cancellation instruction message, the AmendmentIndicator is set to 'true' or '1' (see sequence diagrams related to order confirmation cancellation instruction messages).

**P615** The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

**P616** The intermediary party is, for example, a distributor.

**P617** There may be one or more intermediaries in the transaction chain

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Heading path: BusinessTransactions / Order Confirmation Amendment .
