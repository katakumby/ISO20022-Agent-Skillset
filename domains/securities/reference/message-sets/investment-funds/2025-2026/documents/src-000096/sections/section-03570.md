---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.8 FundCashInBreakdown3"]
file_pages: [4820]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.8 FundCashInBreakdown3

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4820 to 4820.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4820

```text
DeMinimus <DeMnms> contains one of the following elements (see "DeMinimus1Choice" on
page 4475 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DeMinimusApplicable <DeMnmsAplbl> [1..1] ± 4475
Or}   DeMinimusNotApplicable <DeMnmsNotAplbl> [1..1] ± 4475
66.1.28.8  FundCashInBreakdown3
Definition: Breakdown of cash movements into a fund as a result of investment funds transactions, eg,
subscriptions or switch-in.
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
66.1.28.8.1  Amount <Amt>
Presence: [0..1]
Definition: Amount of cash flow in, expressed as an amount of money.
Impacted by: C2 "ActiveOrHistoricCurrency", C10 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 5269
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4820 May 2026
```

