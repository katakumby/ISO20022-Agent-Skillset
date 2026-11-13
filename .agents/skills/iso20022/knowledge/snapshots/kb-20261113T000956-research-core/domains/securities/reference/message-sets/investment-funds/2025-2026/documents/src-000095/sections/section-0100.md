---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Scenarios For Confirmations When 'Multiple’ Orders Specified in a Single Message"]
content_origin: "source-transcription"
---

# Scenarios For Confirmations When 'Multiple’ Orders Specified in a Single Message

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Scenarios For Confirmations When 'Multiple’ Orders Specified in a Single Message.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P491** Scenarios For Confirmations When 'Multiple’ Orders Specified in a Single Message

**P492** The SubscriptionOrder (setr.010), RedemptionOrder (setr.004), SubscriptionOrderConfirmation (setr.012) and RedemptionOrderConfirmation (setr.006) messages all allow the specification of one or more individual orders or order executions for the same investment account.

**P493** The following section shows the various possibilities.

**P494** [1]	Some institutions send more than one individual order per message. Most institutions, on receipt of a ‘multiple’ order will respond with individual status and confirmation messages:

[fig-0069 - original figure evidence](../diagrams/fig-0069.md)

**P496** [2]	Some institutions send more than one individual order per message. Some institutions will send back a single confirmation message with all the executions for the order:

[fig-0070 - original figure evidence](../diagrams/fig-0070.md)

**P498** The OrderInstructionStatusReport (setr.016) message is not shown on the diagram.

**P499** This means the ‘order executing party' will wait until all orders are executed and then send a single SubscriptionOrderConfirmation (setr.012) message with the three individual executions. Because the trade dates may be different this could mean a delay for those orders that are executed on an earlier trade date.

**P500** [3]	Some institutions offer full flexibility and will, for example, send a ‘combination’ depending on the trade date cycles of the investment funds in the order message.

[fig-0071 - original figure evidence](../diagrams/fig-0071.md)

**P502** The OrderInstructionStatusReport (setr.016) message is not shown on the diagram.

**P503** An institution could decide ‘it’s always single a confirmation message per order’ or the institution could offer flexibility.

