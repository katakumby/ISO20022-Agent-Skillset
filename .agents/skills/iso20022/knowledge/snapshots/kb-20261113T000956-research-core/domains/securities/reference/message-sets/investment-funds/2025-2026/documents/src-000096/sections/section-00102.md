---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["11 camt.044.001.03 FundConfirmedCashForecastReportCancellationV03", "11.2 Structure"]
file_pages: [147, 148]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.044.001.03"]
---

# 11.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 147 to 148.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 147

```text
11.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <FndConfdCshFcstRptCxl> [1..1]  
   MessageIdentification <MsgId> [1..1] ± 149
   PoolReference <PoolRef> [0..1] ± 149
   PreviousReference <PrvsRef> [0..1] ± 149
   RelatedReference <RltdRef> [0..*] ± 150
   MessagePagination <MsgPgntn> [1..1] ± 150
   CashForecastReportToBeCancelled <CshFcstRptToBeCanc> [0..1] ± C7, C16,
C17,
C18,
C19
150
11.3 Constraints
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
C5 AdditionalBalanceRule
If AdditionalBalance is present, then at least one or more elements in the list
(AdditionalBalance/TotalUnitsFromUnitOrders, AdditionalBalance/TotalUnitsFromCashOrders,
AdditionalBalance/TotalCashFromUnitOrders, AdditionalBalance/TotalCashFromCashOrders)
must be present.
Approved by the Securities SEG on 27 January 2026 camt.044.001.03
FundConfirmedCashForecastReportCancellationV0
3
Investment Funds - Maintenance 2025 - 2026 147 May 2026
```

## File page 148

```text
C6 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered by the ISO 9362 Registration Authority in the BIC directory,
and consists of eight (8) or eleven (11) contiguous characters.
C7 ConsolidatedNetCashRule
If ConsolidatedNetCashForecast is present, then at least one occurrence of either
FundOrSubFundDetails or FundCashForecastDetails must be present. Both
FundOrSubFundDetails and FundCashForecastDetails may be present.
C8 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C9 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C10 ExceptionalCashFlowIndicatorRule
If Exceptional NetCashFlow Indicator is "true" or "1" (Yes), then CashInForecastDetails/
ExceptionalCashFlowIndicator and CashOutForecastDetails/ ExceptionalCashFlowIndicator
must be present.
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
C15 FundIdentification3Rule
If Legal Entity Identifier is not present, then Identification or Name must be present.
Identification, Name and Legal Entity Identifier may all be present.
C16 FundOrSubFundAndShareClassGuideline
When using the message to provide cash in and cash out amounts for more than one fund/sub
fund, and more than one share classes, (two or more FundOrSubFundDetails sequences and
two or more FundCashForecastDetails sequences and used), in this usage there is no way to
determine which share class belongs to which fund/sub fund from the message content itself,
which may not be desirable and this type of usage should be bilaterally agreed.
Approved by the Securities SEG on 27 January 2026 camt.044.001.03
FundConfirmedCashForecastReportCancellationV0
3
Investment Funds - Maintenance 2025 - 2026 148 May 2026
```

