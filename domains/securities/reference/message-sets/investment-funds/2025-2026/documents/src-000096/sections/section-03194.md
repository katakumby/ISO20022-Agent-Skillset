---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.7 Cash", "66.1.7.5 FundDetailedConfirmedCashForecastReport3", "66.1.7.5.2 FundCashForecastDetails <FndCshFcstDtls>", "66.1.7.5.2.18 BreakdownByCurrency <BrkdwnByCcy>"]
file_pages: [4425]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.7.5.2.18 BreakdownByCurrency <BrkdwnByCcy>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4425 to 4425.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4425

```text
BreakdownByCountry <BrkdwnByCtry> contains the following elements (see
"BreakdownByCountry2" on page 4873 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Country <Ctry> [1..1] CodeSet C12 4873
   CashInForecast <CshInFcst> [0..*]  C5 4874
     CashSettlementDate <CshSttlmDt> [1..1] Date 4874
     SubTotalAmount <SubTtlAmt> [0..1] Amount C2, C10 4874
     SubTotalUnitsNumber <SubTtlUnitsNb> [0..1] ± 4875
     ExceptionalCashFlowIndicator <XcptnlCshFlowInd> [0..1] Indicator 4875
     CashInBreakdownDetails <CshInBrkdwnDtls> [0..*] ± 4875
     AdditionalBalance <AddtlBal> [0..1] ± 4876
   CashOutForecast <CshOutFcst> [0..*]  C6 4876
     CashSettlementDate <CshSttlmDt> [1..1] Date 4877
     SubTotalAmount <SubTtlAmt> [0..1] Amount C2, C10 4877
     SubTotalUnitsNumber <SubTtlUnitsNb> [0..1] ± 4878
     ExceptionalCashFlowIndicator <XcptnlCshFlowInd> [0..1] Indicator 4878
     CashOutBreakdownDetails <CshOutBrkdwnDtls> [0..*] ± 4878
     AdditionalBalance <AddtlBal> [0..1] ± 4878
   NetCashForecast <NetCshFcst> [0..*] ± C5 4879
66.1.7.5.2.18  BreakdownByCurrency <BrkdwnByCcy>
Presence: [0..*]
Definition: Cash flow by currency.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4425 May 2026
```

