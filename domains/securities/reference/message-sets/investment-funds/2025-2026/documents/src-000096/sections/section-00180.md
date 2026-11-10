---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.10 CancelledPriceValuationDetails <CancPricValtnDtls>", "14.4.10.1 PriceValuationDetails <PricValtnDtls>", "14.4.10.1.14 PriceDetails <PricDtls>", "14.4.10.1.14.15 TaxLiabilityDetails <TaxLbltyDtls>", "14.4.10.1.14.15.1 Type <Tp>"]
file_pages: [266]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.10.1.14.15.1 Type <Tp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 266 to 266.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 266

```text
TaxLiabilityDetails <TaxLbltyDtls> contains the following Tax43 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  266
{Or     Code <Cd> [1..1] CodeSet 266
Or}     Proprietary <Prtry> [1..1] Text 267
   Amount <Amt> [0..7] Amount C3 267
   Rate <Rate> [0..1] Rate 267
   Country <Ctry> [1..1] CodeSet C11 268
   TaxCalculationDetails <TaxClctnDtls> [0..1]  268
     EUCapitalGain <EUCptlGn> [0..1]  268
{Or       Code <Cd> [1..1] CodeSet 269
Or}       Proprietary <Prtry> [1..1] Text 269
     PercentageOfDebtClaim <PctgOfDebtClm> [0..1] Rate 269
     PercentageGrandfatheredDebt <PctgGrdfthdDebt> [0..1] Rate 269
     TaxableIncomePerDividend <TaxblIncmPerDvdd> [0..1] Amount C3 269
     EUDividendStatus <EUDvddSts> [0..1]  270
{Or       Code <Cd> [1..1] CodeSet 270
Or}       Proprietary <Prtry> [1..1] Text 270
Constraints
• AmountAndOrRateRule
If Amount is not present, then Rate is mandatory. If Amount is present, then Rate is optional.
14.4.10.1.14.15.1  Type <Tp>
Presence: [1..1]
Definition: Type of tax applied.
Type <Tp> contains one of the following TaxType4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 266
Or}   Proprietary <Prtry> [1..1] Text 267
14.4.10.1.14.15.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of tax expressed as a code.
Datatype: "TaxType12Code" on page 5374
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 266 May 2026
```

