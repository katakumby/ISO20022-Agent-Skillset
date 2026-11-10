---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "13.3 Constraints"]
file_pages: [166, 167]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.001.001.05"]
---

# 13.3 Constraints

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 166 to 167.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 166

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           Rate <Rate> [0..1] Rate 220
         Yield <Yld> [0..1] Rate 220
     PerformanceDetails <PrfrmncDtls> [0..1]  C1 220
       CorporateActionFactor <CorpActnFctr> [0..1] Quantity 220
       CumulativeCorporateActionFactor <CmltvCorpActnFctr> [0..1] Quantity 221
       AccumulationPeriod <AcmltnPrd> [0..1] ± 221
       NormalPerformance <NrmlPrfrmnc> [0..1] Quantity 221
   Extension <Xtnsn> [0..*] ± C14 0
13.3 Constraints
C1 AccumulationPeriodRule
AccumulationPeriod must be present if CumulativeCorporateActionFactor is present.
C2 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C3 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C4 AmountAndOrRateRule
If Amount is not present, then Rate is mandatory. If Amount is present, then Rate is optional.
C5 AmountAndOrRateRule
If Amount is not present, then Rate is mandatory. If Amount is present, then Rate is optional.
C6 AmountSignRule
If Amount is present, then AmountSign is optional. If Amount is not present, then AmountSign is
not allowed.
C7 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C8 CalculationBasisRule
If Type is not NonAdjustedUnpublished, then CalculationBasis is not allowed. If Type is
NonAdjustedUnpublished, then CalculationBasis may be present.
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 166 May 2026
```

## File page 167

```text
C9 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C10 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C11 CurrencyPredefinedPeriodsRule
Currency in ByPredefinedTimePeriods/HighestPriceValue12Months/Amount,
ByPredefinedTimePeriods/LowestPriceValue12Months/Amount, ByPredefinedTimePeriods/
OneYearPriceChange/Amount, ByPredefinedTimePeriods/ThreeYearPriceChange/Amount and
ByPredefinedTimePeriods/FiveYearPriceChange/Amount must be the same as Currency.
C12 CurrencyPriceChangeRule
Currency in PriceChange/Amount must be the same as Currency.
C13 CurrencyUserDefinedPeriodsRule
Currency in ByUserDefinedTimePeriod/HighestPriceValue/Amount, ByUserDefinedTimePeriod/
LowestPriceValue/Amount and ByUserDefinedTimePeriod/PriceChange/Amount must be the
same as Currency.
C14 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C15 FinancialInstrumentIdentificationGuideline
It is recommended that ISIN be used in Identification\SecurityIdentification3Choice.
C16 NewPriceReportRule
If Function is "NEWP" then CancellationIdentification must not be present.
On Condition
    /Function is equal to value 'NewPriceReport'
Following Must be True
    /CancellationIdentification Must be absent
This constraint is defined at the MessageDefinition level.
C17 OtherCodeRule
If Structured is OTHR, then AdditionalInformation is mandatory.
C18 OtherCodeRule
If Structured is OTHR, then AdditionalInformation is mandatory.
C19 PriceDetailsRule
If SuspendedIndicator is "true" or "1" (Yes), then PriceDetails is optional.
If SuspendedIndicator is "false" or "0" (No), and if FinancialInstrumentDetails /
DualFundIndicator is "false" or "0" (No), then PriceDetails must be present at least once.
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 167 May 2026
```

