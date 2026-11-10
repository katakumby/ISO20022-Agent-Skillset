---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.2 Message Datatypes", "22.2.2 CodeSet", "22.2.2.74 BondType1Code"]
file_pages: [434]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.2.2.74 BondType1Code

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 434 to 434.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 434

```text
22.2.2.74  BondType1Code
Definition: Specifies the type of bonds.
Type: CodeSet
CodeName Name Definition
EUSB SovereignBond Bond of type sovereign bond.
OEPB OtherPublicBond Bond of type other public bond.
CVTB ConvertibleBond Bond of type convertible bond.
CRPB CorporateBond Bond of type corporate Bond.
CVDB CoveredBond Bond of type covered Bond.
OTHR Other Other bond type.
22.2.2.75  CancelledStatusReason15Code
Definition: Specifies the underlying reason for the cancellation of the associated transaction.
Type: CodeSet
CodeName Name Definition
CANI CancelledByYourself Transaction is cancelled by yourself.
CSUB CancelledByAgent Instruction has been cancelled by the
agent due to an event deadline
extension.
22.2.2.76  CountryCode
Definition: Code to identify a country, a dependency, or another area of particular geopolitical interest,
on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code).
Type: CodeSet
Format
pattern [A-Z]{2,2}
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
22.2.2.77  CountrySubDivisionCode
Definition: Code to identify a name of a unit resulting from the division of a country, dependency, or
other area of special geopolitical interest contained in ISO 3166-1, on the basis of country names
obtained from the United Nations (ISO 3166-2: Country subdivision code).
Type: CodeSet
Format
pattern [A-Z]{2,2}\-[0-9A-Z]{1,3}
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
434 July 2025
```

