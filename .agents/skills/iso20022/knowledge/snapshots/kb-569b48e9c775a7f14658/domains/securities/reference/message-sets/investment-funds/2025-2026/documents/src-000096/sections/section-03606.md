---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.26 BreakdownByUserDefinedParameter3", "66.1.28.26.1 Party <Pty>"]
file_pages: [4856]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.26.1 Party <Pty>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4856 to 4856.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4856

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [0..1]  C1, C2 4856
     AccountIdentification <AcctId> [0..1] ± 4857
     OwnerIdentification <OwnrId> [0..1] ± 4857
     AccountServicer <AcctSvcr> [0..1] ± 4858
   Country <Ctry> [0..1] CodeSet C12 4858
   Currency <Ccy> [0..1] CodeSet C2 4858
   UserDefined <UsrDfnd> [0..1] ± 4858
   CashInForecast <CshInFcst> [0..*]  C5 4859
     CashSettlementDate <CshSttlmDt> [1..1] Date 4859
     SubTotalAmount <SubTtlAmt> [0..1] Amount C2, C10 4859
     SubTotalUnitsNumber <SubTtlUnitsNb> [0..1] ± 4860
     ExceptionalCashFlowIndicator <XcptnlCshFlowInd> [0..1] Indicator 4860
     CashInBreakdownDetails <CshInBrkdwnDtls> [0..*] ± 4860
     AdditionalBalance <AddtlBal> [0..1] ± 4861
   CashOutForecast <CshOutFcst> [0..*]  C6 4861
     CashSettlementDate <CshSttlmDt> [1..1] Date 4862
     SubTotalAmount <SubTtlAmt> [0..1] Amount C2, C10 4862
     SubTotalUnitsNumber <SubTtlUnitsNb> [0..1] ± 4863
     ExceptionalCashFlowIndicator <XcptnlCshFlowInd> [0..1] Indicator 4863
     CashOutBreakdownDetails <CshOutBrkdwnDtls> [0..*] ± 4863
     AdditionalBalance <AddtlBal> [0..1] ± 4863
   NetCashForecast <NetCshFcst> [0..*] ± C5 4864
Constraints
• UserDefinedRule
At least one message element in the list (Party, Country, Currency, UserDefined) must be present.
More than one element in the list (Party, Country, Currency, UserDefined) may be present.
66.1.28.26.1  Party <Pty>
Presence: [0..1]
Definition: Party for which the cash flow is being reported.
Impacted by: C1 "AccountOrOwner1Rule", C2 "AccountOrOwner2Rule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4856 May 2026
```

