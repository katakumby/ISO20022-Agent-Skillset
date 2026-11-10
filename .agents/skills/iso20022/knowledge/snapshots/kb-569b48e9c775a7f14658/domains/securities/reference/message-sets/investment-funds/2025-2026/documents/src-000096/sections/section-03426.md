---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.25 InvestmentFundCashForecast", "66.1.25.2 EstimatedFundCashForecast5", "66.1.25.2.4 FinancialInstrumentDetails <FinInstrmDtls>"]
file_pages: [4673]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.25.2.4 FinancialInstrumentDetails <FinInstrmDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4673 to 4673.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4673

```text
PreviousTradeDateTime <PrvsTradDtTm> contains one of the following elements (see
"DateAndDateTimeChoice" on page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4466
Or}   DateTime <DtTm> [1..1] DateTime 4466
66.1.25.2.4  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [1..1]
Definition: Investment fund class to which the cash flow is related.
Impacted by: C12 "FinancialInstrumentIdentificationGuideline"
FinancialInstrumentDetails <FinInstrmDtls> contains the following elements (see
"FinancialInstrument9" on page 4493 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4493
   Name <Nm> [0..1] Text 4494
   SupplementaryIdentification <SplmtryId> [0..1] Text 4494
   RequestedNAVCurrency <ReqdNAVCcy> [0..1] CodeSet C2 4494
   ClassType <ClssTp> [0..1] Text 4495
   SecuritiesForm <SctiesForm> [0..1] CodeSet 4495
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4495
   DualFundIndicator <DualFndInd> [1..1] Indicator 4495
Constraints
• FinancialInstrumentIdentificationGuideline
It is recommended that ISIN be used in Identification\SecurityIdentification3Choice.
66.1.25.2.5  EstimatedTotalNAV <EstmtdTtlNAV>
Presence: [0..*]
Definition: Estimated total value of all the holdings, less the fund's liabilities, attributable to a specific
investment fund class.
Impacted by: C2 "ActiveOrHistoricCurrency", C10 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 5269
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4673 May 2026
```

