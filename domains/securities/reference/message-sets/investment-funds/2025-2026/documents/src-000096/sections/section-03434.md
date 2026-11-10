---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.25 InvestmentFundCashForecast", "66.1.25.3 Fund1"]
file_pages: [4681, 4682]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.25.3 Fund1

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4681 to 4682.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4681

```text
EstimatedNetCashForecastDetails <EstmtdNetCshFcstDtls> contains the following elements (see
"NetCashForecast4" on page 4413 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashSettlementDate <CshSttlmDt> [1..1] Date 4413
   NetAmount <NetAmt> [0..1] Amount C2, C10 4414
   NetUnitsNumber <NetUnitsNb> [0..1] ± 4414
   FlowDirection <FlowDrctn> [1..1] CodeSet 4414
   AdditionalBalance <AddtlBal> [0..1] ± 4414
Constraints
• AdditionalBalanceRule
If AdditionalBalance is present, then at least one or more elements in the list (AdditionalBalance/
TotalUnitsFromUnitOrders, AdditionalBalance/TotalUnitsFromCashOrders, AdditionalBalance/
TotalCashFromUnitOrders, AdditionalBalance/TotalCashFromCashOrders) must be present.
On Condition
    /AdditionalBalance is present
Following Must be True
    /AdditionalBalance/TotalUnitsFromUnitOrders Must be present
 Or    /AdditionalBalance/TotalUnitsFromCashOrders Must be present
 Or    /AdditionalBalance/TotalCashFromUnitOrders Must be present
 Or    /AdditionalBalance/TotalCashFromCashOrders Must be present
66.1.25.3  Fund1
Definition: Information about an investment fund.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4681 May 2026
```

## File page 4682

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 4683
   LegalEntityIdentifier <LglNttyIdr> [0..1] IdentifierSet 4683
   Identification <Id> [0..1]  4683
     Identification <Id> [1..1] Text 4683
     Type <Tp> [1..1] ± 4683
   Currency <Ccy> [0..1] CodeSet C2 4684
   TradeDateTime <TradDtTm> [0..1] ± 4684
   PreviousTradeDateTime <PrvsTradDtTm> [0..1] ± 4684
   EstimatedTotalNAV <EstmtdTtlNAV> [0..1] Amount C2, C10 4685
   PreviousTotalNAV <PrvsTtlNAV> [0..1] Amount C2, C10 4685
   EstimatedTotalUnitsNumber <EstmtdTtlUnitsNb> [0..1] ± 4685
   PreviousTotalUnitsNumber <PrvsTtlUnitsNb> [0..1] ± 4686
   EstimatedPercentageOfFundTotalNAV
<EstmtdPctgOfFndTtlNAV>
[0..1] Rate 4686
   EstimatedCashInForecastDetails <EstmtdCshInFcstDtls> [0..*] ± 4686
   EstimatedCashOutForecastDetails
<EstmtdCshOutFcstDtls>
[0..*] ± 4686
   EstimatedNetCashForecastDetails
<EstmtdNetCshFcstDtls>
[0..*]  4686
     CashSettlementDate <CshSttlmDt> [0..1] Date 4687
     NetAmount <NetAmt> [0..1] Amount C2, C10 4687
     NetUnitsNumber <NetUnitsNb> [0..1] ± 4687
     FlowDirection <FlowDrctn> [1..1] CodeSet 4687
Constraints
• FundIdentification1Rule
If Identification is not present, then Name or LegalEntityIdentifier must be present. Identification,
Name and Legal Entity Identifier may all be present.
On Condition
    /Identification is absent
Following Must be True
    /Name Must be present
 Or    /LegalEntityIdentifier Must be present
• FundIdentification2Rule
If Name is not present, then Identification or Legal Entity Identifier must be present. Identification,
Name and Legal Entity Identifier may all be present.
On Condition
    /Name is absent
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4682 May 2026
```

