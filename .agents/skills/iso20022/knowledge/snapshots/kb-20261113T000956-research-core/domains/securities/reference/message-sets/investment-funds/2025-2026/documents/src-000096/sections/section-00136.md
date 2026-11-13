---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "13.4 Message Building Blocks", "13.4.3 PreviousReference <PrvsRef>", "13.4.9.14 PriceDetails <PricDtls>", "13.4.9.14.16 TaxRefundDetails <TaxRfndDtls>", "13.4.9.14.16.1 Type <Tp>"]
file_pages: [202]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.001.001.05"]
---

# 13.4.9.14.16.1 Type <Tp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 202 to 202.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 202

```text
TaxRefundDetails <TaxRfndDtls> contains the following Tax43 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  202
{Or     Code <Cd> [1..1] CodeSet 202
Or}     Proprietary <Prtry> [1..1] Text 203
   Amount <Amt> [0..7] Amount C3 203
   Rate <Rate> [0..1] Rate 203
   Country <Ctry> [1..1] CodeSet C9 204
   TaxCalculationDetails <TaxClctnDtls> [0..1]  204
     EUCapitalGain <EUCptlGn> [0..1]  204
{Or       Code <Cd> [1..1] CodeSet 205
Or}       Proprietary <Prtry> [1..1] Text 205
     PercentageOfDebtClaim <PctgOfDebtClm> [0..1] Rate 205
     PercentageGrandfatheredDebt <PctgGrdfthdDebt> [0..1] Rate 205
     TaxableIncomePerDividend <TaxblIncmPerDvdd> [0..1] Amount C3 205
     EUDividendStatus <EUDvddSts> [0..1]  206
{Or       Code <Cd> [1..1] CodeSet 206
Or}       Proprietary <Prtry> [1..1] Text 206
Constraints
• AmountAndOrRateRule
If Amount is not present, then Rate is mandatory. If Amount is present, then Rate is optional.
13.4.9.14.16.1  Type <Tp>
Presence: [1..1]
Definition: Type of tax applied.
Type <Tp> contains one of the following TaxType4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 202
Or}   Proprietary <Prtry> [1..1] Text 203
13.4.9.14.16.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of tax expressed as a code.
Datatype: "TaxType12Code" on page 5374
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 202 May 2026
```

