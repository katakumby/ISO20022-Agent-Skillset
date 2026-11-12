---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.5 Equalisation4", "66.1.26.5.5 DepreciationDepositPerUnit <DprctnDpstPerUnit>"]
file_pages: [4731]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.5.5 DepreciationDepositPerUnit <DprctnDpstPerUnit>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4731 to 4731.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4731

```text
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
66.1.26.5.5  DepreciationDepositPerUnit <DprctnDpstPerUnit>
Presence: [0..1]
Definition: Performance fee to be paid by the investor when the net asset value reaches the high-
watermark if the net asset value was under the high-watermark on subscription date.
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
66.1.26.5.6  EqualisationCreditPerUnit <EqulstnCdtPerUnit>
Presence: [0..1]
Definition: Prepayment amount to be paid by the investor at the moment of the subscription. The
amount is based on the positive difference between the gross asset value at subscription and the high-
watermark, when the investment fund units are subscribed to above their high-watermark.
Impacted by: C2 "ActiveOrHistoricCurrency", C10 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 5269
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4731 May 2026
```

