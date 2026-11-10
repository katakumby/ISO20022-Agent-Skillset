---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.12 Rate", "22.1.12.2 InterestRateContractTerm2", "22.1.12.2.2 Value <Val>"]
file_pages: [359]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.12.2.2 Value <Val>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 359 to 359.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 359

```text
22.1.12.2.2  Value <Val>
Presence: [1..1]
Definition: Value of the contract term in number of units.
Impacted by: C7 "NumberRule"
Datatype: "Max3Number" on page 452
Constraints
• NumberRule
If Number is negative, then Sign must be present.
22.1.12.3  InterestRate6Choice
Definition: Choice between a fixed rate and a floating rate.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Fixed <Fxd> [1..1] Rate 359
Or}   Floating <Fltg> [1..1] ± 359
22.1.12.3.1  Fixed <Fxd>
Presence: [1..1]
Definition: Indicates that the rate is fixed.
Datatype: "PercentageRate" on page 454
22.1.12.3.2  Floating <Fltg>
Presence: [1..1]
Definition: Provides details about the variable rate.
Floating <Fltg> contains the following elements (see "FloatingInterestRate6" on page 362 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReferenceRate <RefRate> [1..1] ± 362
   Term <Term> [1..1] ± 363
   BasisPointSpread <BsisPtSprd> [1..1] Quantity C8 363
22.1.12.4  BenchmarkCurveName5Choice
Definition: Choice of format for benchmark curve name.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Index <Indx> [1..1] CodeSet 360
Or}   Name <Nm> [1..1] Text 361
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
359 July 2025
```

