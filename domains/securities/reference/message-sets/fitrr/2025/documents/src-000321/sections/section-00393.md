---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.2 Message Datatypes", "22.2.5 IdentifierSet", "22.2.5.4 LEIIdentifier"]
file_pages: [451]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.2.5.4 LEIIdentifier

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 451 to 451.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 451

```text
Format
pattern [A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}
22.2.5.4  LEIIdentifier
Definition: Legal Entity Identifier is a code allocated to a party as described in ISO 17442 "Financial
Services - Legal Entity Identifier (LEI)".
Type: IdentifierSet
Identification scheme: Global LEI System; LEIIdentifier
Format
pattern [A-Z0-9]{18,18}[0-9]{2,2}
22.2.5.5  MICIdentifier
Definition: Market Identifier Code. The identification of a financial market, as stipulated in the norm ISO
10383 'Codes for exchanges and market identifications'.
Type: IdentifierSet
Identification scheme: SWIFT; MICIdentifier
Format
pattern [A-Z0-9]{4,4}
22.2.6 Indicator
22.2.6.1  PlusOrMinusIndicator
Definition: Indicates a positive or negative value.
Type: Indicator
Meaning When True: Plus
Meaning When False: Minus
22.2.6.2  TrueFalseIndicator
Definition: A flag indicating a True or False value.
Type: Indicator
Meaning When True: True
Meaning When False: False
22.2.7 Quantity
22.2.7.1  DecimalNumber
Definition: Number of objects represented as a decimal number, for example 0.75 or 45.6.
Type: Quantity
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
451 July 2025
```

