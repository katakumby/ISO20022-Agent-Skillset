---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.25 CashMovementDetails <CshMvmntDtls>", "3.4.11.25.14 RateAndAmountDetails <RateAndAmtDtls>", "3.4.11.25.14.13 TaxCreditRate <TaxCdtRate>"]
file_pages: [241]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.25.14.13 TaxCreditRate <TaxCdtRate>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 241 to 241.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 241

```text
SolicitationFeeRate <SlctnFeeRate> contains one of the following elements (see
"SolicitationFeeRateFormat11Choice" on page 1024 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1024
Or   AmountToQuantity <AmtToQty> [1..1]  1025
     Amount <Amt> [1..1] Amount C1 1025
     Quantity <Qty> [1..1] Quantity 1025
Or   Amount <Amt> [1..1] Amount C1 1025
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1026
3.4.11.25.14.13  TaxCreditRate <TaxCdtRate>
Presence: [0..1]
Definition: Amount of money per equity allocated as the result of a tax credit.
TaxCreditRate <TaxCdtRate> contains one of the following elements (see "RateFormat26Choice" on
page 1120 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1120
Or   Amount <Amt> [1..1] Amount C1 1120
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1120
3.4.11.25.14.14  TaxOnIncome <TaxOnIncm>
Presence: [0..1]
Definition: Overall tax withheld at source by fund managers prior to considering the tax obligation of
each unit holder.
TaxOnIncome <TaxOnIncm> contains one of the following elements (see
"RateAndAmountFormat57Choice" on page 1123 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1123
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1123
Or}   Amount <Amt> [1..1] Amount C1 1123
3.4.11.25.14.15  TaxOnProfits <TaxOnPrfts>
Presence: [0..1]
Definition: Taxation applied on an amount clearly identified as capital profits, capital gains.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 241 February 2026
```

