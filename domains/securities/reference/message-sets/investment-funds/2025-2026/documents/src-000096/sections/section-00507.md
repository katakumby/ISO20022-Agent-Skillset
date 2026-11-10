---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["29 sese.006.001.09 TransferInCancellationRequestV09"]
file_pages: [689]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.006.001.09"]
---

# 29 sese.006.001.09 TransferInCancellationRequestV09

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 689 to 689.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 689

```text
29 sese.006.001.09
TransferInCancellationRequestV09
29.1 MessageDefinition Functionality
Scope
The TransferInCancellationRequest message is sent by an instructing party, for example, an investment
manager or its authorised representative, to the executing party, for example, a transfer agent, to
request the cancellation of a previously sent transfer in instruction.
Usage
The TransferInCancellationRequest message is used to request the cancellation of one or more
transfer in instructions.
There is no amendment, but a cancellation and re-instruct policy.
To request the cancellation of one or more transfer in instructions, the transfer reference of the transfer,
as specified in the original TransferInInstruction message, is specified in the transfer reference element.
The message identification of the original TransferOutInstruction message may also be quoted in
PreviousReference but this is not recommended.
The deadline and acceptance of a cancellation request is subject to a service level agreement (SLA).
This cancellation message is a cancellation request. There is no automatic acceptance of the
cancellation.
The rejection or acceptance of a TransferInCancellationRequest is made using a
TransferCancellationStatusReport message.
Outline
The TransferInCancellationRequestV09 MessageDefinition is composed of 9 MessageBuildingBlocks:
A. MessageIdentification
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
F. Function
Approved by the Securities SEG on 27 January 2026 sese.006.001.09
TransferInCancellationRequestV09
Investment Funds - Maintenance 2025 - 2026 689 May 2026
```

