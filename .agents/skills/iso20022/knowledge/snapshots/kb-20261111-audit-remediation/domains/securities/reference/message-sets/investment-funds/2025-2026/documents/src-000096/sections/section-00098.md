---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04", "10.4 Message Building Blocks", "10.4.7 FundCashForecastDetails <FndCshFcstDtls>", "10.4.7.19 BreakdownByUserDefinedParameter <BrkdwnByUsrDfndParam>"]
file_pages: [142]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.043.001.04"]
---

# 10.4.7.19 BreakdownByUserDefinedParameter <BrkdwnByUsrDfndParam>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 142 to 142.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 142

```text
BreakdownByCurrency <BrkdwnByCcy> contains the following elements (see
"BreakdownByCurrency2" on page 4880 for details)
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
10.4.7.19  BreakdownByUserDefinedParameter <BrkdwnByUsrDfndParam>
Presence: [0..*]
Definition: Cash flow by a user defined parameter/s.
Impacted by: C17 "UserDefinedRule"
Approved by the Securities SEG on 27 January 2026 camt.043.001.04
FundDetailedConfirmedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 142 May 2026
```

