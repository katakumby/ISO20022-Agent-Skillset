---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["11 Message Items Types", "11.1 MessageComponents", "11.1.4 Miscellaneous", "11.1.4.3 OriginalBusinessQuery1", "11.1.4.3.2 MessageNameIdentification <MsgNmId>"]
file_pages: [163]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 11.1.4.3.2 MessageNameIdentification <MsgNmId>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 163 to 163.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 163

```text
11.1.4.3.2  MessageNameIdentification <MsgNmId>
Presence: [0..1]
Definition: Specifies the query message name identifier to which the message refers.
Datatype: "Max35Text" on page 188
11.1.4.3.3  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 185
11.1.4.4  SupplementaryData1
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 163
   Envelope <Envlp> [1..1] (External Schema) 163
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
11.1.4.4.1  PlaceAndName <PlcAndNm>
Presence: [0..1]
Definition: Unambiguous reference to the location where the supplementary data must be inserted in
the message instance.
In the case of XML, this is expressed by a valid XPath.
Datatype: "Max350Text" on page 187
11.1.4.4.2  Envelope <Envlp>
Presence: [1..1]
Definition: Technical element wrapping the supplementary data.
Type: (External Schema)
Technical component that contains the validated supplementary data information. This technical
envelope allows to segregate the supplementary data information from any other information.
11.1.4.5  MessageHeader3
Definition: Set of characteristics, such as the identification or the creation date and time, specific to the
message.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
163 March 2024
```

