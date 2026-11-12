---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.47 Tax", "66.1.47.2 InformativeTax2", "66.1.47.2.5 IndividualTax <IndvTax>", "66.1.47.2.5.8 TaxCalculationDetails <TaxClctnDtls>", "66.1.47.2.5.8.1 Basis <Bsis>", "66.1.47.2.5.8.1.1 Code <Cd>"]
file_pages: [5234]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.47.2.5.8.1.1 Code <Cd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5234 to 5234.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5234

```text
66.1.47.2.5.8.1.1  Code <Cd>
Presence: [1..1]
Definition: Tax basis expressed as a code.
Datatype: "TaxationBasis2Code" on page 5366
CodeName Name Definition
FLAT Flat Charge/tax basis is a lump sum.
PERU PerUnit Charges/tax basis is per unit of financial
instrument.
66.1.47.2.5.8.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Tax basis expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.47.2.5.8.2  TaxableAmount <TaxblAmt>
Presence: [1..1]
Definition: Amount of money on which the tax is charged.
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
66.1.47.3  TaxReference1
Definition: Pension scheme tax reference.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5234 May 2026
```

