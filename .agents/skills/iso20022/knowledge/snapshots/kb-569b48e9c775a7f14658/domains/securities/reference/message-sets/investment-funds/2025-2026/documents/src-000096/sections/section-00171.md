---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.10 CancelledPriceValuationDetails <CancPricValtnDtls>", "14.4.10.1 PriceValuationDetails <PricValtnDtls>", "14.4.10.1.12 OfficialValuationIndicator <OffclValtnInd>"]
file_pages: [255, 256, 257]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.10.1.12 OfficialValuationIndicator <OffclValtnInd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 255 to 257.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 255

```text
CodeName Name Definition
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
14.4.10.1.12  OfficialValuationIndicator <OffclValtnInd>
Presence: [1..1]
Definition: Indicates whether the valuation is an official valuation.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
14.4.10.1.13  SuspendedIndicator <SspdInd>
Presence: [1..1]
Definition: Indicates whether the valuation of the investment fund class is suspended.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
14.4.10.1.14  PriceDetails <PricDtls>
Presence: [0..*]
Definition: Amount of money for which goods or services are offered, sold, or bought.
Impacted by: C8 "CalculationBasisRule"
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 255 May 2026
```

## File page 256

```text
PriceDetails <PricDtls> contains the following UnitPrice24 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PriceType <PricTp> [1..1]  C18 258
{Or     Code <Cd> [1..1] CodeSet 258
Or}     Proprietary <Prtry> [1..1] Text 259
   PriceMethod <PricMtd> [0..1] CodeSet 259
   ValueInInvestmentCurrency <ValInInvstmtCcy> [1..*] ± 260
   ValueInAlternativeCurrency <ValInAltrntvCcy> [0..*] ± 260
   ForExecutionIndicator <ForExctnInd> [1..1] Indicator 260
   CumDividendIndicator <CumDvddInd> [1..1] Indicator 260
   CalculationBasis <ClctnBsis> [0..1] Rate 260
   EstimatedPriceIndicator <EstmtdPricInd> [1..1] Indicator 261
   NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity 261
   TaxableIncomePerShare <TaxblIncmPerShr> [0..1] Amount C3 261
   TaxableIncomePerShareCalculated
<TaxblIncmPerShrClctd>
[0..1]  261
{Or     Code <Cd> [1..1] CodeSet 261
Or}     Proprietary <Prtry> [1..1] Text 262
   TaxableIncomePerDividend <TaxblIncmPerDvdd> [0..1] Amount C3 262
   EUDividendStatus <EUDvddSts> [0..1]  262
{Or     Code <Cd> [1..1] CodeSet 262
Or}     Proprietary <Prtry> [1..1] Text 263
   ChargeDetails <ChrgDtls> [0..*]  263
     Type <Tp> [1..1]  263
{Or       Code <Cd> [1..1] CodeSet 263
Or}       Proprietary <Prtry> [1..1] Text 264
     ChargesFees <ChrgsFees> [1..1] ± 264
     CalculationBasis <ClctnBsis> [0..1]  264
{Or       Code <Cd> [1..1] CodeSet 265
Or}       Proprietary <Prtry> [1..1] Text 265
   TaxLiabilityDetails <TaxLbltyDtls> [0..*]  C4 265
     Type <Tp> [1..1]  266
{Or       Code <Cd> [1..1] CodeSet 266
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 256 May 2026
```

## File page 257

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}       Proprietary <Prtry> [1..1] Text 267
     Amount <Amt> [0..7] Amount C3 267
     Rate <Rate> [0..1] Rate 267
     Country <Ctry> [1..1] CodeSet C11 268
     TaxCalculationDetails <TaxClctnDtls> [0..1]  268
       EUCapitalGain <EUCptlGn> [0..1]  268
{Or         Code <Cd> [1..1] CodeSet 269
Or}         Proprietary <Prtry> [1..1] Text 269
       PercentageOfDebtClaim <PctgOfDebtClm> [0..1] Rate 269
       PercentageGrandfatheredDebt <PctgGrdfthdDebt> [0..1] Rate 269
       TaxableIncomePerDividend <TaxblIncmPerDvdd> [0..1] Amount C3 269
       EUDividendStatus <EUDvddSts> [0..1]  270
{Or         Code <Cd> [1..1] CodeSet 270
Or}         Proprietary <Prtry> [1..1] Text 270
   TaxRefundDetails <TaxRfndDtls> [0..*]  C4 270
     Type <Tp> [1..1]  271
{Or       Code <Cd> [1..1] CodeSet 271
Or}       Proprietary <Prtry> [1..1] Text 272
     Amount <Amt> [0..7] Amount C3 272
     Rate <Rate> [0..1] Rate 272
     Country <Ctry> [1..1] CodeSet C11 273
     TaxCalculationDetails <TaxClctnDtls> [0..1]  273
       EUCapitalGain <EUCptlGn> [0..1]  273
{Or         Code <Cd> [1..1] CodeSet 274
Or}         Proprietary <Prtry> [1..1] Text 274
       PercentageOfDebtClaim <PctgOfDebtClm> [0..1] Rate 274
       PercentageGrandfatheredDebt <PctgGrdfthdDebt> [0..1] Rate 274
       TaxableIncomePerDividend <TaxblIncmPerDvdd> [0..1] Amount C3 274
       EUDividendStatus <EUDvddSts> [0..1]  275
{Or         Code <Cd> [1..1] CodeSet 275
Or}         Proprietary <Prtry> [1..1] Text 275
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 257 May 2026
```

