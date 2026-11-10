---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["25 colr.002.001.02 CollateralValueReportV02", "25.4 Message Building Blocks", "25.4.2 ReportOrError <RptOrErr>", "25.4.2.1 BusinessReport <BizRpt>", "25.4.2.1.6 CollateralValueReport <CollValRpt>", "25.4.2.1.6.2 CollateralValue <CollVal>", "25.4.2.1.6.2.4 Securities <Scties>", "25.4.2.1.6.2.4.2 Position <Pos>", "25.4.2.1.6.2.4.2.1 Type <Tp>"]
file_pages: [608]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.002.001.02"]
---

# 25.4.2.1.6.2.4.2.1 Type <Tp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 608 to 608.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 608

```text
Position <Pos> contains the following SecuritiesPosition1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] Text 608
   Quantity <Qty> [1..1]  608
{Or     Quantity <Qty> [1..1] ± 609
Or     Proprietary <Prtry> [1..1]  609
       Identification <Id> [1..1] Text 609
       Issuer <Issr> [1..1] Text 609
       SchemeName <SchmeNm> [0..1] Text 609
       Balance <Bal> [1..1] Quantity 609
Or}     QuantityAndAvailability <QtyAndAvlbty> [1..1]  610
       Quantity <Qty> [1..1] ± 610
       AvailabilityIndicator <AvlbtyInd> [1..1] Indicator 610
25.4.2.1.6.2.4.2.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of a position or a balance, such as earmarked or delivered.
Datatype: "Max4AlphaNumericText" on page 3328
25.4.2.1.6.2.4.2.2  Quantity <Qty>
Presence: [1..1]
Definition: Specifies the quantity of a position or a balance.
Quantity <Qty> contains one of the following SubBalanceQuantity2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 609
Or   Proprietary <Prtry> [1..1]  609
     Identification <Id> [1..1] Text 609
     Issuer <Issr> [1..1] Text 609
     SchemeName <SchmeNm> [0..1] Text 609
     Balance <Bal> [1..1] Quantity 609
Or}   QuantityAndAvailability <QtyAndAvlbty> [1..1]  610
     Quantity <Qty> [1..1] ± 610
     AvailabilityIndicator <AvlbtyInd> [1..1] Indicator 610
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
colr.002.001.02 CollateralValueReportV02
Target2-Securities 608 August 2026
```

