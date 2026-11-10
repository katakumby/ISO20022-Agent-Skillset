---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "12.2 Structure"]
file_pages: [154, 155]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.045.001.03"]
---

# 12.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 154 to 155.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 154

```text
12.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <FndDtldConfdCshFcstRptCxl> [1..1]  
   MessageIdentification <MsgId> [1..1] ± 156
   PoolReference <PoolRef> [0..1] ± 156
   PreviousReference <PrvsRef> [0..1] ± 156
   RelatedReference <RltdRef> [0..*] ± 157
   MessagePagination <MsgPgntn> [1..1] ± 157
   CashForecastReportToBeCancelled <CshFcstRptToBeCanc> [0..1] ± 157
12.3 Constraints
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
Approved by the Securities SEG on 27 January 2026 camt.045.001.03
FundDetailedConfirmedCashForecastReportCancell
ationV03
Investment Funds - Maintenance 2025 - 2026 154 May 2026
```

## File page 155

```text
C7 AdditionalBalanceRule
If AdditionalBalance is present, then at least one or more elements in the list
(AdditionalBalance/TotalUnitsFromUnitOrders, AdditionalBalance/TotalUnitsFromCashOrders,
AdditionalBalance/TotalCashFromUnitOrders, AdditionalBalance/TotalCashFromCashOrders)
must be present.
C8 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered by the ISO 9362 Registration Authority in the BIC directory,
and consists of eight (8) or eleven (11) contiguous characters.
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
Approved by the Securities SEG on 27 January 2026 camt.045.001.03
FundDetailedConfirmedCashForecastReportCancell
ationV03
Investment Funds - Maintenance 2025 - 2026 155 May 2026
```

