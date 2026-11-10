---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
flow_id: "flow-src-000180-p194-through-type"
title: "Through Type"
source_locations: [{"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Through Type Scenarios", "Through Type"], "locator": "/w:document/w:body/w:p[194]", "paragraph_id": "P194", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Through Type Scenarios", "Through Type"], "locator": "/w:document/w:body/w:p[195]", "paragraph_id": "P195", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Through Type Scenarios", "Through Type"], "locator": "/w:document/w:body/w:p[196]", "paragraph_id": "P196", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Through Type Scenarios", "Through Type"], "locator": "/w:document/w:body/w:p[197]", "paragraph_id": "P197", "table_id": null}]
participants: ["participant-src-000180-broker", "participant-src-000180-broker-executing-broker", "participant-src-000180-central-matching-utility-cmu", "participant-src-000180-investment-manager", "participant-src-000180-trustee"]
message_mapping_evidence: [{"source_label": "SecuritiesTradeConfirmation", "message_id": "setr.027.001.05", "source_id": "src-000181", "locator": "file pages 28-139; 3 setr.027.001.05 SecuritiesTradeConfirmationV05"}, {"source_label": "SecuritiesTradeConfirmationResponse", "message_id": "setr.030.001.03", "source_id": "src-000181", "locator": "file pages 148-161; 5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03"}, {"source_label": "SecuritiesTradeConfirmationStatusAdvice", "message_id": "setr.044.001.04", "source_id": "src-000181", "locator": "file pages 162-221; 6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04"}]
message_ids: ["setr.027.001.05", "setr.030.001.03", "setr.044.001.04"]
message_families: ["setr.027", "setr.030", "setr.044"]
search_terms: ["Through Type", "Investment Manager", "Broker"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---





# Through Type

Source context: Post-Trade Matching. This reference preserves the source-defined segment and its evidence.

This source-defined scenario begins with the first confirmation exchange below. Its purpose, conditional agreement/rejection, cancellation alternatives and outcomes are specified by the source narrative. No additional formal preconditions or postconditions are invented. [Related activity process](flow-src-000180-p146-through-type.md) provides the broader activity context.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Investment Manager | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Broker | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-broker.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P195** The executing broker and the investment manager send a confirmation to the CMU. The CMU will forward the two confirmations received to the trustee. The trustee will send an affirmation message to the CMU if it agrees with the detail of the trade. The message will bind the parties to the trade details of the confirmation being affirmed. The CMU will send an affirmation status message to the executing broker upon receipt of the affirmation message from the trustee. The trade will then move into the settlement process.

Source diagram evidence: [fig-0014](../documents/src-000180/diagrams/fig-0014.md). The reconstructed sequence and actual review evidence are linked below.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000180](../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart1_PostTradeMatching_2024_2025_v2.docx). Heading path: BusinessTransactions / BusinessTransactions - Local Matching Scenarios / Through Type Scenarios / Through Type.

## Curated source sequence

[Dedicated source reconstruction](../diagrams/business-transactions/fig-0014.md). The source order is preserved below; typical-sequence arrows do not override narrative conditions or alternatives.

| Step | Message | Initiating sender | Receiving participant |
| --- | --- | --- | --- |
| 1 | SecuritiesTradeConfirmation | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 2 | SecuritiesTradeConfirmation | [InvestmentManager](../../../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 3 | SecuritiesTradeConfirmation | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [Trustee](../../../../../../../shared/reference/participants/participant-src-000180-trustee.md) |
| 4 | SecuritiesTradeConfirmation | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [Trustee](../../../../../../../shared/reference/participants/participant-src-000180-trustee.md) |
| 5 | SecuritiesTradeConfirmationResponse | [Trustee](../../../../../../../shared/reference/participants/participant-src-000180-trustee.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 6 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) |


