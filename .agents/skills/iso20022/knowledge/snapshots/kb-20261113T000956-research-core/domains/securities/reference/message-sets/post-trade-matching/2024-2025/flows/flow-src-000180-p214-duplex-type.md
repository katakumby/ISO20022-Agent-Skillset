---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
flow_id: "flow-src-000180-p214-duplex-type"
title: "Duplex Type"
source_locations: [{"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Duplex Type Scenarios", "Duplex Type"], "locator": "/w:document/w:body/w:p[214]", "paragraph_id": "P214", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Duplex Type Scenarios", "Duplex Type"], "locator": "/w:document/w:body/w:p[215]", "paragraph_id": "P215", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Duplex Type Scenarios", "Duplex Type"], "locator": "/w:document/w:body/w:p[216]", "paragraph_id": "P216", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Duplex Type Scenarios", "Duplex Type"], "locator": "/w:document/w:body/w:p[217]", "paragraph_id": "P217", "table_id": null}]
participants: ["participant-src-000180-cash-correspondent", "participant-src-000180-cash-settlement-agent", "participant-src-000180-central-matching-utility-cmu", "participant-src-000180-transfer-agent", "participant-src-000180-underwriter"]
message_mapping_evidence: [{"source_label": "SecuritiesTradeConfirmation", "message_id": "setr.027.001.05", "source_id": "src-000181", "locator": "file pages 28-139; 3 setr.027.001.05 SecuritiesTradeConfirmationV05"}, {"source_label": "SecuritiesTradeConfirmationResponse", "message_id": "setr.030.001.03", "source_id": "src-000181", "locator": "file pages 148-161; 5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03"}, {"source_label": "SecuritiesTradeConfirmationStatusAdvice", "message_id": "setr.044.001.04", "source_id": "src-000181", "locator": "file pages 162-221; 6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04"}]
message_ids: ["setr.027.001.05", "setr.030.001.03", "setr.044.001.04"]
message_families: ["setr.027", "setr.030", "setr.044"]
search_terms: ["Duplex Type", "Cash Settlement Agent", "Transfer Agent", "Underwriter"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---





# Duplex Type

Source context: Post-Trade Matching. This reference preserves the source-defined segment and its evidence.

This source-defined scenario begins with the first confirmation exchange below. Its purpose, conditional agreement/rejection, cancellation alternatives and outcomes are specified by the source narrative. No additional formal preconditions or postconditions are invented. [Related activity process](flow-src-000180-p159-duplex-type.md) provides the broader activity context.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Cash Settlement Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-cash-settlement-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Transfer Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-transfer-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Underwriter | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-underwriter.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P215** The Underwriter sends a trade confirmation to the CMU. The CMU forwards the confirmation received from the Underwriter to the Transfer Agent. Should the trade detail on the confirmation agree with that of the Transfer Agent, it sends an affirmation message to the CMU. Upon receipt of the affirmation message from the Transfer Agent, the CMU forwards the confirmation received from the Underwriter to the Cash Settlement Agent. Should the trade detail on the confirmation agree with that of the Cash Settlement Agent, it sends an affirmation message to the CMU. The message will bind the parties to the trade details of the confirmation being affirmed. The CMU sends an affirmation status message to the Underwriter and the trade can move into the settlement process.

Source diagram evidence: [fig-0018](../documents/src-000180/diagrams/fig-0018.md). The reconstructed sequence and actual review evidence are linked below.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000180](../../../../../../../evidence/omitted/620693d01e301c06503cea9a.md). Heading path: BusinessTransactions / BusinessTransactions - Local Matching Scenarios / Duplex Type Scenarios / Duplex Type.

## Curated source sequence

[Dedicated source reconstruction](../diagrams/business-transactions/fig-0018.md). The source order is preserved below; typical-sequence arrows do not override narrative conditions or alternatives.

| Step | Message | Initiating sender | Receiving participant |
| --- | --- | --- | --- |
| 1 | SecuritiesTradeConfirmation | [Underwriter](../../../../../../../shared/reference/participants/participant-src-000180-underwriter.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 2 | SecuritiesTradeConfirmation | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [TransferAgent](../../../../../../../shared/reference/participants/participant-src-000180-transfer-agent.md) |
| 3 | SecuritiesTradeConfirmationResponse | [TransferAgent](../../../../../../../shared/reference/participants/participant-src-000180-transfer-agent.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 4 | SecuritiesTradeConfirmation | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [CashCorrespondent](../../../../../../../shared/reference/participants/participant-src-000180-cash-correspondent.md) |
| 5 | SecuritiesTradeConfirmationResponse | [CashCorrespondent](../../../../../../../shared/reference/participants/participant-src-000180-cash-correspondent.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 6 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [Underwriter](../../../../../../../shared/reference/participants/participant-src-000180-underwriter.md) |



Additional source context: [cash settlement agent](../../../../../../../shared/reference/participants/participant-src-000180-cash-settlement-agent.md). This is a narrative/alternative role, not an additional arrow inferred in the main sequence.
