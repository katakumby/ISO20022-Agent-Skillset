---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
flow_id: "flow-src-000180-p120-business-process-diagram"
title: "BusinessProcess Diagram"
source_locations: [{"source_id": "src-000180", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[120]", "paragraph_id": "P120", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[121]", "paragraph_id": "P121", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[122]", "paragraph_id": "P122", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[123]", "paragraph_id": "P123", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[124]", "paragraph_id": "P124", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[125]", "paragraph_id": "P125", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[126]", "paragraph_id": "P126", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[127]", "paragraph_id": "P127", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[128]", "paragraph_id": "P128", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[129]", "paragraph_id": "P129", "table_id": null}, {"source_id": "src-000180", "heading_path": ["BusinessProcess Description", "BusinessProcess Diagram"], "locator": "/w:document/w:body/w:p[130]", "paragraph_id": "P130", "table_id": null}]
participants: ["participant-src-000180-central-matching-utility-cmu", "participant-src-000180-exchange", "participant-src-000180-executing-servicing-party", "participant-src-000180-instructing-party", "participant-src-000180-trade-counterparty"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["BusinessProcess Diagram", "Instructing Party", "Exchange"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Table review remains independent of source-diagram reconstruction review.", "Table review remains independent of source-diagram reconstruction review."]
manual_curated: true
---





# BusinessProcess Diagram

Source context: Post-Trade Matching. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Exchange | [Participant](../../../../../../../shared/reference/participants/participant-src-000180-exchange.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P121** This section presents the business processes. Describing the business processes and their need for business information helps in the identification of the communication problems which exist among Business Actors. 

**P122** The following diagram reflects the trade lifecycle from order through confirmation/affirmation. Additional updates and diagrams will be made before final publication. It should be noted that the Order and Market-Side confirmation processes are outside the scope of this project but are shown to provide clarity.

**P123** Out Of scopeOut Of scopeOrder ProcessNotification of Execution ProcessAllocation Process/No AllocationConfirmation/Affirmation ProcessAllocationMarket-Side Confirmation ProcessMatching ProcessMatching ProcessOrder ProcessNotification of Execution ProcessAllocation Process/No AllocationConfirmation/Affirmation ProcessAllocationMarket-Side Confirmation ProcessMatching ProcessMatching Process

Source diagram evidence: [fig-0003](../documents/src-000180/diagrams/fig-0003.md). The dedicated source reconstruction and recorded visual checks are linked below.

**P124** Definitions of the business processes: 

**P125** Order Process – Process by which an instructing party places an order to buy or sell to an executing party, at a given price (OUT OF SCOPE).

**P126** Market-Side Confirmation Process - Upon receipt of an order, the executing party looks in the market place for a Trade Counterparty willing to buy or sell the specific securities in the amounts needed, at a given price. For each trade agreed, the two Trade Counterparties exchange information to agree on the details of the trade (OUT OF SCOPE).

**P127** Notification of Execution Process – Once the order has been fully or partially executed, the executing party advises the instructing party (in real-time) by providing the trade details. Such advices are particularly critical in the instance of a block trade that needs to be allocated prior to confirmation. They are also important when the order is carried out partially over several days, or any other period, with differing prices.

**P128** Allocation Process – The instructing party instructs the executing party about how the block is to be allocated among the different funds or clients.

**P129** Confirmation/Matching/Affirmation Process - The executing party advises the instructing party of his client trade confirmation per order or, if a block trade, per allocation.  Trade details from both the instructing and executing parties are compared. Matching is completed to verify that all aspects of a trade are communicated and confirmed as agreed upon in the original trade agreement. Matching can occur either via a central facility (CMU) or locally. A final step in some markets is the positive acknowledgment by the instructing party of the confirmation - the affirmation.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000180](../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart1_PostTradeMatching_2024_2025_v2.docx). Heading path: BusinessProcess Description / BusinessProcess Diagram.

## Curated process interpretation

The source begins with Order Process and Market-Side Confirmation Process above its red scope boundary, both explicitly out of scope. Notification of Execution leads to the first Matching Process decision. Its Allocation path passes through Allocation Process and a second Matching Process before Confirmation/Affirmation; its /No Allocation path goes directly to Confirmation/Affirmation. Two separately occurring matching diamonds are retained. P122 warns that further updates and diagrams would precede final publication; that source qualification is preserved. P125–129 defines the activity responsibilities: instructing party places the order and allocates blocks; executing party seeks the counterparty, reports execution and sends client confirmations; counterparties agree market-side details; matching can be central or local, with positive affirmation in some markets.

[Complete source diagram reconstruction](../diagrams/processes/fig-0003.md). 

[Complete source diagram reconstruction](../diagrams/processes/fig-0003.md). 
