---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.25 InvestmentFundCashForecast", "66.1.25.6 FundCashForecast7", "66.1.25.6.15 PercentageOfShareClassTotalNAV <PctgOfShrClssTtlNAV>"]
file_pages: [4704]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.25.6.15 PercentageOfShareClassTotalNAV <PctgOfShrClssTtlNAV>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4704 to 4704.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4704

```text
Definition: Foreign exchange rate.
ForeignExchangeRate <FXRate> contains the following elements (see "ForeignExchangeTerms19"
on page 4529 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 4529
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 4530
   ExchangeRate <XchgRate> [1..1] Rate 4530
66.1.25.6.15  PercentageOfShareClassTotalNAV <PctgOfShrClssTtlNAV>
Presence: [0..1]
Definition: Net cash flow expressed as a percentage of the total NAV for the share class.
Datatype: "PercentageRate" on page 5401
66.1.25.6.16  CashInForecastDetails <CshInFcstDtls>
Presence: [0..*]
Definition: Cash movements into the fund as a result of transactions in shares in an investment fund, for
example, subscriptions or switch-ins.
Impacted by: C3 "AdditionalBalanceRule"
CashInForecastDetails <CshInFcstDtls> contains the following elements (see "CashInForecast6" on
page 4410 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashSettlementDate <CshSttlmDt> [1..1] Date 4410
   SubTotalAmount <SubTtlAmt> [0..1] Amount C2, C10 4411
   SubTotalUnitsNumber <SubTtlUnitsNb> [0..1] ± 4411
   ExceptionalCashFlowIndicator <XcptnlCshFlowInd> [0..1] Indicator 4411
   AdditionalBalance <AddtlBal> [0..1] ± 4411
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4704 May 2026
```

