---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.3 Constraints"]
file_pages: [229, 230]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
topic_continuations: [{"constraint_ids": ["C18", "C19", "C20", "C21"], "until_heading": "14.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 231, "topic": "14.3 Constraints", "reference_path": "domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00158.md"}]
---

# 14.3 Constraints

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 229 to 230.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 14.3 Constraints topic continues in [Constraints continuation C18–C21 (file p231)](section-00158.md#file-page-231). Read the text before **14.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 229

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             Amount <Amt> [0..1] Amount C3 288
             AmountSign <AmtSgn> [0..1] Indicator 289
             Rate <Rate> [0..1] Rate 289
           Yield <Yld> [0..1] Rate 289
       PerformanceDetails <PrfrmncDtls> [0..1]  C1 289
         CorporateActionFactor <CorpActnFctr> [0..1] Quantity 289
         CumulativeCorporateActionFactor <CmltvCorpActnFctr> [0..1] Quantity 290
         AccumulationPeriod <AcmltnPrd> [0..1] ± 290
         NormalPerformance <NrmlPrfrmnc> [0..1] Quantity 290
   Extension <Xtnsn> [0..*] ± C16 290
14.3 Constraints
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
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 229 May 2026
```

## File page 230

```text
C8 CalculationBasisRule
If Type is not NonAdjustedUnpublished, then CalculationBasis is not allowed. If Type is
NonAdjustedUnpublished, then CalculationBasis may be present.
C9 CompletePriceCancellation1Rule
If CompletePriceCancellation is "false" or "0" (No), then one or more instances of
CancelledPriceValuationDetails must be present.
On Condition
    /CompletePriceCancellation is equal to value 'False'
Following Must be True
    /CancelledPriceValuationDetails[*] Must be present
This constraint is defined at the MessageDefinition level.
C10 CompletePriceCancellation2Rule
If CompletePriceCancellation is "true" or "1" (Yes), then CancelledPriceValuationDetails must
not be present.
On Condition
    /CompletePriceCancellation is equal to value 'True'
Following Must be True
    /CancelledPriceValuationDetails[*] Must be absent
This constraint is defined at the MessageDefinition level.
C11 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C12 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C13 CurrencyPredefinedPeriodsRule
Currency in ByPredefinedTimePeriods/HighestPriceValue12Months/Amount,
ByPredefinedTimePeriods/LowestPriceValue12Months/Amount, ByPredefinedTimePeriods/
OneYearPriceChange/Amount, ByPredefinedTimePeriods/ThreeYearPriceChange/Amount and
ByPredefinedTimePeriods/FiveYearPriceChange/Amount must be the same as Currency.
C14 CurrencyPriceChangeRule
Currency in PriceChange/Amount must be the same as Currency.
C15 CurrencyUserDefinedPeriodsRule
Currency in ByUserDefinedTimePeriod/HighestPriceValue/Amount, ByUserDefinedTimePeriod/
LowestPriceValue/Amount and ByUserDefinedTimePeriod/PriceChange/Amount must be the
same as Currency.
C16 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C17 FinancialInstrumentIdentificationGuideline
It is recommended that ISIN be used in Identification\SecurityIdentification3Choice.
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 230 May 2026
```

