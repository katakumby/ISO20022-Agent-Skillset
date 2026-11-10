---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.5 Financial Instrument", "22.1.5.8 SecurityIdentification19", "22.1.5.8.3 Description <Desc>"]
file_pages: [331]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.5.8.3 Description <Desc>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 331 to 331.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 331

```text
Type <Tp> contains one of the following elements (see "IdentificationSource3Choice" on page 333 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 333
Or}   Proprietary <Prtry> [1..1] Text 333
22.1.5.8.3  Description <Desc>
Presence: [0..1]
Definition: Textual description of a security instrument.
Datatype: "Max140Text" on page 454
22.1.6 Financial Instrument Identification
22.1.6.1  FinancialInstrumentIdentification6Choice
Definition: Choice between formats for the identification of the financial instruments.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISIN <ISIN> [1..1] IdentifierSet 331
Or}   Index <Indx> [1..1] ± 331
22.1.6.1.1  ISIN <ISIN>
Presence: [1..1]
Definition: International Securities Identification Number (ISIN). A numbering system designed by the
United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-
character prefix representing the country of issue, followed by the national security number (if one
exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for
securities in that country.
Datatype: "ISINOct2015Identifier" on page 450
22.1.6.1.2  Index <Indx>
Presence: [1..1]
Definition: Index on which the financial instrument is based.
Index <Indx> contains the following elements (see "FinancialInstrument58" on page 328 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 328
   Name <Nm> [1..1] ± 328
22.1.6.2  FinancialInstrumentIdentification7Choice
Definition: Choice for identifying the underlying instruments that a derivative can consist of.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
331 July 2025
```

