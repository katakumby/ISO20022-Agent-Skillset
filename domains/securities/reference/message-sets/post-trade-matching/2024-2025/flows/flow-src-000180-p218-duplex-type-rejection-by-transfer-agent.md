---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
flow_id: "flow-src-000180-p218-duplex-type-rejection-by-transfer-agent"
title: "Duplex Type Rejection by Transfer Agent"
source_locations: [{"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Duplex Type Scenarios", "Duplex Type Rejection by Transfer Agent"], "locator": "/w:document/w:body/w:p[218]", "paragraph_id": "P218", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Duplex Type Scenarios", "Duplex Type Rejection by Transfer Agent"], "locator": "/w:document/w:body/w:p[219]", "paragraph_id": "P219", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Duplex Type Scenarios", "Duplex Type Rejection by Transfer Agent"], "locator": "/w:document/w:body/w:p[220]", "paragraph_id": "P220", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Duplex Type Scenarios", "Duplex Type Rejection by Transfer Agent"], "locator": "/w:document/w:body/w:p[221]", "paragraph_id": "P221", "table_id": null}]
participants: ["participant-src-000180-cash-correspondent", "participant-src-000180-cash-settlement-agent", "participant-src-000180-central-matching-utility-cmu", "participant-src-000180-transfer-agent", "participant-src-000180-underwriter"]
message_mapping_evidence: [{"source_label": "SecuritiesTradeConfirmation", "message_id": "setr.027.001.05", "source_id": "src-000181", "locator": "file pages 28-139; 3 setr.027.001.05 SecuritiesTradeConfirmationV05"}, {"source_label": "SecuritiesTradeConfirmationCancellation", "message_id": "setr.029.001.02", "source_id": "src-000181", "locator": "file pages 140-147; 4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02"}, {"source_label": "SecuritiesTradeConfirmationResponse", "message_id": "setr.030.001.03", "source_id": "src-000181", "locator": "file pages 148-161; 5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03"}, {"source_label": "SecuritiesTradeConfirmationStatusAdvice", "message_id": "setr.044.001.04", "source_id": "src-000181", "locator": "file pages 162-221; 6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04"}]
message_ids: ["setr.027.001.05", "setr.029.001.02", "setr.030.001.03", "setr.044.001.04"]
message_families: ["setr.027", "setr.029", "setr.030", "setr.044"]
search_terms: ["Duplex Type Rejection by Transfer Agent", "Transfer Agent", "Underwriter"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---





# Duplex Type Rejection by Transfer Agent

Source context: Post-Trade Matching. This reference preserves the source-defined segment and its evidence.

This source-defined scenario begins with the first confirmation exchange below. Its purpose, conditional agreement/rejection, cancellation alternatives and outcomes are specified by the source narrative. No additional formal preconditions or postconditions are invented. [Related activity process](flow-src-000180-p159-duplex-type.md) provides the broader activity context.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Transfer Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-transfer-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Underwriter | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-underwriter.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P219** The Underwriter sends a trade confirmation to the CMU. The CMU forwards the confirmation received from the Underwriter to the Transfer Agent. The Transfer Agent compares the trade detail with its own trade detail and if there are irreconcilable differences, sends a disaffirmation message to the CMU. Upon receipt of the disaffirmation message, the CMU sends a disaffirmation status message to the Underwriter which may lead to a new trade confirmation message from the Underwriter to the CMU or a confirmation cancellation message from the Underwriter to the CMU. The CMU will forward a cancellation to the Transfer Agent and send a cancellation status advice to the Underwriter.

Source diagram evidence: [fig-0019](../documents/src-000180/diagrams/fig-0019.md). The reconstructed sequence and actual review evidence are linked below.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000180](../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart1_PostTradeMatching_2024_2025_v2.docx). Heading path: BusinessTransactions / BusinessTransactions - Local Matching Scenarios / Duplex Type Scenarios / Duplex Type Rejection by Transfer Agent.

## Curated source sequence

[Dedicated source reconstruction](../diagrams/business-transactions/fig-0019.md). The source order is preserved below; typical-sequence arrows do not override narrative conditions or alternatives.

| Step | Message | Initiating sender | Receiving participant |
| --- | --- | --- | --- |
| 1 | SecuritiesTradeConfirmation | [Underwriter](../../../../../../../shared/reference/participants/participant-src-000180-underwriter.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 2 | SecuritiesTradeConfirmation | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [TransferAgent](../../../../../../../shared/reference/participants/participant-src-000180-transfer-agent.md) |
| 3 | SecuritiesTradeConfirmationResponse | [TransferAgent](../../../../../../../shared/reference/participants/participant-src-000180-transfer-agent.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 4 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [Underwriter](../../../../../../../shared/reference/participants/participant-src-000180-underwriter.md) |
| 5 | SecuritiesTradeConfirmationCancellation | [Underwriter](../../../../../../../shared/reference/participants/participant-src-000180-underwriter.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 6 | SecuritiesTradeConfirmationCancellation | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [TransferAgent](../../../../../../../shared/reference/participants/participant-src-000180-transfer-agent.md) |
| 7 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [Underwriter](../../../../../../../shared/reference/participants/participant-src-000180-underwriter.md) |



Additional source context: [cash settlement agent](../../../../../../../shared/reference/participants/participant-src-000180-cash-settlement-agent.md). This is a narrative/alternative role, not an additional arrow inferred in the main sequence.
