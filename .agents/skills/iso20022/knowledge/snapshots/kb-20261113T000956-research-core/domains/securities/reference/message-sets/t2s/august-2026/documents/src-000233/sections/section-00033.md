---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["4 admi.007.001.01 ReceiptAcknowledgementV01", "4.4 Message Building Blocks", "4.4.2 Report <Rpt>", "4.4.2.2 RequestHandling <ReqHdlg>"]
file_pages: [66, 67]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.007.001.01"]
---

# 4.4.2.2 RequestHandling <ReqHdlg>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 66 to 67.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 66

```text
ReferenceIssuer <RefIssr> contains the following elements (see "PartyIdentification136" on page 3060
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
4.4.2.2  RequestHandling <ReqHdlg>
Presence: [1..1]
Definition: Gives the status of the request.
RequestHandling <ReqHdlg> contains the following RequestHandling2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StatusCode <StsCd> [1..1] Text 66
   StatusDateTime <StsDtTm> [0..1] DateTime 66
   Description <Desc> [0..1] Text 66
4.4.2.2.1  StatusCode <StsCd>
Presence: [1..1]
Definition: Specifies the status of the request, for example the result of the schema validation or a
business processing result/error.
Datatype: "Max4AlphaNumericText" on page 3328
4.4.2.2.2  StatusDateTime <StsDtTm>
Presence: [0..1]
Definition: Date and time when the status was generated.
Datatype: "ISODateTime" on page 3320
4.4.2.2.3  Description <Desc>
Presence: [0..1]
Definition: Description of the status, in free format text.
Datatype: "Max140Text" on page 3326
4.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C3 "SupplementaryDataRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
admi.007.001.01 ReceiptAcknowledgementV01
Target2-Securities 66 August 2026
```

## File page 67

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 3011 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 3011
   Envelope <Envlp> [1..1] (External Schema) 3012
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
admi.007.001.01 ReceiptAcknowledgementV01
Target2-Securities 67 August 2026
```

