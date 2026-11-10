---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.8 Market", "22.1.8.4 TradingVenueIdentification1Choice", "22.1.8.4.3 Other <Othr>"]
file_pages: [338]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.8.4.3 Other <Othr>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 338 to 338.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 338

```text
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 434
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
22.1.8.4.3  Other <Othr>
Presence: [1..1]
Definition: Identification used where a venue does not have an already defined code type.
Other <Othr> contains the following elements (see "TradingVenueIdentification2" on page 333 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 333
   Type <Tp> [1..1] CodeSet 334
22.1.9 Miscellaneous
22.1.9.1  TonsOrCurrency2Choice
Definition: Specifies the commodity quantity in tons or the amount and currency used (for example
carbone dioxide).
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Number <Nb> [1..1] Quantity 338
Or}   Amount <Amt> [1..1] Amount C2, C5 338
22.1.9.1.1  Number <Nb>
Presence: [1..1]
Definition: Total number of specific transactions expresses in tons.
Datatype: "DecimalNumber" on page 451
22.1.9.1.2  Amount <Amt>
Presence: [1..1]
Definition: Total volume of specific transactions expresses in currency and amount format.
Impacted by: C2 "ActiveOrHistoricCurrency", C5 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 416
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
338 July 2025
```

