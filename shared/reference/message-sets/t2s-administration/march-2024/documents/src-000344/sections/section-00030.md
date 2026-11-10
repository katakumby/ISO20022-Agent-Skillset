---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["4 admi.007.001.01 ReceiptAcknowledgementV01", "4.4 Message Building Blocks", "4.4.2 Report <Rpt>", "4.4.2.2 RequestHandling <ReqHdlg>"]
file_pages: [36, 37]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.007.001.01"]
---

# 4.4.2.2 RequestHandling <ReqHdlg>

Source: [src-000344](../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 36 to 37.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 36

```text
ReferenceIssuer <RefIssr> contains the following elements (see "PartyIdentification136" on page 54
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 54
   LEI <LEI> [0..1] IdentifierSet 54
4.4.2.2  RequestHandling <ReqHdlg>
Presence: [1..1]
Definition: Gives the status of the request.
RequestHandling <ReqHdlg> contains the following RequestHandling2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StatusCode <StsCd> [1..1] Text 36
   StatusDateTime <StsDtTm> [0..1] DateTime 36
   Description <Desc> [0..1] Text 36
4.4.2.2.1  StatusCode <StsCd>
Presence: [1..1]
Definition: Specifies the status of the request, for example the result of the schema validation or a
business processing result/error.
Datatype: "Max4AlphaNumericText" on page 69
4.4.2.2.2  StatusDateTime <StsDtTm>
Presence: [0..1]
Definition: Date and time when the status was generated.
Datatype: "ISODateTime" on page 66
4.4.2.2.3  Description <Desc>
Presence: [0..1]
Definition: Description of the status, in free format text.
Datatype: "Max140Text" on page 68
4.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C3 "SupplementaryDataRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
admi.007.001.01 ReceiptAcknowledgementV01
Target2-Securities - Administration - Maintenance 2023 -
2024
36 March 2024
```

## File page 37

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 53 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 53
   Envelope <Envlp> [1..1] (External Schema) 53
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
admi.007.001.01 ReceiptAcknowledgementV01
Target2-Securities - Administration - Maintenance 2023 -
2024
37 March 2024
```

