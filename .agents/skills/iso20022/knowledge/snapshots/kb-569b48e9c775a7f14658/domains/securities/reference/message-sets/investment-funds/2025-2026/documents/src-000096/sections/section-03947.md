---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.47 Tax", "66.1.47.4 Tax38", "66.1.47.4.4 Country <Ctry>"]
file_pages: [5240]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.47.4.4 Country <Ctry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5240 to 5240.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5240

```text
Definition: Amount of money resulting from the calculation of the tax.
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
66.1.47.4.4  Country <Ctry>
Presence: [0..1]
Definition: Country where the tax is due.
Impacted by: C12 "Country"
Datatype: "CountryCode" on page 5290
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.47.4.5  ExemptionIndicator <XmptnInd>
Presence: [1..1]
Definition: Indicates whether a tax exemption applies.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.47.4.6  ExemptionReason <XmptnRsn>
Presence: [0..1]
Definition: Reason for the tax exemption.
ExemptionReason <XmptnRsn> contains one of the following ExemptionReason1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5241
Or}   Proprietary <Prtry> [1..1] ± 5243
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5240 May 2026
```

