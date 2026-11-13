---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["25 sese.002.001.09 TransferOutCancellationRequestV09"]
file_pages: [513]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.002.001.09"]
---

# 25 sese.002.001.09 TransferOutCancellationRequestV09

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 513 to 513.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 513

```text
25 sese.002.001.09
TransferOutCancellationRequestV09
25.1 MessageDefinition Functionality
Scope
The TransferOutCancellationRequest message is sent by an instructing party, for example, an
investment manager or its authorised representative, to the executing party, for example, a transfer
agent, to request the cancellation of a previously sent transfer out instruction.
Usage
The TransferOutCancellationRequest message is used to request the cancellation of one or more
transfer out instructions.
There is no amendment, but a cancellation and re-instruct policy.
To request the cancellation of one or more transfer out instructions, the transfer reference of the
transfer, as specified in the original TransferOutInstruction message, is specified in the transfer
reference element.
The message identification of the original TransferOutInstruction message may also be quoted in
PreviousReference but this is not recommended.
The deadline and acceptance of a cancellation request is subject to a service level agreement (SLA).
This cancellation message is a cancellation request. There is no automatic acceptance of the
cancellation.
The rejection or acceptance of a TransferOutCancellationRequest is made using a
TransferCancellationStatusReport message.
Outline
The TransferOutCancellationRequestV09 MessageDefinition is composed of 8 MessageBuildingBlocks:
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
F. TransferReferences
Approved by the Securities SEG on 27 January 2026 sese.002.001.09
TransferOutCancellationRequestV09
Investment Funds - Maintenance 2025 - 2026 513 May 2026
```

