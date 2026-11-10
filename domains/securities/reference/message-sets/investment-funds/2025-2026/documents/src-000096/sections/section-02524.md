---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.16 RedemptionLegDetails <RedLegDtls>", "53.4.5.16.3 FinancialInstrumentQuantityChoice <FinInstrmQtyChc>", "53.4.5.16.3.2 PercentageOfTotalSubscriptionAmount <PctgOfTtlSbcptAmt>"]
file_pages: [3559]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.16.3.2 PercentageOfTotalSubscriptionAmount <PctgOfTtlSbcptAmt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3559 to 3559.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3559

```text
53.4.5.16.3.2  PercentageOfTotalSubscriptionAmount <PctgOfTtlSbcptAmt>
Presence: [1..1]
Definition: Percentage of the total switch amount (buy-driven) to be invested in a particular investment
fund or investment fund class.
Datatype: "PercentageRate" on page 5401
53.4.5.16.3.3  NetAmount <NetAmt>
Presence: [1..1]
Definition: Amount of money to be received following redemption of fund units.
Net Amount = (Quantity * Price) - (Fees + Taxes).
Impacted by: C3 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"
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
53.4.5.16.3.4  GrossAmount <GrssAmt>
Presence: [1..1]
Definition: Amount of money to be redeemed from the fund.
Gross Amount = Quantity * Price.
Impacted by: C3 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"
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
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3559 May 2026
```

