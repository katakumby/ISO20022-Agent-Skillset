---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["23 camt.025.001.09 ReceiptV09"]
file_pages: [604]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.025.001.09"]
---

# 23 camt.025.001.09 ReceiptV09

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 604 to 604.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 604

```text
23 camt.025.001.09
ReceiptV09
23.1 MessageDefinition Functionality
Scope
The Receipt message is sent by a message recipient to the message sender. It is sent to acknowledge
the receipt of one or multiple messages sent previously.
The Receipt message is an application receipt acknowledgement and conveys information about the
processing of the original message(s).
Usage
The Receipt message is used when the exchange of messages takes place in an asynchronous
manner.
This may happen, for instance, when an action is requested from the message sender (a deletion,
modification or cancellation). The message sender will first acknowledge the request (with a Receipt
message) and then execute it.
The message can contain information based on the following elements: reference of the message(s) it
acknowledges, the status code (optional) and further explanation:
- reference of the message it acknowledges
- potentially, a status code and status reason information.
Outline
The ReceiptV09 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReceiptDetails
Details of the receipt.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.025.001.09 ReceiptV09
Cash Management - Maintenance 2024 - 2025 604 February 2025
```

