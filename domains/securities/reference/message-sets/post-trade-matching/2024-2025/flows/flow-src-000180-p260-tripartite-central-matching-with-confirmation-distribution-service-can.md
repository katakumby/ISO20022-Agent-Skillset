---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
flow_id: "flow-src-000180-p260-tripartite-central-matching-with-confirmation-distribution-service-can"
title: "Tripartite Central Matching With Confirmation Distribution Service Cancellation by Executing Broker"
source_locations: [{"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Central Matching", "Tripartite Central Matching With Confirmation Distribution Service Scenarios", "Tripartite Central Matching With Confirmation Distribution Service Cancellation by Executing Broker"], "locator": "/w:document/w:body/w:p[260]", "paragraph_id": "P260", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Central Matching", "Tripartite Central Matching With Confirmation Distribution Service Scenarios", "Tripartite Central Matching With Confirmation Distribution Service Cancellation by Executing Broker"], "locator": "/w:document/w:body/w:p[261]", "paragraph_id": "P261", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Central Matching", "Tripartite Central Matching With Confirmation Distribution Service Scenarios", "Tripartite Central Matching With Confirmation Distribution Service Cancellation by Executing Broker"], "locator": "/w:document/w:body/w:p[262]", "paragraph_id": "P262", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Central Matching", "Tripartite Central Matching With Confirmation Distribution Service Scenarios", "Tripartite Central Matching With Confirmation Distribution Service Cancellation by Executing Broker"], "locator": "/w:document/w:body/w:p[263]", "paragraph_id": "P263", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Central Matching", "Tripartite Central Matching With Confirmation Distribution Service Scenarios", "Tripartite Central Matching With Confirmation Distribution Service Cancellation by Executing Broker"], "locator": "/w:document/w:body/w:p[264]", "paragraph_id": "P264", "table_id": null}]
participants: ["participant-src-000180-broker", "participant-src-000180-broker-executing-broker", "participant-src-000180-central-matching-utility-cmu", "participant-src-000180-investment-manager", "participant-src-000180-trustee"]
message_mapping_evidence: [{"source_label": "SecuritiesTradeConfirmation", "message_id": "setr.027.001.05", "source_id": "src-000181", "locator": "file pages 28-139; 3 setr.027.001.05 SecuritiesTradeConfirmationV05"}, {"source_label": "SecuritiesTradeConfirmationCancellation", "message_id": "setr.029.001.02", "source_id": "src-000181", "locator": "file pages 140-147; 4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02"}, {"source_label": "SecuritiesTradeConfirmationStatusAdvice", "message_id": "setr.044.001.04", "source_id": "src-000181", "locator": "file pages 162-221; 6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04"}]
message_ids: ["setr.027.001.05", "setr.029.001.02", "setr.044.001.04"]
message_families: ["setr.027", "setr.029", "setr.044"]
search_terms: ["Tripartite Central Matching With Confirmation Distribution Service Cancellation by Executing Broker", "Investment Manager", "Broker"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "The final narrative sentence assigns a received cancellation to the investment manager although the preceding text and artwork show broker initiation; source contradiction retained under issue-000031."]
manual_curated: true
issue_ids: ["issue-000031"]
---





# Tripartite Central Matching With Confirmation Distribution Service Cancellation by Executing Broker

Source context: Post-Trade Matching. This reference preserves the source-defined segment and its evidence.

This source-defined scenario begins with the first confirmation exchange below. Its purpose, conditional agreement/rejection, cancellation alternatives and outcomes are specified by the source narrative. No additional formal preconditions or postconditions are invented. [Related activity process](flow-src-000180-p180-tripartite-central-matching-with-confirmation-distribution-service.md) provides the broader activity context.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Investment Manager | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Broker | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-broker.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P261** The executing broker sends a trade confirmation to the CMU. The CMU forwards the confirmation received from the broker to the investment manager. The investment manager compares the details of the trade to its own details and sends a trade confirmation to the CMU. The CMU performs a matching process and sends matching status messages to both parties reflecting the outcome of the matching process. The broker may, for whatever reason, send a confirmation cancellation message to the CMU or it may send a new confirmation to the CMU. The CMU forwards a cancellation message to the investment manager. The CMU advise the executing broker that they send a cancellation to the investment manager. The CMU will forward the cancellation received from the investment manager and send the cancellation on behalf of the executing broker to the trustee.

Source diagram evidence: [fig-0028](../documents/src-000180/diagrams/fig-0028.md). The reconstructed sequence and actual review evidence are linked below.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000180](../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart1_PostTradeMatching_2024_2025_v2.docx). Heading path: BusinessTransactions / BusinessTransactions - Central Matching / Tripartite Central Matching With Confirmation Distribution Service Scenarios / Tripartite Central Matching With Confirmation Distribution Service Cancellation by Executing Broker.

## Curated source sequence

[Dedicated source reconstruction](../diagrams/business-transactions/fig-0028.md). The source order is preserved below; typical-sequence arrows do not override narrative conditions or alternatives.

| Step | Message | Initiating sender | Receiving participant |
| --- | --- | --- | --- |
| 1 | SecuritiesTradeConfirmation | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 2 | SecuritiesTradeConfirmation | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [InvestmentManager](../../../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) |
| 3 | SecuritiesTradeConfirmation | [InvestmentManager](../../../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 4 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [InvestmentManager](../../../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) |
| 5 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) |
| 6 | SecuritiesTradeConfirmationCancellation | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 7 | SecuritiesTradeConfirmationCancellation | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [InvestmentManager](../../../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) |
| 8 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) |
| 9 | SecuritiesTradeConfirmationCancellation | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [Trustee](../../../../../../../shared/reference/participants/participant-src-000180-trustee.md) |
| 10 | SecuritiesTradeConfirmationCancellation | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [Trustee](../../../../../../../shared/reference/participants/participant-src-000180-trustee.md) |



Source contradiction issue-000031: the final narrative sentence attributes a received cancellation to the investment manager, whereas the preceding narrative and source figure show broker initiation. The diagram preserves artwork direction; the original contradictory sentence remains above.
