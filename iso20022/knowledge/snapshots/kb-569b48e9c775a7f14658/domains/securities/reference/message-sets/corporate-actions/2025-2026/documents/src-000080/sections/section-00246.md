---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "6.4 Message Building Blocks"]
file_pages: [330]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.034.001.16"]
---

# 6.4 Message Building Blocks

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 330 to 330.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 330

```text
C36 StatusQuantity5Rule
If CorporateActionInstruction/StatusQuantity is present, then the InstructionProcessingStatus/
Forwarded/ForwardedQuantity or InstructionProcessingStatus/Returned/ReturnedQuantity or
InstructionProcessingStatus/ReceivedByIssuerOrOfferor/AcceptedByIssuerQuantity are not
allowed.
On Condition
    /CorporateActionInstruction/StatusQuantity is present
Following Must be True
    /InstructionProcessingStatus[*]/Forwarded/ForwardedQuantity Must be absent
 And    /InstructionProcessingStatus[*]/Returned/ReturnedQuantity Must be 
absent
 And    /InstructionProcessingStatus[*]/ReceivedByIssuerOrOfferor/
AcceptedByIssuerQuantity Must be absent
 And    /CorporateActionInstruction/StatusCashAmount Must be absent
This constraint is defined at the MessageDefinition level.
C37 StatusQuantity6Rule
If InstructionProcessingStatus/Forwarded/ForwardedQuantity or InstructionProcessingStatus/
Returned/ReturnedQuantity or InstructionProcessingStatus/ReceivedByIssuerOrOfferor/
AcceptedByIssuerQuantity are present, then CorporateActionInstruction/StatusCashAmount
and CorporateActionInstruction/StatusQuantity must be absent.
On Condition
    /InstructionProcessingStatus[*]/Forwarded/ForwardedQuantity is present
 Or    /InstructionProcessingStatus[*]/Returned/ReturnedQuantity is present
 Or    /InstructionProcessingStatus[*]/ReceivedByIssuerOrOfferor/
AcceptedByIssuerQuantity is present
Following Must be True
    /CorporateActionInstruction/StatusCashAmount Must be absent
 And    /CorporateActionInstruction/StatusQuantity Must be absent
This constraint is defined at the MessageDefinition level.
C38 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
6.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
6.4.1 InstructionIdentification <InstrId>
Presence: [0..1]
Definition: Identification of a related instruction document.
InstructionIdentification <InstrId> contains the following elements (see "DocumentIdentification9" on
page 877 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 877
6.4.2 OtherDocumentIdentification <OthrDocId>
Presence: [0..*]
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 330 February 2026
```

