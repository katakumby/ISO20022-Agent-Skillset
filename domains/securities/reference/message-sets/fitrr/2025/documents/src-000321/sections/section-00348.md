---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.3 SecuritiesReferenceDataReport7", "22.1.13.3.6 DerivativeInstrumentAttributes <DerivInstrmAttrbts>", "22.1.13.3.6.8 AssetClassSpecificAttributes <AsstClssSpcfcAttrbts>"]
file_pages: [404]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.3.6.8 AssetClassSpecificAttributes <AsstClssSpcfcAttrbts>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 404 to 404.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 404

```text
CodeName Name Definition
OPTL Optional Determined by a third party or optional
for counterparty.
CASH Cash Cash transfer.
22.1.13.3.6.8  AssetClassSpecificAttributes <AsstClssSpcfcAttrbts>
Presence: [0..1]
Definition: Specific attributes of the underlying asset class of the financial instrument.
Impacted by: C11 "OneElementPresentRule"
AssetClassSpecificAttributes <AsstClssSpcfcAttrbts> contains the following AssetClass2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Commodity <Cmmdty> [0..1]  404
     Product <Pdct> [1..1] ± 405
     TransactionType <TxTp> [0..1] CodeSet 405
     FinalPriceType <FnlPricTp> [0..1] CodeSet 406
   Interest <Intrst> [0..1]  406
     InterestRate <IntrstRate> [1..1] ± 406
     FirstLegInterestRate <FrstLegIntrstRate> [0..1] ± 407
     OtherNotionalCurrency <OthrNtnlCcy> [0..1] CodeSet C2 407
     OtherLegInterestRate <OthrLegIntrstRate> [0..1] ± 407
   ForeignExchange <FX> [0..1]  408
     FXType <FxTp> [0..1] CodeSet 408
     OtherNotionalCurrency <OthrNtnlCcy> [0..1] CodeSet C2 408
Constraints
• OneElementPresentRule
At least one of the 3 elements must be present.
Following Must be True
    /Commodity Must be present
 Or    /Interest Must be present
 Or    /ForeignExchange Must be present
22.1.13.3.6.8.1  Commodity <Cmmdty>
Presence: [0..1]
Definition: The fields in this section should only be populated for instruments that have non-financial
instrument of type commodity as underlying.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
404 July 2025
```

