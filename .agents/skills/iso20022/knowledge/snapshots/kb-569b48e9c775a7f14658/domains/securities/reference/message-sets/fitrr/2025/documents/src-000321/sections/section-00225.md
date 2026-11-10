---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.1 Amount", "22.1.1.2 AmountAndDirection61"]
file_pages: [275]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.1.2 AmountAndDirection61

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 275 to 275.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 275

```text
22.1.1.2  AmountAndDirection61
Definition: Amount of money expressed with an optional currency code and debit/credit indicator.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1 275
   Sign <Sgn> [0..1] Indicator 275
22.1.1.2.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money that results in an increase (positively signed) or decrease (negatively
signed), with specification of the currency.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 415
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
22.1.1.2.2  Sign <Sgn>
Presence: [0..1]
Definition: Indicates that the amount value is positive or negative.
Datatype: One of the following values must be used (see "PlusOrMinusIndicator" on page 451):
• Meaning When True: Plus
• Meaning When False: Minus
22.1.2 Commodity
22.1.2.1  AssetClassCommodityMultiCommodityExotic1
Definition: Defines commodity attributes of a derivative where the type is multi commodity exotic.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 275
22.1.2.1.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType13Code" on page 422
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
275 July 2025
```

