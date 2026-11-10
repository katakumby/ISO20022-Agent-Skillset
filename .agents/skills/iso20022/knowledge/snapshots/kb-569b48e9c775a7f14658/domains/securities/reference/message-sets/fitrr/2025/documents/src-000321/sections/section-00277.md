---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.5 Financial Instrument", "22.1.5.5 FinancialInstrument48Choice"]
file_pages: [327]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.5.5 FinancialInstrument48Choice

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 327 to 327.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 327

```text
Definition: Underlying currency 2 of the currency pair (the currency 1 will be populated in the notional
currency).
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 417
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
22.1.5.5  FinancialInstrument48Choice
Definition: Choice to specific an instrument of type ISIN, LEI or Index.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISIN <ISIN> [1..1] IdentifierSet 327
Or   LEI <LEI> [1..1] IdentifierSet 327
Or}   Index <Indx> [1..1] ± 327
22.1.5.5.1  ISIN <ISIN>
Presence: [1..1]
Definition: Identifies the financial instrument using an ISIN.
Datatype: "ISINOct2015Identifier" on page 450
22.1.5.5.2  LEI <LEI>
Presence: [1..1]
Definition: The LEI code of the issuer where the instrument is referring to an issuer rather than one
single instrument.
Datatype: "LEIIdentifier" on page 451
22.1.5.5.3  Index <Indx>
Presence: [1..1]
Definition: Index on which the financial instrument is based.
Index <Indx> contains the following elements (see "FinancialInstrument58" on page 328 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 328
   Name <Nm> [1..1] ± 328
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
327 July 2025
```

