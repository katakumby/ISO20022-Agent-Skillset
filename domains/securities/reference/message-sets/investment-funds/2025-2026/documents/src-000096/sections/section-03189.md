---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.7 Cash", "66.1.7.5 FundDetailedConfirmedCashForecastReport3", "66.1.7.5.2 FundCashForecastDetails <FndCshFcstDtls>", "66.1.7.5.2.5 TotalNAV <TtlNAV>"]
file_pages: [4420]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.7.5.2.5 TotalNAV <TtlNAV>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4420 to 4420.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4420

```text
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
66.1.7.5.2.5  TotalNAV <TtlNAV>
Presence: [0..*]
Definition: Total value of all the holdings, less the fund's liabilities, attributable to a specific investment
fund class.
Impacted by: C2 "ActiveOrHistoricCurrency", C10 "CurrencyAmount"
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
66.1.7.5.2.6  PreviousTotalNAV <PrvsTtlNAV>
Presence: [0..*]
Definition: Previous value of all the holdings, less the fund's liabilities, attributable to a specific
investment fund class.
Impacted by: C2 "ActiveOrHistoricCurrency", C10 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 5269
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4420 May 2026
```

