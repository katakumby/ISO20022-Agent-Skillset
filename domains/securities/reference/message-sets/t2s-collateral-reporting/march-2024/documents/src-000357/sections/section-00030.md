---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 colr.002.001.02 CollateralValueReportV02", "3.4 Message Building Blocks", "3.4.2 ReportOrError <RptOrErr>", "3.4.2.1 BusinessReport <BizRpt>", "3.4.2.1.6 CollateralValueReport <CollValRpt>", "3.4.2.1.6.2 CollateralValue <CollVal>", "3.4.2.1.6.2.4 Securities <Scties>", "3.4.2.1.6.2.4.2 Position <Pos>", "3.4.2.1.6.2.4.2.1 Type <Tp>"]
file_pages: [34]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.002.001.02"]
---

# 3.4.2.1.6.2.4.2.1 Type <Tp>

Source: [src-000357](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 34 to 34.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 34

```text
Position <Pos> contains the following SecuritiesPosition1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] Text 34
   Quantity <Qty> [1..1]  34
{Or     Quantity <Qty> [1..1] ± 35
Or     Proprietary <Prtry> [1..1]  35
       Identification <Id> [1..1] Text 35
       Issuer <Issr> [1..1] Text 35
       SchemeName <SchmeNm> [0..1] Text 35
       Balance <Bal> [1..1] Quantity 35
Or}     QuantityAndAvailability <QtyAndAvlbty> [1..1]  36
       Quantity <Qty> [1..1] ± 36
       AvailabilityIndicator <AvlbtyInd> [1..1] Indicator 36
3.4.2.1.6.2.4.2.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of a position or a balance, such as earmarked or delivered.
Datatype: "Max4AlphaNumericText" on page 83
3.4.2.1.6.2.4.2.2  Quantity <Qty>
Presence: [1..1]
Definition: Specifies the quantity of a position or a balance.
Quantity <Qty> contains one of the following SubBalanceQuantity2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 35
Or   Proprietary <Prtry> [1..1]  35
     Identification <Id> [1..1] Text 35
     Issuer <Issr> [1..1] Text 35
     SchemeName <SchmeNm> [0..1] Text 35
     Balance <Bal> [1..1] Quantity 35
Or}   QuantityAndAvailability <QtyAndAvlbty> [1..1]  36
     Quantity <Qty> [1..1] ± 36
     AvailabilityIndicator <AvlbtyInd> [1..1] Indicator 36
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
colr.002.001.02 CollateralValueReportV02
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
34 March 2024
```

