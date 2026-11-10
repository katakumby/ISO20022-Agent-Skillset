---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
flow_id: "flow-src-000180-p265-tripartite-central-matching-with-confirmation-distribution-service-can"
title: "Tripartite Central Matching With Confirmation Distribution Service Cancellation by Investment Manager"
source_locations: [{"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Central Matching", "Tripartite Central Matching With Confirmation Distribution Service Scenarios", "Tripartite Central Matching With Confirmation Distribution Service Cancellation by Investment Manager"], "locator": "/w:document/w:body/w:p[265]", "paragraph_id": "P265", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Central Matching", "Tripartite Central Matching With Confirmation Distribution Service Scenarios", "Tripartite Central Matching With Confirmation Distribution Service Cancellation by Investment Manager"], "locator": "/w:document/w:body/w:p[266]", "paragraph_id": "P266", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Central Matching", "Tripartite Central Matching With Confirmation Distribution Service Scenarios", "Tripartite Central Matching With Confirmation Distribution Service Cancellation by Investment Manager"], "locator": "/w:document/w:body/w:p[267]", "paragraph_id": "P267", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Central Matching", "Tripartite Central Matching With Confirmation Distribution Service Scenarios", "Tripartite Central Matching With Confirmation Distribution Service Cancellation by Investment Manager"], "locator": "/w:document/w:body/w:p[268]", "paragraph_id": "P268", "table_id": null}]
participants: ["participant-src-000180-broker", "participant-src-000180-broker-executing-broker", "participant-src-000180-central-matching-utility-cmu", "participant-src-000180-investment-manager", "participant-src-000180-trustee"]
message_mapping_evidence: [{"source_label": "SecuritiesTradeConfirmation", "message_id": "setr.027.001.05", "source_id": "src-000181", "locator": "file pages 28-139; 3 setr.027.001.05 SecuritiesTradeConfirmationV05"}, {"source_label": "SecuritiesTradeConfirmationCancellation", "message_id": "setr.029.001.02", "source_id": "src-000181", "locator": "file pages 140-147; 4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02"}, {"source_label": "SecuritiesTradeConfirmationStatusAdvice", "message_id": "setr.044.001.04", "source_id": "src-000181", "locator": "file pages 162-221; 6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04"}]
message_ids: ["setr.027.001.05", "setr.029.001.02", "setr.044.001.04"]
message_families: ["setr.027", "setr.029", "setr.044"]
search_terms: ["Tripartite Central Matching With Confirmation Distribution Service Cancellation by Investment Manager", "Investment Manager", "Broker"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---





# Tripartite Central Matching With Confirmation Distribution Service Cancellation by Investment Manager

Source context: Post-Trade Matching. This reference preserves the source-defined segment and its evidence.

This source-defined scenario begins with the first confirmation exchange below. Its purpose, conditional agreement/rejection, cancellation alternatives and outcomes are specified by the source narrative. No additional formal preconditions or postconditions are invented. [Related activity process](flow-src-000180-p180-tripartite-central-matching-with-confirmation-distribution-service.md) provides the broader activity context.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Investment Manager | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Broker | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-broker.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P266** The executing broker sends a trade confirmation to the CMU. The CMU forwards the confirmation received from the broker to the investment manager. The investment manager compares the details of the trade to its own details and sends a trade confirmation to the CMU. The CMU performs a matching process and sends matching status messages to both parties reflecting the outcome of the matching process. The investment manager may, for whatever reason, send a confirmation cancellation message to the CMU or it may send a new confirmation to the CMU. The CMU forwards a cancellation message to the executing broker. The CMU advise the investment manager that they send a cancellation to the executing broker. The CMU will forward the cancellation received from the investment manager and send the cancellation on behalf of the executing broker to the trustee.

Source diagram evidence: [fig-0029](../documents/src-000180/diagrams/fig-0029.md). The reconstructed sequence and actual review evidence are linked below.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000180](../../../../../../../evidence/omitted/620693d01e301c06503cea9a.md). Heading path: BusinessTransactions / BusinessTransactions - Central Matching / Tripartite Central Matching With Confirmation Distribution Service Scenarios / Tripartite Central Matching With Confirmation Distribution Service Cancellation by Investment Manager.

## Curated source sequence

[Dedicated source reconstruction](../diagrams/business-transactions/fig-0029.md). The source order is preserved below; typical-sequence arrows do not override narrative conditions or alternatives.

| Step | Message | Initiating sender | Receiving participant |
| --- | --- | --- | --- |
| 1 | SecuritiesTradeConfirmation | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 2 | SecuritiesTradeConfirmation | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [InvestmentManager](../../../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) |
| 3 | SecuritiesTradeConfirmation | [InvestmentManager](../../../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 4 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [InvestmentManager](../../../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) |
| 5 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) |
| 6 | SecuritiesTradeConfirmationCancellation | [InvestmentManager](../../../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 7 | SecuritiesTradeConfirmationCancellation | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) |
| 8 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [InvestmentManager](../../../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) |
| 9 | SecuritiesTradeConfirmationCancellation | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [Trustee](../../../../../../../shared/reference/participants/participant-src-000180-trustee.md) |
| 10 | SecuritiesTradeConfirmationCancellation | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [Trustee](../../../../../../../shared/reference/participants/participant-src-000180-trustee.md) |


