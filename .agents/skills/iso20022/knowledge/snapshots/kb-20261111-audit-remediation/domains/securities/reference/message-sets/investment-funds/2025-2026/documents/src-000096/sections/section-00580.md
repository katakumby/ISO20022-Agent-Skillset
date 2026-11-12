---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["31 sese.008.001.09 ReversalOfTransferInConfirmationV09", "32.1 MessageDefinition Functionality"]
file_pages: [784]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.009.001.09"]
---

# 32.1 MessageDefinition Functionality

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 784 to 784.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 784

```text
32 sese.009.001.09
RequestForTransferStatusReportV09
32.1 MessageDefinition Functionality
Scope
The RequestForTransferStatusReport is sent by an instructing party, for example, an investment
manager or its authorised representative, to the executing party, for example, a transfer agent to
request the status of a previously instructed transfer.
The RequestForTransferStatusReport may also be sent by any party in the transfer transaction to
another party in the transfer transaction chain to request information relevant for the settlement of a
transfer transaction.
Usage
The RequestForTransferStatusReport is used to request either:
- the status of one or several information requests or transfer instructions or,
- the status of one or several transfer cancellation instructions, or
- information relevant to one or more transfer instructions.
Outline
The RequestForTransferStatusReportV09 MessageDefinition is composed of 4
MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. RequestDetails
Information to identify the transfer for which the status is requested.
C. MarketPracticeVersion
Identifies the market practice to which the message conforms.
D. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.009.001.09
RequestForTransferStatusReportV09
Investment Funds - Maintenance 2025 - 2026 784 May 2026
```

