---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["17 semt.001.001.03 SecuritiesMessageRejectionV03"]
file_pages: [371]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.001.001.03"]
---

# 17 semt.001.001.03 SecuritiesMessageRejectionV03

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 371 to 371.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 371

```text
17 semt.001.001.03
SecuritiesMessageRejectionV03
17.1 MessageDefinition Functionality
Scope
An account servicer, for example, a registrar, transfer agent or custodian bank, sends the
SecuritiesMessageRejection message to the account owner, for example, an investor or its authorised
agent, to reject a previously received message on which action cannot be taken.
The message may also be sent by an executing party, for example, transfer agent to the instructing
party, for example, investment manager or its authorised representative to reject a previously received
message on which action cannot be taken.
Usage
The SecuritiesMessageRejection message is used for the following reasons:
- the executing party does not recognise the linked reference, so the executing party cannot process the
message
- the instructing party should not have sent the message.
Reasons that a receiver does not expect a message include no SLA in place between the Sender and
the Receiver.
The SecuritiesMessageRejection message must not be used to reject an instruction message that
cannot be processed for business reasons, for example, if information is missing in an instruction
message or because securities are not available for settlement.
Outline
The SecuritiesMessageRejectionV03 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies a message from a business application standpoint.
B. RelatedReference
Reference to a linked message that was previously received.
C. Reason
Reason to reject the message.
Approved by the Securities SEG on 27 January 2026 semt.001.001.03 SecuritiesMessageRejectionV03
Investment Funds - Maintenance 2025 - 2026 371 May 2026
```

