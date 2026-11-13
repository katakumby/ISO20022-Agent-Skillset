---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13"]
file_pages: [719, 720]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.040.001.13"]
---

# 12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 719 to 720.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 719

```text
12 seev.040.001.13
CorporateActionInstructionCancellationRequ
estV13
12.1 MessageDefinition Functionality
Scope
The CorporateActionInstructionCancellationRequest message is sent by an account owner to an
account servicer to request cancellation of a previously sent corporate action election instruction.
Usage
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate), using the relevant elements in the business application header (BAH).
Outline
The CorporateActionInstructionCancellationRequestV13 MessageDefinition is composed of 8
MessageBuildingBlocks:
A. ChangeInstructionIndicator
Indicates that cancelled instruction will be replaced by a new corporate action instruction to be sent
later.
B. InstructionIdentification
Identification of a previously sent instruction document.
C. CorporateActionGeneralInformation
General information about the corporate action event.
D. AccountDetails
General information about the safekeeping account and the account owner.
E. CorporateActionInstruction
Information about the corporate action option.
F. ProtectInstruction
Provides detailed information on protect and cover protect instructions.
G. AdditionalInformation
Provides additional information.
H. SupplementaryData
Approved by the Securities SEG on 27 January 2026 seev.040.001.13
CorporateActionInstructionCancellationRequestV13
Corporate Actions - Maintenance 2025 - 2026 719 February 2026
```

## File page 720

```text
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 seev.040.001.13
CorporateActionInstructionCancellationRequestV13
Corporate Actions - Maintenance 2025 - 2026 720 February 2026
```

