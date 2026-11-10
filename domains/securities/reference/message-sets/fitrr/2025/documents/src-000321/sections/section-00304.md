---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.11 Price", "22.1.11.4 SecuritiesTransactionPrice6", "22.1.11.4.3 DigitalToken <DgtlTkn>", "22.1.11.4.3.1 Identifier <Idr>"]
file_pages: [354]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.11.4.3.1 Identifier <Idr>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 354 to 354.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 354

```text
DigitalToken <DgtlTkn> contains the following DigitalTokenAmount2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identifier <Idr> [1..1] IdentifierSet 354
   Unit <Unit> [0..1] Quantity 354
   Description <Desc> [0..1] Text 354
22.1.11.4.3.1  Identifier <Idr>
Presence: [1..1]
Definition: Specifies the digital token identifier (DTI).
Datatype: "DTI2021Identifier" on page 450
22.1.11.4.3.2  Unit <Unit>
Presence: [0..1]
Definition: Quantity of digital tokens expressed as a number, for example, a number of blockchain
tokens.
Datatype: "Max30DecimalNumber" on page 452
22.1.11.4.3.3  Description <Desc>
Presence: [0..1]
Definition: Provides a description of the digital token identifier.
Datatype: "Max30Text" on page 455
22.1.11.5  SecuritiesTransactionPrice1
Definition: Descriptive fields capturing where no strike price is known.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Pending <Pdg> [1..1] CodeSet 354
   Currency <Ccy> [0..1] CodeSet C2 354
22.1.11.5.1  Pending <Pdg>
Presence: [1..1]
Definition: Price is currently not available, but pending.
Datatype: "PriceStatus1Code" on page 443
CodeName Name Definition
PNDG Pending Price is pending.
NOAP NotApplicable No price for transaction (e.g. transfer
between accounts).
22.1.11.5.2  Currency <Ccy>
Presence: [0..1]
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
354 July 2025
```

