---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.12 FundCashOutBreakdown3", "66.1.28.12.1 Amount <Amt>"]
file_pages: [4827]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.12.1 Amount <Amt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4827 to 4827.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4827

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [0..1] Amount C2, C10 4827
   UnitsNumber <UnitsNb> [0..1] ± 4827
   NewAmountIndicator <NewAmtInd> [0..1] Indicator 4828
   InvestmentFundTransactionOutType
<InvstmtFndTxOutTp>
[1..1]  4828
{Or     Code <Cd> [1..1] CodeSet 4828
Or}     Proprietary <Prtry> [1..1] ± 4828
   OriginalOrderQuantityType <OrgnlOrdrQtyTp> [1..1]  4829
{Or     Code <Cd> [1..1] CodeSet 4829
Or}     Proprietary <Prtry> [1..1] ± 4829
   ChargeDetails <ChrgDtls> [0..*] ± 4829
   CommissionDetails <ComssnDtls> [0..*] ± 4830
   SettlementCurrency <SttlmCcy> [0..1] CodeSet C1 4830
66.1.28.12.1  Amount <Amt>
Presence: [0..1]
Definition: Amount of cash flow out, expressed as an amount of money.
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
Note: The decimal separator is a dot.
66.1.28.12.2  UnitsNumber <UnitsNb>
Presence: [0..1]
Definition: Amount of the cash flow out, expressed as a number of units.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4827 May 2026
```

