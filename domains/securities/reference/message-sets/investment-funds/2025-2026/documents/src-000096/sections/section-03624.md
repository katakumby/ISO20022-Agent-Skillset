---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.36 BreakdownByCountry2", "66.1.28.36.2 CashInForecast <CshInFcst>"]
file_pages: [4874]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.36.2 CashInForecast <CshInFcst>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4874 to 4874.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4874

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.28.36.2  CashInForecast <CshInFcst>
Presence: [0..*]
Definition: Cash movement into the fund as a result of transactions in shares in an investment fund, for
example, subscriptions or switch-ins.
Impacted by: C5 "AdditionalBalanceRule"
CashInForecast <CshInFcst> contains the following CashInForecast5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashSettlementDate <CshSttlmDt> [1..1] Date 4874
   SubTotalAmount <SubTtlAmt> [0..1] Amount C2, C10 4874
   SubTotalUnitsNumber <SubTtlUnitsNb> [0..1] ± 4875
   ExceptionalCashFlowIndicator <XcptnlCshFlowInd> [0..1] Indicator 4875
   CashInBreakdownDetails <CshInBrkdwnDtls> [0..*] ± 4875
   AdditionalBalance <AddtlBal> [0..1] ± 4876
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
66.1.28.36.2.1  CashSettlementDate <CshSttlmDt>
Presence: [1..1]
Definition: Date on which cash is available.
Datatype: "ISODate" on page 5388
66.1.28.36.2.2  SubTotalAmount <SubTtlAmt>
Presence: [0..1]
Definition: Sub-total amount of the cash flow in, expressed as an amount of money.
Impacted by: C2 "ActiveOrHistoricCurrency", C10 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 5269
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4874 May 2026
```

