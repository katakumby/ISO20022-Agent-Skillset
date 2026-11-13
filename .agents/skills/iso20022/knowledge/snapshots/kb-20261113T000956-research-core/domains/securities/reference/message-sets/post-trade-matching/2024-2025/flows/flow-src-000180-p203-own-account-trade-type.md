---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
flow_id: "flow-src-000180-p203-own-account-trade-type"
title: "Own Account Trade Type"
source_locations: [{"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Own Account Trade Type Scenarios", "Own Account Trade Type"], "locator": "/w:document/w:body/w:p[203]", "paragraph_id": "P203", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Own Account Trade Type Scenarios", "Own Account Trade Type"], "locator": "/w:document/w:body/w:p[204]", "paragraph_id": "P204", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Own Account Trade Type Scenarios", "Own Account Trade Type"], "locator": "/w:document/w:body/w:p[205]", "paragraph_id": "P205", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Own Account Trade Type Scenarios", "Own Account Trade Type"], "locator": "/w:document/w:body/w:p[206]", "paragraph_id": "P206", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessTransactions", "BusinessTransactions - Local Matching Scenarios", "Own Account Trade Type Scenarios", "Own Account Trade Type"], "locator": "/w:document/w:body/w:p[207]", "paragraph_id": "P207", "table_id": null}]
participants: ["participant-src-000180-broker", "participant-src-000180-broker-executing-broker", "participant-src-000180-central-matching-utility-cmu", "participant-src-000180-institutional-investor", "participant-src-000180-issuer-agent", "participant-src-000180-underwriter"]
message_mapping_evidence: [{"source_label": "SecuritiesTradeConfirmation", "message_id": "setr.027.001.05", "source_id": "src-000181", "locator": "file pages 28-139; 3 setr.027.001.05 SecuritiesTradeConfirmationV05"}, {"source_label": "SecuritiesTradeConfirmationResponse", "message_id": "setr.030.001.03", "source_id": "src-000181", "locator": "file pages 148-161; 5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03"}, {"source_label": "SecuritiesTradeConfirmationStatusAdvice", "message_id": "setr.044.001.04", "source_id": "src-000181", "locator": "file pages 162-221; 6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04"}]
message_ids: ["setr.027.001.05", "setr.030.001.03", "setr.044.001.04"]
message_families: ["setr.027", "setr.030", "setr.044"]
search_terms: ["Own Account Trade Type", "Broker"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
---





# Own Account Trade Type

Source context: Post-Trade Matching. This reference preserves the source-defined segment and its evidence.

This source-defined scenario begins with the first confirmation exchange below. Its purpose, conditional agreement/rejection, cancellation alternatives and outcomes are specified by the source narrative. No additional formal preconditions or postconditions are invented. [Related activity process](flow-src-000180-p153-own-account-trade-type.md) provides the broader activity context.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Broker | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-broker.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P204** The executing broker sends a trade confirmation to the CMU. Once received from the broker, The CMU forwards the trade confirmation to the Institutional Investor. Should the Institutional Investor agree with the detail of the confirmation an affirmation message is sent to the CMU. The message will bind the parties to the trade details of the confirmation being affirmed. The CMU sends an affirmation status message to the executing broker upon receipt of an affirmation message from the Institutional Investor. The trade will then move into the settlement process.

Source diagram evidence: [fig-0016](../documents/src-000180/diagrams/fig-0016.md). The reconstructed sequence and actual review evidence are linked below.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000180](../../../../../../../evidence/omitted/620693d01e301c06503cea9a.md). Heading path: BusinessTransactions / BusinessTransactions - Local Matching Scenarios / Own Account Trade Type Scenarios / Own Account Trade Type.

## Curated source sequence

[Dedicated source reconstruction](../diagrams/business-transactions/fig-0016.md). The source order is preserved below; typical-sequence arrows do not override narrative conditions or alternatives.

| Step | Message | Initiating sender | Receiving participant |
| --- | --- | --- | --- |
| 1 | SecuritiesTradeConfirmation | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 2 | SecuritiesTradeConfirmation | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [InstitutionalInvestor](../../../../../../../shared/reference/participants/participant-src-000180-institutional-investor.md) |
| 3 | SecuritiesTradeConfirmationResponse | [InstitutionalInvestor](../../../../../../../shared/reference/participants/participant-src-000180-institutional-investor.md) | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) |
| 4 | SecuritiesTradeConfirmationStatusAdvice | [CentralMatchingUtility](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | [ExecutingBroker](../../../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) |



Additional source context: [underwriter](../../../../../../../shared/reference/participants/participant-src-000180-underwriter.md). This is a narrative/alternative role, not an additional arrow inferred in the main sequence.

Additional source context: [issuer agent](../../../../../../../shared/reference/participants/participant-src-000180-issuer-agent.md). This is a narrative/alternative role, not an additional arrow inferred in the main sequence.
