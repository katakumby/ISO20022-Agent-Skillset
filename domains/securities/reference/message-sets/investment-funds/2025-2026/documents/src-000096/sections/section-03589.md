---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.20 BreakdownByParty3", "66.1.28.20.2 AdditionalParameters <AddtlParams>"]
file_pages: [4839]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.20.2 AdditionalParameters <AddtlParams>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4839 to 4839.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4839

```text
AccountServicer <AcctSvcr> contains one of the following elements (see "PartyIdentification2Choice"
on page 4887 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICOrBEI <BICOrBEI> [1..1] IdentifierSet C5 4887
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4888
Or}   NameAndAddress <NmAndAdr> [1..1] ± 4888
66.1.28.20.2  AdditionalParameters <AddtlParams>
Presence: [0..1]
Definition: Additional parameter/s applied to the cash flow by party.
AdditionalParameters <AddtlParams> contains the following elements (see "AdditionalParameters1"
on page 4871 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Country <Ctry> [0..1] CodeSet C12 4871
   Currency <Ccy> [0..1] CodeSet C2 4872
   GeographicalArea <GeoArea> [0..1] Text 4872
66.1.28.20.3  CashInForecast <CshInFcst>
Presence: [0..*]
Definition: Cash movement into the fund as a result of transactions in shares in an investment fund, for
example, subscriptions or switch-ins.
Impacted by: C5 "AdditionalBalanceRule"
CashInForecast <CshInFcst> contains the following CashInForecast5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashSettlementDate <CshSttlmDt> [1..1] Date 4840
   SubTotalAmount <SubTtlAmt> [0..1] Amount C2, C10 4840
   SubTotalUnitsNumber <SubTtlUnitsNb> [0..1] ± 4840
   ExceptionalCashFlowIndicator <XcptnlCshFlowInd> [0..1] Indicator 4840
   CashInBreakdownDetails <CshInBrkdwnDtls> [0..*] ± 4841
   AdditionalBalance <AddtlBal> [0..1] ± 4841
Constraints
• AdditionalBalanceRule
If AdditionalBalance is present, then at least one or more elements in the list (AdditionalBalance/
TotalUnitsFromUnitOrders, AdditionalBalance/TotalUnitsFromCashOrders, AdditionalBalance/
TotalCashFromUnitOrders, AdditionalBalance/TotalCashFromCashOrders) must be present.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4839 May 2026
```

