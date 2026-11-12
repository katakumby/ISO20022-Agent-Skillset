---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.9 Miscellaneous", "22.1.9.2 ValidationRuleSchemeName1Choice"]
file_pages: [339]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.9.2 ValidationRuleSchemeName1Choice

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 339 to 339.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 339

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
22.1.9.2  ValidationRuleSchemeName1Choice
Definition: Identifies a name of the identification scheme.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 339
Or}   Proprietary <Prtry> [1..1] Text 339
22.1.9.2.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalValidationRuleIdentification1Code" on page 437
22.1.9.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 456
22.1.9.3  CountryCodeAndName3
Definition: Specifies a country by its code and its name.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] CodeSet C4 339
   Name <Nm> [1..1] Text 340
22.1.9.3.1  Code <Cd>
Presence: [1..1]
Definition: Country is specified by its code.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 434
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
339 July 2025
```

