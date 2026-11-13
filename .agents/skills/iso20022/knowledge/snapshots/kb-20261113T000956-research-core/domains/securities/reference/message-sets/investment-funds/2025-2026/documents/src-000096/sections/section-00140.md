---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "13.4 Message Building Blocks", "13.4.3 PreviousReference <PrvsRef>", "13.4.9.14 PriceDetails <PricDtls>", "13.4.9.14.16 TaxRefundDetails <TaxRfndDtls>", "13.4.9.14.16.5 TaxCalculationDetails <TaxClctnDtls>", "13.4.9.14.16.5.5 EUDividendStatus <EUDvddSts>"]
file_pages: [206, 207]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.001.001.05"]
---

# 13.4.9.14.16.5.5 EUDividendStatus <EUDvddSts>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 206 to 207.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 206

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
13.4.9.14.16.5.5  EUDividendStatus <EUDvddSts>
Presence: [0..1]
Definition: Specifies whether dividend is in the scope of the European directive on taxation of savings
income in the form of interest payments (Council Directive 2003/48/EC 3 June), or an income realised
upon sale, a refund or redemption of shares and units, etc.
EUDividendStatus <EUDvddSts> contains one of the following EUDividendStatusType3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 206
Or}   Proprietary <Prtry> [1..1] Text 206
13.4.9.14.16.5.5.1  Code <Cd>
Presence: [1..1]
Definition: EU dividend status expressed as an ISO 20022 code.
Datatype: "EUDividendStatus1Code" on page 5297
CodeName Name Definition
DIVI DividendInScope Dividend is in the scope of the directive.
DIVO DividendOutScope Dividend is out of the scope of the
directive.
UKWN DividendUnknown Unknown whether the dividend is in or
out of the scope of the directive.
13.4.9.14.16.5.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Trade conditions expressed as an extended code.
Datatype: "Max350Text" on page 5403
13.4.9.15  ValuationStatistics <ValtnSttstcs>
Presence: [0..*]
Definition: Information related to the price variations of an investment fund class.
Impacted by: C11 "CurrencyPredefinedPeriodsRule", C12 "CurrencyPriceChangeRule", C13
"CurrencyUserDefinedPeriodsRule"
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 206 May 2026
```

## File page 207

```text
ValuationStatistics <ValtnSttstcs> contains the following ValuationStatistics4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Currency <Ccy> [1..1] CodeSet C3 208
   PriceTypeChangeBasis <PricTpChngBsis> [1..1]  C18 208
     Structured <Strd> [1..1] CodeSet 209
     AdditionalInformation <AddtlInf> [0..1] Text 210
   PriceChange <PricChng> [1..1]  C5, C6 210
     Amount <Amt> [0..1] Amount C3 211
     AmountSign <AmtSgn> [0..1] Indicator 211
     Rate <Rate> [0..1] Rate 211
   Yield <Yld> [0..1] Rate 211
   ByPredefinedTimePeriods <ByPrdfndTmPrds> [0..1]  211
     HighestPriceValue12Months <HghstPricVal12Mnths> [0..1]  212
       Amount <Amt> [1..1] Amount C3 212
     LowestPriceValue12Months <LwstPricVal12Mnths> [0..1]  213
       Amount <Amt> [1..1] Amount C3 213
     OneYearPriceChange <OneYrPricChng> [0..1]  C5, C6 213
       Amount <Amt> [0..1] Amount C3 214
       AmountSign <AmtSgn> [0..1] Indicator 214
       Rate <Rate> [0..1] Rate 214
     ThreeYearPriceChange <ThreeYrPricChng> [0..1]  C5, C6 214
       Amount <Amt> [0..1] Amount C3 215
       AmountSign <AmtSgn> [0..1] Indicator 215
       Rate <Rate> [0..1] Rate 215
     FiveYearPriceChange <FiveYrPricChng> [0..1]  C5, C6 215
       Amount <Amt> [0..1] Amount C3 216
       AmountSign <AmtSgn> [0..1] Indicator 216
       Rate <Rate> [0..1] Rate 216
   ByUserDefinedTimePeriod <ByUsrDfndTmPrd> [0..*]  217
     Period <Prd> [1..1]  217
{Or       Date <Dt> [1..1] ± 217
Or}       DateTime <DtTm> [1..1] ± 218
     HighestPriceValue <HghstPricVal> [0..1]  218
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 207 May 2026
```

