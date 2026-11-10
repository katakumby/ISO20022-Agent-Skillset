---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.47 Tax", "66.1.47.5 Tax35", "66.1.47.5.1 Type <Tp>", "66.1.47.5.1.2 Proprietary <Prtry>"]
file_pages: [5248]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.47.5.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5248 to 5248.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5248

```text
66.1.47.5.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of tax expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.47.5.2  AppliedAmount <ApldAmt>
Presence: [1..1]
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
66.1.47.5.3  AppliedRate <ApldRate>
Presence: [0..1]
Definition: Rate used to calculate the tax.
Datatype: "PercentageRate" on page 5401
66.1.47.5.4  Country <Ctry>
Presence: [0..1]
Definition: Country where the tax is due.
Impacted by: C12 "Country"
Datatype: "CountryCode" on page 5290
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5248 May 2026
```

