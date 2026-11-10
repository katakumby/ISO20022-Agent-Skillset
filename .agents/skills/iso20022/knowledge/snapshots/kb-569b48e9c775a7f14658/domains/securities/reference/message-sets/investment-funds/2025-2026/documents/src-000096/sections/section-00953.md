---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09"]
file_pages: [1302]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.014.001.09"]
---

# 37 sese.014.001.09 PortfolioTransferCancellationRequestV09

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1302 to 1302.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1302

```text
37 sese.014.001.09
PortfolioTransferCancellationRequestV09
37.1 MessageDefinition Functionality
Scope
The PortfolioTransferCancellationRequest message is sent by, for example, an investment manager or
its authorised representative, to the executing party, for example, a transfer agent, to request the
cancellation of a previously sent PortfolioTransferInstruction message.
Usage
The PortfolioTransferCancellationRequest message is used to request the cancellation of a portfolio
transfer instruction.
There is no amendment, but a cancellation and re-instruct policy.
To request the cancellation of a portfolio transfer instruction, the transfer reference of the portfolio
transfer, as specified in the original PortfolioTransferInstruction message, is specified in the transfer
reference element.
The message identification of the original PortfolioTransferInstruction message may also be quoted in
PreviousReference but this is not recommended.
The deadline and acceptance of a cancellation request is subject to a service level agreement (SLA).
This cancellation message is a cancellation request. There is no automatic acceptance of the
cancellation.
The rejection or acceptance of a PortfolioTransferCancellationRequest is made using an
TransferCancellationStatusReport message.
Outline
The PortfolioTransferCancellationRequestV09 MessageDefinition is composed of 7
MessageBuildingBlocks:
A. MessageReference
Reference that uniquely identifies the message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. RelatedReference
Reference to a linked message that was previously received.
E. MasterReference
Unique and unambiguous identifier for a group of individual transfers as assigned by the instructing
party. This identifier links the individual transfers together.
Approved by the Securities SEG on 27 January 2026 sese.014.001.09
PortfolioTransferCancellationRequestV09
Investment Funds - Maintenance 2025 - 2026 1302 May 2026
```

