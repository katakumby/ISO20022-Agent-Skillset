---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.19 Equalisation3", "66.1.26.19.3 EqualisationMethodologyType <EqulstnMthdlgyTp>", "66.1.26.19.3.2 RelatedSubscription <RltdSbcpt>", "66.1.26.19.3.2.2 RelatedQuantity <RltdQty>"]
file_pages: [4771]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.19.3.2.2 RelatedQuantity <RltdQty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4771 to 4771.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4771

```text
66.1.26.19.3.2.2  RelatedQuantity <RltdQty>
Presence: [0..1]
Definition: Number of investment fund units from the related subscription order.
Datatype: "DecimalNumber" on page 5400
66.1.26.19.3.2.3  RelatedAmount <RltdAmt>
Presence: [0..1]
Definition: Amount of money paid by the investor for the related subscription order.
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
66.1.26.19.3.2.4  ContingentLiquidationPerUnit <CntngntLqdtnPerUnit>
Presence: [0..1]
Definition: Performance fee to be paid by the investor when the value of the investment fund units were
below their applicable high-watermark on subscription date, and above the high-watermark on
redemption date.
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
66.1.26.19.3.2.5  DepreciationDepositPerUnit <DprctnDpstPerUnit>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4771 May 2026
```

