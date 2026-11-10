---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.24 RateAndAmountFormat1Choice", "82.1.19.24.2 Amount <Amt>"]
file_pages: [3005]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.24.2 Amount <Amt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3005 to 3005.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3005

```text
Definition: The value is expressed as a rate.
Datatype: "PercentageRate" on page 3325
82.1.19.24.2  Amount <Amt>
Presence: [1..1]
Definition: The value is expressed as a currency and amount.
Impacted by: C1 "ActiveCurrency", C4 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 3209
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
82.1.19.24.3  NotSpecifiedRate <NotSpcfdRate>
Presence: [1..1]
Definition: No value is specified.
NotSpecifiedRate <NotSpcfdRate> contains one of the following RateType12FormatChoice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3005
Or}   Proprietary <Prtry> [1..1] ± 3005
82.1.19.24.3.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the type of rate.
Datatype: "RateType12Code" on page 3282
CodeName Name Definition
OPEN Open Rate has not been established.
UKWN Unknown Rate is unknown by the sender or has
not been established.
NILP NilPayment Rate will not be paid.
82.1.19.24.3.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3005 August 2026
```

