---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16"]
file_pages: [320, 321]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.034.001.16"]
---

# 6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 320 to 321.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 320

```text
6 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
6.1 MessageDefinition Functionality
Scope
The CorporateActionInstructionStatusAdvice message is sent by an account servicer to an account
owner or its designated agent, to report the status of a received corporate action election instruction.
This message is used to advise the status, or a change in status, of a corporate action-related
transaction previously instructed by, or executed on behalf of, the account owner. This will include the
acknowledgement/rejection of a corporate action instruction.
Usage
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate), using the relevant elements in the business application header (BAH).
Outline
The CorporateActionInstructionStatusAdviceV16 MessageDefinition is composed of 8
MessageBuildingBlocks:
A. InstructionIdentification
Identification of a related instruction document.
B. OtherDocumentIdentification
Identification of other documents as well as the document number.
C. CorporateActionGeneralInformation
General information about the corporate action event.
D. InstructionProcessingStatus
Information about the processing status of the instruction.
E. CorporateActionInstruction
Information about the corporate action instruction.
F. ProtectInstruction
Provides detailed information on protect and cover protect instructions.
G. AdditionalInformation
Provides additional information.
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 320 February 2026
```

## File page 321

```text
H. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 321 February 2026
```

