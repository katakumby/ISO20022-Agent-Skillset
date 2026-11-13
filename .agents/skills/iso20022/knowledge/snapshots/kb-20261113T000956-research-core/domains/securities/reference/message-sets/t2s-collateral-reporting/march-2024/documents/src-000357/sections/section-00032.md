---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 colr.002.001.02 CollateralValueReportV02", "3.4 Message Building Blocks", "3.4.2 ReportOrError <RptOrErr>", "3.4.2.1 BusinessReport <BizRpt>", "3.4.2.1.6 CollateralValueReport <CollValRpt>", "3.4.2.1.6.2 CollateralValue <CollVal>", "3.4.2.1.6.2.4 Securities <Scties>", "3.4.2.1.6.2.4.2 Position <Pos>", "3.4.2.1.6.2.4.2.2 Quantity <Qty>", "3.4.2.1.6.2.4.2.2.3 QuantityAndAvailability <QtyAndAvlbty>"]
file_pages: [36]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.002.001.02"]
---

# 3.4.2.1.6.2.4.2.2.3 QuantityAndAvailability <QtyAndAvlbty>

Source: [src-000357](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 36 to 36.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 36

```text
Datatype: "Number" on page 81
3.4.2.1.6.2.4.2.2.3  QuantityAndAvailability <QtyAndAvlbty>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance and whether the balance is available.
QuantityAndAvailability <QtyAndAvlbty> contains the following QuantityAndAvailability1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity <Qty> [1..1] ± 36
   AvailabilityIndicator <AvlbtyInd> [1..1] Indicator 36
3.4.2.1.6.2.4.2.2.3.1  Quantity <Qty>
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
3.4.2.1.6.2.4.2.2.3.2  AvailabilityIndicator <AvlbtyInd>
Presence: [1..1]
Definition: Indicates whether the quantity of securities on the sub-balance is available.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 81):
• Meaning When True: Yes
• Meaning When False: No
3.4.2.1.6.2.4.3  ValuationPrice <ValtnPric>
Presence: [1..1]
Definition: Specifies the price of the security for valuation purposes.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
colr.002.001.02 CollateralValueReportV02
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
36 March 2024
```

