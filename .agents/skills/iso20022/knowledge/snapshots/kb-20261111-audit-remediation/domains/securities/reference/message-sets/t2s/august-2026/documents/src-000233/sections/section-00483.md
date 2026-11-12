---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["25 colr.002.001.02 CollateralValueReportV02", "25.4 Message Building Blocks", "25.4.2 ReportOrError <RptOrErr>", "25.4.2.1 BusinessReport <BizRpt>", "25.4.2.1.6 CollateralValueReport <CollValRpt>", "25.4.2.1.6.2 CollateralValue <CollVal>", "25.4.2.1.6.2.4 Securities <Scties>", "25.4.2.1.6.2.4.2 Position <Pos>", "25.4.2.1.6.2.4.2.2 Quantity <Qty>", "25.4.2.1.6.2.4.2.2.1 Quantity <Qty>"]
file_pages: [609]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.002.001.02"]
---

# 25.4.2.1.6.2.4.2.2.1 Quantity <Qty>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 609 to 609.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 609

```text
25.4.2.1.6.2.4.2.2.1  Quantity <Qty>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance.
Quantity <Qty> contains one of the following elements (see "FinancialInstrumentQuantity1Choice" on
page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
25.4.2.1.6.2.4.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance.
Proprietary <Prtry> contains the following GenericIdentification15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 609
   Issuer <Issr> [1..1] Text 609
   SchemeName <SchmeNm> [0..1] Text 609
   Balance <Bal> [1..1] Quantity 609
25.4.2.1.6.2.4.2.2.2.1  Identification <Id>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: "Max4AlphaNumericText" on page 3328
25.4.2.1.6.2.4.2.2.2.2  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 3328
25.4.2.1.6.2.4.2.2.2.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Datatype: "Max35Text" on page 3328
25.4.2.1.6.2.4.2.2.2.4  Balance <Bal>
Presence: [1..1]
Definition: Value of the balance.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
colr.002.001.02 CollateralValueReportV02
Target2-Securities 609 August 2026
```

