---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.6 Financial Instrument Identification", "22.1.6.2 FinancialInstrumentIdentification7Choice", "22.1.6.2.1 Single <Sngl>"]
file_pages: [332]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.6.2.1 Single <Sngl>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 332 to 332.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 332

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Single <Sngl> [1..1] ± 332
Or}   Basket <Bskt> [1..1]  332
     ISIN <ISIN> [0..*] IdentifierSet 332
     Index <Indx> [0..*] ± 332
22.1.6.2.1  Single <Sngl>
Presence: [1..1]
Definition: Instrument consists of single instrument.
Single <Sngl> contains one of the following elements (see "FinancialInstrumentIdentification6Choice"
on page 331 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISIN <ISIN> [1..1] IdentifierSet 331
Or}   Index <Indx> [1..1] ± 331
22.1.6.2.2  Basket <Bskt>
Presence: [1..1]
Definition: Instrument consists of multiple instruments.
Basket <Bskt> contains the following BasketDescription3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..*] IdentifierSet 332
   Index <Indx> [0..*] ± 332
22.1.6.2.2.1  ISIN <ISIN>
Presence: [0..*]
Definition: International Securities Identification Number (ISIN). A numbering system designed by the
United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-
character prefix representing the country of issue, followed by the national security number (if one
exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for
securities in that country.
Datatype: "ISINOct2015Identifier" on page 450
22.1.6.2.2.2  Index <Indx>
Presence: [0..*]
Definition: Index on which the financial instrument is based.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
332 July 2025
```

