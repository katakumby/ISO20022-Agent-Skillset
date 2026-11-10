---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.3 Miscellaneous", "10.1.3.3 OriginalBusinessInstruction1"]
file_pages: [69]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.3.3 OriginalBusinessInstruction1

Source: [src-000354](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 69 to 69.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 69

```text
10.1.3.3  OriginalBusinessInstruction1
Definition: Unique identification, as assigned by the original requestor, to unambiguously identify the
business instruction message.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 69
   MessageNameIdentification <MsgNmId> [0..1] Text 69
   CreationDateTime <CreDtTm> [0..1] DateTime 69
10.1.3.3.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the original initiating party, to unambiguously identify
the original instruction message.
Datatype: "Max35Text" on page 83
10.1.3.3.2  MessageNameIdentification <MsgNmId>
Presence: [0..1]
Definition: Specifies the instruction message name identifier to which the message refers.
Datatype: "Max35Text" on page 83
10.1.3.3.3  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 80
10.1.3.4  SupplementaryData1
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 69
   Envelope <Envlp> [1..1] (External Schema) 70
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
10.1.3.4.1  PlaceAndName <PlcAndNm>
Presence: [0..1]
Approved by the Securities SEG on 17 April 2025. Message Items Types
Target2-Securities - Collateral Management Reference Data 69 May 2025
```

