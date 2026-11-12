---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p805-individual-asset-transfer"
title: "Individual Asset Transfer"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "locator": "/w:document/w:body/w:p[805]", "paragraph_id": "P805", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "locator": "/w:document/w:body/w:p[806]", "paragraph_id": "P806", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "locator": "/w:document/w:body/w:p[807]", "paragraph_id": "P807", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "locator": "/w:document/w:body/w:p[808]", "paragraph_id": "P808", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "locator": "/w:document/w:body/w:p[809]", "paragraph_id": "P809", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "locator": "/w:document/w:body/w:p[810]", "paragraph_id": "P810", "table_id": null}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party", "participant-src-000095-transfer-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Individual Asset Transfer", "Instructing Party", "Executing Party", "Transfer Agent"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Individual Asset Transfer

Source context: Investment Funds. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Executing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Transfer Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P806** This message flow section illustrates the use of the transfer messages in typical message sequencing scenarios. The transfer instruction messages are sent by the instructing party to the executing party to instruct either a transfer out or a transfer in.

**P807** The transfer confirmation messages are sent by the executing party to the instructing party to confirm a transfer out or transfer in.

**P808** The transfer status messages are sent by the executing party to the instructing party to provide the status of the transfer instructions.

**P809** There may be one or more intermediaries in the transaction chain.

**P810** The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Heading path: BusinessTransactions / Individual Asset Transfer.
