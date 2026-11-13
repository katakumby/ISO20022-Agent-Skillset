---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p155-customer-credit-transfer-initiation"
title: "CustomerCreditTransferInitiation"
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation"], "locator": "/w:document/w:body/w:p[155]", "paragraph_id": "P155", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation"], "locator": "/w:document/w:body/w:p[156]", "paragraph_id": "P156", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessTransactions", "CustomerCreditTransferInitiation"], "locator": "/w:document/w:body/w:p[157]", "paragraph_id": "P157", "table_id": null}]
participants: ["participant-src-000173-initiating-party", "participant-src-000173-debtor-agent"]
message_mapping_evidence: [{"source_id": "src-000173", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000173", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["pain.001", "pain.002"]
search_terms: ["CustomerCreditTransferInitiation", "Initiating Party", "Debtor Agent", "pain.001", "pain.002"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---



# CustomerCreditTransferInitiation

Source context: Payments Initiation. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Initiating Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-initiating-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P156** The CustomerCreditTransferInitiation message is sent from the initiating party to the debtor agent. Depending on the service level agreed between the debtor agent and the initiating party, the debtor agent may send a CustomerPaymentStatusReport message to inform the initiating party of the status of the initiation.

**P157** A number of additional message flows have been included to illustrate the complete end-to-end execution of the CustomerCreditTransferInitiation. However, these messages are out of scope. These message flows are:

## Messages and alternative paths

Source-supported message family mentions: `pain.001`, `pain.002`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Heading path: BusinessTransactions / CustomerCreditTransferInitiation.

<!-- INITIATION-CONTEXT -->
[Reviewed full flow context, literal directions, participants and source qualifications](flow-src-000173-p170-one-actor-plays-roles-of-initiating-party-debtor-and-ultimate-debtor-s.md)
<!-- /INITIATION-CONTEXT -->
