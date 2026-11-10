---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04", "10.4 Message Building Blocks", "10.4.7 FundCashForecastDetails <FndCshFcstDtls>", "10.4.7.17 BreakdownByCountry <BrkdwnByCtry>"]
file_pages: [140]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.043.001.04"]
---

# 10.4.7.17 BreakdownByCountry <BrkdwnByCtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 140 to 140.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 140

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
10.4.7.17  BreakdownByCountry <BrkdwnByCtry>
Presence: [0..*]
Definition: Cash flow by country.
Approved by the Securities SEG on 27 January 2026 camt.043.001.04
FundDetailedConfirmedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 140 May 2026
```

