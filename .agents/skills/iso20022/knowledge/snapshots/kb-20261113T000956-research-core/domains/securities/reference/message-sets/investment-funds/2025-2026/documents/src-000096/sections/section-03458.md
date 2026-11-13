---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.25 InvestmentFundCashForecast", "66.1.25.7 CashInOutForecast7"]
file_pages: [4706]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.25.7 CashInOutForecast7

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4706 to 4706.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4706

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
66.1.25.7  CashInOutForecast7
Definition: Cash movements into or out of a fund as a result of investment funds transactions, for
example, subscriptions, redemptions or switches.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashSettlementDate <CshSttlmDt> [0..1] Date 4706
   Amount <Amt> [1..1] Amount C2, C10 4706
66.1.25.7.1  CashSettlementDate <CshSttlmDt>
Presence: [0..1]
Definition: Date on which cash is available.
Datatype: "ISODate" on page 5388
66.1.25.7.2  Amount <Amt>
Presence: [1..1]
Definition: Amount of the cash flow.
Impacted by: C2 "ActiveOrHistoricCurrency", C10 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 5269
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4706 May 2026
```

