---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "57.1 MessageDefinition Functionality"]
file_pages: [4205, 4206]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.017.001.05"]
---

# 57.1 MessageDefinition Functionality

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4205 to 4206.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4205

```text
57 setr.017.001.05
OrderCancellationStatusReportV05
57.1 MessageDefinition Functionality
Scope
The OrderCancellationStatusReport message is sent by an executing party, for example, a transfer
agent, to the instructing party, for example, an investment manager or its authorised representative, to
report the status of an order cancellation request that was previously received.
Usage
The OrderCancellationStatusReport message is used to provide the status of:
- one or more individual order cancellation requests by using IndividualCancellationStatusReport, or,
- an order cancellation request message by using CancellationStatusReport.
If the OrderCancellationStatusReport message is used to report the status of an individual order
cancellation request, then the repetitive IndividualCancellationStatusReport sequence is used and the
order reference of the individual order is quoted in OrderReference. The message identification of the
message in which the individual order was conveyed may also be quoted in RelatedReference but this
is not recommended.
If the OrderCancellationStatusReport message is used to report the status of an entire order
cancellation request message, for example, the SubscriptionBulkOrderCancellationRequest, or a
SubscriptionOrderCancellationRequest containing several orders, then the CancellationStatusReport
sequence is used. The message identification of the order cancellation request message may also be
quoted in RelatedReference but this is not recommended. All the order cancellation requests within the
message must have the same status.
One of the following statuses can be reported:
- the order cancellation is pending, or,
- the order cancellation request is rejected, or,
- the order is cancelled.
When the cancellation is rejected, the reason for the rejection must be specified.
Outline
The OrderCancellationStatusReportV05 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. Reference
Reference to the message or communication that was previously received.
C. StatusReport
Approved by the Securities SEG on 27 January 2026 setr.017.001.05 OrderCancellationStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4205 May 2026
```

## File page 4206

```text
Status of the order cancellation.
D. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 setr.017.001.05 OrderCancellationStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4206 May 2026
```

