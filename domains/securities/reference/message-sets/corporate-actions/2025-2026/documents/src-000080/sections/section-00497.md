---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.11 CashMovementDetails <CshMvmntDtls>", "8.4.12.11.14 RateAndAmountDetails <RateAndAmtDtls>", "8.4.12.11.14.11 TaxCreditRate <TaxCdtRate>"]
file_pages: [657]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.11.14.11 TaxCreditRate <TaxCdtRate>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 657 to 657.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 657

```text
SolicitationFeeRate <SlctnFeeRate> contains one of the following elements (see
"SolicitationFeeRateFormat12Choice" on page 1105 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1105
Or   AmountToQuantity <AmtToQty> [1..1]  1105
     Amount <Amt> [1..1] Amount C1 1106
     Quantity <Qty> [1..1] Quantity 1106
Or}   Amount <Amt> [1..1] Amount C1 1106
8.4.12.11.14.11  TaxCreditRate <TaxCdtRate>
Presence: [0..1]
Definition: Amount of money per equity allocated as the result of a tax credit.
TaxCreditRate <TaxCdtRate> contains one of the following elements (see "RateFormat27Choice" on
page 1106 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1106
Or}   Amount <Amt> [1..1] Amount C1 1107
8.4.12.11.14.12  WithholdingTaxRate <WhldgTaxRate>
Presence: [0..*]
Definition: Percentage of a cash distribution that will be withheld by the tax authorities of the jurisdiction
of the issuer, for which a relief at source and/or reclaim may be possible.
WithholdingTaxRate <WhldgTaxRate> contains one of the following elements (see
"RateAndAmountFormat55Choice" on page 1124 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1124
Or   Amount <Amt> [1..1] Amount C1 1124
Or}   RateTypeAndRate <RateTpAndRate> [1..1]  1124
     RateType <RateTp> [1..1]  1125
{Or       Code <Cd> [1..1] CodeSet 1125
Or}       Proprietary <Prtry> [1..1] ± 1125
     Rate <Rate> [1..1] Rate 1126
8.4.12.11.14.13  SecondLevelTax <ScndLvlTax>
Presence: [0..*]
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 657 February 2026
```

