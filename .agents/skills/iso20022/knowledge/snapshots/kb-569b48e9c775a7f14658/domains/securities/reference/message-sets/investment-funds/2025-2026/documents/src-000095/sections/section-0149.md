---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Confirmation Status Request ", "Switch "]
content_origin: "source-transcription"
---

# Switch 

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Order Confirmation Status Request  / Switch .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P745** Switch 

**P746** An instructing party sends a SwitchOrder message to the executing party. 

**P747** The executing party replies with a SwitchOrderConfirmation message.

**P748** As execution details need to be amended, the executing party sends another SwitchOrderConfirmation message with the AmendmentIndicator set to 'true' or '1'..

**P749** Later, the executing party sends a RequestForOrderConfirmationStatusReport message to find out the status of its SwitchOrderConfirmation (amendment) message.

**P750** The instructing party sends an OrderConfirmationStatusReport message to the executing party, indicating the status of the SwitchOrderConfirmation (amendment) is accepted.

[fig-0105 - original figure evidence](../diagrams/fig-0105.md)

