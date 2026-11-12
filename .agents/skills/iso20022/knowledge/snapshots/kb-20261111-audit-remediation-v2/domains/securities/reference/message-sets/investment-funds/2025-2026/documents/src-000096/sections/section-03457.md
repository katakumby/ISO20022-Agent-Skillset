---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.25 InvestmentFundCashForecast", "66.1.25.6 FundCashForecast7", "66.1.25.6.17 CashOutForecastDetails <CshOutFcstDtls>"]
file_pages: [4705]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.25.6.17 CashOutForecastDetails <CshOutFcstDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4705 to 4705.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4705

```text
 Or    /AdditionalBalance/TotalCashFromUnitOrders Must be present
 Or    /AdditionalBalance/TotalCashFromCashOrders Must be present
66.1.25.6.17  CashOutForecastDetails <CshOutFcstDtls>
Presence: [0..*]
Definition: Cash movements out of the fund as a result of transactions in shares in an investment fund,
for example, redemptions or switch-outs.
Impacted by: C4 "AdditionalBalanceRule"
CashOutForecastDetails <CshOutFcstDtls> contains the following elements (see
"CashOutForecast6" on page 4408 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashSettlementDate <CshSttlmDt> [1..1] Date 4409
   SubTotalAmount <SubTtlAmt> [0..1] Amount C2, C10 4409
   SubTotalUnitsNumber <SubTtlUnitsNb> [0..1] ± 4409
   ExceptionalCashFlowIndicator <XcptnlCshFlowInd> [0..1] Indicator 4409
   AdditionalBalance <AddtlBal> [0..1] ± 4410
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
66.1.25.6.18  NetCashForecastDetails <NetCshFcstDtls>
Presence: [0..*]
Definition: Net cash as a result of the cash-in and cash-out flows.
Impacted by: C5 "AdditionalBalanceRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4705 May 2026
```

