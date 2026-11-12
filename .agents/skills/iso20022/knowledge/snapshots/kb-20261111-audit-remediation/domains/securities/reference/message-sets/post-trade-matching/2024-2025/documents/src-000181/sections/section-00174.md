---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.2 Agreement", "7.1.2.1 Agreement5", "7.1.2.1.2 Date <Dt>"]
file_pages: [226]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.2.1.2 Date <Dt>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 226 to 226.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 226

```text
Datatype: "Max350Text" on page 669
7.1.2.1.2  Date <Dt>
Presence: [0..1]
Definition: Numeric representation of the day of the month and year.
Datatype: "ISODateTime" on page 662
7.1.2.1.3  Currency <Ccy>
Presence: [0..1]
Definition: Contractual currency forming the basis of a financing agreement and associated
transactions. Usually, but not always, the same as the trade currency.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 613
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
7.1.2.1.4  ClosingType <ClsgTp>
Presence: [0..1]
Definition: Type of financing closing.
Datatype: "ClosingType1Code" on page 620
CodeName Name Definition
OVER Overnight Repo with a term of one day.
TERM Term Repo with a term of more than one day.
FLEX Flexible Identifies "a classic term repo with the
added feature that the cash is repaid to
the buyer in installments" (Definition from
"Mastering Repo Markets" by Bob
Steiner).
OPEN Open Repo which can be terminated by either
party at any time, and which has an
unspecified repurchase date.
7.1.2.1.5  StartDate <StartDt>
Presence: [0..1]
Definition: Start date of a financing deal that is the date the buyer pays the seller cash and takes control
of the collateral.
Datatype: "ISODateTime" on page 662
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 226 February 2025
```

