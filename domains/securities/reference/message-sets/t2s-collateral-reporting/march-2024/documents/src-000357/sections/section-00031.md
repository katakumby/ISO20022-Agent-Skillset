---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 colr.002.001.02 CollateralValueReportV02", "3.4 Message Building Blocks", "3.4.2 ReportOrError <RptOrErr>", "3.4.2.1 BusinessReport <BizRpt>", "3.4.2.1.6 CollateralValueReport <CollValRpt>", "3.4.2.1.6.2 CollateralValue <CollVal>", "3.4.2.1.6.2.4 Securities <Scties>", "3.4.2.1.6.2.4.2 Position <Pos>", "3.4.2.1.6.2.4.2.2 Quantity <Qty>", "3.4.2.1.6.2.4.2.2.1 Quantity <Qty>"]
file_pages: [35]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.002.001.02"]
---

# 3.4.2.1.6.2.4.2.2.1 Quantity <Qty>

Source: [src-000357](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 35 to 35.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 35

```text
3.4.2.1.6.2.4.2.2.1  Quantity <Qty>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance.
Quantity <Qty> contains one of the following elements (see "FinancialInstrumentQuantity1Choice" on
page 54 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 55
Or   FaceAmount <FaceAmt> [1..1] Amount 55
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 55
3.4.2.1.6.2.4.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance.
Proprietary <Prtry> contains the following GenericIdentification15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 35
   Issuer <Issr> [1..1] Text 35
   SchemeName <SchmeNm> [0..1] Text 35
   Balance <Bal> [1..1] Quantity 35
3.4.2.1.6.2.4.2.2.2.1  Identification <Id>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: "Max4AlphaNumericText" on page 83
3.4.2.1.6.2.4.2.2.2.2  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 83
3.4.2.1.6.2.4.2.2.2.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Datatype: "Max35Text" on page 83
3.4.2.1.6.2.4.2.2.2.4  Balance <Bal>
Presence: [1..1]
Definition: Value of the balance.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
colr.002.001.02 CollateralValueReportV02
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
35 March 2024
```

