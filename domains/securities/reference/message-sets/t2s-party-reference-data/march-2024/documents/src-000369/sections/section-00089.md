---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["8 reda.041.001.02 PartyActivityAdviceV02", "8.4 Message Building Blocks", "8.4.2 PartyActivity <PtyActvty>", "8.4.2.2 Change <Chng>", "8.4.2.2.2 Record <Rcrd>", "8.4.2.2.2.11 Restriction <Rstrctn>", "8.4.2.2.2.11.2 New <New>", "8.4.2.2.2.11.2.3 ValidUntil <VldUntil>"]
file_pages: [109, 110]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.041.001.02"]
---

# 8.4.2.2.2.11.2.3 ValidUntil <VldUntil>

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 109 to 110.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 109

```text
8.4.2.2.2.11.2.3  ValidUntil <VldUntil>
Presence: [0..1]
Definition: Date until when the restriction is valid.
Datatype: "ISODateTime" on page 185
8.4.2.2.2.12  Other <Othr>
Presence: [1..*]
Definition: Specifies a proprietary update type.
Other <Othr> contains the following UpdateLogProprietary1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FieldName <FldNm> [1..1] Text 109
   OldFieldValue <OdFldVal> [1..1] Text 109
   NewFieldValue <NewFldVal> [1..1] Text 109
8.4.2.2.2.12.1  FieldName <FldNm>
Presence: [1..1]
Definition: Name of the field whose value has been changed.
Datatype: "Max35Text" on page 188
8.4.2.2.2.12.2  OldFieldValue <OdFldVal>
Presence: [1..1]
Definition: Value of the field before the change.
Datatype: "Max350Text" on page 187
8.4.2.2.2.12.3  NewFieldValue <NewFldVal>
Presence: [1..1]
Definition: Value of the field after the change.
Datatype: "Max350Text" on page 187
8.4.2.2.3  OperationTimeStamp <OprTmStmp>
Presence: [1..1]
Definition: Specifies the timestamp of the operation.
Datatype: "ISODateTime" on page 185
8.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C4 "SupplementaryDataRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
109 March 2024
```

## File page 110

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 163 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 163
   Envelope <Envlp> [1..1] (External Schema) 163
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
110 March 2024
```

