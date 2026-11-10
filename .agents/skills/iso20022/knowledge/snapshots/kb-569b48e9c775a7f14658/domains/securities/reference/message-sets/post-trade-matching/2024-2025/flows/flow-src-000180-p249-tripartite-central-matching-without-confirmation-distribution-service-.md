---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
flow_id: "flow-src-000180-p249-tripartite-central-matching-without-confirmation-distribution-service-"
title: "Tripartite Central Matching Without Confirmation Distribution Service Rejection"
source_locations: [{"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Central Matching", "Tripartite Central Matching Without Confirmation Distribution Service Scenarios", "Tripartite Central Matching Without Confirmation Distribution Service Rejection"], "locator": "/w:document/w:body/w:p[249]", "paragraph_id": "P249", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Central Matching", "Tripartite Central Matching Without Confirmation Distribution Service Scenarios", "Tripartite Central Matching Without Confirmation Distribution Service Rejection"], "locator": "/w:document/w:body/w:p[250]", "paragraph_id": "P250", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Central Matching", "Tripartite Central Matching Without Confirmation Distribution Service Scenarios", "Tripartite Central Matching Without Confirmation Distribution Service Rejection"], "locator": "/w:document/w:body/w:p[251]", "paragraph_id": "P251", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Central Matching", "Tripartite Central Matching Without Confirmation Distribution Service Scenarios", "Tripartite Central Matching Without Confirmation Distribution Service Rejection"], "locator": "/w:document/w:body/w:p[252]", "paragraph_id": "P252", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Central Matching", "Tripartite Central Matching Without Confirmation Distribution Service Scenarios", "Tripartite Central Matching Without Confirmation Distribution Service Rejection"], "locator": "/w:document/w:body/w:p[253]", "paragraph_id": "P253", "table_id": null}]
participants: ["participant-src-000180-broker", "participant-src-000180-broker-executing-broker", "participant-src-000180-central-matching-utility-cmu", "participant-src-000180-investment-manager", "participant-src-000180-trustee"]
message_mapping_evidence: [{"source_label": "SecuritiesTradeConfirmation", "message_id": "setr.027.001.05", "source_id": "src-000181", "locator": "file pages 28-139; 3 setr.027.001.05 SecuritiesTradeConfirmationV05"}, {"source_label": "SecuritiesTradeConfirmationCancellation", "message_id": "setr.029.001.02", "source_id": "src-000181", "locator": "file pages 140-147; 4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02"}, {"source_label": "SecuritiesTradeConfirmationResponse", "message_id": "setr.030.001.03", "source_id": "src-000181", "locator": "file pages 148-161; 5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03"}, {"source_label": "SecuritiesTradeConfirmationStatusAdvice", "message_id": "setr.044.001.04", "source_id": "src-000181", "locator": "file pages 162-221; 6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04"}]
message_ids: ["setr.027.001.05", "setr.029.001.02", "setr.030.001.03", "setr.044.001.04"]
message_families: ["setr.027", "setr.029", "setr.030", "setr.044"]
search_terms: ["Tripartite Central Matching Without Confirmation Distribution Service Rejection", "Investment Manager", "Broker"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "The final narrative sentence assigns a received cancellation to the investment manager although the preceding text and artwork show broker initiation; source contradiction retained under issue-000031."]
manual_curated: true
issue_ids: ["issue-000031"]
---





# Tripartite Central Matching Without Confirmation Distribution Service Rejection

Source context: Post-Trade Matching. This reference preserves the source-defined segment and its evidence.

This source-defined scenario begins with the first confirmation exchange below. Its purpose, conditional agreement/rejection, cancellation alternatives and outcomes are specified by the source narrative. No additional formal preconditions or postconditions are invented. [Related activity process](flow-src-000180-p173-tripartite-central-matching-without-confirmation-distribution-service.md) provides the broader activity context.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Investment Manager | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Broker | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-broker.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P250** The executing broker sends a trade confirmation to the CMU. The CMU advise both parties that the trade confirmation is not paired yet. The investment manager sends the corresponding trade confirmation to the CMU. The CMU performs a matching process between the two confirmations and sends matching status messages to both parties, reflecting the outcome of the matching process. The CMU forward the confirmation received from both the executing broker and investment manager to the trustee. Should the trustee not agree with the details of the confirmations, it may send a disaffirmation message to the CMU. The CMU sends a disaffirmation status message to the executing broker, which may lead to a new confirmation being sent to the CMU of a confirmation cancellation being sent to the CMU. The CMU forward the cancellation to the investment manager. The CMU advise the executing broker that they send the cancellation to the investment manager. The CMU will forward the cancellation received from the investment manager and send the cancellation on behalf of the executing broker to the trustee.

Source diagram evidence: [fig-0026](../documents/src-000180/diagrams/fig-0026.md). The reconstructed sequence and actual review evidence are linked below.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000180](../../../../../../../evidence/omitted/620693d01e301c06503cea9a.md). Heading path: BusinessTransactions / BusinessTransactions - Central Matching / Tripartite Central Matching Without Confirmation Distribution Service Scenarios / Tripartite Central Matching Without Confirmation Distribution Service Rejection.

## Curated source sequence

[Dedicated source reconstruction](../diagrams/business-transactions/fig-0026.md). The source order is preserved below; typical-sequence arrows do not override narrative conditions or alternatives.

| Step | Message | Initiating sender | Receiving participant |
| --- | --- | --- | --- |
| 1 | SecuritiesTradeConfirmation | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 2 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [InvestmentManager](../../../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) |
| 3 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) |
| 4 | SecuritiesTradeConfirmation | [InvestmentManager](../../../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 5 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [InvestmentManager](../../../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) |
| 6 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) |
| 7 | SecuritiesTradeConfirmation | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [Trustee](../../../../../../../shared/reference/participants/participant-src-000180-trustee.md) |
| 8 | SecuritiesTradeConfirmation | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [Trustee](../../../../../../../shared/reference/participants/participant-src-000180-trustee.md) |
| 9 | SecuritiesTradeConfirmationResponse | [Trustee](../../../../../../../shared/reference/participants/participant-src-000180-trustee.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 10 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) |
| 11 | SecuritiesTradeConfirmationCancellation | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 12 | SecuritiesTradeConfirmationCancellation | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [InvestmentManager](../../../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) |
| 13 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) |
| 14 | SecuritiesTradeConfirmationCancellation | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [Trustee](../../../../../../../shared/reference/participants/participant-src-000180-trustee.md) |
| 15 | SecuritiesTradeConfirmationCancellation | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [Trustee](../../../../../../../shared/reference/participants/participant-src-000180-trustee.md) |



Source contradiction issue-000031: the final narrative sentence attributes a received cancellation to the investment manager, whereas the preceding narrative and source figure show broker initiation. The diagram preserves artwork direction; the original contradictory sentence remains above.
