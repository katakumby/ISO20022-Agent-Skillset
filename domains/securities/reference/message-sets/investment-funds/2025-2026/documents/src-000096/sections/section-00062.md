---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["7 camt.040.001.04 FundEstimatedCashForecastReportV04", "7.2 Structure"]
file_pages: [96, 97]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.040.001.04"]
---

# 7.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 96 to 97.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 96

```text
7.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <FndEstmtdCshFcstRpt> [1..1]  C7, C16,
C17,
C18,
C19
   MessageIdentification <MsgId> [1..1] ± 98
   PoolReference <PoolRef> [0..1] ± 99
   PreviousReference <PrvsRef> [0..*] ± 99
   RelatedReference <RltdRef> [0..*] ± 99
   MessagePagination <MsgPgntn> [1..1] ± 100
   FundOrSubFundDetails <FndOrSubFndDtls> [0..*] ± C13,
C14,
C15
100
   EstimatedFundCashForecastDetails <EstmtdFndCshFcstDtls> [0..*] ± C10 102
   ConsolidatedNetCashForecast <CnsltdNetCshFcst> [0..1] ± 103
   Extension <Xtnsn> [0..*] ± C11 104
7.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C3 AdditionalBalanceRule
If AdditionalBalance is present, then at least one or more elements in the list
(AdditionalBalance/TotalUnitsFromUnitOrders, AdditionalBalance/TotalUnitsFromCashOrders,
AdditionalBalance/TotalCashFromUnitOrders, AdditionalBalance/TotalCashFromCashOrders)
must be present.
C4 AdditionalBalanceRule
If AdditionalBalance is present, then at least one or more elements in the list
(AdditionalBalance/TotalUnitsFromUnitOrders, AdditionalBalance/TotalUnitsFromCashOrders,
AdditionalBalance/TotalCashFromUnitOrders, AdditionalBalance/TotalCashFromCashOrders)
must be present.
Approved by the Securities SEG on 27 January 2026 camt.040.001.04
FundEstimatedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 96 May 2026
```

## File page 97

```text
C5 AdditionalBalanceRule
If AdditionalBalance is present, then at least one or more elements in the list
(AdditionalBalance/TotalUnitsFromUnitOrders, AdditionalBalance/TotalUnitsFromCashOrders,
AdditionalBalance/TotalCashFromUnitOrders, AdditionalBalance/TotalCashFromCashOrders)
must be present.
C6 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered by the ISO 9362 Registration Authority in the BIC directory,
and consists of eight (8) or eleven (11) contiguous characters.
C7 ConsolidatedNetCashRule
If ConsolidatedNetCashForecast is present, then at least one occurrence of either
FundOrSubFundDetails or EstimatedFundCashForecastDetails must be present. Both
FundOrSubFundDetails and EstimatedFundCashForecastDetails may be present.
On Condition
    /ConsolidatedNetCashForecast is present
Following Must be True
    /FundOrSubFundDetails[*] Must be present
 Or    /EstimatedFundCashForecastDetails[*] Must be present
This constraint is defined at the MessageDefinition level.
C8 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C9 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C10 ExceptionalCashFlowIndicatorRule
If Exceptional NetCashFlowIndicator is "true" or "1" (Yes), then either
EstimatedCashInForecastDetails/ExceptionalCashFlowIndicator or
EstimatedCashOutForecastDetails/ExceptionalCashFlowIndicator must be present. Both may
be present.
C11 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C12 FinancialInstrumentIdentificationGuideline
It is recommended that ISIN be used in Identification\SecurityIdentification3Choice.
C13 FundIdentification1Rule
If Identification is not present, then Name or LegalEntityIdentifier must be present. Identification,
Name and Legal Entity Identifier may all be present.
C14 FundIdentification2Rule
If Name is not present, then Identification or Legal Entity Identifier must be present.
Identification, Name and Legal Entity Identifier may all be present.
Approved by the Securities SEG on 27 January 2026 camt.040.001.04
FundEstimatedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 97 May 2026
```

