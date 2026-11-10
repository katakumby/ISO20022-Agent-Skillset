---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.34 SpreadRate1", "7.1.19.34.1 Sign <Sgn>"]
file_pages: [323]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.34.1 Sign <Sgn>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 323 to 323.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 323

```text
7.1.19.34.1  Sign <Sgn>
Presence: [1..1]
Definition: Specifies the sign of the rate.
Datatype: One of the following values must be used (see "PlusOrMinusIndicator" on page 665):
• Meaning When True: Plus
• Meaning When False: Minus
7.1.19.34.2  RateOrAmount <RateOrAmt>
Presence: [1..1]
Definition: Specifies if the spreadf is expressed as an amount or a rate.
RateOrAmount <RateOrAmt> contains one of the following AmountOrRate1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1, C9 323
Or}   Rate <Rate> [1..1] Rate 323
7.1.19.34.2.1  Amount <Amt>
Presence: [1..1]
Definition: Amount expressed as an amount of money.
Impacted by: C1 "ActiveCurrency", C9 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 611
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
7.1.19.34.2.2  Rate <Rate>
Presence: [1..1]
Definition: Amount expressed as a rate.
Datatype: "PercentageRate" on page 667
7.1.19.35  FutureOrOptionDetails3
Definition: Parameters for contracts which obligate the buyer to receive and the seller to deliver in the
future the assets specified at an agreed price or contracts which grant to the holder either the privilege
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 323 February 2025
```

