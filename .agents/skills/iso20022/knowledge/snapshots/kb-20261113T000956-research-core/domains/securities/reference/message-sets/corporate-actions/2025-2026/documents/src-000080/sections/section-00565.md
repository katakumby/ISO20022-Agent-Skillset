---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15"]
file_pages: [733, 734]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.041.001.15"]
---

# 13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 733 to 734.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 733

```text
13 seev.041.001.15
CorporateActionInstructionCancellationRequ
estStatusAdviceV15
13.1 MessageDefinition Functionality
Scope
The CorporateActionInstructionCancellationRequestStatusAdvice message is sent by an account
servicer to an account owner or its designated agent to report the status of a previously received
CorporateActionInstructionCancellationRequest message sent by the account owner. This will include
the acknowledgement/rejection of a request to cancel an outstanding instruction.
Usage
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate), using the relevant elements in the business application header (BAH).
Outline
The CorporateActionInstructionCancellationRequestStatusAdviceV15 MessageDefinition is composed
of 8 MessageBuildingBlocks:
A. InstructionCancellationRequestIdentification
Identification of a related instruction cancellation request document.
B. OtherDocumentIdentification
Identification of other documents as well as the document number.
C. CorporateActionGeneralInformation
General information about the corporate action event.
D. InstructionCancellationRequestStatus
Provides information about the processing status of the instruction cancellation request.
E. CorporateActionInstruction
Information about the corporate action option.
F. ProtectInstruction
Provides detailed information on protect and cover protect instructions.
G. AdditionalInformation
Provides additional information.
Approved by the Securities SEG on 27 January 2026 seev.041.001.15
CorporateActionInstructionCancellationRequestStat
usAdviceV15
Corporate Actions - Maintenance 2025 - 2026 733 February 2026
```

## File page 734

```text
H. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 seev.041.001.15
CorporateActionInstructionCancellationRequestStat
usAdviceV15
Corporate Actions - Maintenance 2025 - 2026 734 February 2026
```

