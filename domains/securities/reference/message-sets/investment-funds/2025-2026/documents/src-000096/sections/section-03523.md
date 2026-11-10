---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.19 Equalisation3", "66.1.26.19.5 GrossAssetValue <GrssAsstVal>"]
file_pages: [4773]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.19.5 GrossAssetValue <GrssAsstVal>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4773 to 4773.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4773

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.26.19.5  GrossAssetValue <GrssAsstVal>
Presence: [0..1]
Definition: Value of the investment fund on subscription date before accruals for performance fees.
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
66.1.26.20  OtherDistributionStrategy1
Definition: Other distribution strategy.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DistributionStrategyType <DstrbtnStrtgyTp> [0..1] Text 4773
   Target <Trgt> [0..1] ± 4774
   AdditionalInformation <AddtlInf> [0..1] ± 4774
66.1.26.20.1  DistributionStrategyType <DstrbtnStrtgyTp>
Presence: [0..1]
Definition: Type of distribution strategy.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4773 May 2026
```

