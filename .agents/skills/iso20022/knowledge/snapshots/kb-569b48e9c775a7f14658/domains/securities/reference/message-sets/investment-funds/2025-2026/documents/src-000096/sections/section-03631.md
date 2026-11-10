---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.38 BreakdownByCurrency2", "66.1.28.38.1 Currency <Ccy>"]
file_pages: [4881]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.38.1 Currency <Ccy>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4881 to 4881.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4881

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Currency <Ccy> [1..1] CodeSet C2 4881
   CashOutForecast <CshOutFcst> [0..*]  C6 4881
     CashSettlementDate <CshSttlmDt> [1..1] Date 4882
     SubTotalAmount <SubTtlAmt> [0..1] Amount C2, C10 4882
     SubTotalUnitsNumber <SubTtlUnitsNb> [0..1] ± 4883
     ExceptionalCashFlowIndicator <XcptnlCshFlowInd> [0..1] Indicator 4883
     CashOutBreakdownDetails <CshOutBrkdwnDtls> [0..*] ± 4883
     AdditionalBalance <AddtlBal> [0..1] ± 4883
   CashInForecast <CshInFcst> [0..*]  C5 4884
     CashSettlementDate <CshSttlmDt> [1..1] Date 4885
     SubTotalAmount <SubTtlAmt> [0..1] Amount C2, C10 4885
     SubTotalUnitsNumber <SubTtlUnitsNb> [0..1] ± 4885
     ExceptionalCashFlowIndicator <XcptnlCshFlowInd> [0..1] Indicator 4885
     CashInBreakdownDetails <CshInBrkdwnDtls> [0..*] ± 4885
     AdditionalBalance <AddtlBal> [0..1] ± 4886
   NetCashForecast <NetCshFcst> [0..*] ± C5 4886
66.1.28.38.1  Currency <Ccy>
Presence: [1..1]
Definition: Currency for which the cash flow is being reported.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 5276
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
66.1.28.38.2  CashOutForecast <CshOutFcst>
Presence: [0..*]
Definition: Cash movement out of the fund as a result of transactions in shares in an investment fund,
for example, redemptions or switch-outs.
Impacted by: C6 "AdditionalBalanceRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4881 May 2026
```

