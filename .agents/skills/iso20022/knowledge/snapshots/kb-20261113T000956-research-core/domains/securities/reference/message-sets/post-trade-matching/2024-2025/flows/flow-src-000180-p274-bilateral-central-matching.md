---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
flow_id: "flow-src-000180-p274-bilateral-central-matching"
title: "Bilateral Central Matching"
source_locations: [{"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Central Matching", "Bilateral Central Matching Scenarios", "Bilateral Central Matching"], "locator": "/w:document/w:body/w:p[274]", "paragraph_id": "P274", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Central Matching", "Bilateral Central Matching Scenarios", "Bilateral Central Matching"], "locator": "/w:document/w:body/w:p[275]", "paragraph_id": "P275", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Central Matching", "Bilateral Central Matching Scenarios", "Bilateral Central Matching"], "locator": "/w:document/w:body/w:p[276]", "paragraph_id": "P276", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Central Matching", "Bilateral Central Matching Scenarios", "Bilateral Central Matching"], "locator": "/w:document/w:body/w:p[277]", "paragraph_id": "P277", "table_id": null}]
participants: ["participant-src-000180-broker", "participant-src-000180-broker-executing-broker", "participant-src-000180-central-matching-utility-cmu", "participant-src-000180-prime-broker"]
message_mapping_evidence: [{"source_label": "SecuritiesTradeConfirmation", "message_id": "setr.027.001.05", "source_id": "src-000181", "locator": "file pages 28-139; 3 setr.027.001.05 SecuritiesTradeConfirmationV05"}, {"source_label": "SecuritiesTradeConfirmationStatusAdvice", "message_id": "setr.044.001.04", "source_id": "src-000181", "locator": "file pages 162-221; 6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04"}]
message_ids: ["setr.027.001.05", "setr.044.001.04"]
message_families: ["setr.027", "setr.044"]
search_terms: ["Bilateral Central Matching", "Prime Broker", "Broker"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
issue_ids: ["issue-000031"]
---







# Bilateral Central Matching

Source context: Post-Trade Matching. This reference preserves the source-defined segment and its evidence.

This source-defined scenario begins with the first confirmation exchange below. Its purpose, conditional agreement/rejection, cancellation alternatives and outcomes are specified by the source narrative. No additional formal preconditions or postconditions are invented. [Related activity process](flow-src-000180-p185-bilateral-central-matching.md) provides the broader activity context.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Prime Broker | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-prime-broker.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Broker | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-broker.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P275** The executing broker sends a confirmation to the CMU. The CMU advise both parties that the trade confirmation is not paired yet. The prime broker sends a confirmation to the CMU. The CMU performs a matching process between the two confirmations and sends matching status messages to both parties reflecting the outcome of the matching process. If the confirmations are matched, the trade can move into the settlement process.

Source diagram evidence: [fig-0031](../documents/src-000180/diagrams/fig-0031.md). The reconstructed sequence and actual review evidence are linked below.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000180](../../../../../../../evidence/omitted/620693d01e301c06503cea9a.md). Heading path: BusinessTransactions / BusinessTransactions - Central Matching / Bilateral Central Matching Scenarios / Bilateral Central Matching.

## Curated source sequence

[Dedicated source reconstruction](../diagrams/business-transactions/fig-0031.md). The source order is preserved below; typical-sequence arrows do not override narrative conditions or alternatives.

| Step | Message | Initiating sender | Receiving participant |
| --- | --- | --- | --- |
| 1 | SecuritiesTradeConfirmation | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 2 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [PrimeBroker](../../../../../../../shared/reference/participants/participant-src-000180-prime-broker.md) |
| 3 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) |
| 4 | SecuritiesTradeConfirmation | [PrimeBroker](../../../../../../../shared/reference/participants/participant-src-000180-prime-broker.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 5 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) |
| 6 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [PrimeBroker](../../../../../../../shared/reference/participants/participant-src-000180-prime-broker.md) |



## Source recipient inconsistency

The narrative on Word27 calls the second party the prime broker. The diagram and T15 label two brokers, with Broker1/Broker2 in activity cells. However, the final T15 Status Advice cell on Word28 names broker and investment manager as cancellation-status recipients. Preserve this unresolved source vocabulary in [issue-000031](../../../../../../../tracking/issues.md#issue-000031); do not silently replace either recipient.
