---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.47 Tax", "66.1.47.2 InformativeTax2", "66.1.47.2.5 IndividualTax <IndvTax>", "66.1.47.2.5.3 InformativeRate <InftvRate>"]
file_pages: [5229]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.47.2.5.3 InformativeRate <InftvRate>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5229 to 5229.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5229

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.47.2.5.3  InformativeRate <InftvRate>
Presence: [0..1]
Definition: Rate used to calculate the tax. This rate is provided for information only.
Datatype: "PercentageRate" on page 5401
66.1.47.2.5.4  Country <Ctry>
Presence: [0..1]
Definition: Country where the tax is due.
Impacted by: C12 "Country"
Datatype: "CountryCode" on page 5290
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.47.2.5.5  ExemptionIndicator <XmptnInd>
Presence: [1..1]
Definition: Indicates whether a tax exemption applies.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.47.2.5.6  ExemptionReason <XmptnRsn>
Presence: [0..1]
Definition: Reason for the tax exemption.
ExemptionReason <XmptnRsn> contains one of the following ExemptionReason1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5230
Or}   Proprietary <Prtry> [1..1] ± 5232
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5229 May 2026
```

