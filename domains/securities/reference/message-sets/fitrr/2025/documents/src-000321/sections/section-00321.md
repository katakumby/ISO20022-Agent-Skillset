---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.2 SecuritiesTransactionReport7", "22.1.13.2.8 Transaction <Tx>", "22.1.13.2.8.6 Price <Pric>"]
file_pages: [374]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.2.8.6 Price <Pric>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 374 to 374.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 374

```text
Definition: Indicates as to whether an increase or a decrease of notional of derivative contracts has
taken place.
Datatype: "VariationType1Code" on page 449
CodeName Name Definition
DECR Decrease Decrease to undertaking amount.
INCR Increase Increase to undertaking amount.
22.1.13.2.8.6  Price <Pric>
Presence: [1..1]
Definition: Traded price of the transaction excluding, where applicable, commission and accrued
interest.
In the case of option contracts, it is the premium of the derivative contract per underlying security or
index point.
In the case of spread bets it should be the reference price of the direct underlying instrument.
Where price is currently not available but pending, the value should be 'PNDG'.
For CDS it should be the coupon in basis points.
Where price reported in monetary terms, it shall be provided in the major currency unit.
Where price is not applicable the field should be left blank.
Price <Pric> contains one of the following elements (see "SecuritiesTransactionPrice22Choice" on
page 349 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Price <Pric> [1..1] ± 349
Or   DigitalTokenPrice <DgtlTknPric> [1..1] ± 350
Or}   NoPrice <NoPric> [1..1] ± 350
22.1.13.2.8.7  NetAmount <NetAmt>
Presence: [0..1]
Definition: Net amount of the transaction means the cash amount which is paid by the buyer of the debt
instrument upon the settlement of the transaction.
Datatype: "ImpliedCurrencyAndAmount" on page 416
22.1.13.2.8.8  TradeVenue <TradVn>
Presence: [1..1]
Definition: Identification of the venue where the transaction was executed.
Usage:
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
374 July 2025
```

