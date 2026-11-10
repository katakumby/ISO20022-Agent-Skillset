---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.25 InvestmentFundCashForecast", "66.1.25.2 EstimatedFundCashForecast5", "66.1.25.2.17 BreakdownByCountry <BrkdwnByCtry>"]
file_pages: [4677]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.25.2.17 BreakdownByCountry <BrkdwnByCtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4677 to 4677.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4677

```text
BreakdownByParty <BrkdwnByPty> contains the following elements (see "BreakdownByParty3" on
page 4836 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1]  C1, C2 4837
     AccountIdentification <AcctId> [0..1] ± 4838
     OwnerIdentification <OwnrId> [0..1] ± 4838
     AccountServicer <AcctSvcr> [0..1] ± 4838
   AdditionalParameters <AddtlParams> [0..1] ± 4839
   CashInForecast <CshInFcst> [0..*]  C5 4839
     CashSettlementDate <CshSttlmDt> [1..1] Date 4840
     SubTotalAmount <SubTtlAmt> [0..1] Amount C2, C10 4840
     SubTotalUnitsNumber <SubTtlUnitsNb> [0..1] ± 4840
     ExceptionalCashFlowIndicator <XcptnlCshFlowInd> [0..1] Indicator 4840
     CashInBreakdownDetails <CshInBrkdwnDtls> [0..*] ± 4841
     AdditionalBalance <AddtlBal> [0..1] ± 4841
   CashOutForecast <CshOutFcst> [0..*]  C6 4841
     CashSettlementDate <CshSttlmDt> [1..1] Date 4842
     SubTotalAmount <SubTtlAmt> [0..1] Amount C2, C10 4842
     SubTotalUnitsNumber <SubTtlUnitsNb> [0..1] ± 4843
     ExceptionalCashFlowIndicator <XcptnlCshFlowInd> [0..1] Indicator 4843
     CashOutBreakdownDetails <CshOutBrkdwnDtls> [0..*] ± 4843
     AdditionalBalance <AddtlBal> [0..1] ± 4844
   NetCashForecast <NetCshFcst> [0..*] ± C5 4844
66.1.25.2.17  BreakdownByCountry <BrkdwnByCtry>
Presence: [0..*]
Definition: Estimated cash flow by country.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4677 May 2026
```

