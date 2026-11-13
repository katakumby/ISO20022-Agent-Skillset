---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.40 Securities Quantity", "66.1.40.3 UnitsOrAmountOrPercentage1Choice", "66.1.40.3.1 Amount <Amt>"]
file_pages: [5143]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.40.3.1 Amount <Amt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5143 to 5143.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5143

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1, C13 5143
Or   Unit <Unit> [1..1] Quantity 5143
Or}   Percentage <Pctg> [1..1] Rate 5143
66.1.40.3.1  Amount <Amt>
Presence: [1..1]
Definition: Cash amount.
Impacted by: C1 "ActiveCurrency", C13 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.40.3.2  Unit <Unit>
Presence: [1..1]
Definition: Number of units.
Datatype: "DecimalNumber" on page 5400
66.1.40.3.3  Percentage <Pctg>
Presence: [1..1]
Definition: Percentage of cash amount.
Datatype: "PercentageRate" on page 5401
66.1.41 Service Level Agreement
66.1.41.1  ModificationScope44
Definition: Scope of the modification to be applied on an identified set of information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 5144
   ServiceLevelAgreement <SvcLvlAgrmt> [1..1] ± 5144
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5143 May 2026
```

