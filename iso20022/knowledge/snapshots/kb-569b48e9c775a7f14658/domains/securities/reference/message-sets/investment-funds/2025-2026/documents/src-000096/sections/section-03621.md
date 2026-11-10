---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.33 CashAll1", "66.1.28.33.1 Indicator <Ind>"]
file_pages: [4871]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.33.1 Indicator <Ind>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4871 to 4871.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4871

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Indicator <Ind> [1..1] Indicator 4871
   Currency <Ccy> [0..1] CodeSet C1 4871
66.1.28.33.1  Indicator <Ind>
Presence: [1..1]
Definition: Indicates whether all assets in the portfolio are to be liquidated and transferred as cash.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.28.33.2  Currency <Ccy>
Presence: [0..1]
Definition: Currency of the cash.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 5275
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
66.1.28.34  AdditionalParameters1
Definition: Sort criteria.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Country <Ctry> [0..1] CodeSet C12 4871
   Currency <Ccy> [0..1] CodeSet C2 4872
   GeographicalArea <GeoArea> [0..1] Text 4872
66.1.28.34.1  Country <Ctry>
Presence: [0..1]
Definition: Specifies the country.
Impacted by: C12 "Country"
Datatype: "CountryCode" on page 5290
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4871 May 2026
```

