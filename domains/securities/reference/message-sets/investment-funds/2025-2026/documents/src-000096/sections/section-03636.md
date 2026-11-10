---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.38 BreakdownByCurrency2", "66.1.28.38.3 CashInForecast <CshInFcst>", "66.1.28.38.3.6 AdditionalBalance <AddtlBal>"]
file_pages: [4886]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.38.3.6 AdditionalBalance <AddtlBal>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4886 to 4886.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4886

```text
Definition: Breakdown of cash in amounts by transaction and order type.
CashInBreakdownDetails <CshInBrkdwnDtls> contains the following elements (see
"FundCashInBreakdown3" on page 4820 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [0..1] Amount C2, C10 4820
   UnitsNumber <UnitsNb> [0..1] ± 4821
   NewAmountIndicator <NewAmtInd> [0..1] Indicator 4821
   InvestmentFundTransactionInType <InvstmtFndTxInTp> [1..1]  4821
{Or     Code <Cd> [1..1] CodeSet 4821
Or}     Proprietary <Prtry> [1..1] ± 4822
   OriginalOrderQuantityType <OrgnlOrdrQtyTp> [1..1]  4822
{Or     Code <Cd> [1..1] CodeSet 4822
Or}     Proprietary <Prtry> [1..1] ± 4822
   ChargeDetails <ChrgDtls> [0..*] ± 4823
   CommissionDetails <ComssnDtls> [0..*] ± 4823
   SettlementCurrency <SttlmCcy> [0..1] CodeSet C1 4823
66.1.28.38.3.6  AdditionalBalance <AddtlBal>
Presence: [0..1]
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
66.1.28.38.4  NetCashForecast <NetCshFcst>
Presence: [0..*]
Definition: Net cash as a result of the cash-in and cash-out flows specified for the currency.
Impacted by: C5 "AdditionalBalanceRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4886 May 2026
```

