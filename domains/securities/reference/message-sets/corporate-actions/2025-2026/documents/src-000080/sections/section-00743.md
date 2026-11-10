---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.32 RatioFormat17Choice", "16.1.15.32.3 AmountToAmount <AmtToAmt>"]
file_pages: [936]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.32.3 AmountToAmount <AmtToAmt>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 936 to 936.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 936

```text
CodeName Name Definition
UKWN Unknown Rate is unknown by the sender or has
not been established.
16.1.15.32.3  AmountToAmount <AmtToAmt>
Presence: [1..1]
Definition: Ratio expressed as a quotient of amounts.
AmountToAmount <AmtToAmt> contains the following AmountToAmountRatio2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount1 <Amt1> [1..1] Amount C1 936
   Amount2 <Amt2> [1..1] Amount C1 936
16.1.15.32.3.1  Amount1 <Amt1>
Presence: [1..1]
Definition: Numerator of the quotient of amounts.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 1155
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
16.1.15.32.3.2  Amount2 <Amt2>
Presence: [1..1]
Definition: Denominator of the quotient of amounts.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 1155
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
16.1.15.33  GrossDividendRateFormat38Choice
Definition: Choice between an amount or an unspecified rate.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 936 February 2026
```

