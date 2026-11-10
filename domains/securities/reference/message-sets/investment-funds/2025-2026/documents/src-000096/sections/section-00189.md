---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.10 CancelledPriceValuationDetails <CancPricValtnDtls>", "14.4.10.1 PriceValuationDetails <PricValtnDtls>", "14.4.10.1.14 PriceDetails <PricDtls>", "14.4.10.1.14.16 TaxRefundDetails <TaxRfndDtls>", "14.4.10.1.14.16.5 TaxCalculationDetails <TaxClctnDtls>", "14.4.10.1.14.16.5.5 EUDividendStatus <EUDvddSts>"]
file_pages: [275, 276]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.10.1.14.16.5.5 EUDividendStatus <EUDvddSts>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 275 to 276.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 275

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
14.4.10.1.14.16.5.5  EUDividendStatus <EUDvddSts>
Presence: [0..1]
Definition: Specifies whether dividend is in the scope of the European directive on taxation of savings
income in the form of interest payments (Council Directive 2003/48/EC 3 June), or an income realised
upon sale, a refund or redemption of shares and units, etc.
EUDividendStatus <EUDvddSts> contains one of the following EUDividendStatusType3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 275
Or}   Proprietary <Prtry> [1..1] Text 275
14.4.10.1.14.16.5.5.1  Code <Cd>
Presence: [1..1]
Definition: EU dividend status expressed as an ISO 20022 code.
Datatype: "EUDividendStatus1Code" on page 5297
CodeName Name Definition
DIVI DividendInScope Dividend is in the scope of the directive.
DIVO DividendOutScope Dividend is out of the scope of the
directive.
UKWN DividendUnknown Unknown whether the dividend is in or
out of the scope of the directive.
14.4.10.1.14.16.5.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Trade conditions expressed as an extended code.
Datatype: "Max350Text" on page 5403
14.4.10.1.15  ValuationStatistics <ValtnSttstcs>
Presence: [0..*]
Definition: Information related to the price variations of an investment fund class.
Impacted by: C13 "CurrencyPredefinedPeriodsRule", C14 "CurrencyPriceChangeRule", C15
"CurrencyUserDefinedPeriodsRule"
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 275 May 2026
```

## File page 276

```text
ValuationStatistics <ValtnSttstcs> contains the following ValuationStatistics4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Currency <Ccy> [1..1] CodeSet C3 277
   PriceTypeChangeBasis <PricTpChngBsis> [1..1]  C19 277
     Structured <Strd> [1..1] CodeSet 278
     AdditionalInformation <AddtlInf> [0..1] Text 279
   PriceChange <PricChng> [1..1]  C5, C6 279
     Amount <Amt> [0..1] Amount C3 280
     AmountSign <AmtSgn> [0..1] Indicator 280
     Rate <Rate> [0..1] Rate 280
   Yield <Yld> [0..1] Rate 280
   ByPredefinedTimePeriods <ByPrdfndTmPrds> [0..1]  280
     HighestPriceValue12Months <HghstPricVal12Mnths> [0..1]  281
       Amount <Amt> [1..1] Amount C3 281
     LowestPriceValue12Months <LwstPricVal12Mnths> [0..1]  282
       Amount <Amt> [1..1] Amount C3 282
     OneYearPriceChange <OneYrPricChng> [0..1]  C5, C6 282
       Amount <Amt> [0..1] Amount C3 283
       AmountSign <AmtSgn> [0..1] Indicator 283
       Rate <Rate> [0..1] Rate 283
     ThreeYearPriceChange <ThreeYrPricChng> [0..1]  C5, C6 283
       Amount <Amt> [0..1] Amount C3 284
       AmountSign <AmtSgn> [0..1] Indicator 284
       Rate <Rate> [0..1] Rate 284
     FiveYearPriceChange <FiveYrPricChng> [0..1]  C5, C6 284
       Amount <Amt> [0..1] Amount C3 285
       AmountSign <AmtSgn> [0..1] Indicator 285
       Rate <Rate> [0..1] Rate 285
   ByUserDefinedTimePeriod <ByUsrDfndTmPrd> [0..*]  286
     Period <Prd> [1..1]  286
{Or       Date <Dt> [1..1] ± 286
Or}       DateTime <DtTm> [1..1] ± 287
     HighestPriceValue <HghstPricVal> [0..1]  287
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 276 May 2026
```

