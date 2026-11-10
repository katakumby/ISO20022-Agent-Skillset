---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.12 Rate", "22.1.12.7 FloatingInterestRate8", "22.1.12.7.1 ReferenceRate <RefRate>"]
file_pages: [364]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.12.7.1 ReferenceRate <RefRate>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 364 to 364.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 364

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReferenceRate <RefRate> [1..1] ± 364
   Term <Term> [0..1] ± 364
22.1.12.7.1  ReferenceRate <RefRate>
Presence: [1..1]
Definition: Identifies the reference index for the instrument.
Usage:
Index or name if the reference rate is not included in the index list.
ReferenceRate <RefRate> contains one of the following elements (see
"BenchmarkCurveName5Choice" on page 359 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Index <Indx> [1..1] CodeSet 360
Or}   Name <Nm> [1..1] Text 361
22.1.12.7.2  Term <Term>
Presence: [0..1]
Definition: Term of the reference rate.
Term <Term> contains the following elements (see "InterestRateContractTerm2" on page 358 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] CodeSet 358
   Value <Val> [1..1] Quantity C7 359
22.1.13 Regulatory Reporting
22.1.13.1  SecurityInstrumentDescription17
Definition: Identifies the security instrument by its name and typical characteristics.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
364 July 2025
```

