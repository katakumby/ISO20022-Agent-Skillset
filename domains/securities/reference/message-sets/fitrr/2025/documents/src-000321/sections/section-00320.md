---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.2 SecuritiesTransactionReport7", "22.1.13.2.8 Transaction <Tx>", "22.1.13.2.8.3 Quantity <Qty>"]
file_pages: [373]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.2.8.3 Quantity <Qty>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 373 to 373.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 373

```text
22.1.13.2.8.3  Quantity <Qty>
Presence: [1..1]
Definition: Number of units of the financial instrument, or the number of derivative contracts in the
transaction.
Quantity <Qty> contains one of the following elements (see "FinancialInstrumentQuantity25Choice" on
page 324 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 324
Or   NominalValue <NmnlVal> [1..1] Amount C2, C5 324
Or}   MonetaryValue <MntryVal> [1..1] Amount C2, C5 324
22.1.13.2.8.4  DigitalTokenQuantity <DgtlTknQty>
Presence: [0..*]
Definition: Number of token units of a tokenised financial instrument.
DigitalTokenQuantity <DgtlTknQty> contains the following DigitalTokenAmount2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identifier <Idr> [1..1] IdentifierSet 373
   Unit <Unit> [0..1] Quantity 373
   Description <Desc> [0..1] Text 373
22.1.13.2.8.4.1  Identifier <Idr>
Presence: [1..1]
Definition: Specifies the digital token identifier (DTI).
Datatype: "DTI2021Identifier" on page 450
22.1.13.2.8.4.2  Unit <Unit>
Presence: [0..1]
Definition: Quantity of digital tokens expressed as a number, for example, a number of blockchain
tokens.
Datatype: "Max30DecimalNumber" on page 452
22.1.13.2.8.4.3  Description <Desc>
Presence: [0..1]
Definition: Provides a description of the digital token identifier.
Datatype: "Max30Text" on page 455
22.1.13.2.8.5  DerivativeNotionalChange <DerivNtnlChng>
Presence: [0..1]
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
373 July 2025
```

