---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05"]
file_pages: [3802]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55 setr.015.001.05 SwitchOrderConfirmationV05

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3802 to 3802.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3802

```text
55 setr.015.001.05
SwitchOrderConfirmationV05
55.1 MessageDefinition Functionality
Scope
The SwitchOrderConfirmation message is sent by an executing party, for example, a transfer agent, to
the instructing party, for example, an investment manager or its authorised representative, to confirm
the details of the execution of a previously received SwitchOrder instruction.
Usage
The SwitchOrderConfirmation message is used to confirm that all the legs of the previously instructed
switch order have been executed. The reference of the switch order confirmation is identified in
DealReference.
The reference of the original switch order is specified in OrderReference. The message identification of
the SwitchOrder message in which the switch order was conveyed may also be quoted in
RelatedReference but this is not recommended.
When the message is used to convey a confirmation amendment/s, the AmendmentIndicator must be
present with the value 'true' or '1'. When this is the case, the message must only contain a confirmation
amendment/s and not contain both a confirmation amendment/s and a 'new' confirmation/s.
Outline
The SwitchOrderConfirmationV05 MessageDefinition is composed of 7 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. RelatedReference
Reference to a linked message that was previously received.
E. SwitchExecutionDetails
Information related to a switch execution.
F. CopyDetails
Information provided when the message is a copy of a previous message.
G. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3802 May 2026
```

