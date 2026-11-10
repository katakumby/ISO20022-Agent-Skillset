---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
flow_id: "flow-src-000180-p198-through-type-cancellation"
title: "Through Type Cancellation"
source_locations: [{"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Through Type Scenarios", "Through Type Cancellation"], "locator": "/w:document/w:body/w:p[198]", "paragraph_id": "P198", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Through Type Scenarios", "Through Type Cancellation"], "locator": "/w:document/w:body/w:p[199]", "paragraph_id": "P199", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Through Type Scenarios", "Through Type Cancellation"], "locator": "/w:document/w:body/w:p[200]", "paragraph_id": "P200", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Through Type Scenarios", "Through Type Cancellation"], "locator": "/w:document/w:body/w:p[201]", "paragraph_id": "P201", "table_id": null}]
participants: ["participant-src-000180-broker", "participant-src-000180-broker-executing-broker", "participant-src-000180-central-matching-utility-cmu", "participant-src-000180-investment-manager", "participant-src-000180-trustee"]
message_mapping_evidence: [{"source_label": "SecuritiesTradeConfirmation", "message_id": "setr.027.001.05", "source_id": "src-000181", "locator": "file pages 28-139; 3 setr.027.001.05 SecuritiesTradeConfirmationV05"}, {"source_label": "SecuritiesTradeConfirmationCancellation", "message_id": "setr.029.001.02", "source_id": "src-000181", "locator": "file pages 140-147; 4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02"}, {"source_label": "SecuritiesTradeConfirmationResponse", "message_id": "setr.030.001.03", "source_id": "src-000181", "locator": "file pages 148-161; 5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03"}, {"source_label": "SecuritiesTradeConfirmationStatusAdvice", "message_id": "setr.044.001.04", "source_id": "src-000181", "locator": "file pages 162-221; 6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04"}]
message_ids: ["setr.027.001.05", "setr.029.001.02", "setr.030.001.03", "setr.044.001.04"]
message_families: ["setr.027", "setr.029", "setr.030", "setr.044"]
search_terms: ["Through Type Cancellation", "Investment Manager", "Broker"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---





# Through Type Cancellation

Source context: Post-Trade Matching. This reference preserves the source-defined segment and its evidence.

This source-defined scenario begins with the first confirmation exchange below. Its purpose, conditional agreement/rejection, cancellation alternatives and outcomes are specified by the source narrative. No additional formal preconditions or postconditions are invented. [Related activity process](flow-src-000180-p146-through-type.md) provides the broader activity context.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Investment Manager | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Broker | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-broker.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P199** The executing broker and the investment manager send a confirmation to the CMU. The CMU will forward the two confirmations received to the trustee. The trustee will send an affirmation message to the CMU if it agrees with the detail of the trade. The message will bind the parties to the trade details of the confirmation being affirmed. The CMU will send an affirmation status message to the executing broker upon receipt of the affirmation message from the trustee. The executing broker and investment manager may, for whatever reason, decide to cancel the confirmation and a new confirmation may be sent. Cancellation of the confirmation may also imply the cancellation of the trade, in which case a new confirmation will not be sent.

Source diagram evidence: [fig-0015](../documents/src-000180/diagrams/fig-0015.md). The reconstructed sequence and actual review evidence are linked below.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000180](../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart1_PostTradeMatching_2024_2025_v2.docx). Heading path: BusinessTransactions / BusinessTransactions - Local Matching Scenarios / Through Type Scenarios / Through Type Cancellation.

## Curated source sequence

[Dedicated source reconstruction](../diagrams/business-transactions/fig-0015.md). The source order is preserved below; typical-sequence arrows do not override narrative conditions or alternatives.

| Step | Message | Initiating sender | Receiving participant |
| --- | --- | --- | --- |
| 1 | SecuritiesTradeConfirmation | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 2 | SecuritiesTradeConfirmation | [InvestmentManager](../../../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 3 | SecuritiesTradeConfirmation | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [Trustee](../../../../../../../shared/reference/participants/participant-src-000180-trustee.md) |
| 4 | SecuritiesTradeConfirmation | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [Trustee](../../../../../../../shared/reference/participants/participant-src-000180-trustee.md) |
| 5 | SecuritiesTradeConfirmationResponse | [Trustee](../../../../../../../shared/reference/participants/participant-src-000180-trustee.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 6 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) |
| 7 | SecuritiesTradeConfirmationCancellation | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 8 | SecuritiesTradeConfirmationCancellation | [InvestmentManager](../../../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 9 | SecuritiesTradeConfirmationCancellation | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [Trustee](../../../../../../../shared/reference/participants/participant-src-000180-trustee.md) |
| 10 | SecuritiesTradeConfirmationCancellation | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [Trustee](../../../../../../../shared/reference/participants/participant-src-000180-trustee.md) |
| 11 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [InvestmentManager](../../../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) |
| 12 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) |


