---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["25 colr.002.001.02 CollateralValueReportV02", "25.4 Message Building Blocks", "25.4.2 ReportOrError <RptOrErr>", "25.4.2.1 BusinessReport <BizRpt>", "25.4.2.1.6 CollateralValueReport <CollValRpt>", "25.4.2.1.6.2 CollateralValue <CollVal>", "25.4.2.1.6.2.4 Securities <Scties>", "25.4.2.1.6.2.4.2 Position <Pos>", "25.4.2.1.6.2.4.2.2 Quantity <Qty>", "25.4.2.1.6.2.4.2.2.3 QuantityAndAvailability <QtyAndAvlbty>"]
file_pages: [610]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.002.001.02"]
---

# 25.4.2.1.6.2.4.2.2.3 QuantityAndAvailability <QtyAndAvlbty>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 610 to 610.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 610

```text
Datatype: "Number" on page 3324
25.4.2.1.6.2.4.2.2.3  QuantityAndAvailability <QtyAndAvlbty>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance and whether the balance is available.
QuantityAndAvailability <QtyAndAvlbty> contains the following QuantityAndAvailability1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity <Qty> [1..1] ± 610
   AvailabilityIndicator <AvlbtyInd> [1..1] Indicator 610
25.4.2.1.6.2.4.2.2.3.1  Quantity <Qty>
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
25.4.2.1.6.2.4.2.2.3.2  AvailabilityIndicator <AvlbtyInd>
Presence: [1..1]
Definition: Indicates whether the quantity of securities on the sub-balance is available.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
25.4.2.1.6.2.4.3  ValuationPrice <ValtnPric>
Presence: [1..1]
Definition: Specifies the price of the security for valuation purposes.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
colr.002.001.02 CollateralValueReportV02
Target2-Securities 610 August 2026
```

