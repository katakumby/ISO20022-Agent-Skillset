---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
flow_id: "flow-src-000180-p278-bilateral-central-matching-cancellation"
title: "Bilateral Central Matching Cancellation"
source_locations: [{"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Central Matching", "Bilateral Central Matching Scenarios", "Bilateral Central Matching Cancellation"], "locator": "/w:document/w:body/w:p[278]", "paragraph_id": "P278", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Central Matching", "Bilateral Central Matching Scenarios", "Bilateral Central Matching Cancellation"], "locator": "/w:document/w:body/w:p[279]", "paragraph_id": "P279", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Central Matching", "Bilateral Central Matching Scenarios", "Bilateral Central Matching Cancellation"], "locator": "/w:document/w:body/w:p[280]", "paragraph_id": "P280", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Central Matching", "Bilateral Central Matching Scenarios", "Bilateral Central Matching Cancellation"], "locator": "/w:document/w:body/w:p[281]", "paragraph_id": "P281", "table_id": null}]
participants: ["participant-src-000180-broker", "participant-src-000180-broker-executing-broker", "participant-src-000180-central-matching-utility-cmu", "participant-src-000180-prime-broker"]
message_mapping_evidence: [{"source_label": "SecuritiesTradeConfirmation", "message_id": "setr.027.001.05", "source_id": "src-000181", "locator": "file pages 28-139; 3 setr.027.001.05 SecuritiesTradeConfirmationV05"}, {"source_label": "SecuritiesTradeConfirmationCancellation", "message_id": "setr.029.001.02", "source_id": "src-000181", "locator": "file pages 140-147; 4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02"}, {"source_label": "SecuritiesTradeConfirmationStatusAdvice", "message_id": "setr.044.001.04", "source_id": "src-000181", "locator": "file pages 162-221; 6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04"}]
message_ids: ["setr.027.001.05", "setr.029.001.02", "setr.044.001.04"]
message_families: ["setr.027", "setr.029", "setr.044"]
search_terms: ["Bilateral Central Matching Cancellation", "Prime Broker", "Broker"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---





# Bilateral Central Matching Cancellation

Source context: Post-Trade Matching. This reference preserves the source-defined segment and its evidence.

This source-defined scenario begins with the first confirmation exchange below. Its purpose, conditional agreement/rejection, cancellation alternatives and outcomes are specified by the source narrative. No additional formal preconditions or postconditions are invented. [Related activity process](flow-src-000180-p185-bilateral-central-matching.md) provides the broader activity context.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Prime Broker | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-prime-broker.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Broker | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-broker.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P279** The executing broker sends a confirmation to the CMU. The CMU advise both parties that the trade confirmation is not paired yet. The prime broker sends a confirmation to the CMU. The CMU performs a matching process between the two confirmations and sends matching status messages to both parties reflecting the outcome of the matching process. It may, for whatever reason, lead to the sending of a confirmation cancellation from the executing broker to the CMU or to the sending of a new confirmation from the broker to the CMU. Or, it may lead to the sending of a confirmation cancellation from the prime broker to the CMU or to the sending of a new confirmation from the broker to the CMU. The CMU will send a cancellation status advice to the executing broker and the prime broker.

Source diagram evidence: [fig-0032](../documents/src-000180/diagrams/fig-0032.md). The reconstructed sequence and actual review evidence are linked below.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000180](../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart1_PostTradeMatching_2024_2025_v2.docx). Heading path: BusinessTransactions / BusinessTransactions - Central Matching / Bilateral Central Matching Scenarios / Bilateral Central Matching Cancellation.

## Curated source sequence

[Dedicated source reconstruction](../diagrams/business-transactions/fig-0032.md). The source order is preserved below; typical-sequence arrows do not override narrative conditions or alternatives.

| Step | Message | Initiating sender | Receiving participant |
| --- | --- | --- | --- |
| 1 | SecuritiesTradeConfirmation | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 2 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [PrimeBroker](../../../../../../../shared/reference/participants/participant-src-000180-prime-broker.md) |
| 3 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) |
| 4 | SecuritiesTradeConfirmation | [PrimeBroker](../../../../../../../shared/reference/participants/participant-src-000180-prime-broker.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 5 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) |
| 6 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [PrimeBroker](../../../../../../../shared/reference/participants/participant-src-000180-prime-broker.md) |
| 7 | SecuritiesTradeConfirmationCancellation | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 8 | SecuritiesTradeConfirmationCancellation | [PrimeBroker](../../../../../../../shared/reference/participants/participant-src-000180-prime-broker.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 9 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) |
| 10 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [PrimeBroker](../../../../../../../shared/reference/participants/participant-src-000180-prime-broker.md) |


