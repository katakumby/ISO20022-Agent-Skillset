---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessProcess Description", "BusinessProcess Diagram"]
content_origin: "source-transcription"
---

# BusinessProcess Diagram

Source: [src-000180](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart1_PostTradeMatching_2024_2025_v2.docx). Locator: heading path BusinessProcess Description / BusinessProcess Diagram.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P120** BusinessProcess Diagram

**P121** This section presents the business processes. Describing the business processes and their need for business information helps in the identification of the communication problems which exist among Business Actors. 

**P122** The following diagram reflects the trade lifecycle from order through confirmation/affirmation. Additional updates and diagrams will be made before final publication. It should be noted that the Order and Market-Side confirmation processes are outside the scope of this project but are shown to provide clarity.

**P123** Out Of scopeOut Of scopeOrder ProcessNotification of Execution ProcessAllocation Process/No AllocationConfirmation/Affirmation ProcessAllocationMarket-Side Confirmation ProcessMatching ProcessMatching ProcessOrder ProcessNotification of Execution ProcessAllocation Process/No AllocationConfirmation/Affirmation ProcessAllocationMarket-Side Confirmation ProcessMatching ProcessMatching Process

[fig-0003 - original figure evidence](../diagrams/fig-0003.md)

**P124** Definitions of the business processes: 

**P125** Order Process – Process by which an instructing party places an order to buy or sell to an executing party, at a given price (OUT OF SCOPE).

**P126** Market-Side Confirmation Process - Upon receipt of an order, the executing party looks in the market place for a Trade Counterparty willing to buy or sell the specific securities in the amounts needed, at a given price. For each trade agreed, the two Trade Counterparties exchange information to agree on the details of the trade (OUT OF SCOPE).

**P127** Notification of Execution Process – Once the order has been fully or partially executed, the executing party advises the instructing party (in real-time) by providing the trade details. Such advices are particularly critical in the instance of a block trade that needs to be allocated prior to confirmation. They are also important when the order is carried out partially over several days, or any other period, with differing prices.

**P128** Allocation Process – The instructing party instructs the executing party about how the block is to be allocated among the different funds or clients.

**P129** Confirmation/Matching/Affirmation Process - The executing party advises the instructing party of his client trade confirmation per order or, if a block trade, per allocation.  Trade details from both the instructing and executing parties are compared. Matching is completed to verify that all aspects of a trade are communicated and confirmed as agreed upon in the original trade agreement. Matching can occur either via a central facility (CMU) or locally. A final step in some markets is the positive acknowledgment by the instructing party of the confirmation - the affirmation.

**P130**   


