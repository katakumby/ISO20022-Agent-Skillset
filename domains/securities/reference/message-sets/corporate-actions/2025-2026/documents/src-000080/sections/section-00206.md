---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14"]
file_pages: [274, 275]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5 seev.033.001.14 CorporateActionInstructionV14

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 274 to 275.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 274

```text
5 seev.033.001.14
CorporateActionInstructionV14
5.1 MessageDefinition Functionality
Scope
The CorporateActionInstruction message is sent by an account owner to an account servicer to instruct
election on a corporate action event.
This message is used to provide the custodian with instructions on how the account owner wishes to
proceed with a corporate action event. Instructions include investment decisions regarding the exercise
of rights issues, the election of stock or cash when the option is available, and decisions on the
conversion or tendering of securities.
Usage
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate), using the relevant elements in the business application header (BAH).
Outline
The CorporateActionInstructionV14 MessageDefinition is composed of 12 MessageBuildingBlocks:
A. ChangeInstructionIndicator
Indicates that the current instruction is replacing a previous one that was cancelled earlier.
B. CancelledInstructionIdentification
Identification of a previously sent cancelled instruction document.
C. InstructionCancellationRequestIdentification
Identification of a previously sent instruction cancellation request document.
D. OtherDocumentIdentification
Identification of other documents as well as the document number.
E. EventsLinkage
Identification of another corporate action event that needs to be closely linked to the processing of
the event notified in this document.
F. CorporateActionGeneralInformation
General information about the corporate action event.
G. AccountDetails
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 274 February 2026
```

## File page 275

```text
General information about the safekeeping account, owner and account balance.
H. BeneficialOwnerDetails
Information about the beneficial owner of the securities.
I. CorporateActionInstruction
Information about the corporate action instruction.
J. ProtectInstruction
Provides detailed information on protect and cover protect instructions.
K. AdditionalInformation
Provides additional information.
L. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 275 February 2026
```

