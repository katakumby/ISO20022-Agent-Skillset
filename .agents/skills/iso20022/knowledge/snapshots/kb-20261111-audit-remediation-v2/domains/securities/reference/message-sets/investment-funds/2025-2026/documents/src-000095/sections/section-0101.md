---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Cancellation and Status "]
content_origin: "source-transcription"
---

# Order Cancellation and Status 

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Order Cancellation and Status .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P504** Order Cancellation and Status 

**P505** This message flow section illustrates the use of the order cancellation messages in typical message sequencing scenarios. The different order cancellation request messages are sent by the instructing party to the executing party. There may be one or more intermediaries in the transaction chain.

**P506** The OrderCancellationStatusReport message is sent by the executing party to the instructing party to inform the instructing party of the acceptance or rejection of an order cancellation request message that was previously sent by the instructing party. 

**P507** The deadline and acceptance of an order cancellation request message is subject to a service level agreement (SLA). 

**P508** Depending on the scenario, the executing party will verify whether:

**P509** it is legally possible to cancel the order, 

**P510** the party that initiated the cancellation request has the right to do so, 

**P511** the cancellation request is allowed by the service level agreement (SLA). 

**P512** The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

**P513** The intermediary party is, for example, an distributor.

