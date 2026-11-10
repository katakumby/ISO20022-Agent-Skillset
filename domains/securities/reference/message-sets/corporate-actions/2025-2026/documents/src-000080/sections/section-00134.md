---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.24 SecuritiesMovementDetails <SctiesMvmntDtls>", "3.4.11.24.17 RateDetails <RateDtls>", "3.4.11.24.17.4 TransformationRate <TrfrmatnRate>"]
file_pages: [193]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.24.17.4 TransformationRate <TrfrmatnRate>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 193 to 193.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 193

```text
NewToOld <NewToOd> contains one of the following elements (see "RatioFormat18Choice" on
page 932 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   QuantityToQuantity <QtyToQty> [1..1] ± 932
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 933
Or   AmountToAmount <AmtToAmt> [1..1]  933
     Amount1 <Amt1> [1..1] Amount C1 933
     Amount2 <Amt2> [1..1] Amount C1 933
Or   AmountToQuantity <AmtToQty> [1..1]  934
     Amount <Amt> [1..1] Amount C1 934
     Quantity <Qty> [1..1] Quantity 934
Or}   QuantityToAmount <QtyToAmt> [1..1]  934
     Amount <Amt> [1..1] Amount C1 934
     Quantity <Qty> [1..1] Quantity 935
3.4.11.24.17.4  TransformationRate <TrfrmatnRate>
Presence: [0..1]
Definition: Rate used to determine the cash consideration split across outturn settlement transactions
that are the result of a transformation of the parent transaction.
Datatype: "Percentage14Rate" on page 1247
3.4.11.24.17.5  ChargesFees <ChrgsFees>
Presence: [0..1]
Definition: Rate used to calculate the amount of the charges/fees that cannot be categorised.
ChargesFees <ChrgsFees> contains one of the following elements (see
"RateAndAmountFormat57Choice" on page 1123 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1123
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1123
Or}   Amount <Amt> [1..1] Amount C1 1123
3.4.11.24.17.6  FiscalStamp <FsclStmp>
Presence: [0..1]
Definition: Percentage of fiscal tax to apply.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 193 February 2026
```

