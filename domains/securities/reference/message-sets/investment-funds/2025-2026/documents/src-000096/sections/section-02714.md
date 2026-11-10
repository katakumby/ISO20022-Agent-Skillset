---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "54.1 MessageDefinition Functionality"]
file_pages: [3797]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.014.001.05"]
---

# 54.1 MessageDefinition Functionality

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3797 to 3797.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3797

```text
54 setr.014.001.05
SwitchOrderCancellationRequestV05
54.1 MessageDefinition Functionality
Scope
The SwitchOrderCancellationRequest message is sent by an instructing party, for example, an
investment manager or its authorised representative, to the executing party, for example, a transfer
agent, to request the cancellation of a previously sent SwitchOrder instruction.
Usage
The SwitchOrderCancellationRequest is used to cancel the entire previously sent SwitchOrder
instruction/s and all the individual legs that it contains. There is no amendment, but a cancellation and
re-instruct policy.
To request the cancellation of a switch order, the order reference of the original switch order is quoted
in the order reference element. The message identification of the SwitchOrder message may also be
quoted in PreviousReference but this is not recommended.
The deadline and acceptance of a cancellation request is subject to a service level agreement (SLA).
This cancellation message is a cancellation request. There is no automatic acceptance of the
cancellation request.
The rejection or acceptance of a SwitchOrderCancellationRequest is made using an
OrderCancellationStatusReport message.
Outline
The SwitchOrderCancellationRequestV05 MessageDefinition is composed of 6
MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. MasterReference
Reference assigned to a set of orders or trades in order to link them together.
E. OrderReferences
Identification of the individual order to be cancelled.
F. CopyDetails
Information provided when the message is a copy of a previous message.
Approved by the Securities SEG on 27 January 2026 setr.014.001.05
SwitchOrderCancellationRequestV05
Investment Funds - Maintenance 2025 - 2026 3797 May 2026
```

