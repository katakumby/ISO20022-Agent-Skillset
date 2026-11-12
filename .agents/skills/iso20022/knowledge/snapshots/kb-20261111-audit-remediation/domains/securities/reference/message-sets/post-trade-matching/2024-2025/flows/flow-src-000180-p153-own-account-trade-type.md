---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
flow_id: "flow-src-000180-p153-own-account-trade-type"
title: "Own Account Trade Type"
source_locations: [{"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Own Account Trade Type"], "locator": "/w:document/w:body/w:p[153]", "paragraph_id": "P153", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Own Account Trade Type"], "locator": "/w:document/w:body/w:p[154]", "paragraph_id": "P154", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Own Account Trade Type"], "locator": "/w:document/w:body/w:p[155]", "paragraph_id": "P155", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Own Account Trade Type"], "locator": "/w:document/w:body/w:p[156]", "paragraph_id": "P156", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Own Account Trade Type"], "locator": "/w:document/w:body/w:tbl[10]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Own Account Trade Type"], "locator": "/w:document/w:body/w:p[157]", "paragraph_id": "P157", "table_id": null}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Own Account Trade Type"], "locator": "/w:document/w:body/w:p[158]", "paragraph_id": "P158", "table_id": null}]
participants: ["participant-src-000180-broker", "participant-src-000180-broker-underwriter", "participant-src-000180-central-matching-utility-cmu", "participant-src-000180-central-matching-utility-jasdec", "participant-src-000180-institutional-investor", "participant-src-000180-institutional-investor-issuer-agent", "participant-src-000180-issuer-agent", "participant-src-000180-underwriter"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Own Account Trade Type", "Institutional Investor/Issuer Agent", "Central Matching Utility (JASDEC)", "Broker/Underwriter", "Underwriter", "Broker"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Table review remains independent of source-diagram reconstruction review."]
manual_curated: true
---



# Own Account Trade Type

Source context: Post-Trade Matching. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Institutional Investor/Issuer Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-institutional-investor-issuer-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Central Matching Utility (JASDEC) | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-jasdec.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Broker/Underwriter | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-broker-underwriter.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Underwriter | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-underwriter.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Broker | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-broker.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P154** The executing broker sends a trade confirmation to the CMU. Once received from the broker, The CMU forwards the trade confirmation to the Institutional Investor. Should the Institutional Investor agree with the detail of the confirmation an affirmation message is sent to the CMU. The message will bind the parties to the trade details of the confirmation being affirmed. The CMU sends an affirmation status message to the executing broker upon receipt of an affirmation message from the Institutional Investor. The trade will then move into the settlement process.

Source diagram evidence: [fig-0008](../documents/src-000180/diagrams/fig-0008.md). The dedicated source reconstruction and recorded visual checks are linked below.

Source table [T10](../documents/src-000180/tables/tbl-0010.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Description of Activities |  |  |
| Broker/Underwriter | Central Matching Utility (JASDEC) | Institutional Investor/Issuer Agent |
| Confirmation: The broker or Underwriter sends a trade confirmation to JASDEC. | Confirmation (broker): Once received from the broker, JASDEC forwards the trade confirmation to the Institutional Investor or Issuer Agent.   |  |
| Cancel Confirmation: The trade may, for some reason, be cancelled upon which the broker will send a cancellation message to JASDEC. |  |  |
|  | Status Advice: JASDEC will send a cancellation status advice to the broker or Underwriter and Institutional Investor or Issuer Agent. |  |
|  | Disaffirmation Status Message: JASDEC sends a disaffirmation status message to the broker upon receipt of the disaffirmation message from the institutional investor which may result in the cancellation of the trade or the sending of a new confirmation.  | Disaffirmation: The Institutional Investor or Issuer Agent will compare the details of the confirmation with their details of the trade. If the details are irreconcilable, a disaffirmation message will be sent to JASDEC. |
|  | Affirmation Status Message: JASDEC sends an affirmation status message to the broker upon receipt of an affirmation message from the Institutional Investor. The trade will then move into the settlement process. | Affirmation: Should the Institutional Investor or Issuer Agent agree with the detail of the confirmation an affirmation message is sent to JASDEC.  The message will bind the parties to the trade details of the confirmation being affirmed. |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000180](../../../../../../../evidence/omitted/620693d01e301c06503cea9a.md). Heading path: Description of BusinessActivities / BusinessProcess – Local Matching / Own Account Trade Type.

## Curated process interpretation

Broker / Underwriter sends its confirmation through CMU to Institutional Investor / Issuer Agent. The recipient compares details: N.G. leads to disaffirmation and a status returning to the sender; O.K. leads to affirmation, status and settlement continuations. Cancellation enters the CMU lane at an unlabelled endpoint; a separate cancellation-status action points to sender and recipient receipts. P154 binds the trade on affirmation. T10 preserves cancellation/new-confirmation alternatives and disaffirmation conditions.

[Complete source diagram reconstruction](../diagrams/processes/fig-0008.md). Slash-separated actor labels describe source alternatives, not a merger of institutions or role definitions.
