---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p360-order-and-confirmation"
title: "Order and Confirmation"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order and Confirmation"], "locator": "/w:document/w:body/w:p[360]", "paragraph_id": "P360", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order and Confirmation"], "locator": "/w:document/w:body/w:p[361]", "paragraph_id": "P361", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order and Confirmation"], "locator": "/w:document/w:body/w:p[362]", "paragraph_id": "P362", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order and Confirmation"], "locator": "/w:document/w:body/w:p[363]", "paragraph_id": "P363", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order and Confirmation"], "locator": "/w:document/w:body/w:p[364]", "paragraph_id": "P364", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order and Confirmation"], "locator": "/w:document/w:body/w:p[365]", "paragraph_id": "P365", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Order and Confirmation"], "locator": "/w:document/w:body/w:p[366]", "paragraph_id": "P366", "table_id": null}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party", "participant-src-000095-transfer-agent", "participant-src-000095-intermediary", "participant-src-000095-distributor"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Order and Confirmation", "Instructing Party", "Executing Party", "Transfer Agent", "Intermediary", "Distributor"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Order and Confirmation

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

**P361** This message flow section illustrates the use of the order and confirmation messages in typical message sequencing scenarios. The different order instructions are sent by the instructing party to the executing party to instruct either a subscription, a redemption or a switch.

**P362** The order confirmation messages are sent by the executing party to the instructing party to the confirm the execution of a subscription or a redemption or a switch.

**P363** The order status messages are sent by the executing party to the instructing party to the provide the status of the order instructions. Use of this optional message is shown in the next section.

**P364** There may be one or more intermediaries in the transaction chain.

**P365** The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

**P366** The intermediary party is, for example, a distributor.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Heading path: BusinessTransactions / Order and Confirmation.
