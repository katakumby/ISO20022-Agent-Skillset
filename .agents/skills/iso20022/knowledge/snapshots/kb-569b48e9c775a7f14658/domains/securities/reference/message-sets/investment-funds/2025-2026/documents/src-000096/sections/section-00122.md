---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "13.4 Message Building Blocks", "13.4.3 PreviousReference <PrvsRef>", "13.4.9.12 OfficialValuationIndicator <OffclValtnInd>"]
file_pages: [186, 187, 188]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.001.001.05"]
---

# 13.4.9.12 OfficialValuationIndicator <OffclValtnInd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 186 to 188.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 186

```text
CodeName Name Definition
YEAR Annual Event takes place every year or once a
year.
SEMI SemiAnnual Event takes place every six months or
two times a year.
QUTR Quarterly Event takes place every three months or
four times a year.
TOMN EveryTwoMonths Event takes place every two months.
MNTH Monthly Event takes place every month or once a
month.
TWMN TwiceAMonth Event takes place two times a month.
TOWK EveryTwoWeeks Event takes place every two weeks.
WEEK Weekly Event takes place once a week.
DAIL Daily Event takes place every day.
ADHO Adhoc Event takes place as necessary.
INDA IntraDay Event takes place several times a day.
OVNG Overnight Event takes place overnight.
ONDE OnDemand Event takes place on demand.
13.4.9.12  OfficialValuationIndicator <OffclValtnInd>
Presence: [1..1]
Definition: Indicates whether the valuation is an official valuation.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
13.4.9.13  SuspendedIndicator <SspdInd>
Presence: [1..1]
Definition: Indicates whether the valuation of the investment fund class is suspended.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
13.4.9.14  PriceDetails <PricDtls>
Presence: [0..*]
Definition: Amount of money for which goods or services are offered, sold, or bought.
Impacted by: C8 "CalculationBasisRule"
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 186 May 2026
```

## File page 187

```text
PriceDetails <PricDtls> contains the following UnitPrice24 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PriceType <PricTp> [1..1]  C17 189
{Or     Code <Cd> [1..1] CodeSet 189
Or}     Proprietary <Prtry> [1..1] Text 190
   PriceMethod <PricMtd> [0..1] CodeSet 190
   ValueInInvestmentCurrency <ValInInvstmtCcy> [1..*] ± 191
   ValueInAlternativeCurrency <ValInAltrntvCcy> [0..*] ± 191
   ForExecutionIndicator <ForExctnInd> [1..1] Indicator 191
   CumDividendIndicator <CumDvddInd> [1..1] Indicator 191
   CalculationBasis <ClctnBsis> [0..1] Rate 191
   EstimatedPriceIndicator <EstmtdPricInd> [1..1] Indicator 192
   NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity 192
   TaxableIncomePerShare <TaxblIncmPerShr> [0..1] Amount C3 192
   TaxableIncomePerShareCalculated
<TaxblIncmPerShrClctd>
[0..1]  192
{Or     Code <Cd> [1..1] CodeSet 193
Or}     Proprietary <Prtry> [1..1] Text 193
   TaxableIncomePerDividend <TaxblIncmPerDvdd> [0..1] Amount C3 193
   EUDividendStatus <EUDvddSts> [0..1]  193
{Or     Code <Cd> [1..1] CodeSet 194
Or}     Proprietary <Prtry> [1..1] Text 194
   ChargeDetails <ChrgDtls> [0..*]  194
     Type <Tp> [1..1]  194
{Or       Code <Cd> [1..1] CodeSet 195
Or}       Proprietary <Prtry> [1..1] Text 195
     ChargesFees <ChrgsFees> [1..1] ± 195
     CalculationBasis <ClctnBsis> [0..1]  196
{Or       Code <Cd> [1..1] CodeSet 196
Or}       Proprietary <Prtry> [1..1] Text 196
   TaxLiabilityDetails <TaxLbltyDtls> [0..*]  C4 196
     Type <Tp> [1..1]  197
{Or       Code <Cd> [1..1] CodeSet 197
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 187 May 2026
```

## File page 188

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}       Proprietary <Prtry> [1..1] Text 198
     Amount <Amt> [0..7] Amount C3 198
     Rate <Rate> [0..1] Rate 198
     Country <Ctry> [1..1] CodeSet C9 199
     TaxCalculationDetails <TaxClctnDtls> [0..1]  199
       EUCapitalGain <EUCptlGn> [0..1]  199
{Or         Code <Cd> [1..1] CodeSet 200
Or}         Proprietary <Prtry> [1..1] Text 200
       PercentageOfDebtClaim <PctgOfDebtClm> [0..1] Rate 200
       PercentageGrandfatheredDebt <PctgGrdfthdDebt> [0..1] Rate 200
       TaxableIncomePerDividend <TaxblIncmPerDvdd> [0..1] Amount C3 200
       EUDividendStatus <EUDvddSts> [0..1]  201
{Or         Code <Cd> [1..1] CodeSet 201
Or}         Proprietary <Prtry> [1..1] Text 201
   TaxRefundDetails <TaxRfndDtls> [0..*]  C4 201
     Type <Tp> [1..1]  202
{Or       Code <Cd> [1..1] CodeSet 202
Or}       Proprietary <Prtry> [1..1] Text 203
     Amount <Amt> [0..7] Amount C3 203
     Rate <Rate> [0..1] Rate 203
     Country <Ctry> [1..1] CodeSet C9 204
     TaxCalculationDetails <TaxClctnDtls> [0..1]  204
       EUCapitalGain <EUCptlGn> [0..1]  204
{Or         Code <Cd> [1..1] CodeSet 205
Or}         Proprietary <Prtry> [1..1] Text 205
       PercentageOfDebtClaim <PctgOfDebtClm> [0..1] Rate 205
       PercentageGrandfatheredDebt <PctgGrdfthdDebt> [0..1] Rate 205
       TaxableIncomePerDividend <TaxblIncmPerDvdd> [0..1] Amount C3 205
       EUDividendStatus <EUDvddSts> [0..1]  206
{Or         Code <Cd> [1..1] CodeSet 206
Or}         Proprietary <Prtry> [1..1] Text 206
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 188 May 2026
```

