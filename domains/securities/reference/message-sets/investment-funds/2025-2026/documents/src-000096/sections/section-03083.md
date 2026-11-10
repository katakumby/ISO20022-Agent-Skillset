---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03", "65.1 MessageDefinition Functionality"]
file_pages: [4303]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.058.001.03"]
---

# 65.1 MessageDefinition Functionality

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4303 to 4303.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4303

```text
65 setr.058.001.03
RequestForOrderConfirmationStatusReportV
03
65.1 MessageDefinition Functionality
Scope
The RequestForOrderConfirmationStatusReport message is ent by an executing party, for example, a
transfer agent, to the instructing party, for example, an investment manager or its authorised
representative, to request the status of one or more order confirmations.
Usage
The RequestForOrderConfirmationStatusReport message is used to request the status of either:
- one or several individual order confirmations, or,
- one or several order confirmation messages.
The response to a RequestForOrderConfirmationStatusReport message is the
OrderConfirmationStatusReport message.
When the RequestForOrderConfirmationStatusReport message is used to request the status of several
individual order confirmations or one or more order confirmation messages, the executing party may
receive several OrderConfirmationStatusReport messages from the instructing party.
When the RequestForOrderConfirmationStatusReport is used to request the status of one or more
individual order confirmations, each individual order confirmation is identified with its order reference.
The message identification of the message in which the individual order confirmation was conveyed
may also be quoted in PreviousReference.
When the RequestForOrderConfirmationStatusReport is used to request the status of an order
confirmation message, then the message identification of the order confirmation message is identified in
PreviousReference.
Outline
The RequestForOrderConfirmationStatusReportV03 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. RequestDetails
Information to identify the order confirmation for which the status is requested.
C. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 setr.058.001.03
RequestForOrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4303 May 2026
```

