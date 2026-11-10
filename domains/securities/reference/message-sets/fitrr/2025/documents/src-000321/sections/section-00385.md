---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.2 Message Datatypes", "22.2.2 CodeSet", "22.2.2.100 PhysicalTransferType4Code"]
file_pages: [443]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.2.2.100 PhysicalTransferType4Code

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 443 to 443.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 443

```text
CodeName Name Definition
CALL Call Right to buy a quantity of an asset for an
agreed price at exercise date.
PUTO Put Right to sell a quantity of an asset for an
agreed price at exercise date.
OTHR Other Right where the holder of the option
decides whether the option is put or call.
22.2.2.100  PhysicalTransferType4Code
Definition: Specifies the asset delivery type when the financial instrument is settled.
Type: CodeSet
CodeName Name Definition
PHYS Physical Physical transfer.
OPTL Optional Determined by a third party or optional
for counterparty.
CASH Cash Cash transfer.
22.2.2.101  PriceStatus1Code
Definition: Specifies the status of the price of a financial instrument.
Type: CodeSet
CodeName Name Definition
PNDG Pending Price is pending.
NOAP NotApplicable No price for transaction (e.g. transfer
between accounts).
22.2.2.102  RateBasis1Code
Definition: Specifies a rate basis.
Type: CodeSet
CodeName Name Definition
DAYS Days Rate is reported in days.
MNTH Months Rate is reported in months.
WEEK Weeks Rate is reported in weeks.
YEAR Years Rate is reported in years.
22.2.2.103  RegulatoryTradingCapacity1Code
Definition: Specifies the regulatory trading capacity.
Type: CodeSet
CodeName Name Definition
MTCH MatchedPrincipal Transaction was carried out as a
matched principal trading.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
443 July 2025
```

