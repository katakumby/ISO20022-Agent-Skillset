---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04", "10.4 Message Building Blocks", "10.4.8 ConsolidatedNetCashForecast <CnsltdNetCshFcst>"]
file_pages: [144, 145]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.043.001.04"]
---

# 10.4.8 ConsolidatedNetCashForecast <CnsltdNetCshFcst>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 144 to 145.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 144

```text
NetCashForecastDetails <NetCshFcstDtls> contains the following elements (see
"NetCashForecast4" on page 4413 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashSettlementDate <CshSttlmDt> [1..1] Date 4413
   NetAmount <NetAmt> [0..1] Amount C2, C10 4414
   NetUnitsNumber <NetUnitsNb> [0..1] ± 4414
   FlowDirection <FlowDrctn> [1..1] CodeSet 4414
   AdditionalBalance <AddtlBal> [0..1] ± 4414
Constraints
• AdditionalBalanceRule
If AdditionalBalance is present, then at least one or more elements in the list (AdditionalBalance/
TotalUnitsFromUnitOrders, AdditionalBalance/TotalUnitsFromCashOrders, AdditionalBalance/
TotalCashFromUnitOrders, AdditionalBalance/TotalCashFromCashOrders) must be present.
On Condition
    /AdditionalBalance is present
Following Must be True
    /AdditionalBalance/TotalUnitsFromUnitOrders Must be present
 Or    /AdditionalBalance/TotalUnitsFromCashOrders Must be present
 Or    /AdditionalBalance/TotalCashFromUnitOrders Must be present
 Or    /AdditionalBalance/TotalCashFromCashOrders Must be present
10.4.8 ConsolidatedNetCashForecast <CnsltdNetCshFcst>
Presence: [0..1]
Definition: Net cash as a result of the cash-in and cash-out flows specified in the fund cash forecast
details.
ConsolidatedNetCashForecast <CnsltdNetCshFcst> contains the following elements (see
"NetCashForecast3" on page 4412 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NetAmount <NetAmt> [0..1] Amount C2, C10 4412
   NetUnitsNumber <NetUnitsNb> [0..1] ± 4412
   FlowDirection <FlowDrctn> [1..1] CodeSet 4413
10.4.9 Extension <Xtnsn>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C12 "ExtensionRule"
Approved by the Securities SEG on 27 January 2026 camt.043.001.04
FundDetailedConfirmedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 144 May 2026
```

## File page 145

```text
Extension <Xtnsn> contains the following elements (see "Extension1" on page 4835 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [1..1] Text 4836
   Text <Txt> [1..1] Text 4836
Constraints
• ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
Approved by the Securities SEG on 27 January 2026 camt.043.001.04
FundDetailedConfirmedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 145 May 2026
```

