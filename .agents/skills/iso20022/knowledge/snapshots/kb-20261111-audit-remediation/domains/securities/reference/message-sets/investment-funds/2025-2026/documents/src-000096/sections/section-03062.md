---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03", "63.1 MessageDefinition Functionality"]
file_pages: [4277]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.055.001.03"]
---

# 63.1 MessageDefinition Functionality

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4277 to 4277.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4277

```text
63 setr.055.001.03
SwitchOrderConfirmationCancellationInstruct
ionV03
63.1 MessageDefinition Functionality
Scope
The SwitchOrderConfirmationCancellationInstruction message is sent by an executing party, for
example, a transfer agent, to the instructing party, for example, an investment manager or its authorised
representative, to cancel a previously sent SwitchOrderConfirmation.
Usage
To request the cancellation of one or more individual order executions, the order reference and deal
reference of each individual order execution in the original SwitchOrderConfirmation are specified in the
order reference and deal reference elements respectively. The message identification of the
SwitchOrderConfirmation message in which the individual order execution was conveyed may also be
quoted in PreviousReference but this is not recommended. The AmendmentIndicator is used to specify
whether the switch order confirmation cancellation is to be followed by an amendment An amendment
of a switch order confirmation is carried out by sending a SwitchOrderConfirmation message in which
the AmendmentIndicator contains the value 'true'.
Outline
The SwitchOrderConfirmationCancellationInstructionV03 MessageDefinition is composed of 8
MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. RelatedReference
Reference to a linked message that was previously received.
E. AmendmentIndicator
Indicates whether a confirmation amendment message will follow the confirmation cancellation
instruction or not.
F. MasterReference
Reference assigned to a set of orders or trades in order to link them together.
G. OrderReferences
Identification of the individual order confirmation to be cancelled.
H. CopyDetails
Approved by the Securities SEG on 27 January 2026 setr.055.001.03
SwitchOrderConfirmationCancellationInstructionV03
Investment Funds - Maintenance 2025 - 2026 4277 May 2026
```

