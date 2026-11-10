---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.24 ResidualCash2", "66.1.28.24.2 Currency <Ccy>"]
file_pages: [4855]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.24.2 Currency <Ccy>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4855 to 4855.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4855

```text
66.1.28.24.2  Currency <Ccy>
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
66.1.28.25  SecurityClassificationType2Choice
Definition: Choice between a CFI code and an other type of identification for the classification of a
financial instrument.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CFI <CFI> [1..1] IdentifierSet 4855
Or}   AlternateClassification <AltrnClssfctn> [1..1] ± 4855
66.1.28.25.1  CFI <CFI>
Presence: [1..1]
Definition: Classification type of the financial instrument, as per the ISO 10962 Classification of
Financial Instrument (CFI) codification.
Datatype: "CFIOct2015Identifier" on page 5391
66.1.28.25.2  AlternateClassification <AltrnClssfctn>
Presence: [1..1]
Definition: Other type of classification of the financial instrument.
AlternateClassification <AltrnClssfctn> contains the following elements (see "GenericIdentification3"
on page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   Issuer <Issr> [0..1] Text 4548
66.1.28.26  BreakdownByUserDefinedParameter3
Definition: Specifies the cash-in and cash-out flows by a user defined parameter/s.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4855 May 2026
```

