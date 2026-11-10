---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "58.1 MessageDefinition Functionality"]
file_pages: [4232, 4233]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.018.001.05"]
---

# 58.1 MessageDefinition Functionality

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4232 to 4233.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4232

```text
58 setr.018.001.05
RequestForOrderStatusReportV05
58.1 MessageDefinition Functionality
Scope
The RequestForOrderStatusReport message is sent by an instructing party, for example, an investment
manager or its authorised representative, to the executing party, for example, a transfer agent, to
request the status of one or more order instructions or order cancellation requests.
Usage
The RequestForOrderStatusReport message is used to request the status of:
- one or several individual order instructions, or,
- one or several order messages, or
- one or several individual order cancellation requests, or,
- one or several order cancellation request messages.
The response to a RequestForOrderStatusReport message is the OrderInstructionStatusReport
message or OrderCancellationStatusReport message.
If the RequestForOrderStatusReport message is used to request the status of several individual order
instructions or one or more order instruction messages, then the instructing party may receive several
OrderInstructionStatusReport messages from the executing party.
If the RequestForOrderStatusReport message is used to request the status of several individual order
cancellation requests or one or more order cancellation messages, then the instructing party may
receive several OrderCancellationStatusReport messages from the executing party.
When the RequestForOrderStatusReport is used to request the status of one or more individual orders
or order cancellations, each individual order is identified with its order reference. The investment
account and/or financial instrument related to the order can also be identified. The message
identification of the message in which the individual order was conveyed may also be quoted in
PreviousReference.
When the RequestForOrderStatusReport is used to request the status of an order message or an order
cancellations request message, then the message identification of the order or cancellation message is
identified in PreviousReference.
The RequestForOrderStatusReport message may not be used to request the status of an investment
account, a transfer or the status of a financial instrument.
Outline
The RequestForOrderStatusReportV05 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageIdentification
Approved by the Securities SEG on 27 January 2026 setr.018.001.05 RequestForOrderStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4232 May 2026
```

## File page 4233

```text
Reference that uniquely identifies the message from a business application standpoint.
B. RequestDetails
Information to identify the order(s) for which the status is requested.
C. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 setr.018.001.05 RequestForOrderStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4233 May 2026
```

