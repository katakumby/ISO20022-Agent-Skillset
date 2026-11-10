---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.11 CashMovementDetails <CshMvmntDtls>", "8.4.12.11.14 RateAndAmountDetails <RateAndAmtDtls>", "8.4.12.11.14.14 TaxOnIncome <TaxOnIncm>"]
file_pages: [658]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.11.14.14 TaxOnIncome <TaxOnIncm>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 658 to 658.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 658

```text
Definition: Rate at which the income will be withheld by a jurisdiction other than the jurisdiction of the
issuer's country of tax incorporation, for which a relief at source and/or reclaim may be possible. It is
levied in complement or offset of the withholding tax rate (TAXR) levied by the jurisdiction of the issuer's
tax domicile.
SecondLevelTax <ScndLvlTax> contains one of the following elements (see
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
8.4.12.11.14.14  TaxOnIncome <TaxOnIncm>
Presence: [0..1]
Definition: Taxation applied on an amount clearly identified as an income.
TaxOnIncome <TaxOnIncm> contains one of the following elements (see
"RateAndAmountFormat59Choice" on page 1121 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1121
Or}   Amount <Amt> [1..1] Amount C1 1121
8.4.12.11.14.15  TaxOnProfits <TaxOnPrfts>
Presence: [0..1]
Definition: Taxation applied on an amount clearly identified as capital profits, capital gains.
Datatype: "Percentage14Rate" on page 1247
8.4.12.11.14.16  TaxReclaimRate <TaxRclmRate>
Presence: [0..1]
Definition: Percentage of cash that was paid in excess of actual tax obligation and was reclaimed.
Datatype: "Percentage14Rate" on page 1247
8.4.12.11.14.17  EqualisationRate <EqulstnRate>
Presence: [0..1]
Definition: Portion of the fund distribution which represents the average accrued income included in the
purchase price for units bought during the account period.
Impacted by: C1 "ActiveCurrency"
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 658 February 2026
```

