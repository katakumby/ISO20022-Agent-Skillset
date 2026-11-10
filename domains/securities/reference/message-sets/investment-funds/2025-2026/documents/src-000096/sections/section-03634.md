---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.38 BreakdownByCurrency2", "66.1.28.38.3 CashInForecast <CshInFcst>"]
file_pages: [4884]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.38.3 CashInForecast <CshInFcst>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4884 to 4884.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4884

```text
Definition: Additional balances for cash amounts and number of units.
In an estimated report, the total cash derived from orders placed as a number of units is an estimated
cash amount and the total number of units derived from orders placed as a cash amount is an
estimated number of units.
AdditionalBalance <AddtlBal> contains the following elements (see "FundBalance1" on page 4389
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalUnitsFromUnitOrders <TtlUnitsFrUnitOrdrs> [0..1] ± 4389
   TotalUnitsFromCashOrders <TtlUnitsFrCshOrdrs> [0..1] ± 4389
   TotalCashFromUnitOrders <TtlCshFrUnitOrdrs> [0..1] Amount C2, C10 4390
   TotalCashFromCashOrders <TtlCshFrCshOrdrs> [0..1] Amount C2, C10 4390
66.1.28.38.3  CashInForecast <CshInFcst>
Presence: [0..*]
Definition: Cash movement into the fund as a result of transactions in shares in an investment fund, for
example, subscriptions or switch-ins.
Impacted by: C5 "AdditionalBalanceRule"
CashInForecast <CshInFcst> contains the following CashInForecast5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashSettlementDate <CshSttlmDt> [1..1] Date 4885
   SubTotalAmount <SubTtlAmt> [0..1] Amount C2, C10 4885
   SubTotalUnitsNumber <SubTtlUnitsNb> [0..1] ± 4885
   ExceptionalCashFlowIndicator <XcptnlCshFlowInd> [0..1] Indicator 4885
   CashInBreakdownDetails <CshInBrkdwnDtls> [0..*] ± 4885
   AdditionalBalance <AddtlBal> [0..1] ± 4886
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4884 May 2026
```

