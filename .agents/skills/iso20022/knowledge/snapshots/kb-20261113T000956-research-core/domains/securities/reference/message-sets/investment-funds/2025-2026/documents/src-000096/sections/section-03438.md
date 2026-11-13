---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.25 InvestmentFundCashForecast", "66.1.25.3 Fund1", "66.1.25.3.10 PreviousTotalUnitsNumber <PrvsTtlUnitsNb>"]
file_pages: [4686]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.25.3.10 PreviousTotalUnitsNumber <PrvsTtlUnitsNb>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4686 to 4686.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4686

```text
66.1.25.3.10  PreviousTotalUnitsNumber <PrvsTtlUnitsNb>
Presence: [0..1]
Definition: Previous total number of units of the fund/sub fund.
PreviousTotalUnitsNumber <PrvsTtlUnitsNb> contains the following elements (see
"FinancialInstrumentQuantity1" on page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
66.1.25.3.11  EstimatedPercentageOfFundTotalNAV <EstmtdPctgOfFndTtlNAV>
Presence: [0..1]
Definition: Estimated consolidated net cash flow expressed as a percentage of the previous total NAV
for the fund/sub fund.
Datatype: "PercentageRate" on page 5401
66.1.25.3.12  EstimatedCashInForecastDetails <EstmtdCshInFcstDtls>
Presence: [0..*]
Definition: Estimated cash movement into the fund/sub fund.
EstimatedCashInForecastDetails <EstmtdCshInFcstDtls> contains the following elements (see
"CashInOutForecast7" on page 4706 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashSettlementDate <CshSttlmDt> [0..1] Date 4706
   Amount <Amt> [1..1] Amount C2, C10 4706
66.1.25.3.13  EstimatedCashOutForecastDetails <EstmtdCshOutFcstDtls>
Presence: [0..*]
Definition: Estimated cash movement out of the fund/sub fund.
EstimatedCashOutForecastDetails <EstmtdCshOutFcstDtls> contains the following elements (see
"CashInOutForecast7" on page 4706 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashSettlementDate <CshSttlmDt> [0..1] Date 4706
   Amount <Amt> [1..1] Amount C2, C10 4706
66.1.25.3.14  EstimatedNetCashForecastDetails <EstmtdNetCshFcstDtls>
Presence: [0..*]
Definition: Net cash as a result of the cash-in and cash-out flows.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4686 May 2026
```

