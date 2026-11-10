---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04", "10.3 Constraints"]
file_pages: [129, 130]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.043.001.04"]
---

# 10.3 Constraints

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 129 to 130.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 129

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
   ConsolidatedNetCashForecast <CnsltdNetCshFcst> [0..1] ± 144
   Extension <Xtnsn> [0..*] ± C12 144
10.3 Constraints
C1 AccountOrOwner1Rule
If AccountIdentification is not present, then OwnerIdentification must be present. Both
AccountIdentification and OwnerIdentification may be present.
C2 AccountOrOwner2Rule
If OwnerIdentification is not present, then AccountIdentification must be present. Both
OwnerIdentification and AccountIdentification may be present.
C3 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C4 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C5 AdditionalBalanceRule
If AdditionalBalance is present, then at least one or more elements in the list
(AdditionalBalance/TotalUnitsFromUnitOrders, AdditionalBalance/TotalUnitsFromCashOrders,
AdditionalBalance/TotalCashFromUnitOrders, AdditionalBalance/TotalCashFromCashOrders)
must be present.
C6 AdditionalBalanceRule
If AdditionalBalance is present, then at least one or more elements in the list
(AdditionalBalance/TotalUnitsFromUnitOrders, AdditionalBalance/TotalUnitsFromCashOrders,
AdditionalBalance/TotalCashFromUnitOrders, AdditionalBalance/TotalCashFromCashOrders)
must be present.
C7 AdditionalBalanceRule
If AdditionalBalance is present, then at least one or more elements in the list
(AdditionalBalance/TotalUnitsFromUnitOrders, AdditionalBalance/TotalUnitsFromCashOrders,
AdditionalBalance/TotalCashFromUnitOrders, AdditionalBalance/TotalCashFromCashOrders)
must be present.
C8 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered by the ISO 9362 Registration Authority in the BIC directory,
and consists of eight (8) or eleven (11) contiguous characters.
Approved by the Securities SEG on 27 January 2026 camt.043.001.04
FundDetailedConfirmedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 129 May 2026
```

## File page 130

```text
C9 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C10 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C11 ExceptionalCashFlowIndicatorRule
If ExceptionalNetCashFlowIndicator is "true" or "1" (Yes), then at least one or more of the
following must be present:
BreakdownByParty/CashInForecast/ExceptionalCashFlowIndicator, or
BreakdownByParty/CashOutForecast/ExceptionalCashFlowIndicator, or
BreakdownByCountry/CashInForecast/ExceptionalCashFlowIndicator, or
BreakdownByCountry/CashOutForecast/ExceptionalCashFlowIndicator, or
BreakdownByCurrency/CashInForecast/ExceptionalCashFlowIndicator, or
BreakdownByCurrency/CashOutForecast/ExceptionalCashFlowIndicator, or
BreakdownByUserDefinedParameter/CashInForecast/ExceptionalCashFlowIndicator, or
BreakdownByUserDefinedParameter/CashOutForecast/ExceptionalCashFlowIndicator.
C12 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C13 FinancialInstrumentIdentificationGuideline
It is recommended that ISIN be used in Identification\SecurityIdentification3Choice.
C14 FundIdentification1Rule
If Identification is not present, then Name or LegalEntityIdentifier must be present. Identification,
Name and Legal Entity Identifier may all be present.
C15 FundIdentification2Rule
If Name is not present, then Identification or Legal Entity Identifier must be present.
Identification, Name and Legal Entity Identifier may all be present.
C16 FundIdentification3Rule
If Legal Entity Identifier is not present, then Identification or Name must be present.
Identification, Name and Legal Entity Identifier may all be present.
C17 UserDefinedRule
At least one message element in the list (Party, Country, Currency, UserDefined) must be
present. More than one element in the list (Party, Country, Currency, UserDefined) may be
present.
Approved by the Securities SEG on 27 January 2026 camt.043.001.04
FundDetailedConfirmedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 130 May 2026
```

