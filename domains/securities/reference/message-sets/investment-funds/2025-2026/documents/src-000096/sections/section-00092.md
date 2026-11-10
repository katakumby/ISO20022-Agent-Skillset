---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04", "10.4 Message Building Blocks", "10.4.7 FundCashForecastDetails <FndCshFcstDtls>", "10.4.7.5 TotalNAV <TtlNAV>"]
file_pages: [136]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.043.001.04"]
---

# 10.4.7.5 TotalNAV <TtlNAV>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 136 to 136.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 136

```text
Definition: Investment fund class to which the cash flow is related.
Impacted by: C13 "FinancialInstrumentIdentificationGuideline"
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
10.4.7.5  TotalNAV <TtlNAV>
Presence: [0..*]
Definition: Total value of all the holdings, less the fund's liabilities, attributable to a specific investment
fund class.
Impacted by: C4 "ActiveOrHistoricCurrency", C10 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 5269
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
10.4.7.6  PreviousTotalNAV <PrvsTtlNAV>
Presence: [0..*]
Approved by the Securities SEG on 27 January 2026 camt.043.001.04
FundDetailedConfirmedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 136 May 2026
```

