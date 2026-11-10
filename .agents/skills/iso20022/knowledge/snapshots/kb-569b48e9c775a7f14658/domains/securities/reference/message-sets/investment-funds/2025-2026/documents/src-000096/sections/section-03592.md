---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.20 BreakdownByParty3", "66.1.28.20.4 CashOutForecast <CshOutFcst>", "66.1.28.20.4.1 CashSettlementDate <CshSttlmDt>"]
file_pages: [4842]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.20.4.1 CashSettlementDate <CshSttlmDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4842 to 4842.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4842

```text
Definition: Cash movement out of the fund as a result of transactions in shares in an investment fund,
for example, redemptions or switch-outs.
Impacted by: C6 "AdditionalBalanceRule"
CashOutForecast <CshOutFcst> contains the following CashOutForecast5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashSettlementDate <CshSttlmDt> [1..1] Date 4842
   SubTotalAmount <SubTtlAmt> [0..1] Amount C2, C10 4842
   SubTotalUnitsNumber <SubTtlUnitsNb> [0..1] ± 4843
   ExceptionalCashFlowIndicator <XcptnlCshFlowInd> [0..1] Indicator 4843
   CashOutBreakdownDetails <CshOutBrkdwnDtls> [0..*] ± 4843
   AdditionalBalance <AddtlBal> [0..1] ± 4844
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
66.1.28.20.4.1  CashSettlementDate <CshSttlmDt>
Presence: [1..1]
Definition: Date on which cash is available.
Datatype: "ISODate" on page 5388
66.1.28.20.4.2  SubTotalAmount <SubTtlAmt>
Presence: [0..1]
Definition: Sub-total amount of the cash flow out, expressed as an amount of money.
Impacted by: C2 "ActiveOrHistoricCurrency", C10 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 5269
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4842 May 2026
```

